"""Per-chapter translation worksheet -- a folder of plain Python data files you
edit, then split into the pack the engine loads.

    python3 tools/lang_worksheet.py new <code>     write lang/<code>.translations/:
                                                   one file per chapter (plus
                                                   00_meta.py for the pack name and
                                                   UI strings), each a
                                                   TRANSLATIONS = {...} dict with
                                                   one entry per translatable piece
                                                   (every puzzle's brief/hints/
                                                   reference), prefilled with English
    python3 tools/lang_worksheet.py apply <code>   merge the folder's files and
                                                   split them into lang/<code>/
                                                   (pack.json, strings.json,
                                                   chapters/...)
    python3 tools/lang_worksheet.py split <code>   convert an old single-file
                                                   lang/<code>.translations.py into
                                                   the per-chapter folder

You edit small dicts -- one file per chapter -- changing each value to your
language, or leaving it as the English to keep English. Multi-line content is a
readable raw triple-quoted string (`r\"\"\"...\"\"\"`), so markdown and backslashes
(regex `\\d`, ...) survive as-is.

    # lang/<code>.translations/01_basics.py
    TRANSLATIONS = {
        "1.1 hints": r\"\"\"Která vestavěná funkce vypíše text na obrazovku? ...
    \"\"\",
    }

`apply` writes only the values you changed, so a partial translation stays partial
(every unchanged value, and any chapter file you don't supply, falls back to
English). The files are read with ast.literal_eval -- pure data, never executed --
and live as a loose `lang/<code>.translations/` folder, which the engine and the
pack checker ignore (they only look at pack directories), so a half-finished one is
never a broken language. (`apply` also still reads a single legacy
`lang/<code>.translations.py` if no folder is present.)
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

META_STEM = "00_meta"   # the file holding the pack name + UI strings


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


# ---- grouping into per-chapter files --------------------------------------
def _chapter_dirs():
    """pid -> its chapter's top-level directory basename, e.g. '1.1' ->
    '01_basics'. The worksheet files are named after these, parallel to the
    pack's chapters/."""
    out = {}
    for pid, d in _puzzles():
        rel = os.path.relpath(d, CHAPTERS_DIR).replace(os.sep, "/")
        out[pid] = rel.split("/")[0]
    return out


def _group(entries):
    """Ordered {stem: [(label, value), ...]}: '00_meta' for name/ui, the chapter
    directory basename for each puzzle piece. Entry order is preserved within a
    file; stems come out sorted (00_meta first, then chapters in order)."""
    chap = _chapter_dirs()
    groups = {}
    for label, val in entries:
        if label == "name" or label.startswith("ui "):
            stem = META_STEM
        else:
            stem = chap.get(label.split(None, 1)[0], META_STEM)
        groups.setdefault(stem, []).append((label, val))
    return {k: groups[k] for k in sorted(groups)}


# ---- the Python data files (write / read) ---------------------------------
def _pyval(s):
    """A source literal for `s`: a plain string for a simple one-liner, a raw
    triple-quoted string for multi-line / backslashed prose (readable, and
    backslashes survive), or repr() for the rare value containing \"\"\"."""
    if "\n" not in s and '"' not in s and "\\" not in s:
        return '"%s"' % s
    if '"""' not in s:
        return 'r"""%s"""' % (s if s.endswith("\n") else s + "\n")
    return repr(s)


def _header(code, stem):
    """The comment block atop each worksheet file."""
    what = ("pack name + UI strings" if stem == META_STEM else
            "chapter %s -- each puzzle's brief / hints / reference" % stem)
    return (
        "# PyQuest translations -- language '%s' -- %s.\n"
        "# Edit each value to your language; leave it as the English to keep\n"
        "# English. Keep each value's markdown and ``` code blocks exactly -- only\n"
        "# the prose is localized (literals the grader checks, like\n"
        '#   print("Hello, output"), stay as they are).\n'
        "# Pure data: read with ast.literal_eval, never executed. This folder is\n"
        "# one file per chapter; after editing any of them run:\n"
        "#     python3 tools/lang_worksheet.py apply %s\n\n" % (code, what, code))


def serialize(entries, header=""):
    out = [header, "TRANSLATIONS = {\n"]
    for label, en in entries:
        out.append('\n"%s": %s,\n' % (label, _pyval(en)))
    out.append("}\n")
    return "".join(out)


def parse(text):
    """The TRANSLATIONS dict from a file's source -- read as data, never run.
    Raises SyntaxError (bad edit) or ValueError (no dict)."""
    tree = ast.parse(text)
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == "TRANSLATIONS"):
            return ast.literal_eval(node.value)
    raise ValueError("no TRANSLATIONS = {...} assignment found")


