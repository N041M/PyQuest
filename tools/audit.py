"""Project audit: solution conformance plus an anti-sidestep attack suite.

    python3 tools/audit.py             every solution.py must pass its own tests.py
    python3 tools/audit.py --sidestep  ALSO attack with the adversaries AND flag any
                                       lesson that no construct check guards
    python3 tools/audit.py --lessons   per-puzzle lesson-guard coverage table
    python3 tools/audit.py --prove-checks  prove each construct check is load-bearing
                                       (a pinned dodge must slip past once it is gone)
    python3 tools/audit.py --engine    self-test the execution guard & toolkit APIs
    python3 tools/audit.py --keys      self-test engine/keys.py + the arrow surfaces
                                       over a pseudo-terminal (POSIX; clean skip else)

The sidestep audit is mutation testing aimed at the GRADER: intentionally
wrong programs must fail. Four generic adversaries attack every puzzle:

  replay        record every (stdin -> stdout) / (call -> return) the tests
                exercise against the reference solution; answer from that
                lookup table, computing nothing.
  chaff-replay  the same table, plus a never-called function stuffed with
                every construct the toolkit can require (ops, loops, try,
                dict, sep=, 3-arg print...). Defeats any construct check that
                merely scans the file; only LIVENESS (engine/toolkit/liveness.py)
                stops it.
  synth         for fixed-output scripts: print each constant line via live
                arithmetic the brief never asked for (`print(7*2)` general-
                ized). Only expression-scoped checks (line_*) stop it.
  named-synth   the same constants parked in a variable and reused, to crack
                store-and-reuse lessons unless they pin the stored value.

plus per-puzzle regression dodges: an optional `dodges.py` in a puzzle folder
lists known sidesteps as (label, source) pairs in DODGES; every one of them
must fail that puzzle's tests, forever.

Randomized inputs defeat the replays (fresh inputs miss the table); liveness-
checked constructs defeat chaff; prescribed-expression checks defeat synth.
A puzzle should be saved by at least one defense per adversary.

Two static meta-audits sit above the adversaries, covering the gap they cannot
reach -- an *alternative-construct* sidestep (a program that computes the right
answer with a different tool) on a varying-output puzzle, which synth can't model
and which used to be hunted by hand:

  lesson-guard   (--sidestep / --lessons) a puzzle that teaches a construct,
                 varies its output (so synth never fires), and pins no construct
                 check is unguarded against that class. Flagged unless it is a
                 documented residual in GUARDED_OK. This turns the old manual
                 sweep into a failing audit row.
  prove-checks   (--prove-checks) the converse: for every puzzle that has both a
                 construct check and a dodges.py, strip the construct layer and
                 confirm a pinned dodge then slips through -- proving the check,
                 not some behavioral assert, is what stops the dodge.

Not part of the engine; safe to delete.
"""

import os
import ast
import sys
import tempfile
import importlib.util

# audit.py lives in tools/; the repo root (which holds the engine package) is
# its parent, so climb one level to make `import engine` work from anywhere.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from engine.content import discover, load_tests, load_hints
from engine.toolkit import (Toolkit, PuzzleSyntaxError, MissingSymbolError,
                            WrongResultError, PuzzleCrashError)
from audit_selftest import _engine_selftest
from audit_keys import keys_selftest

# Puzzles where a passing impostor is the accepted ceiling: the cheapest
# program that passes IS a legitimate answer to the lesson.
ALLOWED = {
    "1.1": "the lesson is printing one fixed literal; any print of it is legit",
}

