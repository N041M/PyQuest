"""Shared composition primitives the verbs reuse: the puzzle card, the status
marker, and the goto/advance helpers. The play verbs and the launcher menu both
build their screens from these, so they live one layer below both.
"""

from ..config import WIDTH, rel, term_size
from ..content import load_hints, brief_path, category
from ..state import current_puzzle, load_answers, switch_to, work_path
from ..render import (paint, id_banner, header, section, field, wrap, cli,
                      nav_row, pane_open, hyperlink,
                      PAD, OK, NO, CUR, DOT, ARROW, STAR)
from ..i18n import t, tp
from .registry import NAV_CLUSTERS, NEEDS_PUZZLE
from .. import keys

# Play-cockpit coordination between the entry point (app.main) and the card
# renderer, gathered into ONE named object rather than scattered flags. `active`
# is set once per process when the session is an interactive, key-capable TTY:
# then the card omits its static bottom row and the cockpit loop (app._play)
# renders that row interactively via nav_select. `card_drawn` is a one-shot
# signal print_current_card raises so main can tell a card actually reached the
# screen (the cockpit opens only when one did). It is module-level because that
# signal crosses from a deeply nested render call up to main.
class _PlayMode:
    active = False          # cockpit mode on (set once at startup)
    card_drawn = False      # a card was rendered since the last reset


play = _PlayMode()


def status_marker(prog, pid, current_id):
    if pid == current_id:
        done = pid in prog["completed"]
        return paint(CUR, "green" if done else "bcyan", "bold")
    if pid in prog["completed"]:
        return paint(OK, "green", "bold")
    return paint(DOT, "gray")


def chapter_tree(puzzles, prog, pickable=False, fold_solved=False):
    """The chapter/puzzle list both `map` and the goto picker draw -- one
    renderer so they can never drift. `pickable` adds the `locked` tags the
    picker needs; the marks/colours/layout are identical either way.
    `fold_solved` (the map's default) collapses a fully-solved chapter to one
    line so the tree stays scannable as the course grows -- except the chapter
    holding the current puzzle, which always shows its rows."""
    cur_id = prog.get("current")
    chapters = {}
    for p in puzzles:
        chapters.setdefault(p["ch_num"], []).append(p)
    prev_cat = None
    for ch in sorted(chapters):
        items = chapters[ch]
        cat = category(items[0])
        if cat != prev_cat:                     # a new curriculum category
            print("")
            print(section(cat))
            prev_cat = cat
        print("")
        print(header("%d · %s" % (ch, items[0]["ch_title"])))
        if (fold_solved
                and all(p["id"] in prog["completed"] for p in items)
                and not any(p["id"] == cur_id for p in items)):
            print("%s  %s  %s" % (PAD, paint(OK, "green", "bold"),
                  paint(t("map.folded", "all %d solved -- expand with  %s")
                        % (len(items), cli("map all")), "gray")))
            continue
        for p in items:
            mark = status_marker(prog, p["id"], cur_id)
            title = p["meta"].get("title", "")
            if p["id"] == cur_id:
                title = paint(title, "bcyan", "bold")
            elif p["id"] in prog["completed"]:
                title = paint(title, "gray")
            tail = ""
            if pickable and p["index"] > prog["highest"] and prog["mode"] != "easy":
                tail = paint("   " + t("card.locked", "locked"), "gray")
            print("%s  %s  %s  %s%s"
                  % (PAD, mark, paint("%-5s" % p["id"], "gray"), title, tail))


def _nav_verbs(prog, cur, puzzles=None):
    """The bottom navigation as (primary, clusters), derived from the registry so
    it can't drift from what dispatch accepts. The primary is the next action
    chip; clusters group the rest, hiding puzzle-only verbs when none is loaded
    and always offering menu/help as the escape hatch.

    Pass `puzzles` so the primary chip is honest on the last puzzle: a solved
    final puzzle has nowhere to advance, so the chip becomes `menu` rather than
    a `next` that would only report 'that was the last puzzle'."""
    has_puzzle = bool(prog.get("active")) and cur is not None
    solved = has_puzzle and cur["id"] in prog["completed"]
    if not has_puzzle:
        primary = "menu"
    elif not solved:
        primary = "check"
    else:
        last = bool(puzzles) and not any(
            p["index"] == cur["index"] + 1 for p in puzzles)
        primary = "menu" if last else "next"
    clusters = []
    for _group, verbs in NAV_CLUSTERS:
        labels = [v for v in verbs
                  if v != primary and (has_puzzle or v not in NEEDS_PUZZLE)]
        if labels:
            clusters.append(labels)
    clusters.append([v for v in ("textbook", "menu", "help") if v != primary])
    return primary, clusters


