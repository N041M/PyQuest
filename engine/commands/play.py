"""The puzzle-loop verbs: status, map, hint, solution, goto, next, skip, retry,
revert, mode. They compose state + content + render via the shared `cards`
helpers. `check` lives in checker.py; the dispatcher is app.py.
"""

import os
import sys

from ..config import MODES, WIDTH
from ..content import load_hints, read_starter
from ..state import (current_puzzle, load_answers, save_answers, save_progress,
                     stat, archive_work, write_work)
from ..render import (paint, wordmark, bar, header, indent, wrap, cli,
                      PAD, OK, CUR, DOT, ARROW, STAR)
from .cards import (status_marker, print_current_card, _goto_list,
                    _resolve_goto, _jump, _advance_one)


def cmd_status(puzzles, by_id, prog):
    cur = current_puzzle(prog, by_id, puzzles)
    done = len(prog["completed"])
    total = len(puzzles)
    print(wordmark("cyan"))
    print("")
    print(PAD + "%s     %s"
          % (paint(prog["mode"] + " mode", "magenta", "bold"),
             bar(done, total, WIDTH - 24)))
    if not prog.get("active"):
        print("")
        print(PAD + paint("No puzzle loaded.", "white", "bold"))
        print(PAD + "Open the menu to pick a level and start:  "
              + paint(cli("begin"), "green", "bold"))
        return
    if cur is None:
        print("\n" + PAD + "No current puzzle.  " + cli("map"))
        return
    if done >= total:
        print("\n" + PAD + paint("%s  All %d puzzles complete." % (STAR, total),
                                 "green", "bold"))
        print(PAD + paint("revisit any with  goto <id>", "gray"))
        return
    print_current_card(prog, cur, show_pointer=(prog["mode"] == "easy"))
    print("")
    print(PAD + paint("hint · solution · next · map · goto · skip · retry · "
                      "revert · mode · theme · user · reset", "gray"))


def cmd_map(puzzles, by_id, prog):
    cur_id = prog.get("current")
    done = len(prog["completed"])
    print(wordmark("cyan"))
    print("")
    print(PAD + bar(done, len(puzzles), WIDTH - 18))
    chapters = {}
    for p in puzzles:
        chapters.setdefault(p["ch_num"], []).append(p)
    for ch_num in sorted(chapters):
        items = chapters[ch_num]
        print("")
        print(header("%d · %s" % (ch_num, items[0]["ch_title"])))
        for p in items:
            mark = status_marker(prog, p["id"], cur_id)
            title = p["meta"].get("title", "")
            if p["id"] == cur_id:
                title = paint(title, "bcyan", "bold")
            elif p["id"] in prog["completed"]:
                title = paint(title, "gray")
            print("%s %s  %s  %s"
                  % (PAD, mark, paint("%-4s" % p["id"], "gray"), title))
    print("")
    print(PAD + paint("%s done   %s here   %s to do" % (OK, CUR, DOT), "gray"))


def cmd_hint(puzzles, by_id, prog):
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print("No current puzzle.")
        return
    hints = load_hints(cur["dir"])
    if not hints:
        print("No hints for this puzzle.")
        return
    st = stat(prog, cur["id"])
    if prog["mode"] == "hard" and st["attempts"] < 3:
        print("Hard mode: hints unlock after 3 attempts (%d so far)."
              % st["attempts"])
        return
    idx = st["hints_used"]
    if idx >= len(hints):
        print("No more hints. Try:  %s" % cli("solution"))
        return
    print(header("hint  %d / %d · %s" % (idx + 1, len(hints), cur["id"]),
                 "yellow"))
    print("")
    print(indent(hints[idx], PAD))
    st["hints_used"] = idx + 1
    save_progress(prog)
    if idx + 1 < len(hints):
        print("")
        print(PAD + paint("run hint again for more", "gray"))


def cmd_solution(puzzles, by_id, prog):
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print("No current puzzle.")
        return
    if prog["mode"] == "hard" and cur["id"] not in prog["completed"]:
        print("Hard mode: the solution unlocks only after you solve it.")
        return
    path = os.path.join(cur["dir"], "solution.py")
    if not os.path.isfile(path):
        print("No solution file for this puzzle.")
        return
    with open(path) as f:
        code = f.read().rstrip()
    print(header("solution · %s · %s"
                 % (cur["id"], cur["meta"].get("title", "")), "magenta"))
    print("")
    print(indent(paint(code, "bcyan"), PAD))
    why = cur["meta"].get("why")
    if why:
        print("")
        print(header("why it works", "magenta"))
        print("")
        for line in wrap(why):
            print(PAD + line)


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
    # (one prompt, then exit -- the same in-and-out as the begin menu).
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
    _advance_one(puzzles, by_id, prog, "next")


def cmd_skip(puzzles, by_id, prog):
    _advance_one(puzzles, by_id, prog, "skip")


def cmd_retry(puzzles, by_id, prog):
    """Replay the current puzzle: reset its workspace to a blank starter."""
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print("No current puzzle.")
        return
    answers = load_answers()
    if prog.get("active"):
        archive_work(cur, answers)           # keep their last code in answers
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
    print_current_card(prog, cur, show_pointer=(prog["mode"] == "easy"),
                       arriving=True)


def cmd_revert(puzzles, by_id, prog):
    """Fully reset the active question: blank the workspace AND clear this one
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
    print(paint("  %s Reverted %s -- blank workspace, progress cleared."
                % (ARROW, cur["id"]), "magenta", "bold"))
    print_current_card(prog, cur, show_pointer=(prog["mode"] == "easy"),
                       arriving=True)


def cmd_mode(prog, arg):
    arg = (arg or "").lower()
    if arg not in MODES:
        print("Usage: %s" % cli("mode <easy|normal|hard>"))
        print("Current mode: %s" % paint(prog["mode"], "magenta", "bold"))
        return
    prog["mode"] = arg
    save_progress(prog)
    desc = {
        "easy": "Pointers shown, hints/solution always available, free jumps.",
        "normal": "Hints on demand, skip forward allowed.",
        "hard": "No skips, hints only after 3 tries, solution after solving.",
    }[arg]
    print(paint("  %s Mode set to '%s'." % (OK, arg), "magenta", "bold"))
    print("  " + desc)
