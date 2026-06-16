"""The read verbs: show information without changing where you are or your
code. `status`/`map` inspect progress; `hint`/`solution` surface the current
puzzle's aids. None of them move the active puzzle or touch work.py (hint only
bumps its own counter). They compose state + content + render via the shared
`cards` helpers. `check` lives in checker.py; the dispatcher is app.py.
"""

import os
import datetime

from ..config import WIDTH, rel
from ..content import load_hints
from ..state import (current_puzzle, save_progress, stat, textbook_path,
                     write_textbook, current_user)
from ..render import (paint, wordmark, bar, header, indent, wrap, cli, field,
                      pane_open, legend, PAD, OK, STAR, ARROW)
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
              + paint(cli("menu"), "green", "bold"))
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


def cmd_search(puzzles, by_id, prog, arg=None):
    """Find a puzzle by a word in its title, concept, or chapter -- a fast way
    into the course without scrolling the map. A read verb: it lists matches
    with their ids (ready to `goto`) and changes nothing."""
    term = (arg or "").strip().lower()
    if not term:
        print(PAD + paint("usage:  " + cli("search <word>"), "yellow"))
        print(PAD + "Find a puzzle by a word in its title or concept.")
        return
    done = set(prog["completed"])
    hits = [p for p in puzzles
            if term in " ".join((p["meta"].get("title", ""),
                                 p["meta"].get("concept", ""),
                                 p["ch_title"])).lower()]
    print(pane_open("search · %s" % term, prog["mode"],
                    len(done), len(puzzles)))
    print("")
    if not hits:
        print(PAD + paint("no puzzle matches '%s'." % term, "yellow"))
        print(PAD + paint("try a broader word, or browse the  " + cli("map"),
                          "gray"))
        print("")
        nav_strip(prog, current_puzzle(prog, by_id, puzzles), puzzles)
        return
    for p in hits:
        solved = p["id"] in done
        print(PAD + " %s  %s  %s"
              % (paint(OK if solved else "·", "green" if solved else "gray"),
                 paint(p["id"].ljust(5), "byellow", "bold"),
                 paint(p["meta"].get("title", ""), "white")))
    print("")
    print(PAD + paint("%d match%s -- open one with  %s"
                      % (len(hits), "" if len(hits) == 1 else "es",
                         cli("goto <id>")), "gray"))
    print("")
    nav_strip(prog, current_puzzle(prog, by_id, puzzles), puzzles)


def _parse_iso(value):
    if not isinstance(value, str):
        return None
    try:
        return datetime.datetime.fromisoformat(value)
    except ValueError:
        return None


def _when(value):
    """A human date for a stored ISO timestamp, with a relative tail. Falls back
    to a dash when the field was never set (a fresh profile's last_seen)."""
    dt = _parse_iso(value)
    if dt is None:
        return paint("--", "gray")
    days = (datetime.datetime.now() - dt).days
    rel = "today" if days <= 0 else "yesterday" if days == 1 else "%d days ago" % days
    return paint(dt.strftime("%Y-%m-%d"), "white") + paint("   %s" % rel, "gray")


def _solve_dates(prog):
    """The set of distinct calendar dates on which puzzles were first solved,
    read from each stat's `solved_on`."""
    out = set()
    for s in prog.get("stats", {}).values():
        d = s.get("solved_on")
        if isinstance(d, str):
            try:
                out.add(datetime.date.fromisoformat(d))
            except ValueError:
                pass
    return out


def _streak(dates):
    """Consecutive days solved, counting back from today -- or from yesterday,
    so the streak isn't 'broken' merely because today's puzzle isn't done yet."""
    if not dates:
        return 0
    day = datetime.date.today()
    if day not in dates:
        day -= datetime.timedelta(days=1)
    n = 0
    while day in dates:
        n += 1
        day -= datetime.timedelta(days=1)
    return n


def cmd_stats(puzzles, by_id, prog):
    """The numbers already kept per puzzle, surfaced: attempts, hints, clean
    first-try solves, streaks, and per-chapter completion. A read verb -- it
    touches nothing, just reflects progress.json back to the learner."""
    done = len(prog["completed"])
    total = len(puzzles)
    st = prog.get("stats", {})
    attempts = sum(s.get("attempts", 0) for s in st.values())
    hints = sum(s.get("hints_used", 0) for s in st.values())
    clean = sum(1 for pid in prog["completed"]
                if st.get(pid, {}).get("attempts", 0) <= 1
                and st.get(pid, {}).get("hints_used", 0) == 0)
    today_n = sum(1 for s in st.values()
                  if s.get("solved_on") == datetime.date.today().isoformat())
    streak = _streak(_solve_dates(prog))

    print(pane_open("stats · %s" % current_user(), prog["mode"], done, total))
    if total and done == total:
        print("")
        print(PAD + paint("%s  course complete  %s" % (STAR, STAR),
                          "green", "bold"))
        print(PAD + paint("all %d puzzles solved -- %d on the first try, "
                          "no hints." % (total, clean), "gray"))
    print("")
    print(field("since", _when(prog.get("created_at"))))
    print(field("active", _when(prog.get("last_seen"))))
    print(field("solved", paint("%d of %d" % (done, total), "bcyan", "bold")))
    if done:
        print(field("today", paint(str(today_n), "white")
                    + paint("   solved today", "gray")))
        if streak:
            print(field("streak", paint("%d day%s" % (streak,
                        "" if streak == 1 else "s"), "byellow", "bold")
                        + paint("   in a row", "gray")))
    print(field("tries", paint(str(attempts), "white")
                + paint("   check runs across all puzzles", "gray")))
    print(field("hints", paint(str(hints), "white")
                + paint("   hints revealed", "gray")))
    if done:
        print(field("clean", paint(str(clean), "green", "bold")
                    + paint("   solved first try, no hints", "gray")))
    print("")
    print(header("by chapter", "cyan"))
    print("")
    chs = {}
    for p in puzzles:
        c = chs.setdefault(p["ch_num"],
                           {"title": p["ch_title"], "done": 0, "total": 0})
        c["total"] += 1
        if p["id"] in prog["completed"]:
            c["done"] += 1
    for ch in sorted(chs):
        c = chs[ch]
        print(PAD + " %s  %s   %s"
              % (paint("%d" % ch, "byellow", "bold"),
                 bar(c["done"], c["total"], 16),
                 paint(c["title"], "white")))
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


