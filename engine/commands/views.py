"""The read verbs: show information without changing where you are or your
code. `status`/`map` inspect progress; `hint`/`solution` surface the current
puzzle's aids. None of them move the active puzzle or touch work.py (hint only
bumps its own counter). They compose state + content + render via the shared
`cards` helpers. `check` lives in checker.py; the dispatcher is app.py.
"""

import os
import datetime

from ..config import WIDTH, rel
from ..content import load_hints, load_reference, category
from ..state import (current_puzzle, save_progress, stat, textbook_path,
                     write_textbook, current_user)
from ..render import (paint, wordmark, bar, header, indent, wrap, cli, field,
                      pane_open, legend, PAD, OK, STAR, ARROW)
from ..i18n import t, tp
from .cards import print_current_card, chapter_tree, nav_strip


def cmd_status(puzzles, by_id, prog):
    cur = current_puzzle(prog, by_id, puzzles)
    done = len(prog["completed"])
    total = len(puzzles)
    print(wordmark("cyan"))
    print("")
    print(PAD + "%s     %s"
          % (paint(prog["mode"] + " " + t("ui.mode", "mode"), "magenta", "bold"),
             bar(done, total, WIDTH - 24)))
    if not prog.get("active"):
        print("")
        print(PAD + paint(t("status.no_loaded", "No puzzle loaded."),
                          "white", "bold"))
        print(PAD + t("status.open_menu", "Open the menu to pick a level and "
                      "start:  ") + paint(cli("menu"), "green", "bold"))
        print("")
        nav_strip(prog, None, puzzles)
        return
    if cur is None:
        print("\n" + PAD + t("status.no_current", "No current puzzle.  ")
              + cli("map"))
        return
    if done >= total:
        print("\n" + PAD + paint(
            tp("status.all_complete", total,
               one="%s  All %d puzzle complete.",
               other="%s  All %d puzzles complete.") % (STAR, total),
            "green", "bold"))
        print(PAD + paint(t("status.revisit_goto", "revisit any with  goto <id>"),
                          "gray"))
        print("")
        nav_strip(prog, cur, puzzles)
        return
    # the card prints the shared nav strip itself, so status needs no footer
    print_current_card(prog, cur, puzzles=puzzles)


