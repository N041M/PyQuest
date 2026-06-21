"""One-file translation worksheet -- a plain Python data file you edit, then
split into the pack the engine loads.

    python3 tools/lang_worksheet.py new <code>     write lang/<code>.translations.py:
                                                   a TRANSLATIONS = {...} dict with
                                                   one entry per translatable piece
                                                   (the pack name, every UI string,
                                                   every puzzle's brief/hints/
                                                   reference), each value prefilled
                                                   with its English
    python3 tools/lang_worksheet.py apply <code>   split a filled file into
                                                   lang/<code>/ (pack.json,
                                                   strings.json, chapters/...)

You edit one dict: change each value to your language, leave it as the English to
keep English. Multi-line content is a readable raw triple-quoted string
(`r\"\"\"...\"\"\"`), so markdown and backslashes (regex `\\d`, ...) survive as-is.

    TRANSLATIONS = {
        "ui menu.play": "hrát",
        "1.1 hints": r\"\"\"Která vestavěná funkce vypíše text na obrazovku? ...
    \"\"\",
    }

`apply` writes only the values you changed, so a partial translation stays partial
(every unchanged value falls back to English). The file is read with
ast.literal_eval -- pure data, never executed -- and lives as a loose
`lang/<code>.translations.py`, which the engine and the pack checker ignore (they
only look at pack directories), so a half-finished one is never a broken language.
"""

import ast
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINE_DIR = os.path.join(ROOT, "engine")
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
LANG_DIR = os.path.join(ROOT, "lang")

# The content files the engine localizes, as (piece-label, filename).
PIECES = (("brief", "brief.md"), ("hints", "hints.md"),
          ("reference", "reference.md"))

NAME_PLACEHOLDER = "<your language's own name, e.g. Čeština>"

PREAMBLE = '''\
# PyQuest translations. Edit the TRANSLATIONS dict below: change each value to
# your language; leave it unchanged to keep English (apply writes only what you
# changed). Keep each value's markdown and ``` code blocks exactly -- only the
# prose is localized, the grader is language-agnostic (literals it checks, like
# print("Hello, output"), stay as they are).
#
#   "name"          your language's display name
#   "ui <key>"      a UI string
#   "<id> <piece>"  a puzzle's brief / hints / reference (e.g. "1.1 hints")
#
# This file is pure data -- it is read with ast.literal_eval, never executed.
# Multi-line values are raw triple-quoted strings (r\"\"\"...\"\"\"). Then:
#
#     python3 tools/lang_worksheet.py apply <code>

'''


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


def _puzzles():
    """[(id, dir), ...] from every chapters/NN_x/MM_y/meta.json, ordered by id."""
    out = []
    for ch in sorted(os.listdir(CHAPTERS_DIR)):
        chd = os.path.join(CHAPTERS_DIR, ch)
        if not os.path.isdir(chd) or ch.startswith(("_", ".")):
            continue
        for pz in sorted(os.listdir(chd)):
            meta = os.path.join(chd, pz, "meta.json")
            if not os.path.isfile(meta):
                continue
            try:
                with open(meta, encoding="utf-8") as f:
                    pid = json.load(f).get("id")
            except (ValueError, OSError):
                continue
            if pid:
                out.append((pid, os.path.join(chd, pz)))
    out.sort(key=lambda t: [int(n) for n in t[0].split(".")])
    return out


def _entries():
    """The ordered (label, English) of every translatable piece. The label is the
    dict key and what `apply` resolves to a destination: `name`, `ui <key>`, or
    `<id> <piece>`."""
    ents = [("name", NAME_PLACEHOLDER)]
    ents += [("ui %s" % k, v) for k, v in _ui_strings()]
    for pid, d in _puzzles():
        for piece, fname in PIECES:
            fp = os.path.join(d, fname)
            if os.path.isfile(fp):
                with open(fp, encoding="utf-8") as f:
                    ents.append(("%s %s" % (pid, piece), f.read()))
    return ents


def _resolve(label, idmap):
    """A label -> where its translation belongs: ("name", None),
    ("string", key), or ("file", relpath). None if it names nothing real."""
    if label == "name":
        return ("name", None)
    parts = label.split(None, 1)
    if len(parts) == 2 and parts[0] == "ui":
        return ("string", parts[1])
    if len(parts) == 2:
        pid, piece = parts[0], parts[1]
        fname = dict(PIECES).get(piece)
        if pid in idmap and fname:
            rel = os.path.relpath(idmap[pid], CHAPTERS_DIR).replace(os.sep, "/")
            return ("file", rel + "/" + fname)
    return None


