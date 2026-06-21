"""One-file translation worksheet: every translatable instance, English
prewritten, in a single editable file -- then split into the pack the engine
loads.

    python3 tools/lang_worksheet.py new <code>     write lang/<code>.worksheet.txt,
                                                   prefilled with every English UI
                                                   string + every puzzle's
                                                   brief/hints/reference
    python3 tools/lang_worksheet.py apply <code>   split a filled worksheet into
                                                   lang/<code>/ (pack.json,
                                                   strings.json, chapters/...)

Translate in place -- overwrite the English under each `#@ pyquest:` marker.
`apply` writes only the entries you actually changed, so a partial translation
stays partial (every untouched string/file falls back to English, the engine's
design). The worksheet lives as a loose `lang/<code>.worksheet.txt` file, which
the engine and the pack checker ignore (they only look at pack directories), so a
half-finished worksheet never shows up as a broken language.
"""

import ast
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINE_DIR = os.path.join(ROOT, "engine")
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
LANG_DIR = os.path.join(ROOT, "lang")

# The content files the engine localizes (mirror of content.LOCALIZED_CONTENT).
LOCALIZED_CONTENT = ("brief.md", "hints.md", "reference.md")

MARK = "#@ pyquest:"          # an entry header; bodies never start with this
NAME_PLACEHOLDER = "Your language's own name -- replace this (e.g. Cestina)"

PREAMBLE = """\
# PyQuest translation worksheet -- every translatable instance, in one file.
#
# Translate the text UNDER each "%s<kind> <id>" marker, replacing the English in
# place. Leave anything you don't want to translate as-is: `apply` writes only
# what you changed, so the rest falls back to English.
#
#   meta name      -> your language's display name (set this first)
#   string <key>   -> a one-line UI string
#   file <path>    -> a content file (brief/hints/reference); keep its markdown
#                     structure and any ``` code blocks exactly -- only the prose
#                     is localized, the grader is language-agnostic.
#
# Then: python3 tools/lang_worksheet.py apply <code>
# Lines above the first marker (like these) are ignored.
""" % MARK


# ---- reading the English source -------------------------------------------
def _ui_strings():
    """Every (key, English) wired through i18n.t("key", "English") in engine/,
    first occurrence wins, sorted by key."""
    out = {}
    for dirpath, dirs, files in os.walk(ENGINE_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for name in files:
            if not name.endswith(".py"):
                continue
            try:
                with open(os.path.join(dirpath, name), encoding="utf-8") as f:
                    tree = ast.parse(f.read())
            except (SyntaxError, OSError):
                continue
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call) or len(node.args) < 2:
                    continue
                fn = node.func
                called = (fn.attr if isinstance(fn, ast.Attribute)
                          else fn.id if isinstance(fn, ast.Name) else None)
                if called != "t":
                    continue
                key, dflt = node.args[0], node.args[1]
                if (isinstance(key, ast.Constant) and isinstance(key.value, str)
                        and isinstance(dflt, ast.Constant)
                        and isinstance(dflt.value, str)):
                    out.setdefault(key.value, dflt.value)
    return sorted(out.items())


def _content_files():
    """Every (relpath, English text) for the localizable content files under
    chapters/, in a stable walk order."""
    out = []
    for dirpath, dirs, files in os.walk(CHAPTERS_DIR):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__")
        for name in sorted(files):
            if name in LOCALIZED_CONTENT:
                full = os.path.join(dirpath, name)
                rel = os.path.relpath(full, CHAPTERS_DIR).replace(os.sep, "/")
                with open(full, encoding="utf-8") as f:
                    out.append((rel, f.read()))
    return out


def _entries():
    """The ordered (kind, id, English body) of everything translatable."""
    ents = [("meta", "name", NAME_PLACEHOLDER)]
    ents += [("string", k, v) for k, v in _ui_strings()]
    ents += [("file", rel, txt) for rel, txt in _content_files()]
    return ents