# Toolkit methods that pin HOW an answer was reached, not just WHAT it printed.
# A puzzle calling any of these has staked its lesson on a construct, so the
# lesson-guard meta-audit considers it covered. Everything else on T (eq, run,
# call, raises, approx, file, source, ...) only checks behavior. Keep this in
# step with engine/toolkit/ when a uses_*/line_*/print_* check is added.
LESSON_CHECKS = {
    "uses_op", "uses_if", "uses_for", "uses_while", "uses_loop", "uses_break",
    "uses_continue", "uses_in", "uses_index", "uses_negative_index",
    "uses_slice", "uses_call", "uses_import", "uses_class", "uses_comprehension",
    "uses_dict", "uses_set", "uses_fstring", "uses_lambda", "uses_try",
    "uses_raise", "uses_with", "uses_with_open", "uses_yield", "uses_unpacking",
    "uses_boolop", "uses_nested_if", "uses_default_param",
    "line_only_literals", "line_shape", "line_uses_op",
    "print_expr", "print_has_min_args", "print_uses_keyword",
    "prints_computed", "prints_name", "assigns_a_variable",
    "reassigns_a_variable", "is_a", "is_generator", "does_not_mutate",
    "raises", "require_live", "scales", "time_call",
    # NB: eq/approx/any_of/unordered/true are GENERIC output asserts (value
    # equality, maybe order- or case-insensitive) -- they pin no lesson, so they
    # are deliberately absent. `raises` IS lesson-specific (it verifies an
    # exception, e.g. 7.2's TypeError trap), so it counts. Bespoke checks built
    # from true/source/tree go through require_live (which is listed) by
    # convention, so the AST-name inventory still recognises them.
}

# Puzzles the lesson-guard flags as unguarded but which are an accepted ceiling,
# each with the reason it is safe to leave open (mirrors ALLOWED, for the static
# audit). A new puzzle that teaches a construct without pinning it stays a hard
# failure until it is either fixed or recorded here with a justification.
GUARDED_OK = {
    "3.1": "the varying True/False output is unobtainable without an order "
           "comparison, and <, >, >= are all valid here, so there is no single "
           "operator to pin without rejecting a correct answer",
    "6.1": "import mode: the grader calls the function by name, so def itself is "
           "forced -- there is no internal construct left to pin",
    "6.2": "import mode: the two parameters are forced by the calls the grader "
           "makes; nothing internal to pin",
    "6.3": "import mode: returning (not printing) is forced -- a print leaves the "
           "return value None and fails the behavioral check",
    "6.5": "import mode: early-return behavior is forced by the grader's calls; "
           "no internal construct to pin",
}

# Dead code containing every construct the toolkit can require. Prepended to
# impostors: a file-scanning construct check is satisfied by it, a liveness
# check is not (nothing here ever runs -- __decoy__ is never called).
CHAFF = '''\
import io as __io
__buf = __io.StringIO()


def __decoy__():
    q = 0
    q += 1
    q = (1 + 2) * (3 // 4) - 5 % 6 + 7 / 8
    s = "abc"[0] + "abc"[-1] + "abc"[0:2] + "abc"[::-1] + f"{q}"
    d = {"k": 1}
    z = {1, 2}
    a, b = 1, 2
    lst = [i for i in [1] if i]
    if q:
        pass
    while q == 99:
        break
    for i in []:
        continue
    try:
        raise ValueError(s)
    except ValueError as e:
        pass
    with __io.StringIO() as f:
        pass
    import json as __json
    class __C:
        pass
    def __g():
        yield 1
    fn = lambda x: x
    lst.append(d.get("k"))
    lst.pop()
    sorted(z)
    sum([])
    min([0])
    max([0])
    len(s)
    list(enumerate([]))
    list(zip([], []))
    s.split()
    "-".join([])
    s.count("a")
    s.replace("a", "b")
    s.find("a")
    s.upper()
    s.strip()
    int("1")
    ("a" in s)
    print(a, b, q, sep="-", end="", file=__buf)
'''


# ---- recording -------------------------------------------------------------
class Recorder(Toolkit):
    """A Toolkit that also keeps results, for building the replay tables."""

    def __init__(self, path, mode):
        Toolkit.__init__(self, path, mode)
        self.stdin_runs = []        # (stdin, normalized stdout)
        self.fn_calls = []          # (name, args, kwargs, result)

    def run(self, stdin="", files=None):
        out = Toolkit.run(self, stdin, files=files)
        self.stdin_runs.append((stdin, out))
        return out

    def call(self, name, *args, **kwargs):
        result = Toolkit.call(self, name, *args, **kwargs)
        self.fn_calls.append((name, args, kwargs, result))
        return result


