"""The navigation + per-puzzle-state verbs: they change which puzzle is active,
wipe its work.py, or annotate it. goto/next/skip/resume move you; retry/restart
reset the workspace (and, for restart, this puzzle's progress); note jots a
personal annotation. The puzzle-state ones are gated to "needs a puzzle loaded"
in the registry (app.py redirects them to `menu` otherwise); goto/resume are
always allowed because they load one. They compose state + content + render via
the shared `cards` helpers; the dispatcher is app.py.
"""

import sys

from ..content import read_starter
from ..state import (current_puzzle, load_answers, save_answers, save_progress,
                     archive_current, switch_to, write_work)
from ..render import paint, cli, PAD, OK, STAR, ARROW
from ..i18n import t
from .cards import (print_current_card, _goto_list, _resolve_goto, _jump,
                    _advance_one)


def cmd_goto(puzzles, by_id, prog, arg):
    if arg:
        target = _resolve_goto(arg, puzzles, by_id, prog)
        if target is None:
            _goto_list(puzzles, by_id, prog,
                       note=t("goto.no_match", "There is no puzzle '%s'. Pick "
                              "one of these:") % arg)
            return
        _jump(target, puzzles, by_id, prog)
        return
    # bare `goto`: show the list, and on a terminal let them pick right here
    # (one prompt, then exit -- the same in-and-out as the menu).
    interactive = sys.stdin.isatty()
    _goto_list(puzzles, by_id, prog, footer=not interactive)
    if not interactive:
        return
    try:
        picked = input(PAD + paint((t("goto.prompt", "id (blank = cancel) >") + " "),
                                   "cyan", "bold")).strip()
    except (EOFError, KeyboardInterrupt):
        print("")
        return
    if not picked:
        return
    if picked.lower().startswith("goto "):          # forgive "goto 2.4"
        picked = picked[5:].strip()
    target = _resolve_goto(picked, puzzles, by_id, prog)
    if target is None:
        print(PAD + paint(t("ui.no_puzzle", "no puzzle '%s'.") % picked,
                          "yellow"))
        return
    _jump(target, puzzles, by_id, prog)


def cmd_next(puzzles, by_id, prog):
    _advance_one(puzzles, by_id, prog, force=False)   # only once solved


def cmd_skip(puzzles, by_id, prog):
    _advance_one(puzzles, by_id, prog, force=True)    # move on, solved or not


_NOTE_CLEAR = ("clear", "delete", "remove", "-")


def cmd_note(puzzles, by_id, prog, arg=None):
    """Jot or read a personal note on the current puzzle. `note <text>` saves it
    (in answers.json, beside your code), bare `note` shows it, and `note clear`
    removes it. The note then appears on the puzzle card."""
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print(t("ui.no_current", "No current puzzle."))
        return
    answers = load_answers()
    entry = answers.setdefault(cur["id"], {"solved": False, "code": ""})
    text = (arg or "").strip()
    if not text:                                  # bare `note`: show it
        existing = entry.get("note")
        if existing:
            print(paint("  " + t("note.header", "note on %s:") % cur["id"],
                        "magenta", "bold"))
            print(PAD + existing)
        else:
            print(PAD + paint(t("note.none_yet", "no note on %s yet.")
                              % cur["id"], "gray"))
            print(PAD + paint((t("note.add_one", "add one with") + "  ")
                              + cli("note <text>"), "gray"))
        return
    if text.lower() in _NOTE_CLEAR:
        if entry.pop("note", None) is not None:
            save_answers(answers)
            print(paint("  %s " % OK + t("note.cleared", "Note cleared on %s.")
                        % cur["id"], "green"))
        else:
            print(PAD + paint(t("note.none_clear", "no note on %s to clear.")
                              % cur["id"], "gray"))
        return
    entry["note"] = text
    save_answers(answers)
    print(paint("  %s " % OK + t("note.saved", "Noted on %s.") % cur["id"],
                "green", "bold"))
    print(PAD + paint(text, "gray"))


def cmd_resume(puzzles, by_id, prog):
    """Jump to the first puzzle you haven't solved -- "take me back to where I
    should be". Always allowed (it's earned progress, never a forward skip); if
    everything is solved it stays put and says so."""
    done = set(prog["completed"])
    target = next((p for p in puzzles if p["id"] not in done), None)
    if target is None:
        print(paint("  %s  " % STAR + t("resume.all_solved",
                    "Every puzzle is solved -- nothing to resume."),
                    "green", "bold"))
        print(PAD + paint((t("resume.revisit", "revisit any with") + "  ")
                          + cli("goto <id>"), "gray"))
        return
    switch_to(target, prog, by_id, puzzles, load_answers())
    print(paint("  %s " % ARROW + t("resume.at", "Resuming at %s.")
                % target["id"], "cyan", "bold"))
    print_current_card(prog, target, arriving=True, puzzles=puzzles)


def cmd_retry(puzzles, by_id, prog):
    """Replay the current puzzle: reset its workspace to a blank starter."""
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print(t("ui.no_current", "No current puzzle."))
        return
    archive_current(prog, by_id, puzzles)    # keep their last code in answers
    prog["active"] = True
    save_progress(prog)
    write_work(read_starter(cur))            # blank the workspace
    solved = cur["id"] in prog["completed"]
    print(paint("  %s " % ARROW + t("retry.reset",
                "Reset %s to a blank workspace -- give it another go.")
                % cur["id"], "cyan", "bold"))
    if solved:
        print(PAD + paint(t("retry.stays_solved",
                          "(it stays marked solved; this is just practice)"),
                          "gray"))
    print(PAD + paint(t("retry.reload",
                      "if your editor still shows old code, reload work.py -- "
                      "its on-disk copy is now blank."), "gray"))
    print_current_card(prog, cur, arriving=True, puzzles=puzzles)


def cmd_restart(puzzles, by_id, prog):
    """Start the active puzzle over: blank the workspace AND clear this one
    puzzle's progress (unsolve it, drop attempts/hints/saved code). Unlike
    `retry`, it makes the puzzle pristine -- as if you had never attempted it."""
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print(t("ui.no_current", "No current puzzle."))
        return
    answers = load_answers()
    answers.pop(cur["id"], None)
    save_answers(answers)
    if cur["id"] in prog["completed"]:
        prog["completed"].remove(cur["id"])
    prog["stats"].pop(cur["id"], None)
    prog["active"] = True
    save_progress(prog)
    write_work(read_starter(cur))
    print(paint("  %s " % ARROW + t("restart.done",
                "Restarted %s -- blank workspace, progress cleared.")
                % cur["id"], "magenta", "bold"))
    print_current_card(prog, cur, arriving=True, puzzles=puzzles)
