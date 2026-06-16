"""Project audit: solution conformance plus an anti-sidestep attack suite.

    python3 tools/audit.py             every solution.py must pass its own tests.py
    python3 tools/audit.py --sidestep  ALSO attack every puzzle with the adversaries
    python3 tools/audit.py --engine    self-test the execution guard & toolkit APIs

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
import re
import json
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
    # title + mode are structural (used everywhere / drives checking), so they
    # are required. concept + why are optional: a puzzle that teaches no new
    # syntax (a drill or capstone) simply omits them and stays out of the
    # textbook -- not every puzzle has to carry an entry.
    for key in ("title", "mode"):
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
        T.uses_class("Counter")             # the named class is present
        try:
            T.attr(obj, "missing")
        except MissingSymbolError:
            pass
        else:
            raise AssertionError("missing attr should be translated")
        os.unlink(path)

    def t_uses_class_named():
        """uses_class(name) ties the check to the symbol under test, so a decoy
        `class X: pass` beside a namedtuple can't satisfy it -- the AST-only
        cover for object puzzles, which have no liveness."""
        from engine.toolkit import LessonNotUsedError
        dodge = ("class _Decoy:\n    pass\n"
                 "from collections import namedtuple\n"
                 "Dog = namedtuple('Dog', ['name', 'age'])\n")
        path, T = learner(dodge)
        T.uses_class()                      # *a* class exists -> generic passes
        try:
            T.uses_class("Dog")             # but no `class Dog:` -> fails
        except LessonNotUsedError:
            os.unlink(path)
            return
        raise AssertionError("a decoy class satisfied uses_class('Dog')")

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

    def t_generator_backstop():
        """is_generator + uses_yield make a generators puzzle sidestep-proof:
        a real generator passes both; a list-returning function with a dead
        yield fails the behavioral check; a bare genexpr fails the AST check."""
        from engine.toolkit import LessonNotUsedError
        # a real yield-based generator passes both checks
        path, T = learner("def g(n):\n    for i in range(n):\n        "
                          "yield i * i\n")
        gen = T.call("g", 3)
        T.is_generator(gen)
        T.uses_yield()
        assert list(gen) == [0, 1, 4]
        os.unlink(path)
        # a list (the obvious sidestep) must fail the behavioral check
        path, T = learner("def g(n):\n    return [i * i for i in range(n)]\n")
        try:
            T.is_generator(T.call("g", 3))
        except WrongResultError:
            os.unlink(path)
        else:
            os.unlink(path)
            raise AssertionError("is_generator must reject a list")
        # a bare generator expression is a generator, but uses no yield
        path, T = learner("def g(n):\n    return (i * i for i in range(n))\n")
        T.is_generator(T.call("g", 3))
        try:
            T.uses_yield()
        except LessonNotUsedError:
            os.unlink(path)
            return
        os.unlink(path)
        raise AssertionError("uses_yield must reject a bare genexpr")

    def t_with_open_construct():
        """uses_with_open demands the FILE be opened with `with`. A live
        `with io.StringIO()` wrapping a print satisfies the generic uses_with
        but must NOT satisfy uses_with_open while the file is read bare -- the
        files-chapter hole the targeted check closes."""
        from engine.toolkit import LessonNotUsedError
        real = "with open('note.txt') as f:\n    t = f.read()\nprint(t)\n"
        path, T = learner(real, mode="script")
        T.timeout = 5
        T.run(files={"note.txt": "hello"})
        T.uses_with_open()                      # the file is opened with `with`
        os.unlink(path)

        dodge = ("import io\n"
                 "t = open('note.txt').read()\n"
                 "with io.StringIO() as s:\n    print(t)\n")
        path, T = learner(dodge, mode="script")
        T.timeout = 5
        T.run(files={"note.txt": "hello"})
        T.uses_with()                           # the generic check is fooled
        try:
            T.uses_with_open()                  # the targeted check is not
        except LessonNotUsedError:
            os.unlink(path)
            return
        raise AssertionError("an unrelated `with` satisfied uses_with_open")

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

    def t_user_lifecycle():
        # delete/rename move whole profile folders; pin both, plus their
        # refusals (missing source, occupied target). Uses clearly-namespaced
        # throwaway profiles and cleans up, so it never touches real users.
        import shutil
        from engine.state import (delete_user, rename_user, list_users,
                                  ensure_user, user_dir)
        a, b = "_selftest_a", "_selftest_b"
        for n in (a, b):
            if os.path.isdir(user_dir(n)):
                shutil.rmtree(user_dir(n))
        try:
            ensure_user(a)
            assert a in list_users()
            assert rename_user(a, b)                  # a -> b
            assert b in list_users() and a not in list_users()
            assert not rename_user("_nope_", a)       # missing source refused
            ensure_user(a)
            assert not rename_user(b, a)              # occupied target refused
            assert delete_user(a) and delete_user(b)
            assert a not in list_users() and b not in list_users()
            assert not delete_user(b)                 # already gone
        finally:
            for n in (a, b):
                if os.path.isdir(user_dir(n)):
                    shutil.rmtree(user_dir(n))

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

    def t_textbook_omits_empty():
        # Not every puzzle earns a textbook entry: one with neither a concept
        # nor a why is left out, a chapter with nothing to teach drops entirely,
        # and a section (Syntax/Tips) appears only when it has content.
        from engine.commands.views import _textbook_md, _has_entry

        def P(ch, title, concept=None, why=None):
            m = {"title": title}
            if concept:
                m["concept"] = concept
            if why:
                m["why"] = why
            return {"ch_num": ch, "ch_title": "Ch%d" % ch, "meta": m}

        assert _has_entry(P(1, "x", concept="c"))
        assert _has_entry(P(1, "x", why="w"))
        assert not _has_entry(P(1, "x"))          # neither -> no entry

        shown = [P(1, "Has syntax", concept="syn"),
                 P(1, "Drill only"),              # no entry -> omitted
                 P(2, "Cap A"), P(2, "Cap B"),    # whole chapter empty -> gone
                 P(3, "Tip only", why="tip")]
        md = _textbook_md(shown, full=False, total=2)
        assert "Has syntax" in md and "syn" in md
        assert "Drill only" not in md             # entry-less puzzle omitted
        assert "Cap A" not in md and "Ch2" not in md  # empty chapter dropped
        assert md.count("### Tips") == 1          # only ch3 carries a tip
        assert "2 of 2 topics" in md              # count is entries, not puzzles
        assert not md.rstrip().endswith("---")    # no rule left dangling

    def t_command_registry():
        from engine.commands.registry import (canonical, suggest,
                                              NEEDS_PUZZLE, CANONICAL)
        # aliases fold to their canonical verb; empty input is status
        assert canonical("load") == "goto"
        assert canonical("replay") == "retry"
        assert canonical("users") == "user"
        assert canonical("current") == "status"
        assert canonical("") == "status"
        # did-you-mean catches near-misses and gives up on noise
        assert suggest("helpp") == "help", suggest("helpp")
        assert suggest("chekc") == "check", suggest("chekc")
        assert suggest("zzzzz") is None
        # the puzzle-context set is exactly the verbs that act on a loaded puzzle
        assert {"check", "hint", "solution", "next", "skip", "retry",
                "revert"} <= NEEDS_PUZZLE
        assert not (NEEDS_PUZZLE & {"status", "goto", "begin", "map", "help"})
        assert NEEDS_PUZZLE <= CANONICAL
        # dispatch and registry must not drift: every verb app.main switches on
        # is a registry verb, and every registry verb is dispatched.
        from engine.config import ROOT
        src = open(os.path.join(ROOT, "engine", "app.py")).read()
        dispatched = set(re.findall(r'cmd == "([a-z]+)"', src))
        assert dispatched == CANONICAL, \
            "dispatch/registry drift: %s" % sorted(dispatched ^ CANONICAL)

    def t_transfer_sanitize():
        # An imported bundle is untrusted: it may be stale (ids gone from this
        # version), hand-edited (inflated highest to unlock the course), or
        # malformed. The sanitizers must scrub it back to something safe before
        # it becomes a profile -- pin both directions: hostile in, clean out;
        # already-valid in, unchanged out. Pure functions, so no filesystem.
        from engine.commands.transfer import (_sanitize_progress,
                                              _sanitize_answers)
        puzzles = [{"id": "1.1", "index": 0}, {"id": "1.2", "index": 1},
                   {"id": "2.1", "index": 2}]
        by_id = {p["id"]: p for p in puzzles}

        hostile = {
            "mode": "wizard",                       # not a real mode
            "completed": ["1.1", "9.9", "1.1", "2.1"],  # unknown id + duplicate
            "highest": 999,                         # inflated to skip the gate
            "stats": {"1.1": {"attempts": 3, "hints_used": 1},
                      "9.9": {"attempts": 5}},      # stat for a gone puzzle
            "current": "9.9",                       # parked on a gone puzzle
            "active": False,
        }
        out, dropped = _sanitize_progress(hostile, by_id, puzzles)
        assert out["mode"] == "normal", out["mode"]
        assert out["completed"] == ["1.1", "2.1"], out["completed"]  # drop+dedupe
        assert out["stats"] == {"1.1": {"attempts": 3, "hints_used": 1}}, \
            out["stats"]
        assert out["current"] == "1.1", out["current"]   # gone -> first puzzle
        assert out["highest"] == 2, out["highest"]        # recomputed, not 999
        assert out["active"] is True, out["active"]       # has progress
        assert dropped == 2, dropped                      # 9.9 + the duplicate

        # a clean, valid profile must pass through untouched (idempotent)
        good = {"mode": "hard", "completed": ["1.1"], "highest": 7,
                "stats": {}, "current": "1.2", "active": True}
        out2, dropped2 = _sanitize_progress(good, by_id, puzzles)
        assert dropped2 == 0, dropped2
        assert out2["mode"] == "hard" and out2["completed"] == ["1.1"]
        assert out2["current"] == "1.2"
        assert out2["highest"] == 1, out2["highest"]      # max(idx 1.1=0, 1.2=1)

        ans = _sanitize_answers({"1.1": {"solved": True, "code": "print(1)"},
                                 "9.9": {"solved": True, "code": "x"},  # gone
                                 "2.1": "not a dict"},                  # malformed
                                by_id)
        assert set(ans) == {"1.1"}, set(ans)
        assert ans["1.1"] == {"solved": True, "code": "print(1)"}, ans["1.1"]

    for fn in (t_exit, t_hang_call, t_hang_unswallowable, t_stdin_in_raises,
               t_print_captured, t_sandbox_files, t_file_missing_translated,
               t_classes, t_uses_class_named,
               t_does_not_mutate, t_does_not_mutate_uncopyable,
               t_eq_case_sensitive, t_deep_approx, t_new_constructs,
               t_generator_backstop, t_with_open_construct,
               t_raises_still_works, t_liveness_dead_chaff,
               t_liveness_real_constructs, t_line_checks, t_lesson_not_used,
               t_structural_checks,
               t_liveness_import_mode, t_atomic_write_json, t_corrupt_backup,
               t_username_validation, t_user_lifecycle,
               t_discover_tolerates_bad_meta, t_textbook_omits_empty,
               t_command_registry, t_transfer_sanitize):
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
