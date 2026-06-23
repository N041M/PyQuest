"""Config-ish verbs: theme (colour palette), mode (difficulty), user
(per-profile progress), and wipe (erase this profile). They compose state +
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
from ..i18n import t


# ---- themes ---------------------------------------------------------------
def _swatch():
    return "".join(paint("██", r) for r in
                   ("cyan", "byellow", "green", "yellow", "red", "magenta"))


def cmd_theme(arg):
    current = load_settings().get("theme", "neon")
    if not arg:
        print(header(t("theme.list_title", "themes"), "cyan"))
        print("")
        for name in THEME_NAMES:
            apply_theme(name)                       # color the row in its theme
            mark = OK if name == current else "·"
            print(PAD + " %s  %s   %s"
                  % (paint(mark, "green" if name == current else "gray"),
                     paint(name.ljust(7), "byellow", "bold"), _swatch()))
        apply_theme(current)                        # restore
        print("")
        print(PAD + paint(t("theme.set_with", "set with  ") + cli("theme <name>"),
                          "gray"))
        print(PAD + paint(t("theme.add_own",
                          "add your own: drop a JSON file in themes/ "
                          "(see themes/README.md)"), "gray"))
        return
    if not apply_theme(arg):
        apply_theme(current)
        print(PAD + paint(t("theme.unknown", "unknown theme '%s'. options: %s")
                          % (arg, ", ".join(THEME_NAMES)), "yellow"))
        return
    set_setting("theme", arg)
    print(paint("  %s " % OK + t("theme.set", "theme set to '%s'.") % arg,
                "green", "bold"))


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
        print(header(t("user.list_title", "users"), "cyan"))
        print("")
        for u in (list_users() or [cur]):
            mark = OK if u == cur else "·"
            print(PAD + " %s  %s  %s"
                  % (paint(mark, "green" if u == cur else "gray"),
                     paint(u.ljust(14), "byellow" if u == cur else "white",
                           "bold"),
                     paint(_user_count(u, puzzles), "gray")))
        print("")
        print(PAD + paint(t("user.switch_create", "switch or create with  ")
                          + cli("user <name>"), "gray"))
        print(PAD + paint(t("user.manage", "rename  %s      delete  %s")
                          % (cli("user rename <old> <new>"),
                             cli("user delete <name>")), "gray"))
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
        print(PAD + paint(t("user.no_spaces",
                          "'%s' can't be a profile name (no spaces).") % arg,
                          "yellow"))
        print(PAD + t("user.manage_hint", "To manage profiles:  %s  ·  %s")
              % (cli("user rename <old> <new>"), cli("user delete <name>")))
        return prog
    name = tokens[0]
    if not valid_username(name):
        print(PAD + paint(t("user.invalid_name", "'%s' can't be a profile name.")
                          % name, "yellow"))
        print(PAD + t("user.name_rules_1",
              "Names become folders under users/, so use only letters,"))
        print(PAD + t("user.name_rules_2",
              "digits, dashes, or underscores (up to 32 characters)."))
        return prog
    if name == cur:
        print(PAD + paint(t("user.already_on", "already on '%s'.") % name,
                          "gray"))
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
    word = (t("user.created_switched", "created and switched to") if creating
            else t("user.switched_to", "switched to"))
    print(paint("  %s %s '%s'." % (ARROW, word, name), "cyan", "bold"))
    return newprog


def _user_delete(name, prog):
    """Remove a profile and all its files. Refuses the active profile (switch
    away first) so the engine is never left pointing at a folder that's gone."""
    cur = current_user()
    if not name:
        print(PAD + paint(t("ui.usage", "usage:  ") + cli("user delete <name>"),
                          "yellow"))
        return prog
    if not valid_username(name) or name not in list_users():
        print(paint("  %s " % NO + t("user.no_profile", "No profile '%s'.")
                    % name, "yellow"))
        return prog
    if name == cur:
        print(paint("  %s " % NO + t("user.is_active", "'%s' is the active "
                    "profile.") % name, "yellow"))
        print(PAD + t("user.switch_first", "Switch to another first:  %s")
              % cli("user <other>"))
        return prog
    delete_user(name)
    print(paint("  %s " % OK + t("user.deleted",
                "Deleted profile '%s' and all its progress.") % name,
                "green", "bold"))
    return prog


