# Language pack scaffolding

Everything here is a starting point, never loaded by the engine: the leading
underscore marks this folder as scaffolding, so PyQuest skips it when listing
languages and `tools/check_pack.py` skips it when checking packs.

Two ways to start a translation:

## example.translations/ — the worksheet format (recommended path)

A complete worksheet exactly as `tools/lang_worksheet.py new <code>` generates
it: one Python data file per chapter plus `00_meta.py` for the pack name and
every UI string, each value prefilled with its English. In this example the
name, three menu strings, and `1.1 hints` are translated (to Czech) to show
what an edited value looks like; everything else is left as the English.

Don't copy this folder — generate your own live one instead, which the tool
can refresh as PyQuest gains strings:

```
python3 tools/lang_worksheet.py new <code>       # writes lang/<code>.translations/
python3 tools/lang_worksheet.py apply <code>     # builds lang/<code>/ from it
python3 tools/lang_worksheet.py update <code>    # refresh after PyQuest updates
```

(This example is a frozen snapshot; it was last refreshed with `update` before
moving here, and `update example` no longer reaches it. Regenerate with `new`
for a current worksheet.)

## pack/ — the pack layout, for hand-building

The exact shape of a shipped pack (`lang/cs/`, `lang/pt/`), empty and ready to
copy:

```
cp -r lang/_template/pack lang/<code>
```

`<code>` is a short language code (`de`, `fr`, ...). Then fill in the files:

### pack.json (required)

The pack's identity. `name` is the language's own name for itself, shown in
the language menu; `code` must match the folder name:

```json
{
  "name": "Deutsch",
  "code": "de"
}
```

Until both are filled the pack fails validation and PyQuest stays on English —
it is never left in a broken language.

### strings.json (required, may stay partial)

A flat map of UI string keys to translations. Any key you leave out falls back
to its English default, so `{}` is already a valid (all-English) pack:

```json
{
  "menu.play": "spielen",
  "stats.streak.one": "%d Tag",
  "stats.streak.other": "%d Tage"
}
```

The full key list with English text is `00_meta.py` in the example worksheet
above. Counted strings take one entry per CLDR plural category your language
uses (`.one` / `.few` / `.other`); keep every `%s`/`%d` from the English text,
in the same order. If your language declines counts differently from English
or Czech, add its one-line rule to `_PLURAL_RULES` in `engine/i18n.py`.

A translation that comes out identical to the English (loanwords like
"%d puzzles" in Portuguese) can simply be left out — the fallback already
serves that exact text.

### chapters/ (optional)

Translated content, one file at a time, mirroring the course tree:

```
chapters/02_strings/01_indexing/reference.md          <- English (shipped)
lang/<code>/chapters/02_strings/01_indexing/reference.md  <- your override
```

Only `brief.md`, `hints.md`, and `reference.md` are served this way; any file
you don't supply stays English. Keep each file's markdown and ``` code blocks
intact — only the prose is localized.

## Before shipping

```
python3 tools/check_pack.py <code>
```

Save every file as UTF-8.