def cmd_textbook(puzzles, by_id, prog, arg=None):
    """Summon the syntax/tips reference as a markdown file you open via a link.
    Two states: bare `textbook` writes only what the learner has reached;
    `textbook all` writes the whole language the course covers. Built from each
    puzzle's `concept`, so it needs no separate authoring and never drifts."""
    # Hard mode withholds the syntax/tips crib, just as it gates hints and the
    # solution -- the learner works from the brief and their own notes alone.
    if prog.get("mode") == "hard":
        print("Hard mode: the textbook is sealed -- work from the brief.")
        return
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
    # Not every puzzle contributes an entry: the count is topics that actually
    # have something to teach (a concept or a tip), not the raw puzzle total.
    total_entries = sum(1 for p in puzzles if _has_entry(p))
    write_textbook(_textbook_md(shown, full, total_entries))
    where = ("the full reference" if full
             else "what you've reached -- %d of %d" % (len(shown), total)
             if shown else "nothing reached yet")
    print(paint("  %s Textbook ready: %s." % (ARROW, where), "magenta", "bold"))
    print(field("read", paint(rel(textbook_path()), "blue", "bold")
                + paint("   open it in your editor", "gray")))
    # `textbook all` and `textbook` write the same file, so the pair is a toggle:
    # expand to the whole language, then revert to just what you've reached.
    print(PAD + paint(("revert to just what you've reached:  " + cli("textbook"))
                      if full else
                      ("see the whole language:  " + cli("textbook all")),
                      "gray"))


def _has_entry(p):
    """A puzzle earns a textbook entry only if it has something to teach -- a
    `concept` (the syntax line) or a `why` (the tip). Puzzles with neither (a
    pure practice/capstone drill, say) simply don't appear."""
    return bool(p["meta"].get("concept") or p["meta"].get("why"))


def _textbook_md(shown, full, total):
    """Render the textbook as structured markdown: per chapter, all the syntax
    bundled together, then all the tips. `concept` supplies the syntax line, the
    optional `why` the tip -- so it needs no separate authoring and never drifts.

    Not every puzzle carries an entry: those with neither a concept nor a tip
    are skipped, and a chapter with nothing to show drops out entirely -- the
    textbook mirrors the course's real content, not one row per puzzle.

    Built as a list, not a table: a `concept` can carry a literal `|` (e.g. the
    set-union operator), which a markdown table would split into a stray column.
    A list also reads cleanly raw, before any markdown renderer touches it."""
    chapters = {}
    for p in shown:
        chapters.setdefault(p["ch_num"], []).append(p)

    body, covered = [], 0
    for ch in sorted(chapters):
        items = chapters[ch]
        syntax = [p for p in items if p["meta"].get("concept")]
        tips = [p for p in items if p["meta"].get("why")]
        if not syntax and not tips:
            continue                       # nothing to teach here -- skip it
        covered += sum(1 for p in items if _has_entry(p))
        # A rule before each chapter -- it parts the preamble from the body and
        # the chapters from one another, with none left dangling at the end.
        body += ["---", "", "## Chapter %d · %s" % (ch, items[0]["ch_title"]), ""]
        # Syntax bundle: a definition list, each topic by name (no puzzle ids --
        # this reads as a textbook, not a pointer back into the course).
        if syntax:
            body += ["### Syntax", ""]
            body += ["- **%s** — %s" % (p["meta"].get("title", ""),
                                        p["meta"]["concept"]) for p in syntax]
            body.append("")
        # Tips bundle: the deeper `why` for each topic that carries one, named
        # the same way so the two sections read independently.
        if tips:
            body += ["### Tips", ""]
            body += ["- **%s** — %s" % (p["meta"].get("title", ""),
                                        p["meta"]["why"]) for p in tips]
            body.append("")

    out = ["# PyQuest Textbook", ""]
    if full:
        out += ["*The whole language PyQuest covers -- every chapter, all %d "
                "topics.*" % total,
                "*Run `textbook` to come back to just the chapters you've "
                "reached.*"]
    elif body:
        out += ["*The syntax and tips you've covered so far -- %d of %d "
                "topics.*" % (covered, total),
                "*Run `textbook all` for the whole language; `textbook` brings "
                "you back here.*"]
    else:
        out += ["*Nothing covered yet -- work through a few topics, or run "
                "`textbook all` to preview the whole language.*"]
    out.append("")

    return "\n".join(out + body).rstrip() + "\n"
