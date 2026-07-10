"""Config-ish verbs: theme (colour palette), mode (difficulty), user
(per-profile progress), and wipe (erase this profile). They compose state +
settings + render.

Profile portability (export/import) is a separate concern -- see transfer.py.
"""

import os
import sys
import json
import shutil

from ..config import load_settings, set_setting, MODES
from ..theme import apply_theme, THEME_NAMES
from ..state import (current_puzzle, load_answers, archive_current,
                     save_progress, load_progress, default_progress,
                     reseed_workspace, answers_path, progress_path,
                     list_users, current_user, ensure_user, valid_username,
                     delete_user, rename_user, write_work, WELCOME_WORK,
                     users_root)
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
        width = max(len(name) for name in THEME_NAMES)
        for name in THEME_NAMES:
            apply_theme(name)                       # color the row in its theme
            mark = OK if name == current else "·"
            print(PAD + " %s  %s   %s"
                  % (paint(mark, "green" if name == current else "gray"),
                     paint(name.ljust(width), "byellow", "bold"), _swatch()))
        apply_theme(current)                        # restore
        print("")
        print(PAD + paint((t("theme.set_with", "set with") + "  ") + cli("theme <name>"),
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
        print(PAD + paint((t("user.switch_create", "switch or create with") + "  ")
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
    # same default app.main() applies on load: a legacy progress.json without
    # the flag must still count a mid-course profile as active, or the reseed
    # below would blank its work.py to the welcome placeholder.
    newprog.setdefault("active", len(newprog["completed"]) > 0)
    # Reseed (not merely ensure) work.py so the workspace shows THIS profile's
    # current puzzle -- otherwise a stale file left in the target user's folder
    # would keep the wrong puzzle on screen and get archived under the new id.
    reseed_workspace(current_puzzle(newprog, by_id, puzzles), load_answers(),
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
        print(PAD + paint((t("ui.usage", "usage:") + "  ") + cli("user delete <name>"),
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
        print(PAD + paint((t("ui.usage", "usage:") + "  ")
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


_WIPE_OK = ("profile", "yes", "confirm")
_WIPE_ALL = ("everything", "all", "global")
_WIPE_PHRASE = "ERASE"                 # typed exactly, so it can't be an accident


def cmd_wipe(puzzles, prog, arg=None):
    """Erase progress, in two tiers. `wipe profile` resets the ACTIVE profile
    to zero -- irreversible, so it requires that explicit second word; the
    gesture is pipe-safe (no prompt to hang a script). `wipe everything` is the
    factory reset: it deletes EVERY profile plus the settings, and being that
    much bigger a blast it additionally demands the learner TYPE the
    confirmation phrase at a real prompt (see _wipe_everything). Bare `wipe`
    only explains.

    Returns prog: the FRESH progress after a real wipe (the caller must adopt
    it -- a cockpit session that kept the old dict would re-save the erased
    state on its next verb, silently undoing the wipe), the incoming one
    otherwise."""
    word = (arg or "").strip().lower()
    if word in _WIPE_ALL:
        return _wipe_everything(puzzles, prog)
    if word not in _WIPE_OK:
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
        print(PAD + paint(t("wipe.all_hint",
                          "(to delete every profile and start factory-fresh:  %s)")
                          % cli("wipe everything"), "gray"))
        return prog
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
    return fresh


def _wipe_everything(puzzles, prog):
    """The factory reset: delete every profile -- and users/settings.json with
    them, so theme/language/active-user go back to defaults too. The next
    launch starts as a fresh install.

    Bulletproofing, deliberately stricter than `wipe profile`: the learner must
    TYPE the confirmation phrase at a real prompt, and without a TTY it refuses
    outright -- there is no argv form, so no script, pipe, or mistyped one-shot
    can ever erase every learner on the machine. Returns the fresh prog on a
    wipe (the caller adopts it; it is inactive, so a cockpit session ends), the
    incoming one on a cancel/refusal."""
    users = list_users()
    print(paint("  %s " % NO + t("wipe.all_warn",
                "This deletes EVERY profile on this install --"), "red", "bold"))
    for u in users:
        print(PAD + " %s  %s" % (paint(u.ljust(14), "byellow", "bold"),
                                 paint(_user_count(u, puzzles), "gray")))
    print("  " + t("wipe.all_warn_2",
          "all progress, saved code, notes, and settings (theme, language)."))
    if not sys.stdin.isatty():
        print(PAD + paint(t("wipe.all_tty_only",
                          "Run this in a terminal -- it needs a typed "
                          "confirmation."), "yellow"))
        return prog
    print(PAD + t("wipe.all_how",
                  "Type %s (exactly) to go ahead; anything else cancels.")
          % paint(_WIPE_PHRASE, "red", "bold"))
    try:
        answer = input(PAD + paint("> ", "red", "bold")).strip()
    except (EOFError, KeyboardInterrupt):
        print("")
        answer = ""
    if answer != _WIPE_PHRASE:
        print(PAD + paint(t("wipe.all_cancelled",
                          "Cancelled -- nothing was deleted."), "gray"))
        return prog
    shutil.rmtree(users_root(), ignore_errors=True)
    fresh = default_progress(puzzles)            # active = False; mode default
    print(paint("  %s " % OK + t("wipe.all_done",
                "Everything wiped -- every profile deleted."), "green", "bold"))
    print("  " + t("wipe.all_fresh",
          "PyQuest is factory-fresh; the next launch starts from scratch."))
    print("  " + t("wipe.open_menu", "Open the menu to start again:  %s")
          % cli("menu"))
    return fresh


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
