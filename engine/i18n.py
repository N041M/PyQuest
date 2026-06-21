"""Human-language piping. English is the built-in default AND the fallback: it
ships in the code itself (the `default` passed to every t() call), so it can
never be missing. Other languages are community 'packs' dropped under lang/<code>/
-- nothing here is translated; this is only the plumbing.

A pack is:
    lang/<code>/pack.json     {"name": "Čeština", "code": "cs"}
    lang/<code>/strings.json  {"<key>": "<translation>", ...}   (partial is fine)
    lang/<code>/chapters/...  optional file-backed content overrides (reference.md)

t(key, default) returns the active pack's value for `key`, or `default` (English)
when there is no pack or the pack omits that key -- so a half-finished pack still
runs, every untranslated string just stays English. localized(path) is the same
idea for FILE-backed content (the textbook's reference.md): it maps a default file
under chapters/ to the pack's mirrored copy when one exists, else returns the
English file unchanged -- so a pack translates the content files it wants and the
rest stay English. Selecting a pack VALIDATES it first; if it doesn't load,
set_language reports exactly what's missing and falls back to English, so the
program is never left in a broken language.
"""

import os
import json

from .config import ROOT, CHAPTERS_DIR

LANG_DIR = os.path.join(ROOT, "lang")

# The active language. "en" means no pack -> every t() returns its English
# default. A pack swaps `strings` in; a per-key miss still falls back.
_active = {"code": "en", "strings": {}}


def t(key, default):
    """The active language's string for `key`, or `default` (always the English
    text, written inline at the call site) when unset or untranslated."""
    return _active["strings"].get(key, default)


def current():
    return _active["code"]


def localized(path):
    """The active language's override for a default content file, or `path`
    unchanged. `path` is a file under chapters/ (e.g. a topic's reference.md);
    the override lives at the mirrored path under lang/<code>/chapters/. This is
    the file-backed analogue of t(): English (the on-disk file) is the fallback,
    a pack overrides per file, and any file a pack doesn't supply stays English.
    A path outside chapters/ (or a pack that has no copy) is returned as-is."""
    code = _active["code"]
    if code == "en":
        return path
    try:
        rel = os.path.relpath(path, CHAPTERS_DIR)
    except ValueError:                       # e.g. different drive on Windows
        return path
    if rel == os.pardir or rel.startswith(os.pardir + os.sep):
        return path                          # not under chapters/ -- never escape
    candidate = os.path.join(_pack_dir(code), "chapters", rel)
    return candidate if os.path.isfile(candidate) else path


def _pack_dir(code):
    return os.path.join(LANG_DIR, code)


def validate(code):
    """Does language `code` load as a usable pack? Returns (True, display_name)
    or (False, what_is_missing) -- the second a human-readable reason naming the
    exact file/field at fault, for the error shown on a failed select."""
    if code == "en":
        return True, "English"
    d = _pack_dir(code)
    if not os.path.isdir(d):
        return False, "no lang/%s/ folder" % code
    meta = _load_json(os.path.join(d, "pack.json"))
    if isinstance(meta, str):                         # _load_json returns the error
        return False, meta
    if not isinstance(meta, dict) or not meta.get("name"):
        return False, "pack.json has no \"name\""
    if meta.get("code") not in (None, code):
        return False, "pack.json code %r does not match folder %r" % (
            meta.get("code"), code)
    strings = _load_json(os.path.join(d, "strings.json"))
    if isinstance(strings, str):
        return False, strings
    if not isinstance(strings, dict):
        return False, "strings.json is not a JSON object"
    return True, meta["name"]


def _load_json(path):
    """The parsed JSON, or a human-readable error STRING (so callers can tell a
    failure from a dict/list result)."""
    if not os.path.isfile(path):
        return "missing %s" % os.path.basename(path)
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except ValueError as e:
        return "%s is not valid JSON (%s)" % (os.path.basename(path), e)
    except OSError as e:
        return "could not read %s (%s)" % (os.path.basename(path), e)


def available():
    """English plus every pack under lang/ that validates: [(code, name), ...].
    Broken packs are simply left out of the list (a select would also reject)."""
    langs = [("en", "English")]
    if os.path.isdir(LANG_DIR):
        for code in sorted(os.listdir(LANG_DIR)):
            if os.path.isdir(_pack_dir(code)):
                ok, name = validate(code)
                if ok:
                    langs.append((code, name))
    return langs


def set_language(code):
    """Activate `code`, falling back to English on any failure. Returns
    (ok, message): ok=False means we fell back and `message` says what was
    missing (suitable to show the user). The active state is ALWAYS usable
    afterwards -- English at worst."""
    if not code or code == "en":
        _active.update(code="en", strings={})
        return True, None
    ok, info = validate(code)
    if not ok:
        _active.update(code="en", strings={})
        return False, ("language '%s' couldn't load: %s. Using English."
                       % (code, info))
    strings = _load_json(os.path.join(_pack_dir(code), "strings.json"))
    _active.update(code=code, strings=strings)
    return True, None
