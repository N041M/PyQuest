"""The verbs (status, map, hint, solution, goto, next, skip, retry, mode, reset,
help) and the screens they compose. Built only from render primitives + state +
content. `check` lives in checker.py; the dispatcher is app.py.
"""

import os
import sys
import json

from .config import MODES, WIDTH, ROOT, rel, load_settings, set_setting
from .theme import apply_theme, THEME_NAMES
from .content import load_hints, read_starter, by_id_lookup
from .state import (current_puzzle, load_answers, save_answers, switch_to,
                    activate, save_progress, stat, archive_work, write_work,
                    work_path, default_progress, load_progress, ensure_workspace,
                    answers_path, progress_path, list_users, current_user,
                    ensure_user, valid_username, WELCOME_WORK)
from .render import (paint, wordmark, id_banner, bar, header, field, wrap,
                     indent, cli, label, PAD, OK, NO, CUR, DOT, ARROW, STAR)


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


# ---- themes ---------------------------------------------------------------
def _swatch():
    return "".join(paint("██", r) for r in
                   ("cyan", "byellow", "green", "yellow", "red", "magenta"))


def cmd_theme(arg):
    current = load_settings().get("theme", "neon")
    if not arg:
        print(header("themes", "cyan"))
        print("")
        for name in THEME_NAMES:
            apply_theme(name)                       # color the row in its theme
            mark = OK if name == current else "·"
            print(PAD + " %s  %s   %s"
                  % (paint(mark, "green" if name == current else "gray"),
                     paint(name.ljust(7), "byellow", "bold"), _swatch()))
        apply_theme(current)                        # restore
        print("")
        print(PAD + paint("set with  " + cli("theme <name>"), "gray"))
        print(PAD + paint("add your own: drop a JSON file in themes/ "
                          "(see themes/README.md)", "gray"))
        return
    if not apply_theme(arg):
        apply_theme(current)
        print(PAD + paint("unknown theme '%s'. options: %s"
                          % (arg, ", ".join(THEME_NAMES)), "yellow"))
        return
    set_setting("theme", arg)
    print(paint("  %s theme set to '%s'." % (OK, arg), "green", "bold"))


# ---- users / profiles -----------------------------------------------------
def _user_count(user, puzzles):
    try:
        with open(progress_path(user)) as f:
            done = len(json.load(f).get("completed", []))
    except (OSError, ValueError):
        done = 0
    return "%d/%d" % (done, len(puzzles))


def cmd_user(arg, puzzles, by_id, prog):
    cur = current_user()
    if not arg:
        print(header("users", "cyan"))
        print("")
        for u in (list_users() or [cur]):
            mark = OK if u == cur else "·"
            print(PAD + " %s  %s  %s"
                  % (paint(mark, "green" if u == cur else "gray"),
                     paint(u.ljust(14), "byellow" if u == cur else "white",
                           "bold"),
                     paint(_user_count(u, puzzles), "gray")))
        print("")
        print(PAD + paint("switch or create with  " + cli("user <name>"),
                          "gray"))
        return prog
    name = arg.strip()
    if not valid_username(name):
        print(PAD + paint("'%s' can't be a profile name." % name, "yellow"))
        print(PAD + "Names become folders under users/, so use only letters,")
        print(PAD + "digits, dashes, or underscores (up to 32 characters).")
        return prog
    if name == cur:
        print(PAD + paint("already on '%s'." % name, "gray"))
        return prog
    # save the current user's work before leaving
    here = current_puzzle(prog, by_id, puzzles)
    if here is not None:
        archive_work(here, load_answers())
    creating = name not in list_users()
    ensure_user(name)
    set_setting("user", name)
    newprog, _ = load_progress(puzzles)
    for k, v in (("mode", "normal"), ("completed", []), ("stats", {}),
                 ("highest", 0)):
        newprog.setdefault(k, v)
    ensure_workspace(current_puzzle(newprog, by_id, puzzles), load_answers(),
                     newprog.get("active"))
    word = "created and switched to" if creating else "switched to"
    print(paint("  %s %s '%s'." % (ARROW, word, name), "cyan", "bold"))
    return newprog