# ---- the adversaries -------------------------------------------------------
def build_impostor(rec):
    """The replay dodge: answer from a lookup table, never compute anything.

    It deliberately uses print() with a computed (non-literal) argument and a
    couple of assignments, so only checks that demand the puzzle's real
    construct (an operator, loop, slice, try, ...) can stop it."""
    lines = []
    if rec.stdin_runs:
        table = {}
        for stdin, out in rec.stdin_runs:
            table[stdin] = out
        lines.append("import sys")
        lines.append("TABLE = %r" % (table,))
        lines.append("data = sys.stdin.read()")
        lines.append("answer = TABLE.get(data, 'REPLAY-MISS')")
        lines.append("print(answer)")
    if rec.fn_calls:
        table = {}
        names = []
        for name, args, kwargs, result in rec.fn_calls:
            table[(name, repr(args), repr(kwargs))] = result
            if name not in names:
                names.append(name)
        lines.append("TABLE = %r" % (table,))
        for name in names:
            lines.append("def %s(*a, **k):" % name)
            lines.append("    return TABLE[(%r, repr(a), repr(k))]" % name)
    return "\n".join(lines) + "\n"


def _synth_expr(line):
    """An expression computing the constant `line` with LIVE arithmetic the
    brief never asked for -- the `print(7*2)` dodge, generalized."""
    try:
        n = int(line)
        return "int((0 + 1) * %d / 1) // 1 - 0 %% 7" % n
    except ValueError:
        pass
    try:
        f = float(line)
        return "(0.0 + %r) * 1" % f
    except ValueError:
        pass
    return '"" + %r * 1' % line


def build_synth(rec, named=False):
    """The compute-it-differently dodge for fixed-output scripts, or None
    when the recorded output varies with the input (then it can't apply)."""
    outs = set(out for _, out in rec.stdin_runs)
    if len(outs) != 1:
        return None
    body = []
    if named:
        seen = {}
        for line in outs.pop().split("\n"):
            if line not in seen:
                seen[line] = "__v%d" % len(seen)
                body.append("%s = %r" % (seen[line], line))
            body.append("print(%s)" % seen[line])
    else:
        for line in outs.pop().split("\n"):
            body.append("print(%s)" % _synth_expr(line))
    return "\n".join(body) + "\n"


def load_dodges(pdir):
    """Optional per-puzzle dodges.py: DODGES = [(label, source), ...] --
    known sidesteps that must fail this puzzle's tests, forever."""
    path = os.path.join(pdir, "dodges.py")
    if not os.path.exists(path):
        return []
    spec = importlib.util.spec_from_file_location("pyquest_dodges", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return list(getattr(mod, "DODGES", []))


# ---- meta-audit: lesson-guard coverage -------------------------------------
def check_inventory(pdir):
    """The set of toolkit methods a puzzle's tests.py calls on T, read straight
    from the source (no execution). The basis for asking which dimension --
    behavior or construct -- each puzzle actually pins."""
    src = open(os.path.join(pdir, "tests.py")).read()
    methods = set()
    for node in ast.walk(ast.parse(src)):
        if (isinstance(node, ast.Attribute)
                and isinstance(node.value, ast.Name) and node.value.id == "T"):
            methods.add(node.attr)
    return methods


def lesson_guard(p, rec):
    """Static cover for the alternative-construct blind spot.

    The four adversaries cannot model a program that computes the right answer
    with a DIFFERENT construct on a varying-output puzzle: synth only fires on
    fixed-output scripts, and chaff is killed by liveness without ever testing a
    live alternative. So a puzzle that teaches a construct, varies its output,
    and pins no construct check is unguarded against that whole class. Returns:
        None       -- covered (teaches no construct, pins one, or synth applies)
        "allowed"  -- exposed, but a documented residual in GUARDED_OK
        "exposed"  -- exposed and undocumented: a hole to close or justify
    `rec` is a Recorder already run against the solution (for output variance).
    """
    meta = p["meta"]
    if not meta.get("concept"):              # a drill/capstone teaches no syntax
        return None
    if check_inventory(p["dir"]) & LESSON_CHECKS:        # pins HOW, not just WHAT
        return None
    outs = set(out for _, out in rec.stdin_runs)
    synth_covers = (meta.get("mode") == "script" and bool(rec.stdin_runs)
                    and len(outs) == 1)      # a fixed-output script -> synth bites
    if synth_covers:
        return None
    return "allowed" if p["id"] in GUARDED_OK else "exposed"


# ---- meta-audit: prove each construct check is load-bearing -----------------
def _strip_lesson_checks(src):
    """Compile tests.py with every top-level `T.<lesson-check>(...)` statement
    replaced by `pass`, and return (check_callable, count_removed) -- or
    (None, 0) if it pins no construct. AST surgery, then compile: no source
    round-trip, so it runs on 3.8 (ast.unparse is 3.9+)."""
    removed = [0]

    class Strip(ast.NodeTransformer):
        def visit_Expr(self, node):
            f = node.value.func if isinstance(node.value, ast.Call) else None
            if (isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name)
                    and f.value.id == "T" and f.attr in LESSON_CHECKS):
                removed[0] += 1
                return ast.copy_location(ast.Pass(), node)
            return node

    tree = Strip().visit(ast.parse(src))
    ast.fix_missing_locations(tree)
    if not removed[0]:
        return None, 0
    ns = {}
    exec(compile(tree, "<stripped-tests>", "exec"), ns)
    return ns.get("check"), removed[0]


