"""Orchestrates one `check`: load the puzzle's tests, build the tester, run
check()/bonus(), translate failures into the four categories, and render the
pass/fail screen.
"""

import hashlib
import datetime

from .config import WIDTH, now
from .content import load_tests
from .state import (stat, save_progress, load_answers, ensure_workspace,
                    archive_work, current_puzzle, work_path, solve_dates,
                    streak)
from .toolkit import (Toolkit, PuzzleSyntaxError, MissingSymbolError,
                      WrongResultError, LessonNotUsedError, PuzzleCrashError,
                      short_tb)
from .render import (paint, banner, bar, indent, quote_block, cli, PAD,
                     OK, NO, CUR, STAR, ARROW, BOLT, RETRY)
from .i18n import t, tp


def _save_tip():
    # Built per call, not at import: the active language is only set once
    # app.main() runs, so a module-level constant would freeze the English text.
    return paint(t("check.save_tip",
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
        print(PAD + (t("check.start_first", "Start one first:") + "  ")
              + paint(cli("menu"), "green", "bold"))
        return
    answers = load_answers()
    ensure_workspace(cur, answers, active=True)   # reseed the puzzle, never the
    entry = archive_work(cur, answers)    # welcome placeholder, if work.py is gone
    st = stat(prog, cur["id"])
    # The same bytes as the last attempt is almost always an unsaved editor
    # buffer -- their own #1 support issue. Remember a hash per puzzle so the
    # failure screen can SAY so instead of guessing (the generic save tip).
    sha = hashlib.sha1(entry.get("code", "")
                       .encode("utf-8", "replace")).hexdigest()
    unchanged = st["attempts"] > 0 and st.get("last_sha") == sha
    st["attempts"] += 1
    st["last_sha"] = sha
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
              % e.detail, prog, cur, unchanged)
    except MissingSymbolError as e:
        _fail(t("check.missing_title",
                "Missing piece -- something isn't defined yet"),
              t("check.missing_body",
                "Your file doesn't define `%s`.\n\n"
                "Check the spelling, or add it. For a function the brief asks for\n"
                "`%s`, define it with:  def %s(...):")
              % (e.name, e.name, e.name), prog, cur, unchanged)
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
                prog, cur, unchanged)
    except WrongResultError as e:
        diff = _first_diff(e.expected, e.actual)
        body = ("%s\n%s\n\n%s\n%s"
                % (paint(t("check.expected", "Expected:"), "green"),
                   quote_block(e.expected, mark=diff),
                   paint(t("check.got", "Got:"), "red"),
                   quote_block(e.actual, mark=diff)))
        if diff is not None:
            body += "\n\n" + paint(t("check.first_diff",
                                     "%s marks line %d -- the first line that "
                                     "differs.") % (CUR, diff + 1), "byellow")
        if e.because:
            body = e.because + "\n\n" + body
        if not unchanged:            # the precise notice below replaces the guess
            body += "\n\n" + _save_tip()
        _fail(t("check.wrong_title",
                "Wrong result -- the code runs but the answer is off"), body,
              prog, cur, unchanged)
    except PuzzleCrashError as e:
        ctx = (" " + e.because) if e.because else ""
        body = (t("check.crash_body",
                  "Python raised an error%s:\n\n%s\n\n"
                  "Read the error name: it points at what went wrong.\n\n%s")
                % (ctx, quote_block(e.detail),
                   "" if unchanged else _save_tip()))
        tip = _crash_tip(e.detail)
        if tip:
            body = body.rstrip() + "\n\n" + paint(tip, "yellow")
        _fail(t("check.crash_title",
                "Crash -- your code started but hit an error"), body,
              prog, cur, unchanged)
    except Exception:
        tb = short_tb()
        body = quote_block(tb)
        tip = _crash_tip(tb)
        if tip:
            body += "\n\n" + paint(tip, "yellow")
        _fail(t("check.crash_title2", "Crash -- your code hit an error"),
              body, prog, cur, unchanged)
    else:
        newly = cur["id"] not in prog["completed"]
        if newly:
            prog["completed"].append(cur["id"])
            stat(prog, cur["id"])["solved_on"] = now()[:10]   # first-solve date
        # Solving earns the spot: raise the high-water mark so the learner can
        # always revisit a puzzle they completed (an easy-mode free jump that
        # got solved must not be goto-locked after a switch to normal/hard --
        # the same entitlement import's sanitizer recomputes from `completed`).
        if cur["index"] > prog["highest"]:
            prog["highest"] = cur["index"]
        save_progress(prog)
        archive_work(cur, answers, solved=True)
        _solved(cur, prog, puzzles, newly)
        _run_bonus(tests, T)


