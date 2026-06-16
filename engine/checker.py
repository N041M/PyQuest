"""Orchestrates one `check`: load the puzzle's tests, build the tester, run
check()/bonus(), translate failures into the four categories, and render the
pass/fail screen.
"""

from .config import WIDTH, now
from .content import load_tests
from .state import (stat, save_progress, load_answers, ensure_workspace,
                    archive_work, current_puzzle, work_path)
from .toolkit import (Toolkit, PuzzleSyntaxError, MissingSymbolError,
                      WrongResultError, LessonNotUsedError, PuzzleCrashError,
                      short_tb)
from .render import (paint, banner, bar, indent, quote_block, cli, PAD,
                     OK, NO, STAR, ARROW, BOLT, RETRY)


SAVE_TIP = paint("Did you save work.py in your editor? Unsaved edits are the "
                 "#1 cause\nof a check that 'should' pass but doesn't.", "yellow")


def fail_nudge(prog, cur):
    mode = prog["mode"]
    if mode == "hard":
        attempts = stat(prog, cur["id"])["attempts"]
        if attempts >= 3:
            return "Hints are now available:  %s" % paint(cli("hint"), "yellow")
        return ("Hard mode: hints unlock after 3 attempts (%d so far)."
                % attempts)
    return "Stuck?  %s" % paint(cli("hint"), "yellow")


def cmd_check(puzzles, by_id, prog):
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print("No current puzzle.")
        return
    if not prog.get("active"):
        print(PAD + paint("No puzzle loaded.", "white", "bold"))
        print(PAD + "Start one first:  " + paint(cli("menu"), "green", "bold"))
        return
    answers = load_answers()
    ensure_workspace(cur, answers, active=True)   # reseed the puzzle, never the
    archive_work(cur, answers)            # welcome placeholder, if work.py is gone
    st = stat(prog, cur["id"])
    st["attempts"] += 1
    save_progress(prog)
    try:
        tests = load_tests(cur["dir"])
    except Exception:
        print("Internal: could not load this puzzle's tests.\n" + short_tb())
        return
    T = Toolkit(work_path(), cur["meta"].get("mode"))
    try:
        tests.check(T)
    except PuzzleSyntaxError as e:
        _fail("Syntax error -- Python could not read your file",
              "Python stopped at %s\n\n"
              "This usually means a typo: a missing quote, parenthesis, colon,\n"
              "or wrong indentation. Open work.py and check that line."
              % e.detail, prog, cur)
    except MissingSymbolError as e:
        _fail("Missing piece -- something isn't defined yet",
              "Your file doesn't define `%s`.\n\n"
              "Check the spelling, or add it. For a function the brief asks for\n"
              "`%s`, define it with:  def %s(...):"
              % (e.name, e.name, e.name), prog, cur)
    except LessonNotUsedError as e:
        body = ("Your output is correct -- but this puzzle isn't really about "
                "the answer.\nIt's teaching a specific tool, and your solution "
                "reached the result\nanother way, so the lesson got skipped.\n\n"
                "%s\n%s\n\n%s\n%s"
                % (paint("This puzzle wants:", "green"),
                   quote_block(e.expected),
                   paint("Your code:", "yellow"), quote_block(e.actual)))
        if e.because:
            body = e.because + "\n\n" + body
        body += "\n\nRework it to use what the puzzle teaches, then check again."
        _almost("Correct answer -- but not this puzzle's lesson", body,
                prog, cur)
    except WrongResultError as e:
        body = ("%s\n%s\n\n%s\n%s"
                % (paint("Expected:", "green"), quote_block(e.expected),
                   paint("Got:", "red"), quote_block(e.actual)))
        if e.because:
            body = e.because + "\n\n" + body
        body += "\n\n" + SAVE_TIP
        _fail("Wrong result -- the code runs but the answer is off", body,
              prog, cur)
    except PuzzleCrashError as e:
        ctx = (" " + e.because) if e.because else ""
        _fail("Crash -- your code started but hit an error",
              "Python raised an error%s:\n\n%s\n\n"
              "Read the error name: it points at what went wrong.\n\n%s"
              % (ctx, quote_block(e.detail), SAVE_TIP), prog, cur)
    except Exception:
        _fail("Crash -- your code hit an error",
              quote_block(short_tb()), prog, cur)
    else:
        if cur["id"] not in prog["completed"]:
            prog["completed"].append(cur["id"])
            stat(prog, cur["id"])["solved_on"] = now()[:10]   # first-solve date
        save_progress(prog)
        archive_work(cur, answers, solved=True)
        _solved(cur, prog, puzzles)
        _run_bonus(tests, T)


def _run_bonus(tests, T):
    """Optional, non-blocking performance/elegance check after a correct pass.

    A puzzle's tests.py may define `bonus(T)`. It runs only once the answer is
    already accepted, and prints a separate advisory line -- it never blocks
    progress. The LeetCode-style 'correct, and also fast?' split.
    """
    fn = getattr(tests, "bonus", None)
    if not callable(fn):
        return
    try:
        fn(T)
    except (WrongResultError, PuzzleCrashError) as e:
        why = getattr(e, "because", "") or "this works, but could be more efficient"
        print("")
        print(PAD + paint(BOLT + " bonus: not optimal yet — " + why, "yellow"))
    except Exception:
        pass                     # a buggy bonus must never block the learner
    else:
        print("")
        print(PAD + paint(BOLT + " bonus: optimal — efficient solution", "green",
                          "bold"))


def _fail(title, body, prog, cur):
    print(banner("%s  not yet" % NO, "red"))
    print("")
    print(PAD + paint(title, "bred", "bold"))
    print("")
    print(indent(body, PAD))
    print("")
    print(PAD + fail_nudge(prog, cur))


def _almost(title, body, prog, cur):
    """Right answer, wrong lesson: a distinct screen from a plain failure --
    the output matched, only the approach missed the point. Still blocks
    progress (the lesson wasn't practiced), but says so without crying 'wrong'."""
    print(banner("%s  so close" % STAR, "yellow"))
    print("")
    print(PAD + paint(title, "byellow", "bold"))
    print("")
    print(indent(body, PAD))
    print("")
    print(PAD + fail_nudge(prog, cur))


def _solved(cur, prog, puzzles):
    print(banner("%s  solved" % OK, "green"))
    print("")
    print(PAD + "%s   %s"
          % (paint(cur["id"], "byellow", "bold"),
             paint(cur["meta"].get("title", ""), "bold", "white")))
    print(PAD + bar(len(prog["completed"]), len(puzzles), WIDTH - 18))
    print("")
    print(PAD + paint("your code is saved.", "gray"))
    nxt = next((p for p in puzzles if p["index"] == cur["index"] + 1), None)
    if nxt is None:
        print(PAD + paint("%s  that was the last puzzle in the course." % STAR,
                          "green", "bold"))
    else:
        print(PAD + paint(ARROW + " next", "cyan", "bold")
              + paint("   %s · %s" % (nxt["id"], nxt["meta"].get("title", "")),
                      "gray"))
    print(PAD + paint(RETRY + " retry", "magenta", "bold")
          + paint("   to clear it and solve again from scratch", "gray"))
