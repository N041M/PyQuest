"""Liveness: a construct only counts if it can change the behavior.

Construct checks used to scan the whole file, so decorative code (an unused
`x = 1 * 1`, an `if False: pass`, a print() routed to a StringIO) could
satisfy them while a trick computed the real answer. Liveness is mutation
analysis applied to the learner's code: ablate the candidate node (remove the
statement / substitute the expression with a sentinel), re-run the program
against the recorded inputs in-process, and require the behavior to change.
A construct that survives ablation unchanged is decorative and does not count.

Judgment rules (chosen to protect honest code first):
  - statement removal:  any change OR a crash counts as live (removing a
    needed assignment usually crashes with NameError);
  - expression substitution: only a CLEAN run with different output counts as
    live; crashes are inconclusive and the next sentinel is tried (so
    type-fragile chaff engineered to crash stays dead);
  - containers and all-crash expressions fall back to the reachability
    tripwire (see _tripwire);
  - if the baseline itself cannot be reproduced in-process, liveness degrades
    to the plain AST check (never block a learner on a harness quirk;
    audit.py would catch any weakening this opens).

Mixin contract -- needs the tape and the guard:
    self.path, self.mode                  (facade)
    self.guard / self._guarded / self.put_file / self.timeout  (RunnersMixin)
    self._runs, self._calls               the tape (RunnersMixin fills it)
    self._tree, self._live_base, self._live_base_done   caches (facade inits)
"""

import ast
import copy

from .errors import (PuzzleSyntaxError, PuzzleCrashError, WrongResultError,
                     LessonNotUsedError)
from .textutil import normalize