def cmd_reset(puzzles, prog, arg=None):
    keep_mode = prog.get("mode", "normal")
    # wipe this user's saved answers and workspace file
    if os.path.exists(answers_path()):
        os.remove(answers_path())
    fresh = default_progress(puzzles)            # active = False
    fresh["mode"] = keep_mode
    save_progress(fresh)
    write_work(WELCOME_WORK)                      # back to the puzzle-free default
    print(paint("  %s Full reset done." % OK, "green", "bold"))
    print("  Cleared this profile's progress, saved answers, and workspace.")
    print("  Open the menu to start again:  %s" % cli("begin"))


# ---- shortcuts (local vs persistent) --------------------------------------
def _shortcuts_paths():
    shortcuts = os.path.join(ROOT, "shell", "pyquest.zsh")
    home = os.path.expanduser("~")
    shell = os.environ.get("SHELL", "")
    rc = os.path.join(home, ".bashrc" if shell.endswith("bash") else ".zshrc")
    return shortcuts, rc


def _local_source_cmd():
    shortcuts, _ = _shortcuts_paths()
    return 'source "%s"' % shortcuts


def _is_persistent():
    shortcuts, rc = _shortcuts_paths()
    if not os.path.isfile(rc):
        return False
    with open(rc) as f:
        return shortcuts in f.read()


def _install_persistent():
    shortcuts, rc = _shortcuts_paths()
    if not os.path.isfile(shortcuts):
        return "nofile", rc
    if _is_persistent():
        return "installed", rc
    with open(rc, "a") as f:
        f.write('\n# PyQuest shell shortcuts\n'
                '[ -f "%s" ] && source "%s"\n' % (shortcuts, shortcuts))
    return "added", rc


def _uninstall_persistent():
    shortcuts, rc = _shortcuts_paths()
    if not os.path.isfile(rc):
        return False, rc
    with open(rc) as f:
        lines = f.readlines()
    kept, removed = [], False
    for ln in lines:
        if ln.strip() == "# PyQuest shell shortcuts" or (
                "source" in ln and shortcuts in ln):
            removed = True
            continue
        kept.append(ln)
    if removed:
        with open(rc, "w") as f:
            f.writelines(kept)
    return removed, rc


def _disclaimer():
    print(PAD + paint("Shortcuts let you type  ", "gray")
          + paint("check", "green", "bold")
          + paint("  instead of  python3 play.py check.", "gray"))
    print(PAD + paint("They are shell functions defined in shell/pyquest.zsh "
                      "(check, hint, start, …).", "gray"))
    print(PAD + paint("Local = nothing outside this folder changes.  "
                      "Persistent = one line in your shell startup file.",
                      "gray"))


def cmd_setup():
    """Offer both ways to enable the short commands (no surprise edits)."""
    shortcuts, rc = _shortcuts_paths()
    pyver = "Python %d.%d.%d" % sys.version_info[:3]
    print(wordmark("cyan"))
    print("")
    print(header("setup", "cyan"))
    print("")
    print(PAD + paint("python", "cyan", "bold") + "    "
          + paint(pyver, "white", "bold"))
    print(PAD + paint("status", "cyan", "bold") + "    "
          + (paint(OK + " persistent shortcuts enabled in " + rc, "green")
             if _is_persistent()
             else paint("shortcuts not persistently installed", "gray")))
    print("")
    _disclaimer()
    print("")
    print(header("enable the short commands", "magenta"))
    print("")
    print(PAD + paint("A) this terminal only", "white", "bold")
          + paint("   run:  ", "gray") + paint(_local_source_cmd(), "yellow",
                                               "bold"))
    print(PAD + paint("B) every terminal", "white", "bold")
          + paint("      run:  ", "gray")
          + paint("python3 play.py setup persist", "yellow", "bold"))
    print("")
    print(PAD + paint("remove later with  python3 play.py uninstall", "gray"))
    print(PAD + paint("or skip shortcuts entirely -- python3 play.py … always "
                      "works.", "gray"))


