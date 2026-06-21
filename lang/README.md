# Language packs

PyQuest ships in **English**, which is also the fallback: every UI string is
written in English right in the code, so English can never be missing or broken.

A **language pack** is a folder you drop in here — no engine changes — to
translate the interface and the textbook content into another human language.
Translating Python itself is *not* the goal: the grader is language-agnostic,
only the presentation is localized.

## Start with the one-file worksheet

Generate a single Python data file listing *every* translatable piece (the pack
name, all UI strings, and every puzzle's brief/hints/reference) as one
`TRANSLATIONS` dict, each value prefilled with its English — then edit the values
and split it into a pack:

```
python3 tools/lang_worksheet.py new <code>     # writes lang/<code>.translations.py
# ... change each value to your language (leave it to keep English) ...
python3 tools/lang_worksheet.py apply <code>   # builds lang/<code>/ from it
python3 tools/check_pack.py <code>             # validate
```

Each piece is one dict entry, keyed by what it is. Multi-line content is a raw
triple-quoted string, so markdown and backslashes (regex `\d`, ...) survive as
typed:

```python
TRANSLATIONS = {
    "ui menu.play": "hrát",
    "1.1 hints": r"""Která vestavěná funkce vypíše text na obrazovku? ...
""",
}
```

`apply` writes only the values you changed, so a partial translation stays
partial — every unchanged value falls back to English. Keep each value's markdown
and ``` code blocks exactly; only the prose is localized (literals the grader
checks stay as-is). The file is **pure data** — read with `ast.literal_eval`,
never executed — and lives as a loose `lang/<code>.translations.py` (not a pack
folder), so a half-finished one is invisible to the engine and the checker.

See [`example.translations.py`](example.translations.py) — a complete file with a
few values translated to Czech (the name, the UI strings, and `1.1 hints`) to show
the format.

(`apply` produces the pack files below; you can also hand-build them.)

## Layout

A pack is:

```
lang/<code>/
  pack.json       required:  {"name": "Čeština", "code": "<code>"}
  strings.json    required:  {"<key>": "<translation>", ...}   (may be partial)
  chapters/...    optional:  translated content files, mirroring chapters/
```

`<code>` is a short language code (e.g. `cs`, `de`, `fr`) and must match the
folder name. Save every file as **UTF-8**.

## How it loads

- Pick a language in **settings → language** (or `language <code>`). The choice
  persists in `settings.json`.
- On select (and at startup) the pack is **validated**. If it can't load —
  no `pack.json`, invalid JSON, a missing `name`, a code that doesn't match the
  folder — PyQuest prints exactly what's wrong and **stays on English**. It is
  never left in a broken language.
- `strings.json` may be **partial**: any key it omits falls back to the English
  default. So a pack that translates only the menu still works; untranslated
  strings simply stay English.

## strings.json

A flat map of string keys to translations. Keys are added to the engine as
strings are routed through the translator; an up-to-date list of keys (with
their English text) is the set of `t("...", "English")` calls in `engine/`.
Translate the ones you want; leave the rest out.

```json
{
  "menu.play":  "hrát",
  "menu.learn": "učit se"
}
```

## chapters/ — translating the content

Each topic folder under `chapters/` holds learner-facing content files:
`brief.md` (the task), `hints.md`, and `reference.md` (the textbook entry). To
translate any of them, mirror the file's path under your pack's `chapters/`:

```
chapters/02_strings/01_indexing/reference.md          <- English (shipped)
lang/cs/chapters/02_strings/01_indexing/reference.md  <- Czech override
```

When that language is active, the override is served in place of the English
file; any file you don't translate keeps its English original. Like
`strings.json`, this is **per-file partial** — translate the files you want and
leave the rest. Only files inside `chapters/` are ever redirected this way.

A mistyped folder or filename simply isn't found — the engine looks for the real
path, doesn't see your file, and shows English with no error. Run the checker to
catch that before you ship:

```
python3 tools/check_pack.py <code>     # or with no code: check every pack
```

It validates `pack.json` / `strings.json` and flags any content override that
mirrors no real puzzle file (a path typo) or isn't a translatable file.

Nothing here is translated yet — this is the plumbing. Contributions welcome.
