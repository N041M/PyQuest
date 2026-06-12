"""Constants, paths, and the settings file. Depends on nothing in the package."""

import os
import sys
import json
import shutil
import tempfile
import datetime

# Project root is the folder that contains this package (and play.py, chapters/).
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
USERS_DIR = os.path.join(ROOT, "users")            # per-user progress/answers
THEMES_DIR = os.path.join(ROOT, "themes")          # user-made JSON theme presets
SETTINGS_PATH = os.path.join(ROOT, "settings.json")  # current user + theme
WORK_FILENAME = "work.py"
PY = sys.executable
TIMEOUT = 10
MODES = ("easy", "normal", "hard")

DEFAULT_SETTINGS = {"user": "default", "theme": "neon"}


def load_settings():
    try:
        with open(SETTINGS_PATH) as f:
            data = json.load(f)
    except (OSError, ValueError):
        data = {}
    out = dict(DEFAULT_SETTINGS)
    out.update(data or {})
    return out


def write_json(path, data):
    """Write JSON atomically: a crash mid-write can never leave a corrupt or
    half-written file (the temp file is renamed into place in one step)."""
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path) or ".",
                               prefix=os.path.basename(path) + ".")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def save_settings(settings):
    write_json(SETTINGS_PATH, settings)


def set_setting(key, value):
    s = load_settings()
    s[key] = value
    save_settings(s)
    return s


def _term_width():
    try:
        cols = shutil.get_terminal_size((80, 24)).columns
    except Exception:
        cols = 80
    return max(56, min(cols, 120))


WIDTH = _term_width()       # frames span the terminal (capped for readability)


def now():
    return datetime.datetime.now().isoformat(timespec="seconds")


def rel(path):
    return os.path.relpath(path, ROOT)