class LivenessMixin:

    _SENTINELS = (987654321, "\x00sentinel\x00", None, 0.5,
                  ["\x00item"], [("\x00key", 987654321)],
                  {"\x00key": 987654321}, {"\x00elem"})
    _LIVE_TIMEOUT = 2          # seconds per ablated re-run

    # ---- the AST, shared by every source-aware check ------------------------
    def tree(self):
        if self._tree is None:
            try:
                self._tree = ast.parse(self.source())
            except SyntaxError as e:
                raise PuzzleSyntaxError("line %s: %s" % (e.lineno, e.msg))
        return self._tree

    def _find(self, pred):
        """Walk-order indices of nodes matching pred (stable across copies)."""
        return [i for i, n in enumerate(ast.walk(self.tree())) if pred(n)]

    def _node(self, idx):
        return list(ast.walk(self.tree()))[idx]

    # ---- behavior signatures: what the program DOES on the recorded inputs --
    def _live_cases(self):
        """The recorded inputs liveness replays (capped for speed: the first
        runs are the authored edge cases, the last are randomized)."""
        runs = self._runs
        if len(runs) > 6:
            runs = runs[:3] + runs[-3:]
        return runs

    def _exec_script(self, tree, stdin, files):
        """One in-process run of (possibly ablated) script source."""
        code = compile(tree, "<liveness>", "exec")
        for name, content in (files or {}).items():
            self.put_file(name, content)
        self._guarded("liveness", exec, code, {"__name__": "__main__"},
                      _stdin=stdin)
        return normalize(self.printed)

    def _script_sig(self, tree):
        sig = []
        for stdin, files, _ in self._live_cases():
            try:
                sig.append(self._exec_script(tree, stdin, files))
            except BaseException:
                sig.append("\x00CRASH")
        return sig

    def _import_sig(self, tree):
        """Re-import (possibly ablated) source and replay the recorded calls;
        the signature is every result + everything printed."""
        code = compile(tree, "<liveness>", "exec")
        g = {"__name__": "pyquest_liveness"}
        try:
            self._guarded("liveness", exec, code, g)
        except BaseException:
            return ["\x00CRASH"]
        sig = ["module:" + normalize(self.printed)]
        for name, args, kwargs in self._calls:
            fn = g.get(name)
            if not callable(fn):
                sig.append(name + ":missing")
                continue
            try:
                a, k = copy.deepcopy(args), copy.deepcopy(kwargs)
            except Exception:
                a, k = args, kwargs
            try:
                r = self._guarded("liveness", fn, *a, **k)
                sig.append("%s:%r|%s" % (name, r, normalize(self.printed)))
            except PuzzleCrashError:
                sig.append(name + ":\x00CRASH")
            except Exception as e:
                sig.append("%s:raises %s" % (name, type(e).__name__))
        return sig

    def _signature(self, tree):
        old = self.timeout
        self.timeout = min(self._LIVE_TIMEOUT, old)
        try:
            if self.mode == "script":
                return self._script_sig(tree)
            return self._import_sig(tree)
        finally:
            self.timeout = old

    def _baseline(self):
        """The unablated program's in-process behavior, or None when liveness
        cannot run (nothing recorded / not reproducible) -- degrade safely."""
        if not self._live_base_done:
            self._live_base_done = True
            has = self._runs if self.mode == "script" else self._calls
            if has:
                try:
                    base = self._signature(copy.deepcopy(self.tree()))
                except Exception:
                    base = None
                if base and not any("\x00CRASH" in s for s in base):
                    self._live_base = base
        return self._live_base

    # ---- ablation: one mutated copy of the tree -----------------------------
    @staticmethod
    def _swap_node(tree, target, new):
        """Replace `target` wherever it sits in its parent's fields."""
        for parent in ast.walk(tree):
            for field, value in ast.iter_fields(parent):
                if value is target:
                    setattr(parent, field, new)
                    return True
                if isinstance(value, list):
                    for i, item in enumerate(value):
                        if item is target:
                            value[i] = new
                            return True
        return False

    def _ablate(self, idx, action, payload):
        """A deep copy of the tree with one node ablated, or None if the
        ablation cannot be expressed."""
        tree = copy.deepcopy(self.tree())
        target = list(ast.walk(tree))[idx]      # walk order is copy-stable
        if action == "remove":
            ok = self._swap_node(tree, target, ast.Pass())
        elif action == "subst":
            new = ast.parse(repr(payload), mode="eval").body
            ok = self._swap_node(tree, target, new)
        elif action == "dropkw":
            target.keywords = [k for k in target.keywords
                               if k.arg != payload]
            ok = True
        elif action == "trim":
            target.args = target.args[:1]
            ok = True
        else:
            ok = False
        if not ok:
            return None
        return ast.fix_missing_locations(tree)

    _ABLATIONS = {
        "stmt": (("remove", None),),
        "bool": (("subst", True), ("subst", False)),
        "trim": (("trim", None),),
    }

    def _tripwire(self, idx):
        """Reachability: substitute the node with an expression that raises
        the moment it is evaluated. A crash proves the construct executes;
        a clean identical run proves it sits in dead code. The weaker bar for
        constructs whose VALUE can't be probed -- an accumulator dict/set
        starts empty by design, so no sentinel content shows up in the
        output, and a sorted() feeding dict lookups crashes on every foreign
        sentinel key."""
        try:
            tree = copy.deepcopy(self.tree())
            target = list(ast.walk(tree))[idx]
            trap = ast.parse("1 // 0", mode="eval").body
            if not self._swap_node(tree, target, trap):
                return True                      # cannot judge: count it
            sig = self._signature(ast.fix_missing_locations(tree))
        except Exception:
            return True                          # cannot judge: count it
        return any("\x00CRASH" in s for s in sig)

    # ---- the verdict ---------------------------------------------------------
    def _is_live(self, idx, kind):
        base = self._baseline()
        if base is None:
            return True                          # cannot judge: count it
        if kind in self._ABLATIONS:
            ablations = self._ABLATIONS[kind]
        elif kind.startswith("kw:"):
            ablations = (("dropkw", kind[3:]),)
        else:                                    # "expr" / "container"
            ablations = tuple(("subst", s) for s in self._SENTINELS)
        clean_seen = False
        for action, payload in ablations:
            try:
                tree = self._ablate(idx, action, payload)
                sig = self._signature(tree) if tree is not None else None
            except Exception:
                sig = None
            if sig is None:
                if kind == "stmt":
                    return True                  # could not even compile: vital
                continue
            for a, b in zip(sig, base):
                if "\x00CRASH" in a:
                    if kind == "stmt":
                        return True              # removal broke it: it mattered
                else:
                    clean_seen = True
                    if a != b:
                        return True              # clean run, changed behavior
        if kind == "container":
            return self._tripwire(idx)           # executing at all is the bar
        if kind in ("expr", "bool") and not clean_seen:
            return self._tripwire(idx)           # every sentinel crashed
        return False

    def _live_filter(self, found, kind, min_count=1):
        """The subset of candidate node-indices that are live, short-circuited
        once min_count are found. Degrades to 'all' when liveness can't run."""
        if self._baseline() is None:
            return found
        live = []
        for idx in found:
            if self._is_live(idx, kind):
                live.append(idx)
                if len(live) >= min_count:
                    break
        return live

    DECORATIVE = ("only in code that never affects the output -- "
                  "decorative code doesn't count")

    def _require_live(self, want, missing, found, kind, because, min_count=1):
        if len(found) < min_count:
            raise LessonNotUsedError(want, missing, because)
        if len(self._live_filter(found, kind, min_count)) < min_count:
            raise LessonNotUsedError(want, self.DECORATIVE, because)

    def require_live(self, want, missing, found, kind, because="",
                     min_count=1):
        """Public extension seam for bespoke puzzle checks.

        A complex puzzle's tests.py can compose its own structural check from
        audited parts: find candidate nodes with `T.tree()` (walk-order
        indices, e.g. via enumerate(ast.walk(T.tree()))), then demand they be
        live. `kind` is "stmt" (removal must change behavior; crash counts),
        "expr" (sentinel substitution must change a clean run), "bool",
        "container" (reachability bar), "trim", or "kw:<name>". Ship a
        dodges.py entry alongside any bespoke check (SCHEMA.md)."""
        self._require_live(want, missing, found, kind, because, min_count)
