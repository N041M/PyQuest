"""The read verbs: show information without changing where you are or your
code. `status`/`map` inspect progress; `hint`/`solution` surface the current
puzzle's aids. None of them move the active puzzle or touch work.py (hint only
bumps its own counter). They compose state + content + render via the shared
`cards` helpers. `check` lives in checker.py; the dispatcher is app.py.
"""

import os

from ..config import WIDTH
from ..content import load_hints
from ..state import current_puzzle, save_progress, stat
from ..render import (paint, wordmark, bar, header, indent, wrap, cli,
                      pane_open, legend, PAD, STAR)
from .cards import print_current_card, chapter_tree, nav_strip


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
        print("")
        nav_strip(prog, None, puzzles)
        return
    if cur is None:
        print("\n" + PAD + "No current puzzle.  " + cli("map"))
        return
    if done >= total:
        print("\n" + PAD + paint("%s  All %d puzzles complete." % (STAR, total),
                                 "green", "bold"))
        print(PAD + paint("revisit any with  goto <id>", "gray"))
        print("")
        nav_strip(prog, cur, puzzles)
        return
    # the card prints the shared nav strip itself, so status needs no footer
    print_current_card(prog, cur, puzzles=puzzles)


def cmd_map(puzzles, by_id, prog):
    done = len(prog["completed"])
    print(pane_open("map", prog["mode"], done, len(puzzles)))
    chapter_tree(puzzles, prog, pickable=False)
    print("")
    print(legend())
    print("")
    nav_strip(prog, current_puzzle(prog, by_id, puzzles), puzzles)


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
    print(pane_open("hint  %d / %d · %s" % (idx + 1, len(hints), cur["id"]),
                    prog["mode"], len(prog["completed"]), len(puzzles),
                    "yellow"))
    print("")
    print(indent(hints[idx], PAD))
    st["hints_used"] = idx + 1
    save_progress(prog)
    if idx + 1 < len(hints):
        print("")
        print(PAD + paint("run hint again for more", "gray"))
    print("")
    nav_strip(prog, cur, puzzles)


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
    print(pane_open("solution · %s · %s"
                    % (cur["id"], cur["meta"].get("title", "")),
                    prog["mode"], len(prog["completed"]), len(puzzles),
                    "magenta"))
    print("")
    print(indent(paint(code, "bcyan"), PAD))
    why = cur["meta"].get("why")
    if why:
        print("")
        print(header("why it works", "magenta"))
        print("")
        for line in wrap(why):
            print(PAD + line)
    print("")
    nav_strip(prog, cur, puzzles)