def _passes_check(p, src, check, attempts=2):
    """Run one program against a specific check() (a stripped tests.check),
    fresh randomness each attempt -- the prover's analogue of impostor_passes."""
    fd, path = tempfile.mkstemp(suffix=".py", prefix="pyquest_prove_")
    os.close(fd)
    with open(path, "w") as f:
        f.write(src)
    try:
        for _ in range(attempts):
            try:
                check(Toolkit(path, p["meta"].get("mode")))
            except Exception:
                continue
            return True
    finally:
        os.unlink(path)
    return False


def prove_checks(p):
    """For a puzzle that pins a construct AND ships dodges, strip the construct
    layer and see which pinned dodges then slip through. A dodge that passes
    only once the construct checks are gone PROVES those checks -- not a
    behavioral assert -- are what stop it. Returns:
        None              -- nothing to prove (no construct check, or no dodges)
        (proven, removed) -- proven: dodge labels the construct layer alone
                             stops; removed: how many checks were stripped.
    An empty `proven` with dodges present is the interesting case: the dodges
    are caught behaviorally, so the construct checks earn nothing against them."""
    dodges = load_dodges(p["dir"])
    if not dodges:
        return None
    src = open(os.path.join(p["dir"], "tests.py")).read()
    check, removed = _strip_lesson_checks(src)
    if not removed:
        return None
    proven = [label for label, dsrc in dodges
              if _passes_check(p, dsrc, check, attempts=1)]
    return proven, removed


def impostor_passes(p, src, attempts=2):
    """Does this wrong program pass the puzzle's tests on any attempt?"""
    fd, path = tempfile.mkstemp(suffix=".py", prefix="pyquest_impostor_")
    os.close(fd)
    with open(path, "w") as f:
        f.write(src)
    try:
        for _ in range(attempts):
            tests = load_tests(p["dir"])     # fresh randomness each attempt
            try:
                tests.check(Toolkit(path, p["meta"].get("mode")))
            except Exception:
                continue
            return True
    finally:
        os.unlink(path)
    return False


def sidestep_report(p):
    """Attack one puzzle with every adversary, then the static lesson-guard.

    Returns (breaches, dodge_passes, guard): generic impostors that passed,
    pinned dodges that passed (never acceptable), and the lesson-guard verdict
    (None / "allowed" / "exposed"). Reuses one recording for all three."""
    sol = os.path.join(p["dir"], "solution.py")
    rec = Recorder(sol, p["meta"].get("mode"))
    load_tests(p["dir"]).check(rec)          # conformance already verified
    guard = lesson_guard(p, rec)
    impostors = []
    if rec.stdin_runs or rec.fn_calls:
        table = build_impostor(rec)
        impostors.append(("replay", table))
        impostors.append(("chaff-replay", CHAFF + table))
        if p["meta"].get("mode") == "script" and rec.stdin_runs:
            synth = build_synth(rec)
            if synth is not None:
                impostors.append(("synth", CHAFF + synth))
                impostors.append(("named-synth",
                                  CHAFF + build_synth(rec, named=True)))
    breaches = [label for label, src in impostors if impostor_passes(p, src)]
    dodge_passes = [label for label, src in load_dodges(p["dir"])
                    if impostor_passes(p, src, attempts=1)]
    return breaches, dodge_passes, guard


# Project puzzles (a build-up arc that ends in a low-guidance capstone) carry a
# `kind` instead of teaching one construct. They are deliberately sparse: fewer
# hints, no `concept` (so they're out of the textbook and exempt from the
# lesson-guard -- the lesson is the project, not a single tool). `debug` puzzles
# ship broken code to fix, so their starter must FAIL the tests.
PROJECT_KINDS = {"build", "debug", "capstone"}


