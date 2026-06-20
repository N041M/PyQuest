# Language packs

PyQuest ships in **English**, which is also the fallback: every UI string is
written in English right in the code, so English can never be missing or broken.

A **language pack** is a folder you drop in here — no engine changes — to
translate the interface (and, later, the puzzle content) into another human
language. Translating Python itself is *not* the goal: the grader is
language-agnostic, only the presentation is localized.

## Layout

```
lang/<code>/
  pack.json       required:  {"name": "Čeština", "code": "<code>"}
  strings.json    required:  {"<key>": "<translation>", ...}   (may be partial)
  chapters/...    optional:  translated brief.md / hints.md, mirroring chapters/
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

Nothing here is translated yet — this is the plumbing. Contributions welcome.
