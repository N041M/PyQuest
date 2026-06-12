"""Project audit: solution conformance plus an anti-sidestep replay attack.

    python3 audit.py             every solution.py must pass its own tests.py
    python3 audit.py --sidestep  ALSO attack every puzzle with a replay dodge
    python3 audit.py --engine    self-test the execution guard & toolkit APIs

The replay attack is a generic adversary: it records every (stdin -> stdout)
or (function call -> return value) the tests exercise against the reference
solution, writes an impostor program that just replays that table, and runs
the tests again on the impostor -- twice. A puzzle is SIDESTEPPABLE if the
impostor ever passes: its answers can be hardcoded without using the lesson.

Randomized inputs defeat the replay (fresh inputs miss the table); construct
checks defeat it too (the impostor contains no loops, operators, try blocks,
comprehensions...). A puzzle should be saved by at least one of the two.

Not part of the engine; safe to delete.
"""

import io
import os
import json
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.content import discover, load_tests, load_hints
from engine.toolkit import (Toolkit, PuzzleSyntaxError, MissingSymbolError,
                            WrongResultError, PuzzleCrashError)

# Puzzles where a passing replay is the accepted ceiling: the lesson IS
# producing a fixed output with a construct the impostor must also use --
# so "the dodge" and a legitimate answer are the same program.
ALLOWED = {
    "1.1": "the lesson is printing one fixed literal; any print of it is legit",
}


# ---- recording -------------------------------------------------------------
class Recorder(Toolkit):
    """A Toolkit that remembers everything the tests fed the solution."""

    def __init__(self, path, mode):
        Toolkit.__init__(self, path, mode)
        self.stdin_runs = []        # (stdin, normalized stdout)
        self.fn_calls = []          # (name, args, kwargs, result)

    def run(self, stdin=""):
        out = Toolkit.run(self, stdin)
        self.stdin_runs.append((stdin, out))
        return out

    def call(self, name, *args, **kwargs):
        result = Toolkit.call(self, name, *args, **kwargs)
        self.fn_calls.append((name, args, kwargs, result))
        return result


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


def replay_attack(p, attempts=2):
    """Record the solution's run, then attack with the impostor.

    Returns (verdict, detail): verdict is 'robust', 'SIDESTEPPABLE', or
    'allowed' (a known, accepted ceiling -- see ALLOWED)."""
    sol = os.path.join(p["dir"], "solution.py")
    rec = Recorder(sol, p["meta"].get("mode"))
    load_tests(p["dir"]).check(rec)          # conformance already verified
    if not rec.stdin_runs and not rec.fn_calls:
        return "robust", "tests use neither run() nor call()"
    src = build_impostor(rec)
    fd, path = tempfile.mkstemp(suffix=".py", prefix="pyquest_impostor_")
    os.close(fd)
    with open(path, "w") as f:
        f.write(src)
    passes = 0
    try:
        for _ in range(attempts):
            tests = load_tests(p["dir"])     # fresh randomness each attempt
            try:
                tests.check(Toolkit(path, p["meta"].get("mode")))
            except (PuzzleSyntaxError, MissingSymbolError, WrongResultError,
                    PuzzleCrashError):
                continue
            except Exception:
                continue
            passes += 1
    finally:
        os.unlink(path)
    if passes == 0:
        return "robust", ""
    if p["id"] in ALLOWED:
        return "allowed", ALLOWED[p["id"]]
    return "SIDESTEPPABLE", ("impostor passed %d/%d attempts"
                             % (passes, attempts))


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
    Run after any change to toolkit.py."""
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
               t_classes, t_does_not_mutate, t_deep_approx, t_new_constructs,
               t_raises_still_works, t_atomic_write_json, t_corrupt_backup,
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
          % (len(puzzles), " (with replay attack)" if sidestep else ""))
    bad = weak = 0
    for p in puzzles:
        issues = conformance_issues(p)
        verdict = ""
        if not issues and sidestep:
            v, detail = replay_attack(p)
            if v == "SIDESTEPPABLE":
                weak += 1
                verdict = "  !! SIDESTEPPABLE: %s" % detail
            elif v == "allowed":
                verdict = "  (replay ok by design: %s)" % detail
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
        print("%d/%d puzzles sidesteppable by replay" % (weak, len(puzzles)))
    return 1 if (bad or weak) else 0


if __name__ == "__main__":
    sys.exit(main())