def _passes_tests(path, mode, dirpath):
    """Run dirpath's tests.py against `path` (a starter or solution). True if it
    passes cleanly, False if any puzzle/test failure is raised. Used to assert a
    debug puzzle's starter is actually broken."""
    try:
        tests = load_tests(dirpath)
        tests.check(Toolkit(path, mode))
        return True
    except Exception:
        return False


# ---- conformance (every solution passes its own tests) ---------------------
def conformance_issues(p):
    issues = []
    meta = p["meta"]
    if meta.get("id") != p["id"]:
        issues.append("meta id %r != folder id %r" % (meta.get("id"), p["id"]))
    # title + mode are structural (used everywhere / drives checking), so they
    # are required. concept + why are optional: a puzzle that teaches no new
    # syntax (a drill or capstone) simply omits them and stays out of the
    # textbook -- not every puzzle has to carry an entry.
    for key in ("title", "mode"):
        if not meta.get(key):
            issues.append("meta missing %r" % key)
    if meta.get("mode") not in ("script", "import"):
        issues.append("bad mode %r" % meta.get("mode"))
    # The card points the learner at brief.md, so it must exist; a concept-
    # bearing puzzle (one with a textbook entry) must also carry its reference.md
    # -- the standard every topic now meets, pinned so it can't silently regress.
    if not os.path.isfile(os.path.join(p["dir"], "brief.md")):
        issues.append("missing brief.md")
    if meta.get("concept") and not os.path.isfile(
            os.path.join(p["dir"], "reference.md")):
        issues.append("has a concept but no reference.md")
    kind = meta.get("kind")
    if kind and kind not in PROJECT_KINDS:
        issues.append("unknown kind %r (want one of %s)"
                      % (kind, ", ".join(sorted(PROJECT_KINDS))))
    # Lesson puzzles carry exactly 3 escalating hints; project puzzles are
    # low-guidance, so they may carry 0-3.
    hints = load_hints(p["dir"])
    if kind in PROJECT_KINDS:
        if len(hints) > 3:
            issues.append("%d hints (project puzzles allow 0-3)" % len(hints))
    elif len(hints) != 3:
        issues.append("%d hints (want 3)" % len(hints))
    sol = os.path.join(p["dir"], "solution.py")
    try:
        tests = load_tests(p["dir"])
        T = Toolkit(sol, meta.get("mode"))
        tests.check(T)
    except PuzzleSyntaxError as e:
        issues.append("SOLUTION SYNTAX: %s" % e.detail)
    except MissingSymbolError as e:
        issues.append("SOLUTION MISSING SYMBOL: %s" % e.name)
    except WrongResultError as e:
        issues.append("SOLUTION WRONG: expected %r got %r (%s)"
                      % (e.expected, e.actual, e.because))
    except PuzzleCrashError as e:
        issues.append("SOLUTION CRASH: %s" % e.detail)
    except Exception as e:
        issues.append("TESTS ERROR: %s: %s" % (type(e).__name__, e))
    else:
        fn = getattr(tests, "bonus", None)
        if callable(fn):
            try:
                fn(T)
            except Exception as e:
                issues.append("BONUS FAILS for solution: %s" % e)
    # A debug puzzle ships broken code: its starter must FAIL the tests, or there
    # is nothing to fix and the lesson is empty.
    if kind == "debug":
        starter = os.path.join(p["dir"], "starter.py")
        if not os.path.isfile(starter):
            issues.append("debug puzzle has no starter.py to fix")
        elif _passes_tests(starter, meta.get("mode"), p["dir"]):
            issues.append("debug starter already passes (no bug to fix)")
    return issues


