"""The tester: the `T` object handed to each puzzle's tests.py `check(T)`.

It both runs the learner's code and raises *translated* failures, so a missing
function, a syntax error, a wrong result, and a crash each become a different,
friendly message. Construct checks and performance helpers live here too.

Sturdiness: every execution of learner code -- importing the file, calling a
function, timing it -- goes through ONE guard (`_guarded`) that

  - blanks stdin (a stray input() fails fast instead of hanging the check),
  - captures stdout into T.printed (assertable, and off the report screen),
  - enforces a wall-clock timeout (an infinite loop fails, not hangs),
  - translates exit()/sys.exit() (learner code cannot kill the checker),
  - moves the working directory into a throwaway sandbox (learner file I/O
    cannot touch the project; file puzzles get fixtures via files=/put_file).

Script mode gets the same isolation from its subprocess (timeout + sandbox cwd).
"""

import io
import os
import sys
import ast
import copy
import time
import signal
import tempfile
import traceback
import subprocess
import importlib.util

from .config import PY, TIMEOUT


# ---- translated failure categories ----------------------------------------
class PuzzleSyntaxError(Exception):
    def __init__(self, detail):
        self.detail = detail


class MissingSymbolError(Exception):
    def __init__(self, name):
        self.name = name


class WrongResultError(Exception):
    def __init__(self, expected, actual, because=""):
        self.expected = expected
        self.actual = actual
        self.because = because


class PuzzleCrashError(Exception):
    def __init__(self, detail, because=""):
        self.detail = detail
        self.because = because


class _Timeout(BaseException):
    """Raised by the alarm inside learner code. BaseException on purpose:
    a learner's `except Exception:` must not be able to swallow it."""


# ---- small text utilities used by the tester ------------------------------
def normalize(s):
    """Strip trailing whitespace per line and trailing blank lines."""
    if s is None:
        return ""
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in s.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def short_tb():
    tb = traceback.format_exc().strip().split("\n")
    return "\n".join(tb[-3:])


def fmt_args(args, kwargs):
    parts = [repr(a) for a in args]
    parts += ["%s=%r" % (k, v) for k, v in kwargs.items()]
    return ", ".join(parts)


NO_STDIN_MSG = (
    "input() was called, but import-mode puzzles get their values as function\n"
    "arguments -- the checker calls your function directly, so there is no\n"
    "keyboard to read. Remove the input() and use the parameters instead.")

EXIT_MSG = (
    "your code called exit()/sys.exit(), which tries to stop the whole\n"
    "program. A puzzle should finish by returning (or just ending) -- remove\n"
    "the exit call.")


def load_module(path):
    """Import a solution fresh, under the full execution guard.

    Kept as a module-level function for compatibility; it simply borrows a
    throwaway Toolkit's guard."""
    return Toolkit(path, "import").load()


