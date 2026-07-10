"""Where the learner is up to: per-user progress.json + answers.json, and the
shared per-chapter workspace (work.py). Owns "where are we?" -- no visuals.

Each user has their own folder under users/<name>/. The active user comes from
settings.json (config). The workspace file is shared scratch, reseeded from the
active user's saved code whenever the puzzle or user changes.
"""

import os
import re
import sys
import json
import shutil

from .config import (USERS_DIR, ROOT, WORK_FILENAME, TEXTBOOK_FILENAME,
                     load_settings, write_json, now)
from .content import read_starter


def backup_corrupt(path):
    """Move an unreadable JSON file aside instead of letting the next save
    destroy it (invariant: progress is recoverable). Returns the backup path,
    or None if nothing could be moved."""
    backup = path + ".corrupt"
    try:
        os.replace(path, backup)
    except OSError:
        return None
    sys.stderr.write("note: %s was unreadable; it was moved to %s and a "
                     "fresh file started.\n"
                     % (os.path.basename(path), os.path.basename(backup)))
    return backup


# ---- users ----------------------------------------------------------------
USERNAME_RE = re.compile(r"^[A-Za-z0-9_-]{1,32}$")


def valid_username(name):
    """Letters, digits, dash, underscore, max 32 -- names become folder names,
    so anything else (spaces, dots, slashes) is rejected before it can write
    outside users/."""
    return bool(USERNAME_RE.match(name or ""))


def current_user():
    # Re-validate here, not only at the write site: settings.json can be
    # hand-edited or corrupted, and this value is joined into a filesystem path
    # (user_dir). A name like "../foo" must never become a path segment, so an
    # invalid stored user falls back to "default" rather than escaping users/.
    user = load_settings().get("user", "default") or "default"
    return user if valid_username(user) else "default"


def user_dir(user=None):
    return os.path.join(USERS_DIR, user or current_user())


def progress_path(user=None):
    return os.path.join(user_dir(user), "progress.json")


def answers_path(user=None):
    return os.path.join(user_dir(user), "answers.json")


def list_users():
    if not os.path.isdir(USERS_DIR):
        return []
    return sorted(d for d in os.listdir(USERS_DIR)
                  if os.path.isdir(os.path.join(USERS_DIR, d)))


def ensure_user(user=None):
    os.makedirs(user_dir(user), exist_ok=True)


def delete_user(name):
    """Remove a profile's folder and everything in it (progress, answers, the
    workspace, the textbook). Returns True if a directory was removed. The caller
    validates the name and guards against deleting the active profile."""
    d = user_dir(name)
    if not os.path.isdir(d):
        return False
    shutil.rmtree(d)
    return True


def rename_user(old, new):
    """Rename a profile folder old -> new, preserving everything inside.
    Returns True on success. The caller validates both names and that `new`
    does not already exist; repointing settings.json at the active user is the
    caller's job too."""
    src, dst = user_dir(old), user_dir(new)
    if not os.path.isdir(src) or os.path.exists(dst):
        return False
    os.rename(src, dst)
    return True


def migrate_legacy():
    """One-time: seed users/ and move any legacy root files into users/default/."""
    if os.path.isdir(USERS_DIR):
        return
    os.makedirs(os.path.join(USERS_DIR, "default"), exist_ok=True)
    for fn, dst in (("progress.json", progress_path("default")),
                    ("answers.json", answers_path("default"))):
        src = os.path.join(ROOT, fn)
        if os.path.isfile(src):
            shutil.move(src, dst)


# ---- progress.json --------------------------------------------------------
def default_progress(puzzles):
    return {
        "version": 1,
        "mode": "normal",
        "current": puzzles[0]["id"] if puzzles else None,
        "completed": [],
        "highest": 0,
        "stats": {},
        "active": False,            # no puzzle is loaded into work.py yet
        "created_at": now(),
        "last_seen": None,          # stamped when a puzzle is loaded (activate)
    }


# Shown in work.py before any puzzle is loaded (a default, puzzle-free state).
WELCOME_WORK = (
    "# PyQuest -- no puzzle loaded yet.\n"
    "#\n"
    "# Open the menu to choose where to start:\n"
    "#     python3 start.py menu        (or just  menu  with the shortcuts)\n"
    "#\n"
    "# Pick a level and choose 'start', and the puzzle's code will appear\n"
    "# here. Then edit it, save the file, and run  check.\n"
)


def load_progress(puzzles):
    path = progress_path()
    if os.path.exists(path):
        try:
            with open(path) as f:
                data = json.load(f)
            if not isinstance(data, dict):   # valid JSON but not a progress
                raise ValueError("progress.json is not an object")
        except (ValueError, OSError):
            backup_corrupt(path)             # keep the evidence, start fresh
            data = default_progress(puzzles)
        return data, False
    data = default_progress(puzzles)
    save_progress(data)
    return data, True