def _lessons_report(puzzles):
    """The lesson-guard coverage table: for each puzzle, the construct checks it
    pins and the guard's verdict. A human read of the alternative-construct
    attack surface, and what --sidestep gates on. Exits 1 on any EXPOSED row."""
    print("discovered %d puzzles (lesson-guard coverage)\n" % len(puzzles))
    print("  %-5s %-26s %-7s %-8s %s"
          % ("id", "title", "mode", "verdict", "construct checks"))
    exposed = allowed = 0
    for p in puzzles:
        meta = p["meta"]
        rec = Recorder(os.path.join(p["dir"], "solution.py"), meta.get("mode"))
        try:
            load_tests(p["dir"]).check(rec)
        except Exception as e:
            print("  %-5s REC-FAIL: %s" % (p["id"], e))
            continue
        guard = lesson_guard(p, rec)
        lesson = sorted(check_inventory(p["dir"]) & LESSON_CHECKS)
        if guard == "exposed":
            exposed += 1
            tag = "EXPOSED"
        elif guard == "allowed":
            allowed += 1
            tag = "allowed"
        else:
            tag = "ok" if meta.get("concept") else "drill"
        print("  %-5s %-26.26s %-7s %-8s %s"
              % (p["id"], meta.get("title", ""), meta.get("mode"), tag,
                 ", ".join(lesson) or "-"))
    print("\n%d exposed, %d documented residuals" % (exposed, allowed))
    return 1 if exposed else 0


def _prove_report(puzzles):
    """Prove every construct check earns its place: strip the construct layer
    from each puzzle that ships dodges and confirm a pinned dodge then slips
    through. Informational -- a puzzle whose dodges are caught behaviorally is
    surfaced, not failed (such a dodge is still a valid hardcode regression)."""
    print("discovered %d puzzles (proving construct checks load-bearing)\n"
          % len(puzzles))
    proven = behavioral = errored = 0
    for p in puzzles:
        try:
            res = prove_checks(p)
        except Exception as e:
            errored += 1
            print("  ERR  %-5s %s: %s" % (p["id"], type(e).__name__, e))
            continue
        if res is None:
            continue
        labels, removed = res
        if labels:
            proven += 1
            print("  ok   %-5s %d check(s) load-bearing -> dodge slips past once "
                  "gone: %s" % (p["id"], removed, "; ".join(labels)))
        else:
            behavioral += 1
            print("  --   %-5s %d construct check(s), but dodges still fail with "
                  "them stripped (caught behaviorally)" % (p["id"], removed))
    print("\n%d puzzles: a dodge proves the construct check is load-bearing"
          % proven)
    print("%d puzzles: dodges caught behaviorally (construct layer not exercised "
          "by a dodge)" % behavioral)
    if errored:
        print("%d puzzles errored" % errored)
    return 1 if errored else 0


def main():
    if "--engine" in sys.argv:
        return _engine_selftest()
    if "--keys" in sys.argv:
        return keys_selftest()
    puzzles = discover()
    if "--lessons" in sys.argv:
        return _lessons_report(puzzles)
    if "--prove-checks" in sys.argv:
        return _prove_report(puzzles)
    sidestep = "--sidestep" in sys.argv
    print("discovered %d puzzles%s"
          % (len(puzzles), " (with sidestep attack suite)" if sidestep else ""))
    bad = weak = unguarded = 0
    for p in puzzles:
        issues = conformance_issues(p)
        verdict = ""
        if not issues and sidestep:
            breaches, dodge_passes, guard = sidestep_report(p)
            if dodge_passes:
                weak += 1
                verdict = "  !! DODGE PASSES: %s" % ", ".join(dodge_passes)
            elif breaches and p["id"] in ALLOWED:
                verdict = ("  (%s ok by design: %s)"
                           % ("/".join(breaches), ALLOWED[p["id"]]))
            elif breaches:
                weak += 1
                verdict = "  !! SIDESTEPPABLE by: %s" % ", ".join(breaches)
            elif guard == "exposed":
                unguarded += 1
                verdict = ("  ?? UNGUARDED LESSON: teaches a construct, varies "
                           "its output, pins no construct check")
            elif guard == "allowed":
                verdict = ("  (lesson unpinned, ok by design: %s)"
                           % GUARDED_OK[p["id"]])
        if issues:
            bad += 1
            print("FAIL %-5s %s" % (p["id"], p["dir"]))
            for i in issues:
                print("      - %s" % i)
        else:
            print("ok   %-5s %s%s" % (p["id"], p["meta"].get("title", ""),
                                      verdict))
    print("\n%d/%d puzzles pass conformance" % (len(puzzles) - bad, len(puzzles)))
    if sidestep:
        print("%d/%d puzzles sidesteppable" % (weak, len(puzzles)))
        print("%d/%d puzzles with an unguarded lesson" % (unguarded, len(puzzles)))
    return 1 if (bad or weak or unguarded) else 0


if __name__ == "__main__":
    sys.exit(main())
