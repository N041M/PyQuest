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
from .i18n import t


SAVE_TIP = paint(t("check.save_tip",
                   "Did you save work.py in your editor? Unsaved edits are the "
                   "#1 cause\nof a check that 'should' pass but doesn't."),
                 "yellow")


def fail_nudge(prog, cur):
    mode = prog["mode"]
    if mode == "hard":
        attempts = stat(prog, cur["id"])["attempts"]
        if attempts >= 3:
            return t("check.nudge_hints", "Hints are now available:  %s") % paint(
                cli("hint"), "yellow")
        return (t("check.nudge_hard",
                  "Hard mode: hints unlock after 3 attempts (%d so far).")
                % attempts)
    return t("check.nudge_stuck", "Stuck?  %s") % paint(cli("hint"), "yellow")


def cmd_check(puzzles, by_id, prog):
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print(t("ui.no_current", "No current puzzle."))
        return
    if not prog.get("active"):
        print(PAD + paint(t("check.no_loaded", "No puzzle loaded."),
                          "white", "bold"))
        print(PAD + t("check.start_first", "Start one first:  ")
              + paint(cli("menu"), "green", "bold"))
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
        print(t("check.tests_unloadable",
                "Internal: could not load this puzzle's tests.\n") + short_tb())
        return
    T = Toolkit(work_path(), cur["meta"].get("mode"))
    try:
        tests.check(T)
    except PuzzleSyntaxError as e:
        _fail(t("check.syntax_title",
                "Syntax error -- Python could not read your file"),
              t("check.syntax_body",
                "Python stopped at %s\n\n"
                "This usually means a typo: a missing quote, parenthesis, colon,\n"
                "or wrong indentation. Open work.py and check that line.")
              % e.detail, prog, cur)
    except MissingSymbolError as e:
        _fail(t("check.missing_title",
                "Missing piece -- something isn't defined yet"),
              t("check.missing_body",
                "Your file doesn't define `%s`.\n\n"
                "Check the spelling, or add it. For a function the brief asks for\n"
                "`%s`, define it with:  def %s(...):")
              % (e.name, e.name, e.name), prog, cur)
    except LessonNotUsedError as e:
        body = (t("check.lesson_body",
                  "Your output is correct -- but this puzzle isn't really about "
                  "the answer.\nIt's teaching a specific tool, and your solution "
                  "reached the result\nanother way, so the lesson got skipped.")
                + "\n\n%s\n%s\n\n%s\n%s"
                % (paint(t("check.lesson_wants", "This puzzle wants:"), "green"),
                   quote_block(e.expected),
                   paint(t("check.your_code", "Your code:"), "yellow"),
                   quote_block(e.actual)))
        if e.because:
            body = e.because + "\n\n" + body
        body += "\n\n" + t("check.lesson_rework",
                           "Rework it to use what the puzzle teaches, then "
                           "check again.")
        _almost(t("check.lesson_title",
                  "Correct answer -- but not this puzzle's lesson"), body,
                prog, cur)
    except WrongResultError as e:
        body = ("%s\n%s\n\n%s\n%s"
                % (paint(t("check.expected", "Expected:"), "green"),
                   quote_block(e.expected),
                   paint(t("check.got", "Got:"), "red"), quote_block(e.actual)))
        if e.because:
            body = e.because + "\n\n" + body
        body += "\n\n" + SAVE_TIP
        _fail(t("check.wrong_title",
                "Wrong result -- the code runs but the answer is off"), body,
              prog, cur)
    except PuzzleCrashError as e:
        ctx = (" " + e.because) if e.because else ""
        _fail(t("check.crash_title", "Crash -- your code started but hit an error"),
              t("check.crash_body",
                "Python raised an error%s:\n\n%s\n\n"
                "Read the error name: it points at what went wrong.\n\n%s")
              % (ctx, quote_block(e.detail), SAVE_TIP), prog, cur)
    except Exception:
        _fail(t("check.crash_title2", "Crash -- your code hit an error"),
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
        why = getattr(e, "because", "") or t(
            "check.bonus_default", "this works, but could be more efficient")
        print("")
        print(PAD + paint(BOLT + " " + t("check.bonus_no",
                          "bonus: not optimal yet — %s") % why, "yellow"))
    except Exception:
        pass                     # a buggy bonus must never block the learner
    else:
        print("")
        print(PAD + paint(BOLT + " " + t("check.bonus_yes",
                          "bonus: optimal — efficient solution"), "green",
                          "bold"))


def _fail(title, body, prog, cur):
    print(banner("%s  %s" % (NO, t("check.banner_not_yet", "not yet")), "red"))
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
    print(banner("%s  %s" % (STAR, t("check.banner_so_close", "so close")),
                 "yellow"))
    print("")
    print(PAD + paint(title, "byellow", "bold"))
    print("")
    print(indent(body, PAD))
    print("")
    print(PAD + fail_nudge(prog, cur))


def _solved(cur, prog, puzzles):
    print(banner("%s  %s" % (OK, t("check.banner_solved", "solved")), "green"))
    print("")
    print(PAD + "%s   %s"
          % (paint(cur["id"], "byellow", "bold"),
             paint(cur["meta"].get("title", ""), "bold", "white")))
    print(PAD + bar(len(prog["completed"]), len(puzzles), WIDTH - 18))
    print("")
    print(PAD + paint(t("check.code_saved", "your code is saved."), "gray"))
    nxt = next((p for p in puzzles if p["index"] == cur["index"] + 1), None)
    if nxt is None:
        print(PAD + paint("%s  %s" % (STAR, t("check.was_last",
                          "that was the last puzzle in the course.")),
                          "green", "bold"))
    else:
        print(PAD + paint(ARROW + " " + t("check.next", "next"), "cyan", "bold")
              + paint("   %s · %s" % (nxt["id"], nxt["meta"].get("title", "")),
                      "gray"))
    print(PAD + paint(RETRY + " " + t("check.retry", "retry"), "magenta", "bold")
          + paint("   " + t("check.retry_hint",
                            "to clear it and solve again from scratch"), "gray"))
