"""Engine self-test: every guarantee the execution guard and toolkit make,
verified directly. Split out of audit.py (`python3 tools/audit.py --engine`
dispatches here) because it tests the ENGINE, not the puzzles -- a different
concern from the conformance + anti-sidestep audit, and one that is emphatically
NOT "safe to delete". Run it after any change to engine/toolkit/.
"""

import io
import os
import re
import json
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from engine.toolkit import (Toolkit, PuzzleSyntaxError, MissingSymbolError,
                            WrongResultError, PuzzleCrashError)

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

    def t_uses_yield_scoped():
        """uses_yield(name) pins yield to the lesson's role: the named function's
        OWN body must yield. A genexpr target with a decoy yield parked in
        another function (or a dead yield in a nested inner function) passes the
        file-level uses_yield() but must fail the scoped uses_yield(name) -- the
        Ch10 generator hole found by the sidestep playbook."""
        from engine.toolkit import LessonNotUsedError
        # a real yield in the named function passes both forms
        path, T = learner("def gen(n):\n    for i in range(n):\n        yield i\n")
        T.uses_yield()
        T.uses_yield("gen")
        os.unlink(path)
        # yield from in the named function also counts
        path, T = learner("def gen(n):\n    yield from range(n)\n")
        T.uses_yield("gen")
        os.unlink(path)
        # but a yield from delegating to a COMPREHENSION is the forbidden genexpr
        # in disguise -- it must NOT satisfy the scoped check
        path, T = learner("def gen(n):\n    yield from (i for i in range(n))\n")
        try:
            T.uses_yield("gen")
        except LessonNotUsedError:
            os.unlink(path)
        else:
            os.unlink(path)
            raise AssertionError("yield from a genexpr satisfied uses_yield('gen')")
        # genexpr target + a decoy yield in an UNRELATED function: file-level
        # uses_yield() is fooled, scoped uses_yield("gen") is not
        dodge = ("def _decoy():\n    yield 1\n"
                 "def gen(n):\n    return (i for i in range(n))\n")
        path, T = learner(dodge)
        T.uses_yield()                          # fooled by the decoy
        try:
            T.uses_yield("gen")
        except LessonNotUsedError:
            pass
        else:
            os.unlink(path)
            raise AssertionError("decoy yield satisfied uses_yield('gen')")
        os.unlink(path)
        # a DEAD yield buried in a nested inner function is a different scope
        nested = ("def gen(n):\n    def _unused():\n        yield\n"
                  "    return (i for i in range(n))\n")
        path, T = learner(nested)
        try:
            T.uses_yield("gen")
        except LessonNotUsedError:
            os.unlink(path)
            return
        os.unlink(path)
        raise AssertionError("a nested-function yield satisfied uses_yield('gen')")

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
        # The textbook is a per-topic reference: each entry a section headed by
        # its `syntax` (code-formatted) or title, body = concept until a
        # reference.md exists. A puzzle with neither a concept nor a why earns no
        # entry, and a chapter with nothing to teach drops entirely.
        from engine.commands.views import _textbook_md, _has_entry

        def P(ch, title, concept=None, why=None, syntax=None):
            m = {"title": title}
            for k, v in (("concept", concept), ("why", why), ("syntax", syntax)):
                if v:
                    m[k] = v
            return {"ch_num": ch, "ch_title": "Ch%d" % ch, "meta": m}

        assert _has_entry(P(1, "x", concept="c"))
        assert _has_entry(P(1, "x", why="w"))
        assert not _has_entry(P(1, "x"))          # neither -> no entry

        shown = [P(1, "Indexing", concept="char by position", syntax="s[i]"),
                 P(1, "Drill only"),              # no entry -> omitted
                 P(2, "Cap A"), P(2, "Cap B"),    # whole chapter empty -> gone
                 P(3, "Tip only", why="mind the edges")]
        md = _textbook_md(shown, full=False, total=2)
        assert "### `s[i]`" in md and "char by position" in md  # syntax head + body
        assert "Drill only" not in md             # entry-less puzzle omitted
        assert "Cap A" not in md and "Ch2" not in md  # empty chapter dropped
        assert "### Tip only" in md and "mind the edges" in md  # why -> the body
        assert "### Syntax" not in md and "### Tips" not in md  # old bundles gone
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
                "restart"} <= NEEDS_PUZZLE
        assert not (NEEDS_PUZZLE & {"status", "goto", "menu", "map", "help"})
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

    def t_meta_audit():
        """The static meta-audit helpers, pinned (the audit auditing itself):
        check_inventory reads T.* calls from source; lesson_guard flags a
        varying-output construct lesson that pins no check and clears one that
        does; _strip_lesson_checks removes exactly the construct layer and
        leaves a runnable check()."""
        import shutil
        # the meta-audit helpers live in audit.py; import them at call time so
        # this module never imports audit at top (which would be a cycle).
        from audit import (check_inventory, lesson_guard, _strip_lesson_checks,
                           LESSON_CHECKS, GUARDED_OK)
        d = tempfile.mkdtemp(prefix="pyquest_selftest_")

        def write_tests(body):
            with open(os.path.join(d, "tests.py"), "w") as f:
                f.write(body)

        class Rec:                              # a stand-in Recorder
            def __init__(self, runs):
                self.stdin_runs = runs

        try:
            # check_inventory: exactly the T.<attr> names the source uses
            write_tests("def check(T):\n    T.eq(T.run(stdin='x'), 'y')\n"
                        "    T.uses_op('+')\n")
            inv = check_inventory(d)
            assert inv == {"eq", "run", "uses_op"}, inv
            assert inv & LESSON_CHECKS == {"uses_op"}, inv & LESSON_CHECKS

            teach = {"title": "t", "concept": "c", "mode": "script"}
            drill = {"title": "t", "mode": "script"}
            varying = Rec([("1\n", "a"), ("2\n", "b")])
            fixed = Rec([("1\n", "a"), ("2\n", "a")])

            def guard(meta, rec, pid="z.z"):
                return lesson_guard({"id": pid, "dir": d, "meta": meta}, rec)

            # teaches a construct + varies + no construct check -> EXPOSED
            write_tests("def check(T):\n    T.eq(T.run(), 'y')\n")
            assert guard(teach, varying) == "exposed"
            # a documented residual reports as allowed, never exposed
            assert guard(teach, varying, pid=sorted(GUARDED_OK)[0]) == "allowed"
            # fixed-output script -> synth already covers it -> not flagged
            assert guard(teach, fixed) is None
            # a drill (no concept) is never the lesson-guard's business
            assert guard(drill, varying) is None
            # ...and a construct check clears the exposure
            write_tests("def check(T):\n    T.eq(T.run(), 'y')\n"
                        "    T.uses_op('+')\n")
            assert guard(teach, varying) is None

            # _strip_lesson_checks: drop the construct calls, keep behavior,
            # and the survivor still runs
            check, removed = _strip_lesson_checks(
                "def check(T):\n    T.eq(1, 1)\n    T.uses_op('+')\n"
                "    T.uses_call('len')\n")
            assert removed == 2, removed

            class DummyT:                       # only eq should survive the strip
                def eq(self, a, b, **k):
                    assert a == b
                def uses_op(self, *a, **k):
                    raise AssertionError("uses_op was not stripped")
                def uses_call(self, *a, **k):
                    raise AssertionError("uses_call was not stripped")
            check(DummyT())
            none_check, none_removed = _strip_lesson_checks(
                "def check(T):\n    T.eq(1, 1)\n")
            assert none_removed == 0 and none_check is None
        finally:
            shutil.rmtree(d)

    def t_key_decode():
        """The stdlib key reader (engine/keys.py, the curses alternative): its
        import is platform-safe (termios/msvcrt stay lazy), and decode() maps
        each keypress's raw bytes to the right token -- CSI and SS3 arrows,
        Enter/Backspace/Tab, a lone ESC, EOF, and printables. Pure, so it is
        verified without a terminal; supported() is False in this piped run."""
        from engine import keys
        assert not keys.supported(), "raw input claimed under a pipe"
        d = keys.decode
        assert d(b"\x1b[A") == keys.UP and d(b"\x1bOA") == keys.UP
        assert d(b"\x1b[B") == keys.DOWN and d(b"\x1b[C") == keys.RIGHT
        assert d(b"\x1b[D") == keys.LEFT
        assert d(b"\r") == keys.ENTER and d(b"\n") == keys.ENTER
        assert d(b"\x7f") == keys.BACKSPACE and d(b"\t") == keys.TAB
        assert d(b"\x1b") == keys.ESC                  # lone ESC, no sequence
        assert d(b"") == keys.INTERRUPT and d(b"\x03") == keys.INTERRUPT
        assert d(b"q") == "q" and d(b"5") == "5"
        assert d(b"\x1b[Z") == keys.ESC                # unmapped CSI -> ESC
        assert d(b"\x01") == keys.ESC                  # non-printable control

    def t_i18n():
        """The language piping: English is the default + fallback, a valid pack
        translates via t(), a partial pack falls back per missing key, and a
        broken pack is rejected with a reason naming what's wrong -- never left
        active. (No language is shipped translated; this pins the plumbing.)"""
        import json
        import shutil
        from engine import i18n
        saved = i18n.LANG_DIR
        d = tempfile.mkdtemp(prefix="pyquest_selftest_")
        i18n.LANG_DIR = d

        def pack(code, files):
            os.makedirs(os.path.join(d, code))
            for name, content in files.items():
                with open(os.path.join(d, code, name), "w", encoding="utf-8") as f:
                    f.write(content)
        try:
            i18n.set_language("en")
            assert i18n.t("k", "Eng") == "Eng"            # default, no pack
            # a valid, PARTIAL pack
            pack("xx", {"pack.json": '{"name": "Test", "code": "xx"}',
                        "strings.json": '{"menu.play": "TR"}'})
            ok, msg = i18n.set_language("xx")
            assert ok and msg is None and i18n.current() == "xx"
            assert i18n.t("menu.play", "play") == "TR"          # translated
            assert i18n.t("menu.learn", "learn") == "learn"     # missing -> fallback
            assert ("xx", "Test") in i18n.available()
            # broken: no pack.json -> rejected, names it, reverts to English
            pack("yy", {"strings.json": "{}"})
            ok, msg = i18n.set_language("yy")
            assert not ok and "pack.json" in msg, msg
            assert i18n.current() == "en" and i18n.t("menu.play", "play") == "play"
            assert not any(c == "yy" for c, _ in i18n.available())
            # broken: invalid JSON -> rejected with a reason, reverts
            pack("zz", {"pack.json": "{ not json"})
            ok, msg = i18n.set_language("zz")
            assert not ok and "JSON" in msg and i18n.current() == "en", msg
        finally:
            i18n.LANG_DIR = saved
            i18n.set_language("en")
            shutil.rmtree(d)

    def t_i18n_content():
        """File-backed content overrides: a valid pack may translate the learner
        content files (reference.md, hints.md, brief.md) under a mirrored
        chapters/ tree. The loaders serve the override when present and fall back
        to the English file per-topic when not. A path outside chapters/ is never
        redirected (no traversal)."""
        import shutil
        from engine import i18n
        from engine.content import load_reference, load_hints, brief_path
        saved_lang, saved_ch = i18n.LANG_DIR, i18n.CHAPTERS_DIR
        root = tempfile.mkdtemp(prefix="pyquest_selftest_")
        chdir, lang = os.path.join(root, "chapters"), os.path.join(root, "lang")
        pz = os.path.join(chdir, "01_x", "01_y")
        os.makedirs(pz)
        for name, text in (("reference.md", "English reference\n"),
                           ("hints.md", "English hint\n"),
                           ("brief.md", "English brief\n")):
            with open(os.path.join(pz, name), "w", encoding="utf-8") as f:
                f.write(text)

        def valid_pack(code, files=None):
            pdir = os.path.join(lang, code)
            os.makedirs(pdir, exist_ok=True)
            with open(os.path.join(pdir, "pack.json"), "w", encoding="utf-8") as f:
                f.write('{"name": "%s", "code": "%s"}' % (code.upper(), code))
            with open(os.path.join(pdir, "strings.json"), "w", encoding="utf-8") as f:
                f.write("{}")
            for rel, content in (files or {}).items():
                fp = os.path.join(pdir, rel)
                os.makedirs(os.path.dirname(fp), exist_ok=True)
                with open(fp, "w", encoding="utf-8") as f:
                    f.write(content)

        def at(*parts):
            return os.path.join("chapters", "01_x", "01_y", *parts)

        i18n.LANG_DIR, i18n.CHAPTERS_DIR = lang, chdir
        try:
            # xx overrides all three files; yy is a valid pack translating none
            valid_pack("xx", {at("reference.md"): "Translated ref\n",
                              at("hints.md"): "Translated hint\n",
                              at("brief.md"): "Translated brief\n"})
            valid_pack("yy")
            i18n.set_language("en")                                    # defaults
            assert load_reference(pz).strip() == "English reference"
            assert load_hints(pz) == ["English hint"]
            assert brief_path(pz) == os.path.join(pz, "brief.md")
            ok, _ = i18n.set_language("xx")                            # overrides
            assert ok and load_reference(pz).strip() == "Translated ref"
            assert load_hints(pz) == ["Translated hint"]
            assert brief_path(pz) == os.path.join(lang, "xx", at("brief.md"))
            ok, _ = i18n.set_language("yy")                            # fallback
            assert ok and load_reference(pz).strip() == "English reference"
            assert load_hints(pz) == ["English hint"]
            assert brief_path(pz) == os.path.join(pz, "brief.md")
            # a path outside chapters/ is returned untouched, even with a pack on
            assert i18n.localized(os.path.join(root, "elsewhere.md")) == \
                os.path.join(root, "elsewhere.md")
        finally:
            i18n.LANG_DIR, i18n.CHAPTERS_DIR = saved_lang, saved_ch
            i18n.set_language("en")
            shutil.rmtree(root)

    for fn in (t_exit, t_hang_call, t_hang_unswallowable, t_stdin_in_raises,
               t_print_captured, t_sandbox_files, t_file_missing_translated,
               t_classes, t_uses_class_named,
               t_does_not_mutate, t_does_not_mutate_uncopyable,
               t_eq_case_sensitive, t_deep_approx, t_new_constructs,
               t_generator_backstop, t_uses_yield_scoped, t_with_open_construct,
               t_raises_still_works, t_liveness_dead_chaff,
               t_liveness_real_constructs, t_line_checks, t_lesson_not_used,
               t_structural_checks,
               t_liveness_import_mode, t_atomic_write_json, t_corrupt_backup,
               t_username_validation, t_user_lifecycle,
               t_discover_tolerates_bad_meta, t_textbook_omits_empty,
               t_command_registry, t_transfer_sanitize, t_meta_audit,
               t_key_decode, t_i18n, t_i18n_content):
        case(fn.__name__[2:], fn)

    bad = 0
    for label, verdict in results:
        print("%-26s %s" % (label, verdict))
        if verdict != "ok":
            bad += 1
    print("\n%d/%d engine self-tests pass" % (len(results) - bad, len(results)))
    return 1 if bad else 0