def _crash_tip(detail):
    """A one-line beginner explanation for the exception named in a crash, or
    None. Shown UNDER the raw error, never instead of it -- the raw name/message
    is the thing being taught to read. Keyed on the name appearing in the
    detail text, so it covers script mode (stderr's last line) and import mode
    (the shortened traceback) alike."""
    # each tip is a literal t() call (inside a lambda, evaluated only on a
    # hit) so the translation worksheet scanner can collect the keys
    glossary = (
        ("NameError", lambda: t("check.tip_nameerror",
         "NameError: that name isn't defined yet -- check the spelling, or "
         "define it above the line that uses it.")),
        ("UnboundLocalError", lambda: t("check.tip_unbound",
         "UnboundLocalError: the variable is read before it gets a value on "
         "this path -- give it a starting value first.")),
        ("TypeError", lambda: t("check.tip_typeerror",
         "TypeError: the values' types don't fit the operation -- like adding "
         "text to a number; convert first with str() or int().")),
        ("IndexError", lambda: t("check.tip_indexerror",
         "IndexError: that position doesn't exist -- positions start at 0, "
         "and the last one is len(...) - 1.")),
        ("KeyError", lambda: t("check.tip_keyerror",
         "KeyError: that key isn't in the dictionary -- check the exact "
         "spelling, or read with .get(key).")),
        ("ValueError", lambda: t("check.tip_valueerror",
         "ValueError: the type is right but the value doesn't work -- like "
         "int('abc').")),
        ("AttributeError", lambda: t("check.tip_attributeerror",
         "AttributeError: that value has no such method or attribute -- "
         "check what type you are calling it on.")),
        ("ZeroDivisionError", lambda: t("check.tip_zerodivision",
         "ZeroDivisionError: division by zero -- make sure the denominator "
         "can't be 0 before dividing.")),
    )
    text = detail if isinstance(detail, str) else ""
    for name, tip in glossary:
        if name in text:
            return tip()
    return None


def _first_diff(expected, actual):
    """The index of the first line where two multi-line string outputs diverge,
    or None when either isn't a string, nothing differs, or both fit on one
    line (a marker on the only line is noise, the blocks speak for themselves)."""
    if not (isinstance(expected, str) and isinstance(actual, str)):
        return None
    el, al = expected.split("\n"), actual.split("\n")
    if len(el) <= 1 and len(al) <= 1:
        return None
    for i in range(max(len(el), len(al))):
        a = el[i] if i < len(el) else None
        b = al[i] if i < len(al) else None
        if a != b:
            return i
    return None


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


def _unsaved_notice():
    print("")
    print(PAD + paint(t("check.unchanged",
                        "work.py is byte-for-byte identical to your last "
                        "attempt -- did you save it in your editor?"),
                      "byellow", "bold"))


def _fail(title, body, prog, cur, unchanged=False):
    print(banner("%s  %s" % (NO, t("check.banner_not_yet", "not yet")), "red"))
    print("")
    print(PAD + paint(title, "bred", "bold"))
    print("")
    print(indent(body, PAD))
    print("")
    print(PAD + fail_nudge(prog, cur))
    if unchanged:
        _unsaved_notice()


def _almost(title, body, prog, cur, unchanged=False):
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
    if unchanged:
        _unsaved_notice()


def _solved(cur, prog, puzzles, newly=True):
    print(banner("%s  %s" % (OK, t("check.banner_solved", "solved")), "green"))
    print("")
    print(PAD + "%s   %s"
          % (paint(cur["id"], "byellow", "bold"),
             paint(cur["meta"].get("title", ""), "bold", "white")))
    print(PAD + bar(len(prog["completed"]), len(puzzles), WIDTH - 18))
    if newly:
        # milestones land at the moment of success, not buried in `stats`
        chapter = [p for p in puzzles if p["ch_num"] == cur["ch_num"]]
        if all(p["id"] in prog["completed"] for p in chapter):
            print(PAD + paint("%s  " % STAR + t(
                "check.chapter_done", "chapter %d complete -- %d/%d")
                % (cur["ch_num"], len(chapter), len(chapter)),
                "green", "bold"))
        if len(prog["completed"]) == len(puzzles):
            print(PAD + paint("%s  " % STAR + t(
                "check.course_done", "COURSE COMPLETE -- every puzzle solved!"),
                "bgreen", "bold"))
    print("")
    tail = t("check.code_saved", "your code is saved.")
    if newly:
        today = sum(1 for s in prog["stats"].values()
                    if s.get("solved_on") == datetime.date.today().isoformat())
        run = streak(solve_dates(prog))
        tail += "   " + tp("check.today", today,
                           one="%d solved today", other="%d solved today") % today
        if run > 1:
            tail += " · " + tp("check.streak", run,
                               one="%d-day streak",
                               other="%d-day streak") % run
    print(PAD + paint(tail, "gray"))
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