def cmd_map(puzzles, by_id, prog):
    done = len(prog["completed"])
    print(pane_open(t("map.title", "map"), prog["mode"], done, len(puzzles)))
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
        print(PAD + paint(t("search.usage", "usage:  ") + cli("search <word>"),
                          "yellow"))
        print(PAD + t("search.usage_hint",
                      "Find a puzzle by a word in its title or concept."))
        return
    done = set(prog["completed"])
    hits = [p for p in puzzles
            if term in " ".join((p["meta"].get("title", ""),
                                 p["meta"].get("concept", ""),
                                 p["ch_title"])).lower()]
    print(pane_open(t("search.title", "search · %s") % term, prog["mode"],
                    len(done), len(puzzles)))
    print("")
    if not hits:
        print(PAD + paint(t("search.no_match", "no puzzle matches '%s'.") % term,
                          "yellow"))
        print(PAD + paint(t("search.broaden", "try a broader word, or browse "
                            "the  ") + cli("map"), "gray"))
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
    print(PAD + paint(
        tp("search.matches", len(hits),
           one="%d match -- open one with  %s",
           other="%d matches -- open one with  %s")
        % (len(hits), cli("goto <id>")), "gray"))
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
    if days <= 0:
        rel = t("date.today", "today")
    elif days == 1:
        rel = t("date.yesterday", "yesterday")
    else:
        rel = tp("date.days_ago", days,
                 one="%d day ago", other="%d days ago") % days
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

    print(pane_open(t("stats.title", "stats · %s") % current_user(),
                    prog["mode"], done, total))
    if total and done == total:
        print("")
        print(PAD + paint("%s  %s  %s"
                          % (STAR, t("stats.course_complete", "course complete"),
                             STAR), "green", "bold"))
        print(PAD + paint(
            tp("stats.all_solved", total,
               one="all %d puzzle solved -- %d on the first try, no hints.",
               other="all %d puzzles solved -- %d on the first try, no hints.")
            % (total, clean), "gray"))
    print("")
    print(field(t("stats.f_since", "since"), _when(prog.get("created_at"))))
    print(field(t("stats.f_active", "active"), _when(prog.get("last_seen"))))
    print(field(t("stats.f_solved", "solved"),
                paint(t("stats.x_of_y", "%d of %d") % (done, total),
                      "bcyan", "bold")))
    if done:
        print(field(t("stats.f_today", "today"), paint(str(today_n), "white")
                    + paint("   " + t("stats.today_tail", "solved today"),
                            "gray")))
        if streak:
            print(field(t("stats.f_streak", "streak"), paint(
                tp("stats.streak", streak, one="%d day", other="%d days")
                % streak, "byellow", "bold")
                + paint("   " + t("stats.in_a_row", "in a row"), "gray")))
    print(field(t("stats.f_tries", "tries"), paint(str(attempts), "white")
                + paint("   " + t("stats.tries_tail",
                        "check runs across all puzzles"), "gray")))
    print(field(t("stats.f_hints", "hints"), paint(str(hints), "white")
                + paint("   " + t("stats.hints_tail", "hints revealed"), "gray")))
    if done:
        print(field(t("stats.f_clean", "clean"), paint(str(clean), "green", "bold")
                    + paint("   " + t("stats.clean_tail",
                            "solved first try, no hints"), "gray")))
    print("")
    print(header(t("stats.by_chapter", "by chapter"), "cyan"))
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
        print(t("ui.no_current", "No current puzzle."))
        return
    hints = load_hints(cur["dir"])
    if not hints:
        print(t("hint.none", "No hints for this puzzle."))
        return
    st = stat(prog, cur["id"])
    if prog["mode"] == "hard" and st["attempts"] < 3:
        print(t("hint.hard_locked",
                "Hard mode: hints unlock after 3 attempts (%d so far).")
              % st["attempts"])
        return
    idx = st["hints_used"]
    if idx >= len(hints):
        print(t("hint.no_more", "No more hints. Try:  %s") % cli("solution"))
        return
    print(pane_open(t("hint.title", "hint  %d / %d · %s")
                    % (idx + 1, len(hints), cur["id"]),
                    prog["mode"], len(prog["completed"]), len(puzzles),
                    "yellow"))
    print("")
    print(indent(hints[idx], PAD))
    st["hints_used"] = idx + 1
    save_progress(prog)
    if idx + 1 < len(hints):
        print("")
        print(PAD + paint(t("hint.more", "run hint again for more"), "gray"))
    print("")
    nav_strip(prog, cur, puzzles)


def cmd_solution(puzzles, by_id, prog):
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print(t("ui.no_current", "No current puzzle."))
        return
    if prog["mode"] == "hard" and cur["id"] not in prog["completed"]:
        print(t("solution.hard_locked",
                "Hard mode: the solution unlocks only after you solve it."))
        return
    path = os.path.join(cur["dir"], "solution.py")
    if not os.path.isfile(path):
        print(t("solution.none", "No solution file for this puzzle."))
        return
    with open(path, encoding="utf-8") as f:
        code = f.read().rstrip()
    print(pane_open(t("solution.title", "solution · %s · %s")
                    % (cur["id"], cur["meta"].get("title", "")),
                    prog["mode"], len(prog["completed"]), len(puzzles),
                    "magenta"))
    print("")
    print(indent(paint(code, "bcyan"), PAD))
    why = cur["meta"].get("why")
    if why:
        print("")
        print(header(t("solution.why", "why it works"), "magenta"))
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
        print(t("textbook.hard_sealed",
                "Hard mode: the textbook is sealed -- work from the brief."))
        return
    full = (arg or "").strip().lower() in ("all", "full", "everything", "a", "*")
    total = len(puzzles)
    highest, cur = prog.get("highest", 0), prog.get("current")
    # A puzzle counts as reached once solved, or once the learner has got to it.
    # The CURRENT puzzle always counts -- even on a fresh profile -- so the
    # textbook opens on the topic you're pointed at rather than blank; everything
    # up to the earned high-water mark counts once the learner is actually in the
    # course (active / has solves). Nothing AHEAD of the current puzzle is shown,
    # so the reveal stays progressive (no spoilers).
    started = bool(prog.get("active")) or bool(prog["completed"])

    def reached(p):
        if p["id"] in prog["completed"]:
            return True
        return p["id"] == cur or (started and p["index"] <= highest)

    shown = puzzles if full else [p for p in puzzles if reached(p)]
    # Not every puzzle contributes an entry: the count is topics that actually
    # have something to teach (a concept or a tip), not the raw puzzle total.
    total_entries = sum(1 for p in puzzles if _has_entry(p))
    write_textbook(_textbook_md(shown, full, total_entries))
    where = (t("textbook.where_full", "the full reference") if full
             else t("textbook.where_reached", "what you've reached -- %d of %d")
             % (len(shown), total)
             if shown else t("textbook.where_none", "nothing reached yet"))
    print(paint("  %s " % ARROW + t("textbook.ready", "Textbook ready: %s.")
                % where, "magenta", "bold"))
    print(field(t("textbook.f_read", "read"),
                paint(rel(textbook_path()), "blue", "bold")
                + paint("   " + t("textbook.open_it", "open it in your editor"),
                        "gray")))
    # `textbook all` and `textbook` write the same file, so the pair is a toggle:
    # expand to the whole language, then revert to just what you've reached.
    print(PAD + paint((t("textbook.revert", "revert to just what you've "
                         "reached:  ") + cli("textbook")) if full else
                      (t("textbook.see_all", "see the whole language:  ")
                       + cli("textbook all")), "gray"))


