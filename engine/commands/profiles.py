"""Config-ish verbs: theme (colour palette), mode (difficulty), user
(per-profile progress), and reset (wipe this profile). They compose state +
settings + render.

Profile portability (export/import) is a separate concern -- see transfer.py.
"""

import os
import json

from ..config import load_settings, set_setting, MODES
from ..theme import apply_theme, THEME_NAMES
from ..state import (current_puzzle, load_answers, archive_current,
                     save_progress, load_progress, default_progress,
                     ensure_workspace, answers_path, progress_path,
                     list_users, current_user, ensure_user, valid_username,
                     delete_user, rename_user, write_work, WELCOME_WORK)
from ..render import paint, header, cli, PAD, OK, NO, ARROW


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
    tokens = (arg or "").split()
    if not tokens:
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
        print(PAD + paint("rename  " + cli("user rename <old> <new>")
                          + "      delete  " + cli("user delete <name>"),
                          "gray"))
        return prog
    # `delete`/`rename` are management subcommands, not profile names (names
    # never contain spaces, so a multi-token arg is always one of these or a
    # typo). A profile literally named "delete"/"rename" is the price of the
    # keywords -- a deliberate, documented trade.
    sub = tokens[0].lower()
    if sub in ("delete", "remove", "rm"):
        return _user_delete(tokens[1] if len(tokens) > 1 else "", prog)
    if sub in ("rename", "mv"):
        return _user_rename(tokens[1] if len(tokens) > 1 else "",
                            tokens[2] if len(tokens) > 2 else "", prog)
    if len(tokens) > 1:
        print(PAD + paint("'%s' can't be a profile name (no spaces)." % arg,
                          "yellow"))
        print(PAD + "To manage profiles:  %s  ·  %s"
              % (cli("user rename <old> <new>"), cli("user delete <name>")))
        return prog
    name = tokens[0]
    if not valid_username(name):
        print(PAD + paint("'%s' can't be a profile name." % name, "yellow"))
        print(PAD + "Names become folders under users/, so use only letters,")
        print(PAD + "digits, dashes, or underscores (up to 32 characters).")
        return prog
    if name == cur:
        print(PAD + paint("already on '%s'." % name, "gray"))
        return prog
    archive_current(prog, by_id, puzzles)        # save the leaving user's work
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


def _user_delete(name, prog):
    """Remove a profile and all its files. Refuses the active profile (switch
    away first) so the engine is never left pointing at a folder that's gone."""
    cur = current_user()
    if not name:
        print(PAD + paint("usage:  " + cli("user delete <name>"), "yellow"))
        return prog
    if not valid_username(name) or name not in list_users():
        print(paint("  %s No profile '%s'." % (NO, name), "yellow"))
        return prog
    if name == cur:
        print(paint("  %s '%s' is the active profile." % (NO, name), "yellow"))
        print(PAD + "Switch to another first:  %s" % cli("user <other>"))
        return prog
    delete_user(name)
    print(paint("  %s Deleted profile '%s' and all its progress." % (OK, name),
                "green", "bold"))
    return prog


def _user_rename(old, new, prog):
    """Rename a profile, keeping its progress/answers. If it's the active one,
    repoint settings.json so the learner stays put under the new name."""
    if not old or not new:
        print(PAD + paint("usage:  " + cli("user rename <old> <new>"),
                          "yellow"))
        return prog
    if not valid_username(old) or old not in list_users():
        print(paint("  %s No profile '%s'." % (NO, old), "yellow"))
        return prog
    if not valid_username(new):
        print(PAD + paint("'%s' can't be a profile name." % new, "yellow"))
        print(PAD + "Use only letters, digits, dashes, or underscores "
              "(up to 32 characters).")
        return prog
    if new == old:
        print(PAD + paint("'%s' is already its name." % old, "gray"))
        return prog
    if new in list_users():
        print(paint("  %s Profile '%s' already exists." % (NO, new), "yellow"))
        return prog
    rename_user(old, new)
    if old == current_user():
        set_setting("user", new)
    print(paint("  %s Renamed '%s' to '%s'." % (OK, old, new), "green", "bold"))
    return prog


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


# ---- mode (difficulty) ----------------------------------------------------
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