class Toolkit:
    def __init__(self, path, mode, timeout=TIMEOUT):
        self.path = path
        self.mode = mode
        self.timeout = timeout
        self.printed = ""           # stdout captured from the last load/call
        self._module = None
        self._tree = None
        self._sandbox = None

    # ---- the sandbox: a throwaway cwd for everything the learner runs -----
    def sandbox(self):
        """The temp directory all learner code runs in. Shared across the
        runs/calls of one check, so a file written by one run is visible to
        the next (which file puzzles may rely on)."""
        if self._sandbox is None:
            self._sandbox = tempfile.mkdtemp(prefix="pyquest_sandbox_")
        return self._sandbox

    def put_file(self, name, content):
        """Create a fixture file the learner's code can open by name."""
        with open(os.path.join(self.sandbox(), name), "w") as f:
            f.write(content)

    def file(self, name, because=""):
        """The text of a file the learner's code wrote (translated failure
        if it never appeared)."""
        try:
            with open(os.path.join(self.sandbox(), name)) as f:
                return f.read()
        except OSError:
            raise WrongResultError("a file named %r to be written" % name,
                                   "it wasn't created", because)

    # ---- the execution guard ----------------------------------------------
    def _guarded(self, because, fn, *args, **kwargs):
        """Run learner code with every protection on. Infrastructure failures
        (hang, exit, stray input) become PuzzleCrashError; the learner's own
        exceptions pass through untouched for the caller to interpret."""
        old_stdin, old_stdout = sys.stdin, sys.stdout
        sys.stdin = io.StringIO("")
        buf = sys.stdout = io.StringIO()
        try:
            old_cwd = os.getcwd()
        except OSError:
            old_cwd = None
        os.chdir(self.sandbox())
        def on_alarm(signum, frame):
            raise _Timeout()

        alarmed = False
        try:                        # SIGALRM: main thread on Unix; else skip
            old_handler = signal.signal(signal.SIGALRM, on_alarm)
            signal.alarm(self.timeout)
            alarmed = True
        except (ValueError, AttributeError):
            pass
        try:
            return fn(*args, **kwargs)
        except _Timeout:
            raise PuzzleCrashError(
                "Your code ran longer than %ds -- maybe an endless loop?"
                % self.timeout, because=because)
        except EOFError:
            raise PuzzleCrashError(NO_STDIN_MSG, because=because)
        except SystemExit:
            raise PuzzleCrashError(EXIT_MSG, because=because)
        finally:
            if alarmed:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
            sys.stdin, sys.stdout = old_stdin, old_stdout
            if old_cwd is not None:
                os.chdir(old_cwd)
            self.printed = buf.getvalue()

    # ---- script mode -------------------------------------------------------
    def run(self, stdin="", files=None):
        """Run the solution as a script in the sandbox; return normalized
        stdout. `files` seeds fixture files into the sandbox first."""
        for name, content in (files or {}).items():
            self.put_file(name, content)
        try:
            proc = subprocess.run(
                [PY, self.path], input=stdin, capture_output=True,
                text=True, timeout=self.timeout, cwd=self.sandbox())
        except subprocess.TimeoutExpired:
            raise PuzzleCrashError(
                "Your program ran longer than %ds -- maybe an endless loop?"
                % self.timeout)
        if proc.returncode != 0:
            err = proc.stderr.strip()
            last = err.split("\n")[-1] if err else "unknown error"
            if "SyntaxError" in err or "IndentationError" in err:
                raise PuzzleSyntaxError(last)
            raise PuzzleCrashError(last)
        return normalize(proc.stdout)

    def source(self):
        """The raw text of the learner's work file.

        Behavior checks are the rule; this is the rare exception, for a puzzle
        whose lesson IS a specific piece of source (e.g. commenting a line out).
        """
        try:
            with open(self.path) as f:
                return f.read()
        except OSError:
            return ""

    # ---- import mode -------------------------------------------------------
    def load(self):
        if self._module is None:
            name = "pyquest_solution_under_test"
            sys.modules.pop(name, None)
            spec = importlib.util.spec_from_file_location(name, self.path)
            mod = importlib.util.module_from_spec(spec)
            try:
                self._guarded("while importing your file",
                              spec.loader.exec_module, mod)
            except PuzzleCrashError:
                raise
            except SyntaxError as e:
                raise PuzzleSyntaxError("line %s: %s" % (e.lineno, e.msg))
            except Exception:
                raise PuzzleCrashError(short_tb())
            self._module = mod
        return self._module

    def func(self, name):
        mod = self.load()
        fn = getattr(mod, name, None)
        if not callable(fn):
            raise MissingSymbolError(name)
        return fn

    def get(self, name):
        mod = self.load()
        if not hasattr(mod, name):
            raise MissingSymbolError(name)
        return getattr(mod, name)

    def call(self, name, *args, **kwargs):
        fn = self.func(name)
        because = "while calling %s(%s)" % (name, fmt_args(args, kwargs))
        try:
            return self._guarded(because, fn, *args, **kwargs)
        except PuzzleCrashError:
            raise
        except Exception:
            raise PuzzleCrashError(short_tb(), because=because)

    # ---- classes & objects (for the OOP chapters) ---------------------------
    def make(self, classname, *args, **kwargs):
        """Instantiate the learner's class; translated failures throughout."""
        cls = self.get(classname)
        if not isinstance(cls, type):
            raise MissingSymbolError(classname)
        because = "while creating %s(%s)" % (classname, fmt_args(args, kwargs))
        try:
            return self._guarded(because, cls, *args, **kwargs)
        except PuzzleCrashError:
            raise
        except Exception:
            raise PuzzleCrashError(short_tb(), because=because)

    def method(self, obj, name, *args, **kwargs):
        """Call a method on an instance made by make()."""
        m = getattr(obj, name, None)
        if not callable(m):
            raise MissingSymbolError(name)
        because = "while calling .%s(%s)" % (name, fmt_args(args, kwargs))
        try:
            return self._guarded(because, m, *args, **kwargs)
        except PuzzleCrashError:
            raise
        except Exception:
            raise PuzzleCrashError(short_tb(), because=because)

    def attr(self, obj, name):
        """An attribute of an instance, or a translated 'missing piece'."""
        if not hasattr(obj, name):
            raise MissingSymbolError(name)
        return getattr(obj, name)

    # ---- assertions ---------------------------------------------------------
    def eq(self, actual, expected, because="", match_case=False):
        """Equal. String outputs are compared case-INSENSITIVELY by default;
        pass match_case=True for puzzles where capitalisation is the point."""
        a, e = actual, expected
        if isinstance(a, str) and isinstance(e, str):
            na, ne = normalize(a), normalize(e)
            if not match_case:
                na, ne = na.casefold(), ne.casefold()
            ok = na == ne
        else:
            ok = a == e
        if not ok:
            raise WrongResultError(expected, actual, because)

    def true(self, cond, because=""):
        if not cond:
            raise WrongResultError("a true condition", cond, because)

    def is_a(self, value, typ, because=""):
        if not isinstance(value, typ):
            raise WrongResultError(typ.__name__, type(value).__name__, because)

    def raises(self, exc, name, *args, **kwargs):
        fn = self.func(name)
        because = "while calling %s(%s)" % (name, fmt_args(args, kwargs))
        try:
            self._guarded(because, fn, *args, **kwargs)
        except exc:
            return
        except PuzzleCrashError:
            raise                   # hang/exit/input -- a real defect, surface it
        except Exception as e:
            raise WrongResultError(
                "%s to be raised" % exc.__name__, type(e).__name__,
                "A different error was raised.")
        raise WrongResultError(
            "%s to be raised" % exc.__name__, "no error raised", "")

    def _approx_eq(self, a, e, tol):
        """Numbers within tol; lists/tuples/dicts compared recursively so
        float-bearing structures can be asserted in one call."""
        if isinstance(e, bool):
            return a == e
        if isinstance(e, (int, float)):
            try:
                return abs(a - e) <= tol
            except TypeError:
                return False
        if isinstance(e, (list, tuple)):
            return (isinstance(a, (list, tuple)) and len(a) == len(e)
                    and all(self._approx_eq(x, y, tol) for x, y in zip(a, e)))
        if isinstance(e, dict):
            return (isinstance(a, dict) and set(a) == set(e)
                    and all(self._approx_eq(a[k], e[k], tol) for k in e))
        return a == e

    def approx(self, actual, expected, tol=1e-9, because=""):
        """Equal within a tolerance (floats) -- works inside lists, tuples,
        and dicts too."""
        if not self._approx_eq(actual, expected, tol):
            raise WrongResultError("%r (within %g)" % (expected, tol),
                                   actual, because)

    def any_of(self, actual, options, because="", match_case=False):
        """Accept any one of several valid answers (case-insensitive strings
        by default)."""
        def norm(v):
            if isinstance(v, str):
                v = normalize(v)
                return v if match_case else v.casefold()
            return v
        a = norm(actual)
        if not any(a == norm(o) for o in options):
            raise WrongResultError("one of %r" % (list(options),),
                                   actual, because)

    def unordered(self, actual, expected, because=""):
        """Equal ignoring order (lists/tuples of sortable items)."""
        try:
            ok = sorted(actual) == sorted(expected)
        except TypeError:
            ok = list(actual) == list(expected)
        if not ok:
            raise WrongResultError("%r (in any order)" % (expected,),
                                   actual, because)

    def does_not_mutate(self, name, *args, **kwargs):
        """Call name(*args) and require the arguments to come back unchanged --
        for puzzles whose lesson is returning a NEW value (sorted vs .sort).
        Returns the call's result so the value can be asserted too."""
        because = kwargs.pop("because", "")
        try:
            before = copy.deepcopy(args)
        except Exception:
            return self.call(name, *args, **kwargs)    # uncopyable: skip check
        result = self.call(name, *args, **kwargs)
        for arg, prior in zip(args, before):
            if arg != prior:
                raise WrongResultError(
                    "the input left unchanged (%r)" % (prior,),
                    "your function changed it to %r" % (arg,),
                    because or "return a new value instead of modifying "
                               "the argument")
        return result

    # ---- construct checks: confirm the LESSON was used, not just the answer.
    # (Behavior checks are the default; reach for these only where a puzzle can
    # be trivially gamed by typing the answer instead of computing it.)
    def tree(self):
        if self._tree is None:
            try:
                self._tree = ast.parse(self.source())
            except SyntaxError as e:
                raise PuzzleSyntaxError("line %s: %s" % (e.lineno, e.msg))
        return self._tree

    def _print_calls(self):
        return [n for n in ast.walk(self.tree())
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == "print"]

    def prints_computed(self, min_calls=1, because=""):
        """Every print() must show a computed value, not a typed-in literal --
        and there must be a print() at all (no sys.stdout.write end-runs).
        min_calls requires that many separate print() statements, for puzzles
        whose lesson is reuse (one print of a multi-line string dodges it)."""
        calls = self._print_calls()
        if not calls:
            raise WrongResultError("a print() that shows a computed value",
                                   "print() wasn't used", because)
        if len(calls) < min_calls:
            raise WrongResultError(
                "%d separate print() calls" % min_calls,
                "only %d print() call(s)" % len(calls), because)
        for c in calls:
            if not c.args or all(isinstance(a, ast.Constant) for a in c.args):
                raise WrongResultError(
                    "a computed value in print(...)",
                    "the answer typed in as a literal", because)

    # ---- "did you use the construct this puzzle teaches?" -------------------
    def _has(self, *types):
        return any(isinstance(n, types) for n in ast.walk(self.tree()))

    def uses_print(self, because=""):
        if not self._print_calls():
            raise WrongResultError("a print() call", "print() wasn't used",
                                   because)

    def uses_if(self, because=""):
        if not self._has(ast.If):
            raise WrongResultError("an if statement",
                                   "no if was used (a trick avoided it)", because)

    def uses_while(self, because=""):
        if not self._has(ast.While):
            raise WrongResultError("a while loop", "no while loop was used",
                                   because)

    def uses_for(self, because=""):
        if not self._has(ast.For):
            raise WrongResultError("a for loop", "no for loop was used", because)

    def uses_loop(self, because=""):
        if not self._has(ast.For, ast.While):
            raise WrongResultError("a loop (for or while)", "no loop was used",
                                   because)

    def uses_break(self, because=""):
        if not self._has(ast.Break):
            raise WrongResultError("break", "break wasn't used", because)

    def uses_continue(self, because=""):
        if not self._has(ast.Continue):
            raise WrongResultError("continue", "continue wasn't used", because)

    def uses_fstring(self, because=""):
        if not self._has(ast.JoinedStr):
            raise WrongResultError("an f-string", "no f-string was used", because)

    def _subscripts(self):
        return [n for n in ast.walk(self.tree())
                if isinstance(n, ast.Subscript)]

    @staticmethod
    def _index_of(sub):
        idx = sub.slice
        if hasattr(ast, "Index") and isinstance(idx, ast.Index):  # py<3.9
            idx = idx.value
        return idx

    def uses_index(self, because=""):
        """A plain index s[i] (not a slice)."""
        for s in self._subscripts():
            if not isinstance(s.slice, ast.Slice):
                return
        raise WrongResultError("indexing like s[0]", "no indexing was used",
                               because)

    def uses_negative_index(self, because=""):
        """A negative index s[-1] (UnaryOp '-' or a negative literal)."""
        for s in self._subscripts():
            if isinstance(s.slice, ast.Slice):
                continue
            idx = self._index_of(s)
            if isinstance(idx, ast.UnaryOp) and isinstance(idx.op, ast.USub):
                return
            if isinstance(idx, ast.Constant) and isinstance(idx.value, int) \
                    and idx.value < 0:
                return
        raise WrongResultError("a negative index like s[-1]",
                               "no negative index was used", because)

    def uses_slice(self, step=False, because=""):
        for s in self._subscripts():
            if isinstance(s.slice, ast.Slice):
                if not step or s.slice.step is not None:
                    return
        what = "a slice with a step (s[::-1])" if step else "a slice (s[a:b])"
        raise WrongResultError(what, "no such slice was used", because)

    def uses_call(self, name, because=""):
        """A call to a function or method `name` (e.g. append, split, items)."""
        for n in ast.walk(self.tree()):
            if isinstance(n, ast.Call):
                f = n.func
                if isinstance(f, ast.Attribute) and f.attr == name:
                    return
                if isinstance(f, ast.Name) and f.id == name:
                    return
        raise WrongResultError("a call to %s()" % name,
                               "%s() wasn't used" % name, because)

    def uses_dict(self, because=""):
        """A dict literal {...} or dict()."""
        if self._has(ast.Dict):
            return
        for n in ast.walk(self.tree()):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                    and n.func.id == "dict":
                return
        raise WrongResultError("a dict ({} or dict())", "no dict was used",
                               because)

    def uses_set(self, because=""):
        """A set literal {a, b} or set()."""
        if self._has(ast.Set):
            return
        for n in ast.walk(self.tree()):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                    and n.func.id == "set":
                return
        raise WrongResultError("a set ({...} or set())", "no set was used",
                               because)

    def uses_try(self, because=""):
        """A try/except statement -- for puzzles whose lesson IS handling the
        error (an if-guard would behave the same but dodge the concept)."""
        if not self._has(ast.Try):
            raise WrongResultError("a try/except block",
                                   "no try/except was used", because)

    def uses_raise(self, because=""):
        """A raise statement."""
        if not self._has(ast.Raise):
            raise WrongResultError("a raise statement",
                                   "raise wasn't used", because)

    def uses_in(self, because=""):
        """The membership operator: `x in s` or `x not in s` in a condition."""
        for n in ast.walk(self.tree()):
            if isinstance(n, ast.Compare) and any(
                    isinstance(op, (ast.In, ast.NotIn)) for op in n.ops):
                return
        raise WrongResultError("the `in` operator", "`in` wasn't used", because)

    def uses_comprehension(self, with_if=False, because=""):
        """A comprehension (list/set/dict or generator expression). Pass
        with_if=True to require a filtering `if` clause inside it."""
        comps = [n for n in ast.walk(self.tree())
                 if isinstance(n, (ast.ListComp, ast.SetComp, ast.DictComp,
                                   ast.GeneratorExp))]
        if with_if:
            comps = [c for c in comps if any(g.ifs for g in c.generators)]
            what = "a comprehension with an if  ([x for x in ... if ...])"
        else:
            what = "a comprehension like [x for x in ...]"
        if not comps:
            raise WrongResultError(what, "no comprehension was used", because)

    # ---- construct checks staged for the upcoming chapters -----------------
    def uses_with(self, because=""):
        """A with statement (the files chapter: `with open(...) as f`)."""
        if not self._has(ast.With):
            raise WrongResultError("a with statement (with open(...) as f:)",
                                   "no with statement was used", because)

    def uses_import(self, module=None, because=""):
        """An import -- optionally of one specific module."""
        for n in ast.walk(self.tree()):
            if isinstance(n, ast.Import):
                if module is None or any(
                        a.name == module or a.name.startswith(module + ".")
                        for a in n.names):
                    return
            if isinstance(n, ast.ImportFrom):
                if module is None or (n.module or "").split(".")[0] == module:
                    return
        what = ("an import of %s" % module) if module else "an import statement"
        raise WrongResultError(what, "no such import was found", because)

    def uses_class(self, because=""):
        """A class definition."""
        if not self._has(ast.ClassDef):
            raise WrongResultError("a class definition (class Name:)",
                                   "no class was defined", because)

    def uses_yield(self, because=""):
        """yield / yield from (the generators chapter)."""
        if not self._has(ast.Yield, ast.YieldFrom):
            raise WrongResultError("a yield statement",
                                   "yield wasn't used", because)

    def uses_lambda(self, because=""):
        """A lambda expression."""
        if not self._has(ast.Lambda):
            raise WrongResultError("a lambda expression",
                                   "no lambda was used", because)

    def uses_unpacking(self, because=""):
        """Tuple/list unpacking, e.g. a, b = b, a  or  for a, b in pairs."""
        for n in ast.walk(self.tree()):
            if isinstance(n, ast.Assign) and any(
                    isinstance(t, (ast.Tuple, ast.List)) for t in n.targets):
                return
            if isinstance(n, ast.For) and isinstance(n.target,
                                                     (ast.Tuple, ast.List)):
                return
        raise WrongResultError("unpacking (a, b = ...)",
                               "no unpacking was used", because)

    def print_uses_keyword(self, kw, because=""):
        for c in self._print_calls():
            if any(k.arg == kw for k in c.keywords):
                return
        raise WrongResultError("print(..., %s=...)" % kw,
                               "no %s= used" % kw, because)

    def print_has_min_args(self, n, because=""):
        for c in self._print_calls():
            if len(c.args) >= n:
                return
        raise WrongResultError("one print with %d+ separate values" % n,
                               "too few values passed to a single print",
                               because)

    def assigns_a_variable(self, because=""):
        for node in ast.walk(self.tree()):
            if isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                return
        raise WrongResultError("a variable assignment", "no variable used",
                               because)

    def reassigns_a_variable(self, because=""):
        counts = {}
        for node in ast.walk(self.tree()):
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        counts[t.id] = counts.get(t.id, 0) + 1
            elif (isinstance(node, ast.AugAssign)
                  and isinstance(node.target, ast.Name)):
                counts[node.target.id] = counts.get(node.target.id, 0) + 1
        if not any(v >= 2 for v in counts.values()):
            raise WrongResultError("the same variable assigned twice",
                                   "no single variable was reassigned", because)

    _OPS = {"+": ast.Add, "-": ast.Sub, "*": ast.Mult,
            "/": ast.Div, "//": ast.FloorDiv, "%": ast.Mod}

    def uses_op(self, op, min_count=1, because=""):
        """Require the solution to actually compute with operator `op`.

        Counts how many times that arithmetic operator appears anywhere in the
        source. Defeats typing the answer (`print(14)`) and stashing it in a
        variable first (`x = 14; print(x)`), and -- with min_count -- using the
        wrong operation (e.g. multiplication for an addition puzzle)."""
        opcls = self._OPS[op]
        count = sum(1 for node in ast.walk(self.tree())
                    if isinstance(node, ast.BinOp)
                    and isinstance(node.op, opcls))
        if count < min_count:
            want = ("'%s' at least %d times" % (op, min_count)
                    if min_count > 1 else "the '%s' operation" % op)
            raise WrongResultError(want, "it wasn't used", because)

    # ---- performance (advisory; wall-clock, so keep budgets generous) ----
    def time_call(self, name, *args, runs=5, **kwargs):
        """Best-of-`runs` wall-clock seconds for one call."""
        fn = self.func(name)
        because = "while timing %s" % name
        best = None
        for _ in range(max(1, runs)):
            t0 = time.perf_counter()
            try:
                self._guarded(because, fn, *args, **kwargs)
            except PuzzleCrashError:
                raise
            except Exception:
                raise PuzzleCrashError(short_tb(), because=because)
            dt = time.perf_counter() - t0
            best = dt if best is None else min(best, dt)
        return best

    def scales(self, name, make_input, n_small, n_big, slack=2.0, runs=5,
               because=""):
        """Doubling experiment: check the function grows ~linearly.

        Times the call on a small and a big input and compares the time ratio
        to the input-size ratio. An O(n) solution scales with the input; an
        O(n^2) one grows far faster and trips the `slack` threshold.
        """
        fn = self.func(name)
        guard_because = "while timing %s" % name

        def best(n):
            arg = make_input(n)
            b = None
            for _ in range(max(1, runs)):
                t0 = time.perf_counter()
                self._guarded(guard_because, fn, arg)
                dt = time.perf_counter() - t0
                b = dt if b is None else min(b, dt)
            return b

        t1, t2 = best(n_small), best(n_big)
        if t1 < 1e-5:           # too fast to measure reliably -- give the pass
            return
        size_ratio = float(n_big) / float(n_small)
        threshold = size_ratio * slack
        ratio = t2 / t1
        if ratio > threshold:
            raise WrongResultError(
                "~linear scaling (<=%.0fx slower for %.0fx input)"
                % (threshold, size_ratio),
                "%.0fx slower" % ratio,
                because or "looks slower than the target complexity")