def _user_rename(old, new, prog):
    """Rename a profile, keeping its progress/answers. If it's the active one,
    repoint settings.json so the learner stays put under the new name."""
    if not old or not new:
        print(PAD + paint(t("ui.usage", "usage:  ")
                          + cli("user rename <old> <new>"), "yellow"))
        return prog
    if not valid_username(old) or old not in list_users():
        print(paint("  %s " % NO + t("user.no_profile", "No profile '%s'.")
                    % old, "yellow"))
        return prog
    if not valid_username(new):
        print(PAD + paint(t("user.invalid_name", "'%s' can't be a profile name.")
                          % new, "yellow"))
        print(PAD + t("user.name_rules",
              "Use only letters, digits, dashes, or underscores "
              "(up to 32 characters)."))
        return prog
    if new == old:
        print(PAD + paint(t("user.same_name", "'%s' is already its name.") % old,
                          "gray"))
        return prog
    if new in list_users():
        print(paint("  %s " % NO + t("user.exists", "Profile '%s' already "
                    "exists.") % new, "yellow"))
        return prog
    rename_user(old, new)
    if old == current_user():
        set_setting("user", new)
    print(paint("  %s " % OK + t("user.renamed", "Renamed '%s' to '%s'.")
                % (old, new), "green", "bold"))
    return prog


_WIPE_OK = ("profile", "all", "yes", "confirm")


def cmd_wipe(puzzles, prog, arg=None):
    """Erase the whole active profile. Irreversible, so it requires the explicit
    second word -- `wipe profile` -- to fire; bare `wipe` only explains. That
    confirmation gesture is pipe-safe (no prompt to hang a script)."""
    if (arg or "").strip().lower() not in _WIPE_OK:
        user = current_user()
        print(paint("  %s " % NO + t("wipe.warn",
                    "This erases EVERYTHING in profile '%s' --") % user,
                    "yellow", "bold"))
        print("  " + t("wipe.warn_2",
              "every completed puzzle, all saved code, and the workspace."))
        print(PAD + t("wipe.confirm_hint", "It cannot be undone. To go ahead:  %s")
              % cli("wipe profile"))
        print(PAD + paint(t("wipe.restart_hint",
                          "(to clear just the current puzzle instead, use  %s)")
                          % cli("restart"), "gray"))
        return
    keep_mode = prog.get("mode", "normal")
    # wipe this user's saved answers and workspace file
    if os.path.exists(answers_path()):
        os.remove(answers_path())
    fresh = default_progress(puzzles)            # active = False
    fresh["mode"] = keep_mode
    save_progress(fresh)
    write_work(WELCOME_WORK)                      # back to the puzzle-free default
    print(paint("  %s " % OK + t("wipe.done", "Profile wiped."), "green", "bold"))
    print("  " + t("wipe.cleared",
          "Cleared this profile's progress, saved code, and workspace."))
    print("  " + t("wipe.open_menu", "Open the menu to start again:  %s")
          % cli("menu"))


# ---- mode (difficulty) ----------------------------------------------------
def cmd_mode(prog, arg):
    arg = (arg or "").lower()
    if arg not in MODES:
        print(t("mode.usage", "Usage: %s") % cli("mode <easy|normal|hard>"))
        print(t("mode.current", "Current mode: %s")
              % paint(prog["mode"], "magenta", "bold"))
        return
    prog["mode"] = arg
    save_progress(prog)
    desc = {
        "easy": t("mode.desc_easy",
                  "Pointers shown, hints/solution always available, free jumps."),
        "normal": t("mode.desc_normal",
                    "Hints on demand, skip forward allowed."),
        "hard": t("mode.desc_hard",
                  "No skips; hints after 3 tries; solution after solving; "
                  "textbook sealed."),
    }[arg]
    print(paint("  %s " % OK + t("mode.set", "Mode set to '%s'.") % arg,
                "magenta", "bold"))
    print("  " + desc)