def save_progress(prog):
    ensure_user()
    write_json(progress_path(), prog)


def stat(prog, pid):
    return prog["stats"].setdefault(pid, {"attempts": 0, "hints_used": 0})


def current_puzzle(prog, by_id, puzzles):
    cur = by_id.get(prog.get("current"))
    if cur is None and puzzles:
        cur = puzzles[0]
        prog["current"] = cur["id"]
    return cur


# ---- answers.json ---------------------------------------------------------
def load_answers():
    path = answers_path()
    if os.path.exists(path):
        try:
            with open(path) as f:
                data = json.load(f)
            if not isinstance(data, dict):   # valid JSON but not answers
                raise ValueError("answers.json is not an object")
            return data
        except (ValueError, OSError):
            backup_corrupt(path)             # saved code is sacred; keep it
            return {}
    return {}


def save_answers(answers):
    ensure_user()
    write_json(answers_path(), answers)


# ---- workspace (work.py) --------------------------------------------------
# One editable file per user (users/<name>/work.py). It holds the active
# puzzle's draft; switching puzzle or user reseeds it from saved code/starter.
def work_path():
    return os.path.join(user_dir(), WORK_FILENAME)


def read_work():
    path = work_path()
    if os.path.isfile(path):
        with open(path) as f:
            return f.read()
    return ""


def write_work(code):
    ensure_user()
    with open(work_path(), "w", encoding="utf-8") as f:
        f.write(code)


def textbook_path():
    return os.path.join(user_dir(), TEXTBOOK_FILENAME)


def write_textbook(text):
    """(Re)generate the per-user textbook markdown the learner opens via a link.
    Owned by the engine like work.py -- regenerated on each summon."""
    ensure_user()
    with open(textbook_path(), "w", encoding="utf-8") as f:
        f.write(text)


def archive_work(puzzle, answers, solved=None):
    """Save the current work-file contents into answers.json for this puzzle."""
    entry = answers.setdefault(puzzle["id"], {"solved": False, "code": ""})
    entry["code"] = read_work()
    if solved is not None:
        entry["solved"] = solved
    save_answers(answers)
    return entry


def archive_current(prog, by_id, puzzles, answers=None):
    """Snapshot the active puzzle's live draft into answers before switching
    profile, exporting, or jumping away. A no-op when no puzzle is loaded, so
    the welcome placeholder is never saved as a puzzle's code. Returns the
    answers dict it wrote into (loaded here if not supplied)."""
    if answers is None:
        answers = load_answers()
    if prog.get("active"):
        here = current_puzzle(prog, by_id, puzzles)
        if here is not None:
            archive_work(here, answers)
    return answers


def ensure_workspace(puzzle, answers, active=False):
    """Make sure work.py exists. If a puzzle is active, hold its draft; if not,
    show the puzzle-free welcome placeholder."""
    if os.path.isfile(work_path()):
        return
    reseed_workspace(puzzle, answers, active)


def reseed_workspace(puzzle, answers, active=False):
    """Force work.py to match a profile's state: the active puzzle's saved draft
    (or its fresh starter) when a puzzle is loaded, else the welcome placeholder.

    Unlike ensure_workspace (create-if-missing), this ALWAYS rewrites. Used when
    switching profile: each user has their own work.py, but the incoming file may
    be stale relative to that profile's `current` puzzle (e.g. seeded by an
    import or an older session), and trusting it lets the learner edit the wrong
    puzzle -- whose code a later `check` then archives under the current id."""
    if active and puzzle is not None:
        saved = answers.get(puzzle["id"], {}).get("code")
        write_work(saved if saved else read_starter(puzzle))
    else:
        write_work(WELCOME_WORK)


def activate(prog, puzzle, answers):
    """Load `puzzle` into work.py and mark the session active (a puzzle loaded)."""
    prog["active"] = True
    prog["last_seen"] = now()       # "last sat down to work" -- read by stats
    if puzzle is not None:
        saved = answers.get(puzzle["id"], {}).get("code")
        write_work(saved if saved else read_starter(puzzle))
    save_progress(prog)


def switch_to(target, prog, by_id, puzzles, answers, unlock=False):
    """Move the active puzzle to `target`, preserving the current draft and
    loading the target's saved code (or its fresh starter).

    `unlock=True` raises the high-water mark that gates forward `goto` in
    normal/hard mode. Only earned advancement (next/skip) passes it -- a plain
    jump must never permanently unlock the course for the stricter modes."""
    cur = by_id.get(prog.get("current"))
    if cur is not None and prog.get("active"):
        archive_work(cur, answers)        # don't archive the welcome placeholder
    prog["current"] = target["id"]
    prog["active"] = True
    prog["last_seen"] = now()
    if unlock and target["index"] > prog["highest"]:
        prog["highest"] = target["index"]
    saved = answers.get(target["id"], {}).get("code")
    write_work(saved if saved else read_starter(target))
    save_progress(prog)