# ---- the Python data file (write / read) ----------------------------------
def _pyval(s):
    """A source literal for `s`: a plain string for a simple one-liner, a raw
    triple-quoted string for multi-line / backslashed prose (readable, and
    backslashes survive), or repr() for the rare value containing \"\"\"."""
    if "\n" not in s and '"' not in s and "\\" not in s:
        return '"%s"' % s
    if '"""' not in s:
        return 'r"""%s"""' % (s if s.endswith("\n") else s + "\n")
    return repr(s)


def serialize(entries):
    out = [PREAMBLE, "TRANSLATIONS = {\n"]
    for label, en in entries:
        out.append('\n"%s": %s,\n' % (label, _pyval(en)))
    out.append("}\n")
    return "".join(out)


def parse(text):
    """The TRANSLATIONS dict from the file's source -- read as data, never run.
    Raises SyntaxError (bad edit) or ValueError (no dict)."""
    tree = ast.parse(text)
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == "TRANSLATIONS"):
            return ast.literal_eval(node.value)
    raise ValueError("no TRANSLATIONS = {...} assignment found")


# ---- the two commands ------------------------------------------------------
def _path(code):
    return os.path.join(LANG_DIR, code + ".translations.py")


def _norm(body):
    return body if body.endswith("\n") else body + "\n"


def new(code):
    path = _path(code)
    if os.path.exists(path):
        print("refusing to overwrite %s (delete it first to regenerate)"
              % os.path.relpath(path, ROOT))
        return 1
    entries = _entries()
    os.makedirs(LANG_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(serialize(entries))
    ui = sum(1 for label, _ in entries if label.startswith("ui "))
    content = sum(1 for label, _ in entries
                  if not label.startswith(("ui ", "name")))
    print("wrote %s" % os.path.relpath(path, ROOT))
    print("  %d UI string(s) + %d content piece(s); edit the values, then:"
          % (ui, content))
    print("  python3 tools/lang_worksheet.py apply %s" % code)
    return 0


def apply(code):
    path = _path(code)
    if not os.path.isfile(path):
        print("no file at %s -- run `new %s` first"
              % (os.path.relpath(path, ROOT), code))
        return 1
    try:
        with open(path, encoding="utf-8") as f:
            data = parse(f.read())
    except (SyntaxError, ValueError) as e:
        print("couldn't read %s: %s" % (os.path.relpath(path, ROOT), e))
        return 1
    if not isinstance(data, dict):
        print("TRANSLATIONS is not a dict")
        return 1

    english = dict(_entries())
    idmap = {pid: d for pid, d in _puzzles()}
    pack = os.path.join(LANG_DIR, code)
    name, strings, files, blank, unknown = code, {}, [], 0, 0
    for label, en in english.items():
        val = data.get(label)
        if val is None or val == en:             # untouched -> falls back
            blank += 1
            continue
        dest = _resolve(label, idmap)
        if dest is None:
            unknown += 1
            continue
        if dest[0] == "name":
            name = val.strip()
        elif dest[0] == "string":
            strings[dest[1]] = val.strip()
        else:                                    # ("file", relpath)
            out = os.path.join(pack, "chapters", dest[1].replace("/", os.sep))
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, "w", encoding="utf-8") as f:
                f.write(_norm(val))
            files.append(dest[1])

    os.makedirs(pack, exist_ok=True)
    with open(os.path.join(pack, "pack.json"), "w", encoding="utf-8") as f:
        json.dump({"name": name, "code": code}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(pack, "strings.json"), "w", encoding="utf-8") as f:
        json.dump(strings, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("wrote lang/%s/ : pack.json, strings.json (%d key(s)), %d content file(s)"
          % (code, len(strings), len(files)))
    print("  %d value(s) left as English (unchanged)" % blank)
    if unknown:
        print("  %d key(s) ignored (name nothing in the source)" % unknown)
    if name == code:
        print("  ! set the \"name\" value to your language's name")
    print("  validate: python3 tools/check_pack.py %s" % code)
    return 0


def main(argv):
    if len(argv) == 2 and argv[0] in ("new", "apply"):
        return (new if argv[0] == "new" else apply)(argv[1])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
