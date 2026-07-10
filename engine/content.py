"""The structured question: discovery of chapters/puzzles and file loaders.

Owns "what is this puzzle?" -- it never touches progress or visuals.
"""

import os
import sys
import json
import importlib.util

from .config import CHAPTERS_DIR
from . import i18n


def discover():
    """Scan chapters/ and return an ordered list of puzzle dicts."""
    puzzles = []
    if not os.path.isdir(CHAPTERS_DIR):
        return puzzles
    for ch_name in sorted(os.listdir(CHAPTERS_DIR)):
        ch_path = os.path.join(CHAPTERS_DIR, ch_name)
        if not os.path.isdir(ch_path):
            continue
        try:
            ch_num = int(ch_name.split("_")[0])
        except ValueError:
            continue
        ch_title = " ".join(ch_name.split("_")[1:]).title() or ch_name
        for pz_name in sorted(os.listdir(ch_path)):
            pz_path = os.path.join(ch_path, pz_name)
            meta_path = os.path.join(pz_path, "meta.json")
            if not os.path.isfile(meta_path):
                continue
            try:
                pz_num = int(pz_name.split("_")[0])
            except ValueError:
                continue
            try:
                with open(meta_path, encoding="utf-8") as f:
                    meta = json.load(f)
                if not isinstance(meta, dict):
                    raise ValueError("meta.json is not an object")
            except (OSError, ValueError) as e:
                # one broken puzzle must not brick every command
                sys.stderr.write("note: skipping %s (%s)\n" % (meta_path, e))
                continue
            puzzles.append({
                "id": "%d.%d" % (ch_num, pz_num),
                "ch_num": ch_num, "pz_num": pz_num,
                "ch_title": meta.get("chapter", ch_title),
                "dir": pz_path, "meta": meta,
            })
    for i, p in enumerate(puzzles):
        p["index"] = i
    return puzzles


# Curriculum categories group the chapters in the map and textbook. A chapter's
# category is a property of its CONTENT, not its number: a project chapter is any
# whose puzzles carry a `kind`; an advanced chapter declares meta "category";
# everything else is the default (the first entry). Display order follows the
# chapter numbers; this tuple only names the known categories.
CATEGORIES = ("Core", "Advanced", "Projects")


def category(puzzle):
    """The curriculum category a puzzle (hence its chapter) belongs to."""
    meta = puzzle["meta"]
    if meta.get("kind"):
        return "Projects"
    return meta.get("category") or CATEGORIES[0]


# ---- file locations -------------------------------------------------------
# (The editable workspace, work.py, lives per-user; see state.work_path.)
def starter_path(puzzle):
    return os.path.join(puzzle["dir"], "starter.py")


def read_starter(puzzle):
    path = starter_path(puzzle)
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
    return "# %s -- %s\n# TODO: your code here\n" % (
        puzzle["id"], puzzle["meta"].get("title", ""))


# ---- brief / hints / tests ------------------------------------------------
# The per-topic content files routed through i18n.localized -- the set a language
# pack may override under lang/<code>/chapters/. Kept here, beside the loaders
# that read them, as the single source of truth (tools/check_pack.py reuses it).
LOCALIZED_CONTENT = ("brief.md", "hints.md", "reference.md")


def brief_path(dirpath):
    """The brief the card points the learner at, as the active language's
    override when a pack supplies one, else the English brief.md. The brief is
    read by the learner in their own editor, so this returns the path to show,
    not the text."""
    return i18n.localized(os.path.join(dirpath, "brief.md"))


def load_hints(dirpath):
    path = i18n.localized(os.path.join(dirpath, "hints.md"))
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = text.replace("\r\n", "\n")       # Windows-edited hints still split
    parts = [p.strip() for p in text.split("\n---\n")]
    return [p for p in parts if p]


def load_reference(dirpath):
    """The optional reference.md: a topic's detailed, technical textbook entry.
    Returns its markdown, or None when a topic has no reference authored yet (the
    textbook then falls back to the one-line concept). The active language pack
    may override the file; a topic it doesn't translate stays English."""
    if not dirpath:
        return None
    path = i18n.localized(os.path.join(dirpath, "reference.md"))
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n")


def load_tests(dirpath):
    path = os.path.join(dirpath, "tests.py")
    name = "pyquest_tests_" + os.path.basename(dirpath)
    sys.modules.pop(name, None)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    # Don't leave a __pycache__/tests.*.pyc behind: chapters/ is pure data, and
    # every `check` imports this module -- writing bytecode there would litter
    # each lesson folder with engine artifacts on every run.
    saved = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.dont_write_bytecode = saved
    return mod