def _norm(body):
    return body if body.endswith("\n") else body + "\n"


def _dir(code):
    return os.path.join(LANG_DIR, code + ".translations")


def _file(code):
    return os.path.join(LANG_DIR, code + ".translations.py")   # legacy single file


def _write_split(code, entries):
    """Write the per-chapter folder for `entries`. Returns the {stem: [...]} map."""
    d = _dir(code)
    os.makedirs(d, exist_ok=True)
    groups = _group(entries)
    for stem, ents in groups.items():
        with open(os.path.join(d, stem + ".py"), "w", encoding="utf-8") as f:
            f.write(serialize(ents, _header(code, stem)))
    return groups


def _load(code):
    """The merged TRANSLATIONS dict for `code`. Prefers the per-chapter folder
    lang/<code>.translations/ (every file's TRANSLATIONS merged, duplicate keys
    rejected); falls back to a legacy single lang/<code>.translations.py. Raises
    ValueError with a human message on any problem."""
    d = _dir(code)
    if os.path.isdir(d):
        merged = {}
        for fn in sorted(os.listdir(d)):
            fp = os.path.join(d, fn)
            if not (fn.endswith(".py") and os.path.isfile(fp)):
                continue
            with open(fp, encoding="utf-8") as f:
                try:
                    part = parse(f.read())
                except SyntaxError as e:
                    raise ValueError("%s: %s" % (os.path.relpath(fp, ROOT), e))
            if not isinstance(part, dict):
                raise ValueError("%s: TRANSLATIONS is not a dict"
                                 % os.path.relpath(fp, ROOT))
            dup = sorted(set(part) & set(merged))
            if dup:
                raise ValueError("%s: key(s) already defined in another file: %s"
                                 % (os.path.relpath(fp, ROOT), ", ".join(dup)))
            merged.update(part)
        return merged
    single = _file(code)
    if os.path.isfile(single):
        with open(single, encoding="utf-8") as f:
            data = parse(f.read())
        if not isinstance(data, dict):
            raise ValueError("%s: TRANSLATIONS is not a dict"
                             % os.path.relpath(single, ROOT))
        return data
    raise ValueError("no lang/%s.translations/ folder (or legacy "
                     "lang/%s.translations.py) -- run `new %s` first"
                     % (code, code, code))


# ---- the commands ----------------------------------------------------------
def _report_written(code, groups):
    chapters = len(groups) - (1 if META_STEM in groups else 0)
    print("wrote lang/%s.translations/ : %d file(s) (%s + %d chapter file(s))"
          % (code, len(groups), META_STEM, chapters))


def new(code):
    for existing in (_dir(code), _file(code)):
        if os.path.exists(existing):
            print("refusing to overwrite %s (delete it first to regenerate)"
                  % os.path.relpath(existing, ROOT))
            return 1
    entries = _entries()
    os.makedirs(LANG_DIR, exist_ok=True)
    groups = _write_split(code, entries)
    ui = sum(1 for label, _ in entries if label.startswith("ui "))
    content = sum(1 for label, _ in entries
                  if not label.startswith(("ui ", "name")))
    _report_written(code, groups)
    print("  %d UI string(s) + %d content piece(s); edit the values, then:"
          % (ui, content))
    print("  python3 tools/lang_worksheet.py apply %s" % code)
    return 0


def split(code):
    """Convert a legacy single lang/<code>.translations.py into the folder form."""
    single = _file(code)
    if not os.path.isfile(single):
        print("no lang/%s.translations.py to split" % code)
        return 1
    if os.path.isdir(_dir(code)):
        print("lang/%s.translations/ already exists (delete it first)" % code)
        return 1
    try:
        with open(single, encoding="utf-8") as f:
            data = parse(f.read())
    except (SyntaxError, ValueError) as e:
        print("couldn't read %s: %s" % (os.path.relpath(single, ROOT), e))
        return 1
    canonical = _entries()                       # canonical label order
    entries = [(label, data[label]) for label, _ in canonical if label in data]
    extra = sorted(set(data) - {label for label, _ in canonical})
    groups = _write_split(code, entries)
    os.remove(single)
    _report_written(code, groups)
    print("  removed %s" % os.path.relpath(single, ROOT))
    if extra:
        print("  ! dropped %d key(s) that name nothing in the source: %s"
              % (len(extra), ", ".join(extra)))
    return 0


def apply(code):
    try:
        data = _load(code)
    except (SyntaxError, ValueError) as e:
        print("couldn't read translations for '%s': %s" % (code, e))
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
    cmds = {"new": new, "apply": apply, "split": split}
    if len(argv) == 2 and argv[0] in cmds:
        return cmds[argv[0]](argv[1])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