def _has_entry(p):
    """A puzzle earns a textbook entry only if it has something to teach -- a
    `concept` (the syntax line) or a `why` (the tip). Puzzles with neither (a
    pure practice/capstone drill, say) simply don't appear."""
    return bool(p["meta"].get("concept") or p["meta"].get("why"))


def _textbook_md(shown, full, total):
    """Render the textbook as a technical reference: per chapter, a section per
    topic. The heading is the topic's `syntax` -- the construct itself, code-
    formatted (e.g. `s[start:stop]`) -- or its title, and the body is the
    puzzle's detailed `reference.md`. Until a reference is authored, it falls
    back to the one-line `concept` (and `why`), so the textbook is always
    complete and only deepens as references are written. Topics with neither a
    concept nor a why are skipped and an empty chapter drops out, so the textbook
    mirrors the real content, not one row per puzzle."""
    chapters = {}
    for p in shown:
        chapters.setdefault(p["ch_num"], []).append(p)

    body, covered, prev_cat = [], 0, None
    for ch in sorted(chapters):
        items = [p for p in chapters[ch] if _has_entry(p)]
        if not items:
            continue                       # nothing to teach here -- skip it
        covered += len(items)
        # A rule before each chapter -- it parts the preamble from the body and
        # the chapters from one another, with none left dangling at the end. A
        # category heading is inserted at each curriculum boundary.
        body += ["---", ""]
        cat = category(items[0])
        if cat != prev_cat:
            body += ["# %s" % cat, ""]
            prev_cat = cat
        body += ["## %s" % t("textbook.md_chapter", "Chapter %d · %s")
                 % (ch, items[0]["ch_title"]), ""]
        for p in items:
            meta = p["meta"]
            heading = ("`%s`" % meta["syntax"] if meta.get("syntax")
                       else meta.get("title", ""))
            body += ["### %s" % heading, ""]
            ref = load_reference(p["dir"]) if p.get("dir") else None
            if ref and ref.strip():
                body += [ref.rstrip(), ""]          # the full authored reference
            else:                                   # not authored yet -> the gist
                if meta.get("concept"):
                    body += [meta["concept"], ""]
                if meta.get("why"):
                    body += ["*%s*" % meta["why"], ""]

    out = ["# " + t("textbook.md_title", "PyQuest Textbook"), ""]
    if full:
        out += ["*" + t("textbook.md_full_1",
                        "The whole language PyQuest covers -- every chapter, "
                        "all %d topics.") % total + "*",
                "*" + t("textbook.md_full_2",
                        "Run `textbook` to come back to just the chapters "
                        "you've reached.") + "*"]
    elif body:
        out += ["*" + t("textbook.md_reached_1",
                        "A technical reference for what you've reached -- %d of "
                        "%d topics.") % (covered, total) + "*",
                "*" + t("textbook.md_reached_2",
                        "Run `textbook all` for the whole language; `textbook` "
                        "brings you back here.") + "*"]
    else:
        out += ["*" + t("textbook.md_empty",
                        "Nothing covered yet -- work through a few topics, or "
                        "run `textbook all` to preview the whole language.")
                + "*"]
    out.append("")

    return "\n".join(out + body).rstrip() + "\n"