# ---- worksheet (de)serialization ------------------------------------------
def _norm(body):
    """A body always ends in exactly one newline, so the next marker sits on its
    own line (and a one-line string round-trips losslessly)."""
    return body if body.endswith("\n") else body + "\n"


def serialize(entries):
    parts = [PREAMBLE]
    for kind, id_, body in entries:
        parts.append("%s%s %s\n%s" % (MARK, kind, id_, _norm(body)))
    return "".join(parts)


def parse(text):
    """[(kind, id, body), ...] -- body is the verbatim text under each marker
    (preamble before the first marker is dropped)."""
    entries, kind_id, buf = [], None, []
    for line in text.splitlines(keepends=True):
        if line.startswith(MARK):
            if kind_id is not None:
                entries.append((kind_id[0], kind_id[1], "".join(buf)))
            head = line[len(MARK):].rstrip("\n")
            kind, _, id_ = head.partition(" ")
            kind_id, buf = (kind, id_), []
        elif kind_id is not None:
            buf.append(line)
    if kind_id is not None:
        entries.append((kind_id[0], kind_id[1], "".join(buf)))
    return entries


# ---- the two commands ------------------------------------------------------
def _worksheet_path(code):
    return os.path.join(LANG_DIR, code + ".worksheet.txt")


def new(code):
    path = _worksheet_path(code)
    if os.path.exists(path):
        print("refusing to overwrite %s (delete it first to regenerate)"
              % os.path.relpath(path, ROOT))
        return 1
    entries = _entries()
    os.makedirs(LANG_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(serialize(entries))
    strings = sum(1 for k, _, _ in entries if k == "string")
    files = sum(1 for k, _, _ in entries if k == "file")
    print("wrote %s" % os.path.relpath(path, ROOT))
    print("  %d UI string(s) + %d content file(s) to translate"
          % (strings, files))
    print("  translate in place, then: python3 tools/lang_worksheet.py apply %s"
          % code)
    return 0


def apply(code):
    path = _worksheet_path(code)
    if not os.path.isfile(path):
        print("no worksheet at %s -- run `new %s` first"
              % (os.path.relpath(path, ROOT), code))
        return 1
    with open(path, encoding="utf-8") as f:
        filled = parse(f.read())
    english = {(k, i): _norm(b) for k, i, b in _entries()}

    name, strings, files, skipped, unknown = NAME_PLACEHOLDER, {}, [], 0, 0
    pack = os.path.join(LANG_DIR, code)
    for kind, id_, body in filled:
        en = english.get((kind, id_))
        if en is None:
            unknown += 1
            continue
        if body == en:                       # untranslated -> fall back to English
            skipped += 1
            continue
        if kind == "meta" and id_ == "name":
            name = body.rstrip("\n")
        elif kind == "string":
            strings[id_] = body.rstrip("\n")
        elif kind == "file":
            dest = os.path.join(pack, "chapters", id_.replace("/", os.sep))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "w", encoding="utf-8") as f:
                f.write(body)
            files.append(id_)

    os.makedirs(pack, exist_ok=True)
    with open(os.path.join(pack, "pack.json"), "w", encoding="utf-8") as f:
        json.dump({"name": name, "code": code}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(pack, "strings.json"), "w", encoding="utf-8") as f:
        json.dump(strings, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("wrote lang/%s/ : pack.json, strings.json (%d key(s)), %d content file(s)"
          % (code, len(strings), len(files)))
    print("  %d entr(y/ies) left English (untranslated)" % skipped)
    if unknown:
        print("  %d entr(y/ies) ignored (no longer in the English source)"
              % unknown)
    if name == NAME_PLACEHOLDER:
        print("  ! set `meta name` in the worksheet to your language's name")
    print("  validate: python3 tools/check_pack.py %s" % code)
    return 0


def main(argv):
    if len(argv) == 2 and argv[0] in ("new", "apply"):
        return (new if argv[0] == "new" else apply)(argv[1])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