def cmd_setup_persist():
    status, rc = _install_persistent()
    if status == "added":
        print(paint("  %s Shortcuts enabled in %s." % (OK, rc), "green", "bold"))
        print("  Activate now:  %s" % paint("source " + rc, "yellow", "bold"))
    elif status == "installed":
        print(paint("  %s Already enabled in %s." % (OK, rc), "green"))
    else:
        print(paint("  %s shell/pyquest.zsh is missing -- can't install." % NO,
                    "red"))


def cmd_uninstall():
    removed, rc = _uninstall_persistent()
    if removed:
        print(paint("  %s Removed PyQuest shortcuts from %s." % (OK, rc),
                    "green", "bold"))
    else:
        print(paint("  No persistent shortcuts in %s." % rc, "gray"))
    # Whether or not the rc line existed, the current shell may still hold the
    # functions; only the shell can clear those.
    print(PAD + paint("New terminals won't load the shortcuts. This terminal "
                      "keeps them until", "gray"))
    print(PAD + paint("you close it -- or run:  %s"
                      % paint("unset -f begin check start hint next …", "yellow"),
                      "gray"))


def cmd_help():
    print(wordmark("cyan"))
    print("")
    rows = [
        ("begin", "open the main menu (start here)"),
        ("menu", "return to the main menu from anywhere"),
        ("setup", "set up the short commands (offers local or persistent)"),
        ("uninstall", "remove the persistent shortcuts"),
        ("(none)", "show progress and the current puzzle"),
        ("check", "validate your work.py"),
        ("hint", "reveal the next hint"),
        ("solution", "show the reference solution"),
        ("map", "show the chapter/puzzle tree"),
        ("next", "move on to the next puzzle"),
        ("goto", "pick a puzzle from a list (bare goto opens the picker)"),
        ("goto <id>", "jump straight there: goto 2.4, or goto 2 for chapter 2"),
        ("skip", "move on without solving the current puzzle"),
        ("retry", "blank the workspace to practice again (stays solved)"),
        ("revert", "fully reset this puzzle: blank code + clear its progress"),
        ("mode <m>", "set difficulty: easy | normal | hard"),
        ("theme <name>", "switch colour theme (neon, amber, forest, mono)"),
        ("user <name>", "switch or create a profile"),
        ("reset", "wipe progress, saved answers, and workspaces"),
    ]
    pre = "" if os.environ.get("PYQUEST_SHELL") else "python3 play.py "
    for name, desc in rows:
        print("%s%s  %s"
              % (PAD, paint((pre + name).ljust(24), "green", "bold"), desc))


# --------------------------------------------------------------------------
# the interactive launcher menu (the one allowed interactive surface).
# The puzzle-solving loop stays single-shot commands; see ARCHITECTURE.md sec 3.
# --------------------------------------------------------------------------
def cmd_menu(puzzles, by_id, prog):
    """Reach the main menu from anywhere -- an alias for `begin`, so a learner
    mid-puzzle can always type `menu` to get back to start/level/theme/etc."""
    return cmd_begin(puzzles, by_id, prog)


