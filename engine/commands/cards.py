"""Shared composition primitives the verbs reuse: the puzzle card, the status
marker, and the goto/advance helpers. The play verbs and the launcher menu both
build their screens from these, so they live one layer below both.
"""

import os

from ..config import WIDTH, rel
from ..content import load_hints
from ..state import current_puzzle, load_answers, switch_to, work_path
from ..render import (paint, id_banner, header, field, wrap, indent, cli,
                      PAD, OK, NO, CUR, DOT, ARROW, STAR)


def status_marker(prog, pid, current_id):
    if pid == current_id:
        done = pid in prog["completed"]
        return paint(CUR, "green" if done else "bcyan", "bold")
    if pid in prog["completed"]:
        return paint(OK, "green", "bold")
    return paint(DOT, "gray")


def print_current_card(prog, cur, show_pointer, arriving=False):
    meta = cur["meta"]
    solved = cur["id"] in prog["completed"]
    if arriving:
        print(id_banner(cur["id"], "cyan"))
    title = "%s   %s" % (paint(cur["id"], "byellow", "bold"),
                         paint(meta.get("title", ""), "bold", "white"))
    if solved:
        title += paint("   " + OK + " solved", "green")
    print("")
    print(PAD + title)
    print(PAD + paint("chapter %d · %s" % (cur["ch_num"], cur["ch_title"]),
                      "gray"))
    print("")
    for line in wrap(meta.get("concept", "")):
        print(PAD + line)
    print("")
    print(field("read", paint(rel(os.path.join(cur["dir"], "brief.md")),
                              "blue")))
    print(field("edit", paint(rel(work_path()), "blue", "bold")
                + paint("   (save before checking)", "gray")))
    if show_pointer:
        hints = load_hints(cur["dir"])
        if hints:
            print("")
            for i, line in enumerate(wrap(hints[0], WIDTH - len(PAD) - 8)):
                lead = paint("hint  ", "yellow", "bold") if i == 0 else " " * 6
                print(PAD + lead + line)
    print("")
    if solved:
        print(PAD + paint(ARROW + " next", "cyan", "bold")
              + paint("   move on whenever you're ready", "gray"))
    else:
        print(PAD + paint(ARROW + " check", "green", "bold")
              + paint("   when you've written and saved your code", "gray"))


def _goto_list(puzzles, by_id, prog, note=None, footer=True):
    """Show every puzzle as a pickable list (used when `goto` has no/bad id)."""
    cur_id = prog.get("current")
    print(header("goto · choose a puzzle", "cyan"))
    if note:
        print("")
        print(PAD + paint(note, "yellow"))
    chapters = {}
    for p in puzzles:
        chapters.setdefault(p["ch_num"], []).append(p)
    for ch in sorted(chapters):
        items = chapters[ch]
        print("")
        print(PAD + paint("Chapter %d · %s" % (ch, items[0]["ch_title"]),
                          "cyan", "bold"))
        for p in items:
            mark = status_marker(prog, p["id"], cur_id)
            title = p["meta"].get("title", "")
            locked = p["index"] > prog["highest"] and prog["mode"] != "easy"
            if p["id"] == cur_id:
                title = paint(title, "bcyan", "bold")
            elif p["id"] in prog["completed"]:
                title = paint(title, "gray")
            tail = paint("   locked", "gray") if locked else ""
            print("%s  %s  %s  %s%s"
                  % (PAD, mark, paint("%-5s" % p["id"], "gray"), title, tail))
    print("")
    if footer:
        print(PAD + "run  %s   e.g.  %s   (a bare chapter number works too: %s)"
              % (paint(cli("goto <id>"), "cyan", "bold"), cli("goto 2.1"),
                 cli("goto 2")))


def _resolve_goto(arg, puzzles, by_id, prog):
    """Turn what the learner typed into a puzzle.

    Accepts an exact id ('2.4'), forgives stray quotes/whitespace, and treats
    a bare chapter number ('2') as that chapter's first unsolved puzzle (or
    its first puzzle when all are solved). Returns None when nothing matches."""
    arg = (arg or "").strip().strip("'\"").rstrip(".")
    target = by_id.get(arg)
    if target is not None:
        return target
    if arg.isdigit():
        chapter = [p for p in puzzles if p["ch_num"] == int(arg)]
        if chapter:
            return next((p for p in chapter
                         if p["id"] not in prog["completed"]), chapter[0])
    return None


def _jump(target, puzzles, by_id, prog):
    """Shared by goto and the menu picker: enforce the mode locks, then move.
    One door, one lock -- pickers must never bypass what goto enforces."""
    forward = target["index"] > prog["highest"]
    if forward and prog["mode"] != "easy":
        print(paint("  %s '%s' is locked." % (NO, target["id"]), "red", "bold"))
        print("  In %s mode you can only revisit unlocked puzzles."
              % prog["mode"])
        print("  Use %s to advance one, or switch to easy mode."
              % paint(cli("next"), "yellow"))
        return False
    answers = load_answers()
    switch_to(target, prog, by_id, puzzles, answers)
    restored = bool(answers.get(target["id"], {}).get("code"))
    print(paint("  %s Now on %s -- %s%s"
                % (ARROW, target["id"], target["meta"].get("title", ""),
                   "  (your saved code was restored)" if restored else ""),
                "cyan", "bold"))
    print_current_card(prog, target, show_pointer=(prog["mode"] == "easy"),
                       arriving=True)
    return True


def _advance_one(puzzles, by_id, prog, verb):
    """Shared by `next` and `skip`: move to the next puzzle in order."""
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print("No current puzzle.")
        return
    solved = cur["id"] in prog["completed"]
    if not solved and prog["mode"] == "hard":
        print(paint("  %s Hard mode: you must solve %s before moving on."
                    % (NO, cur["id"]), "red", "bold"))
        print("  Switch modes if you want to skip:  %s" % cli("mode normal"))
        return
    nxt = next((p for p in puzzles if p["index"] == cur["index"] + 1), None)
    if nxt is None:
        print(paint("  %s  That was the last puzzle in the course." % STAR,
                    "green", "bold"))
        return
    answers = load_answers()
    switch_to(nxt, prog, by_id, puzzles, answers, unlock=True)
    word = "Moved on from" if solved else "Skipped (not solved)"
    print(paint("  %s %s %s" % (ARROW, word, cur["id"]),
                "cyan" if solved else "yellow", "bold"))
    print_current_card(prog, nxt, show_pointer=(prog["mode"] == "easy"),
                       arriving=True)
