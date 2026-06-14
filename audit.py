"""Project audit: solution conformance plus an anti-sidestep attack suite.

    python3 audit.py             every solution.py must pass its own tests.py
    python3 audit.py --sidestep  ALSO attack every puzzle with the adversaries
    python3 audit.py --engine    self-test the execution guard & toolkit APIs

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

Not part of the engine; safe to delete.
"""

import io
import os
import json
import sys
import tempfile
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.content import discover, load_tests, load_hints
from engine.toolkit import (Toolkit, PuzzleSyntaxError, MissingSymbolError,
                            WrongResultError, PuzzleCrashError)

# Puzzles where a passing impostor is the accepted ceiling: the cheapest
# program that passes IS a legitimate answer to the lesson.
ALLOWED = {
    "1.1": "the lesson is printing one fixed literal; any print of it is legit",
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
    """Attack one puzzle with every adversary.

    Returns (breaches, dodge_passes): generic impostors that passed, and
    pinned dodges that passed (the latter are never acceptable)."""
    sol = os.path.join(p["dir"], "solution.py")
    rec = Recorder(sol, p["meta"].get("mode"))
    load_tests(p["dir"]).check(rec)          # conformance already verified
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
    return breaches, dodge_passes


# ---- conformance (every solution passes its own tests) ---------------------
def conformance_issues(p):
    issues = []
    meta = p["meta"]
    if meta.get("id") != p["id"]:
        issues.append("meta id %r != folder id %r" % (meta.get("id"), p["id"]))
    for key in ("title", "concept", "mode", "why"):
        if not meta.get(key):
            issues.append("meta missing %r" % key)
    if meta.get("mode") not in ("script", "import"):
        issues.append("bad mode %r" % meta.get("mode"))
    hints = load_hints(p["dir"])
    if len(hints) != 3:
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
    return issues


# ---- engine self-test: the guard's guarantees, pinned ----------------------
def _engine_selftest():
    """Every protection the execution guard promises, verified directly.
    Run after any change to the toolkit package."""
    results = []

    def case(label, fn):
        try:
            fn()
        except AssertionError as e:
            results.append((label, "FAIL: %s" % e))
        except Exception as e:
            results.append((label, "FAIL: %s: %s" % (type(e).__name__, e)))
        else:
            results.append((label, "ok"))

    def learner(code, mode="import"):
        fd, path = tempfile.mkstemp(suffix=".py", prefix="pyquest_selftest_")
        os.close(fd)
        with open(path, "w") as f:
            f.write(code)
        return path, Toolkit(path, mode, timeout=1)

    def crashes(fn, fragment):
        try:
            fn()
        except PuzzleCrashError as e:
            assert fragment in str(e.detail), (
                "crash message %r lacks %r" % (e.detail, fragment))
            return
        raise AssertionError("expected a translated crash")

    def t_exit():
        path, T = learner("exit()\n")
        crashes(T.load, "exit()")
        os.unlink(path)

    def t_hang_call():
        path, T = learner("def f():\n    while True:\n        pass\n")
        crashes(lambda: T.call("f"), "longer than")
        os.unlink(path)

    def t_hang_unswallowable():
        path, T = learner("def f():\n    while True:\n        try:\n"
                          "            pass\n        except Exception:\n"
                          "            pass\n")
        crashes(lambda: T.call("f"), "longer than")
        os.unlink(path)

    def t_stdin_in_raises():
        path, T = learner("def f():\n    input()\n")
        crashes(lambda: T.raises(ValueError, "f"), "input()")
        os.unlink(path)

    def t_print_captured():
        path, T = learner("def f():\n    print('noise')\n    return 7\n")
        assert T.call("f") == 7
        assert T.printed == "noise\n", "stdout not captured: %r" % T.printed
        os.unlink(path)

    def t_sandbox_files():
        path, T = learner("text = open('in.txt').read()\n"
                          "open('out.txt', 'w').write(text.upper())\n",
                          mode="script")
        T.timeout = 5                      # subprocess startup needs headroom
        T.run(files={"in.txt": "abc"})
        assert T.file("out.txt") == "ABC"
        assert not os.path.exists("out.txt"), "leaked into the project dir"
        os.unlink(path)

    def t_file_missing_translated():
        path, T = learner("pass\n", mode="script")
        T.timeout = 5
        T.run()
        try:
            T.file("never.txt")
        except WrongResultError:
            os.unlink(path)
            return
        raise AssertionError("missing file should be a translated failure")

    def t_classes():
        path, T = learner(
            "class Counter:\n"
            "    def __init__(self, start):\n        self.n = start\n"
            "    def bump(self):\n        self.n += 1\n        return self.n\n")
        obj = T.make("Counter", 5)
        assert T.method(obj, "bump") == 6
        assert T.attr(obj, "n") == 6
        try:
            T.attr(obj, "missing")
        except MissingSymbolError:
            pass
        else:
            raise AssertionError("missing attr should be translated")
        os.unlink(path)

    def t_does_not_mutate():
        path, T = learner("def sort_copy(nums):\n    nums.sort()\n"
                          "    return nums\n")
        try:
            T.does_not_mutate("sort_copy", [3, 1, 2])
        except WrongResultError:
            os.unlink(path)
            return
        raise AssertionError("in-place sort should be caught")

    def t_does_not_mutate_uncopyable():
        # An uncopyable arg must raise loudly, never silently waive the lesson.
        path, T = learner("def f(x):\n    return x\n")
        try:
            T.does_not_mutate("f", (i for i in range(3)))   # generators: no deepcopy
        except RuntimeError as e:
            assert "deep-copyable" in str(e), "wrong message: %s" % e
            os.unlink(path)
            return
        raise AssertionError("uncopyable arg must raise, not skip the check")

    def t_eq_case_sensitive():
        # Capitalisation is part of the answer by default; leniency is opt-in.
        path, T = learner("pass\n")
        T.eq("Hello, World!", "Hello, World!")              # exact match -> ok
        T.eq("hello", "HELLO", match_case=False)            # opt out -> ok
        try:
            T.eq("hello, world!", "Hello, World!")          # wrong case -> fail
        except WrongResultError:
            os.unlink(path)
            return
        raise AssertionError("eq must reject wrong casing by default")

    def t_deep_approx():
        path, T = learner("pass\n")
        T.approx([1.0000000001, (2.0, 3)], [1, (2, 3.0000000001)])
        T.approx({"a": 0.1 + 0.2}, {"a": 0.3}, tol=1e-9)
        try:
            T.approx([1, 2], [1, 9])
        except WrongResultError:
            os.unlink(path)
            return
        raise AssertionError("wrong nested value should fail")

    def t_new_constructs():
        path, T = learner(
            "import json\nwith open('x') as f:\n    pass\n"
            "class A:\n    pass\n"
            "def g():\n    yield 1\n"
            "h = lambda x: x\n")
        T.uses_with(); T.uses_import("json"); T.uses_class()
        T.uses_yield(); T.uses_lambda()
        try:
            T.uses_import("random")
        except WrongResultError:
            os.unlink(path)
            return
        raise AssertionError("uses_import('random') should fail here")

    def t_raises_still_works():
        path, T = learner("def f(x):\n    if x < 0:\n"
                          "        raise ValueError('no')\n    return x\n")
        T.raises(ValueError, "f", -1)
        assert T.call("f", 3) == 3
        os.unlink(path)

    def t_liveness_dead_chaff():
        """Decorative code can't satisfy a construct check anymore."""
        path, T = learner("print(14)\nprint(20)\nq = 1 * 1\n"
                          "if False:\n    pass\n", mode="script")
        T.timeout = 5
        T.run()
        for check, arg in ((T.uses_op, "*"), (T.uses_if, None)):
            try:
                check(arg) if arg else check()
            except WrongResultError as e:
                assert "decorative" in str(e.actual), e.actual
                continue
            raise AssertionError("dead chaff satisfied %s" % check.__name__)
        os.unlink(path)

    def t_liveness_real_constructs():
        """...but genuinely used constructs still pass."""
        path, T = learner("print(2 + 3 * 4)\nprint((2 + 3) * 4)\n",
                          mode="script")
        T.timeout = 5
        T.run()
        T.uses_op("*")
        T.uses_op("+", min_count=2)
        T.uses_print()
        os.unlink(path)

    def t_line_checks():
        """The prescribed-expression checks accept the lesson's shape and
        reject the same constants computed another way."""
        path, T = learner("print(2 + 3 * 4)\nprint((2 + 3) * 4)\n",
                          mode="script")
        T.timeout = 5
        T.run()
        T.line_shape(0, "+", "*")
        T.line_shape(1, "*", "+")
        T.line_only_literals(0, {2, 3, 4})
        T.line_uses_op(0, "*")
        try:
            T.line_shape(0, "*", "+")        # line 1 has no parenthesized +
        except WrongResultError:
            os.unlink(path)
            return
        raise AssertionError("line_shape accepted the wrong grouping")

    def t_lesson_not_used():
        """Construct checks raise LessonNotUsedError -- the 'right answer,
        wrong lesson' category checker.py renders as its own screen -- and
        uses_boolop pins a combined condition against the one-modulo dodge."""
        from engine.toolkit import LessonNotUsedError
        path, T = learner("n = int(input())\n"
                          "print(n % 2 == 0 and n % 3 == 0)\n", mode="script")
        T.timeout = 5
        T.run(stdin="12\n"); T.run(stdin="5\n")     # a True case and a False
        T.uses_boolop()                             # a real `and` passes
        os.unlink(path)
        path, T = learner("print(int(input()) % 6 == 0)\n", mode="script")
        T.timeout = 5
        T.run(stdin="12\n"); T.run(stdin="5\n")
        try:
            T.uses_boolop()                         # the dodge has no bool op
        except LessonNotUsedError:
            os.unlink(path)
            return
        raise AssertionError("one-modulo dodge satisfied uses_boolop, or the "
                             "failure wasn't a LessonNotUsedError")

    def t_structural_checks():
        """uses_nested_if tells a body-nested if from an elif chain (they
        differ in the AST), and uses_default_param tells a default parameter
        from an *args fallback -- both raise LessonNotUsedError when missed."""
        from engine.toolkit import LessonNotUsedError
        nested = ("n = int(input())\nif n > 0:\n    if n < 100:\n"
                  "        print('s')\n    else:\n        print('b')\n"
                  "else:\n    print('np')\n")
        flat = ("n = int(input())\nif n <= 0:\n    print('np')\n"
                "elif n < 100:\n    print('s')\nelse:\n    print('b')\n")
        path, T = learner(nested, mode="script")
        T.timeout = 5
        T.run(stdin="50\n"); T.run(stdin="-1\n")
        T.uses_nested_if()                          # real nesting passes
        os.unlink(path)
        path, T = learner(flat, mode="script")
        T.timeout = 5
        T.run(stdin="50\n"); T.run(stdin="-1\n")
        try:
            T.uses_nested_if()                      # an elif chain is not nesting
        except LessonNotUsedError:
            pass
        else:
            raise AssertionError("flat elif chain satisfied uses_nested_if")
        os.unlink(path)
        path, T = learner("def f(a, b='x'):\n    return a + b\n")
        T.uses_default_param("f")                   # a real default passes
        try:
            T.uses_default_param("missing")
        except LessonNotUsedError:
            pass
        else:
            raise AssertionError("uses_default_param matched a missing function")
        os.unlink(path)
        path, T = learner("def f(a, *r):\n    return a\n")
        try:
            T.uses_default_param("f")               # *args is not a default
        except LessonNotUsedError:
            os.unlink(path)
            return
        raise AssertionError("*args satisfied uses_default_param")

    def t_liveness_import_mode():
        """A dead self-call can't fake recursion; a real one passes."""
        path, T = learner(
            "def fact(n):\n"
            "    out = 1\n"
            "    for i in range(2, n + 1):\n"
            "        out *= i\n"
            "    if False:\n"
            "        fact(0)\n"
            "    return out\n")
        assert T.call("fact", 5) == 120
        try:
            T.uses_call("fact")
        except WrongResultError as e:
            assert "decorative" in str(e.actual), e.actual
        else:
            raise AssertionError("dead self-call faked recursion")
        os.unlink(path)
        path, T = learner(
            "def fact(n):\n"
            "    return 1 if n <= 1 else n * fact(n - 1)\n")
        assert T.call("fact", 5) == 120
        T.uses_call("fact")
        os.unlink(path)

    def t_atomic_write_json():
        from engine.config import write_json
        d = tempfile.mkdtemp(prefix="pyquest_selftest_")
        path = os.path.join(d, "x.json")
        write_json(path, {"a": 1})
        write_json(path, {"a": 2})                  # replace, not append
        assert json.load(open(path)) == {"a": 2}
        leftovers = [f for f in os.listdir(d) if f != "x.json"]
        assert not leftovers, "temp files left behind: %r" % leftovers

    def t_corrupt_backup():
        from engine.state import backup_corrupt
        d = tempfile.mkdtemp(prefix="pyquest_selftest_")
        path = os.path.join(d, "progress.json")
        open(path, "w").write("{ not json")
        old_err = sys.stderr
        sys.stderr = io.StringIO()
        try:
            backup = backup_corrupt(path)
        finally:
            sys.stderr = old_err
        assert backup and os.path.exists(backup), "no backup made"
        assert not os.path.exists(path), "corrupt file still in place"
        assert open(backup).read() == "{ not json", "evidence altered"

    def t_username_validation():
        from engine.state import valid_username
        for good in ("alice", "user_2", "a-b", "X" * 32):
            assert valid_username(good), "%r should be valid" % good
        for bad in ("../evil", "/tmp/x", "a b", "", ".", "x" * 33, "a.b"):
            assert not valid_username(bad), "%r should be rejected" % bad

    def t_discover_tolerates_bad_meta():
        from engine.config import CHAPTERS_DIR
        from engine.content import discover
        bad_dir = os.path.join(CHAPTERS_DIR, "98_selftest_tmp", "01_bad")
        os.makedirs(bad_dir, exist_ok=True)
        try:
            with open(os.path.join(bad_dir, "meta.json"), "w") as f:
                f.write("{ not json")
            old_err = sys.stderr
            sys.stderr = io.StringIO()
            try:
                ids = [p["id"] for p in discover()]
            finally:
                sys.stderr = old_err
            assert ids, "discovery returned nothing"
            assert not any(i.startswith("98.") for i in ids), \
                "broken puzzle was not skipped"
        finally:
            import shutil
            shutil.rmtree(os.path.join(CHAPTERS_DIR, "98_selftest_tmp"))

    for fn in (t_exit, t_hang_call, t_hang_unswallowable, t_stdin_in_raises,
               t_print_captured, t_sandbox_files, t_file_missing_translated,
               t_classes, t_does_not_mutate, t_does_not_mutate_uncopyable,
               t_eq_case_sensitive, t_deep_approx, t_new_constructs,
               t_raises_still_works, t_liveness_dead_chaff,
               t_liveness_real_constructs, t_line_checks, t_lesson_not_used,
               t_structural_checks,
               t_liveness_import_mode, t_atomic_write_json, t_corrupt_backup,
               t_username_validation, t_discover_tolerates_bad_meta):
        case(fn.__name__[2:], fn)

    bad = 0
    for label, verdict in results:
        print("%-26s %s" % (label, verdict))
        if verdict != "ok":
            bad += 1
    print("\n%d/%d engine self-tests pass" % (len(results) - bad, len(results)))
    return 1 if bad else 0


def main():
    if "--engine" in sys.argv:
        return _engine_selftest()
    sidestep = "--sidestep" in sys.argv
    puzzles = discover()
    print("discovered %d puzzles%s"
          % (len(puzzles), " (with sidestep attack suite)" if sidestep else ""))
    bad = weak = 0
    for p in puzzles:
        issues = conformance_issues(p)
        verdict = ""
        if not issues and sidestep:
            breaches, dodge_passes = sidestep_report(p)
            if dodge_passes:
                weak += 1
                verdict = "  !! DODGE PASSES: %s" % ", ".join(dodge_passes)
            elif breaches and p["id"] in ALLOWED:
                verdict = ("  (%s ok by design: %s)"
                           % ("/".join(breaches), ALLOWED[p["id"]]))
            elif breaches:
                weak += 1
                verdict = "  !! SIDESTEPPABLE by: %s" % ", ".join(breaches)
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
    return 1 if (bad or weak) else 0


if __name__ == "__main__":
    sys.exit(main())