def nav_strip(prog, cur, puzzles=None):
    primary, clusters = _nav_verbs(prog, cur, puzzles)
    print(nav_row(primary, clusters))


def nav_select(prog, cur, puzzles=None):
    """The interactive version of the bottom row -- the play cockpit. Arrow
    across the verbs (the primary chip first), Enter runs the highlighted one,
    type a verb (`goto 2.4`) for anything off the row, Esc/Ctrl-C drops to the
    shell (to edit work.py and run check there, the same as always). Returns the
    chosen command string, or None to leave. The row packs onto one line when it
    fits and stacks the clusters when it doesn't, so nothing is ever cut off --
    and only the row repaints, so the card above stays put."""
    primary, clusters = _nav_verbs(prog, cur, puzzles)
    verbs = [primary] + [v for cl in clusters for v in cl]

    def render(idx, buf):
        # The cursor is a MOVING bracket, not just a colour -- so the selection
        # reads on a console with muted/absent colour (Windows). Exactly one cell
        # is bracketed at a time, so the row's width never jitters as you arrow.
        def cell(v, pos):
            if pos == idx:
                return paint("[%s]" % v, "bcyan", "bold"), "[%s]" % v
            if pos == 0:                        # the primary (default) action
                return paint(v, "byellow", "bold"), v
            return paint(v, "gray"), v

        if buf:
            rows = [PAD + paint("> ", "cyan", "bold") + buf]
        else:
            head, head_plain = cell(primary, 0)
            groups, plains, i = [], [], 1
            for cl in clusters:
                painted, plain = [], []
                for v in cl:
                    p, t_ = cell(v, i)
                    painted.append(p)
                    plain.append(t_)
                    i += 1
                groups.append(" · ".join(painted))
                plains.append(" · ".join(plain))
            one_plain = "%s   %s" % (head_plain, "   ".join(plains))
            if len(PAD) + len(one_plain) <= term_size()[0]:
                rows = [PAD + "   ".join([head] + groups)]        # fits one line
            else:
                rows = [PAD + head] + [PAD + g for g in groups]   # stack to fit
        hint = PAD + paint(t("cockpit.footer", "arrows move · Enter runs it · "
                           "type a verb · Esc to the shell"), "gray")
        return rows + [hint]

    try:
        res = keys.navigate(render, len(verbs), index=0, allow_typing=True)
    except KeyboardInterrupt:
        return None
    if res is None:
        return None
    return verbs[res] if isinstance(res, int) else res


def print_current_card(prog, cur, arriving=False, puzzles=None):
    # Easy mode surfaces the first hint as a pointer right on the card; the
    # stricter modes keep it behind `hint`. This policy lives here, not at every
    # call site.
    show_pointer = prog["mode"] == "easy"
    meta = cur["meta"]
    solved = cur["id"] in prog["completed"]
    if arriving:
        print(id_banner(cur["id"], "cyan"))
    title = "%s   %s" % (paint(cur["id"], "byellow", "bold"),
                         paint(meta.get("title", ""), "bold", "white"))
    if solved:
        title += paint("   " + OK + " " + t("card.solved", "solved"), "green")
    print("")
    print(PAD + title)
    print(PAD + paint(t("card.chapter", "chapter %d · %s")
                      % (cur["ch_num"], cur["ch_title"]), "gray"))
    print("")
    for line in wrap(meta.get("concept", "")):
        print(PAD + line)
    print("")
    bp = brief_path(cur["dir"])
    print(field(t("card.f_read", "read"),
                paint(hyperlink(rel(bp), bp), "blue")))
    print(field(t("card.f_edit", "edit"),
                paint(hyperlink(rel(work_path()), work_path()), "blue", "bold")
                + paint("   " + t("card.save_before", "(save before checking)"),
                        "gray")))
    note = load_answers().get(cur["id"], {}).get("note")
    if note:
        print("")
        for i, line in enumerate(wrap(note, WIDTH - len(PAD) - 8)):
            lead = paint((t("card.note_lead", "note") + "  "), "magenta", "bold") \
                if i == 0 else " " * 6
            print(PAD + lead + line)
    if show_pointer:
        hints = load_hints(cur["dir"])
        if hints:
            print("")
            for i, line in enumerate(wrap(hints[0], WIDTH - len(PAD) - 8)):
                lead = paint((t("card.hint_lead", "hint") + "  "), "yellow", "bold") \
                    if i == 0 else " " * 6
                print(PAD + lead + line)
    print("")
    play.card_drawn = True          # a card reached the screen -> cockpit may open
    if not play.active:             # in the cockpit, app._play renders the row
        nav_strip(prog, cur, puzzles)


