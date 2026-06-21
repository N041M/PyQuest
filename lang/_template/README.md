# Language pack template

Copy this folder to start a translation. It is **scaffolding, not a pack**:
because its name starts with `_`, the engine never lists it as a selectable
language and `tools/check_pack.py` skips it (you can still check it explicitly:
`python3 tools/check_pack.py _template`).

## Make your pack

1. **Copy** `lang/_template/` to `lang/<code>/`, where `<code>` is your
   language's short code (`cs`, `de`, `fr`, ...). The folder name *is* the code.
2. **`pack.json`** — set `"name"` to your language's own name (e.g. `"Čeština"`)
   and `"code"` to match the folder. Save as UTF-8.
3. **`strings.json`** — translate the values (keep the keys). It may be
   **partial**: any key you leave out falls back to English. The keys here are
   the UI strings wired up today; the full, current list is the
   `t("key", "English")` calls in `engine/` — translate the ones you want.
4. **`chapters/`** *(optional)* — translate learner content by mirroring a
   puzzle file's path under your pack. Only `brief.md`, `hints.md`, and
   `reference.md` are localizable. See the example at
   `chapters/01_basics/01_hello/brief.md`; delete it if you don't want it.
   A path that doesn't mirror a real puzzle file is silently ignored — run the
   checker to catch typos.
5. **Validate**: `python3 tools/check_pack.py <code>`. It checks `pack.json` /
   `strings.json` and every content override. Fix anything it flags.
6. **Try it**: settings -> language (or `language <code>`). On any load error
   PyQuest names the problem and stays on English.

Delete this README from your copy. More detail: [`../README.md`](../README.md).