def cmd_begin(puzzles, by_id, prog):
    if not sys.stdin.isatty():
        print(wordmark("cyan"))
        _menu_options(puzzles, by_id, prog)
        print(PAD + paint("(run this in a terminal to choose)", "gray"))
        return
    print(wordmark("cyan"))
    while True:
        _menu_options(puzzles, by_id, prog)
        try:
            choice = input(PAD + paint("> ", "cyan", "bold")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("")
            return
        if choice in ("1", "start", "continue", "play", ""):
            cur = current_puzzle(prog, by_id, puzzles)
            activate(prog, cur, load_answers())     # load the puzzle into work.py
            print("")
            print_current_card(prog, cur, show_pointer=(prog["mode"] == "easy"),
                               arriving=True)
            return
        elif choice in ("2", "level", "select", "goto"):
            _menu_level(puzzles, by_id, prog)
        elif choice in ("3", "theme"):
            _menu_theme()
        elif choice in ("4", "users", "user"):
            prog = _menu_users(puzzles, by_id, prog)
        elif choice in ("5", "shortcuts", "short"):
            _menu_shortcuts()
        elif choice in ("6", "q", "quit", "exit"):
            print(PAD + paint("see you in the terminal -- solve with  "
                              + cli("check"), "gray"))
            return
        else:
            print(PAD + paint("type a number 1-6.", "yellow"))
        print("")


def _menu_options(puzzles, by_id, prog):
    done, total = len(prog["completed"]), len(puzzles)
    cur = current_puzzle(prog, by_id, puzzles)
    print("")
    print(header("main menu", "cyan"))
    print("")

    def item(n, lbl, note=""):
        print(PAD + paint(" %s " % n, "byellow", "bold") + "  "
              + paint(lbl.ljust(15), "white", "bold") + paint(note, "gray"))

    here = "%s · %s · %d/%d" % (cur["id"] if cur else "-", prog["mode"],
                                done, total)
    item("1", "start", here)
    item("2", "select level", "jump to any puzzle")
    item("3", "theme", load_settings().get("theme", "neon"))
    item("4", "users", current_user())
    item("5", "shortcuts", "persistent: %s"
         % ("on" if _is_persistent() else "off"))
    item("6", "quit")
    print("")


def _menu_level(puzzles, by_id, prog):
    _goto_list(puzzles, by_id, prog, footer=False)
    try:
        pid = input(PAD + paint("id (blank = cancel) > ", "cyan", "bold")).strip()
    except (EOFError, KeyboardInterrupt):
        return
    if not pid:
        return
    target = _resolve_goto(pid, puzzles, by_id, prog)
    if target is None:
        print(PAD + paint("no puzzle '%s'." % pid, "yellow"))
        return
    # same lock rules as goto -- the menu must not be a side door
    _jump(target, puzzles, by_id, prog)


def _menu_theme():
    # Stay in the theme menu until the user enters a blank line (cancel).
    while True:
        cmd_theme("")                               # show the picker
        try:
            c = input(PAD + paint("theme name (blank = back) > ", "cyan",
                                  "bold")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if not c:
            return
        if c.startswith("theme "):                  # forgive "theme ocean"
            c = c[6:].strip()
        cmd_theme(c)                                # applies + persists live


def _menu_users(puzzles, by_id, prog):
    # Stay in the users menu until a blank line (cancel).
    while True:
        cmd_user("", puzzles, by_id, prog)          # list users
        try:
            c = input(PAD + paint("user name (blank = back) > ", "cyan",
                                  "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            return prog
        if not c:
            return prog
        if c.lower().startswith("user "):           # forgive "user alice"
            c = c[5:].strip()
        prog = cmd_user(c, puzzles, by_id, prog)


def _menu_shortcuts():
    print("")
    print(header("shortcuts", "cyan"))
    print("")
    _disclaimer()
    print("")
    print(PAD + paint(" 1 ", "byellow", "bold")
          + "  enable for THIS terminal (local, nothing saved)")
    print(PAD + paint(" 2 ", "byellow", "bold")
          + "  install persistently (one line in your startup file)")
    print(PAD + paint(" 3 ", "byellow", "bold")
          + "  uninstall (remove the persistent line)")
    print(PAD + paint(" 4 ", "byellow", "bold") + "  back")
    try:
        c = input(PAD + paint("> ", "cyan", "bold")).strip().lower()
    except (EOFError, KeyboardInterrupt):
        return
    if c in ("1", "local"):
        print(PAD + paint("Run this yourself (a program can't source into your "
                          "shell):", "gray"))
        print(PAD + paint(_local_source_cmd(), "yellow", "bold"))
    elif c in ("2", "persist", "install"):
        cmd_setup_persist()
    elif c in ("3", "uninstall", "remove"):
        cmd_uninstall()