def _goto_list(puzzles, by_id, prog, note=None, footer=True):
    """Show every puzzle as a pickable list (used when `goto` has no/bad id)."""
    print(pane_open(t("goto.title", "goto · choose a puzzle"), prog["mode"],
                    len(prog["completed"]), len(puzzles)))
    if note:
        print("")
        print(PAD + paint(note, "yellow"))
    chapter_tree(puzzles, prog, pickable=True)
    print("")
    if footer:
        print(PAD + t("goto.footer", "run  %s   e.g.  %s   (a bare chapter "
              "number works too: %s)")
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
        print(paint("  %s " % NO + t("jump.locked", "'%s' is locked.")
                    % target["id"], "red", "bold"))
        print("  " + t("jump.locked_2",
              "In %s mode you can only revisit unlocked puzzles.")
              % prog["mode"])
        print("  " + t("jump.locked_3",
              "Use %s to advance one, or switch to easy mode.")
              % paint(cli("next"), "yellow"))
        return False
    answers = load_answers()
    switch_to(target, prog, by_id, puzzles, answers)
    restored = bool(answers.get(target["id"], {}).get("code"))
    print(paint("  %s " % ARROW + t("jump.now_on", "Now on %s -- %s%s")
                % (target["id"], target["meta"].get("title", ""),
                   t("jump.restored", "  (your saved code was restored)")
                   if restored else ""), "cyan", "bold"))
    print_current_card(prog, target, arriving=True, puzzles=puzzles)
    return True


def _advance_one(puzzles, by_id, prog, force):
    """Move to the next puzzle in order. The two verbs differ on what they
    require of the current one:
      `next` (force=False) only advances once it is solved -- it's the "done,
        move on" verb, and refuses an unsolved puzzle (run check, or skip).
      `skip` (force=True) is the deliberate give-up: it moves on whether solved
        or not. Hard mode forbids it -- there you must genuinely solve."""
    cur = current_puzzle(prog, by_id, puzzles)
    if cur is None:
        print(t("ui.no_current", "No current puzzle."))
        return
    solved = cur["id"] in prog["completed"]
    if not solved:
        if not force:
            print(paint("  %s " % NO + t("nav.not_solved", "%s isn't solved yet.")
                        % cur["id"], "yellow", "bold"))
            print("  " + t("nav.not_solved_2",
                  "Run %s until it passes, or %s to move on without solving.")
                  % (cli("check"), cli("skip")))
            return
        if prog["mode"] == "hard":
            print(paint("  %s " % NO + t("nav.hard_solve",
                        "Hard mode: you must solve %s before moving on.")
                        % cur["id"], "red", "bold"))
            print("  " + t("nav.hard_skip",
                  "Switch to an easier mode to skip:  %s") % cli("mode normal"))
            return
    nxt = next((p for p in puzzles if p["index"] == cur["index"] + 1), None)
    if nxt is None:
        print(paint("  %s  " % STAR + t("nav.last_puzzle",
                    "That was the last puzzle in the course."),
                    "green", "bold"))
        return
    answers = load_answers()
    switch_to(nxt, prog, by_id, puzzles, answers, unlock=True)
    word = (t("nav.moved_on", "Moved on from") if solved
            else t("nav.skipped", "Skipped (not solved)"))
    print(paint("  %s %s %s" % (ARROW, word, cur["id"]),
                "cyan" if solved else "yellow", "bold"))
    if nxt["ch_num"] != cur["ch_num"]:      # earned progression into new ground
        _chapter_intro(nxt, puzzles)
    print_current_card(prog, nxt, arriving=True, puzzles=puzzles)


def _chapter_intro(first, puzzles):
    """A small welcome banner when `next`/`skip` crosses into a new chapter --
    the entering mirror of the chapter-complete line on the way out: the
    chapter's name, its category, and the topics ahead. Only on earned
    progression; a `goto` jump is navigation, not an arrival."""
    items = [p for p in puzzles if p["ch_num"] == first["ch_num"]]
    topics = " · ".join(p["meta"].get("title", "") for p in items)
    print("")
    print(header(t("chapter.intro", "chapter %d · %s")
                 % (first["ch_num"], first["ch_title"]), "magenta"))
    print(PAD + paint("%s · %s" % (category(first),
                      tp("chapter.puzzles", len(items),
                         one="%d puzzle", other="%d puzzles") % len(items)),
                      "gray"))
    for line in wrap(topics):
        print(PAD + paint(line, "gray"))
