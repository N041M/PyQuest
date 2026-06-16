"""The navigation + workspace-reset verbs: they change which puzzle is active
or wipe its work.py. goto/next/skip move you; retry/restart reset the workspace
(and, for restart, this puzzle's progress). These are the verbs a learner might
fire at the wrong moment, so most are gated to "needs a puzzle loaded" in the
registry (app.py redirects them to `menu` otherwise); `goto` is always allowed
because it loads one. They compose state + content + render via the shared
`cards` helpers; the dispatcher is app.py.
"""

import sys

from ..content import read_starter
from ..state import (current_puzzle, load_answers, save_answers, save_progress,
                     archive_current, write_work)
from ..render import paint, PAD, ARROW
from .cards import (print_current_card, _goto_list, _resolve_goto, _jump,
                    _advance_one)


def cmd_goto(puzzles, by_id, prog, arg):
    if arg:
        target = _resolve_goto(arg, puzzles, by_id, prog)
        if target is None:
            _goto_list(puzzles, by_id, prog,
                       note="There is no puzzle '%s'. Pick one of these:" % arg)
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
        picked = input(PAD + paint("id (blank = cancel) > ",
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
        print(PAD + paint("no puzzle '%s'." % picked, "yellow"))
        return
    _jump(target, puzzles, by_id, prog)


def cmd_next(puzzles, by_id, prog):
    _advance_one(puzzles, by_id, prog, force=False)   # only once solved


def cmd_skip(puzzles, by_id, prog):
    _advance_one(puzzles, by_id, prog, force=True)    # move on, solved or not


def cmd_retry(puzzles, by_id, prog):
    """Replay the current puzzle: reset its workspace to a blank starter."""
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print("No current puzzle.")
        return
    archive_current(prog, by_id, puzzles)    # keep their last code in answers
    prog["active"] = True
    save_progress(prog)
    write_work(read_starter(cur))            # blank the workspace
    solved = cur["id"] in prog["completed"]
    print(paint("  %s Reset %s to a blank workspace -- give it another go."
                % (ARROW, cur["id"]), "cyan", "bold"))
    if solved:
        print(PAD + paint("(it stays marked solved; this is just practice)",
                          "gray"))
    print(PAD + paint("if your editor still shows old code, reload work.py -- "
                      "its on-disk copy is now blank.", "gray"))
    print_current_card(prog, cur, arriving=True, puzzles=puzzles)


def cmd_restart(puzzles, by_id, prog):
    """Start the active puzzle over: blank the workspace AND clear this one
    puzzle's progress (unsolve it, drop attempts/hints/saved code). Unlike
    `retry`, it makes the puzzle pristine -- as if you had never attempted it."""
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print("No current puzzle.")
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
    print(paint("  %s Restarted %s -- blank workspace, progress cleared."
                % (ARROW, cur["id"]), "magenta", "bold"))
    print_current_card(prog, cur, arriving=True, puzzles=puzzles)
