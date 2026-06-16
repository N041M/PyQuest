"""The read verbs: show information without changing where you are or your
code. `status`/`map` inspect progress; `hint`/`solution` surface the current
puzzle's aids. None of them move the active puzzle or touch work.py (hint only
bumps its own counter). They compose state + content + render via the shared
`cards` helpers. `check` lives in checker.py; the dispatcher is app.py.
"""

import os

from ..config import WIDTH, rel
from ..content import load_hints
from ..state import (current_puzzle, save_progress, stat, lexicon_path,
                     write_lexicon)
from ..render import (paint, wordmark, bar, header, indent, wrap, cli, field,
                      pane_open, legend, PAD, STAR, ARROW)
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


def cmd_lexicon(puzzles, by_id, prog, arg=None):
    """Summon the syntax/tips reference as a markdown file you open via a link.
    Two states: bare `lexicon` writes only what the learner has reached;
    `lexicon all` writes the whole language the course covers. Built from each
    puzzle's `concept`, so it needs no separate authoring and never drifts."""
    full = (arg or "").strip().lower() in ("all", "full", "everything", "a", "*")
    total = len(puzzles)
    highest, cur = prog.get("highest", 0), prog.get("current")
    # A puzzle counts as reached once solved, or once the learner is actually in
    # the course (active / has solves) and has got to it. Before that -- a fresh
    # or just-reset profile -- nothing is reached, so the reached view is empty
    # rather than pretending 1.1 (index 0 <= highest 0) was seen.
    started = bool(prog.get("active")) or bool(prog["completed"])

    def reached(p):
        if p["id"] in prog["completed"]:
            return True
        return started and (p["id"] == cur or p["index"] <= highest)

    shown = puzzles if full else [p for p in puzzles if reached(p)]
    write_lexicon(_lexicon_md(shown, full, total))
    where = ("the full reference" if full
             else "what you've reached -- %d of %d" % (len(shown), total)
             if shown else "nothing reached yet")
    print(paint("  %s Lexicon ready: %s." % (ARROW, where), "magenta", "bold"))
    print(field("read", paint(rel(lexicon_path()), "blue", "bold")
                + paint("   open it in your editor", "gray")))
    print(PAD + paint(("for just what you've reached:  " + cli("lexicon"))
                      if full else
                      ("for the whole language:  " + cli("lexicon all")),
                      "gray"))


def _lexicon_md(shown, full, total):
    """Render the lexicon entries as a markdown document. The `concept` is the
    syntax+tip line; the optional `why` becomes a blockquote for depth."""
    out = ["# PyQuest Lexicon", ""]
    if full:
        out.append("_The full reference -- every syntax idea the course "
                   "covers._")
    elif shown:
        out.append("_Syntax & tips you've reached so far (%d of %d). "
                   "Run `lexicon all` for the full reference._"
                   % (len(shown), total))
    else:
        out.append("_Nothing reached yet -- solve a few puzzles, or run "
                   "`lexicon all` for the full reference._")
    out.append("")
    chapters = {}
    for p in shown:
        chapters.setdefault(p["ch_num"], []).append(p)
    for ch in sorted(chapters):
        items = chapters[ch]
        out += ["## %d · %s" % (ch, items[0]["ch_title"]), ""]
        for p in items:
            out += ["### %s -- %s" % (p["id"], p["meta"].get("title", "")), ""]
            concept = p["meta"].get("concept", "")
            if concept:
                out += [concept, ""]
            why = p["meta"].get("why")
            if why:
                out += ["> %s" % why, ""]
    return "\n".join(out).rstrip() + "\n"
