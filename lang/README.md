# Language packs

PyQuest ships in **English**, which is also the fallback: every UI string is
written in English right in the code, so English can never be missing or broken.

A **language pack** is a folder you drop in here — no engine changes — to
translate the interface and the textbook content into another human language.
Translating Python itself is *not* the goal: the grader is language-agnostic,
only the presentation is localized.

## Two ways to start

**Recommended — the one-file worksheet.** Generate a single file with *every*
translatable instance (all UI strings + every puzzle's brief/hints/reference),
English prewritten, then translate in place and split it back into a pack:

```
python3 tools/lang_worksheet.py new <code>     # writes lang/<code>.worksheet.txt
# ... translate the text under each "#@ pyquest:" marker, in place ...
python3 tools/lang_worksheet.py apply <code>   # builds lang/<code>/ from it
python3 tools/check_pack.py <code>             # validate
```

`apply` writes only the entries you actually changed, so a partial translation
stays partial — everything untouched falls back to English. The worksheet is a
loose `lang/<code>.worksheet.txt` file (not a pack folder), so a half-finished
one is invisible to the engine and the checker.

**By hand — the structural template.** Prefer to build the pack folder directly?
Copy [`_template/`](_template/) to `lang/<code>/` and fill it in; its
[README](_template/README.md) walks through the format below. Folder names
starting with `_` (or `.`) are scaffolding: the engine never lists them as a
language and the checker skips them, so the template can live here without
becoming a selectable "language."

## Layout

Either way, a pack ends up as:

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
