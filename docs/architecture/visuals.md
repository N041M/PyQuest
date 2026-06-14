# Visuals — theme & render

The isolated presentation layer. **All** colour codes, glyphs and box‑drawing
characters live here and nowhere else — a restyle touches only these two files.
`render` consumes `theme`; the rest of the engine consumes `render` (and
`theme.paint`). ← [overview](README.md)

```mermaid
flowchart TB
    cmds["commands/* · checker.py"] --> render
    render["render.py — primitives"] --> theme
    theme["theme.py — palette · glyphs · paint()"] --> config["config.WIDTH"]
    theme --> themesdir[("themes/*.json presets")]
```

---

## theme.py — palette, glyphs, paint

The visual identity: ANSI capability detection, the named palettes, the
deliberate glyph set, and `paint()` (the single colouriser). The glyph set
`✓ ✗ ▸ · → ✦` is the **only** place such characters are allowed.

```mermaid
classDiagram
    class theme {
        <<module>>
        +COLOR  "terminal supports ANSI?"
        +THEMES / THEME_NAMES
        +ANSI  "reset/bold/dim"
        +OK ✓  NO ✗  CUR ▸  DOT ·  ARROW →  STAR ✦
        +LOGO / LOGO_RAMP / DIGITS
        +load_presets() dict  "themes/*.json"
        +apply_theme(name)
        +id_art(text)  "big puzzle-id digits"
        +paint(text, *roles) str
        +paint_code(text, code, bold)
    }
    theme ..> config : WIDTH
    note for theme "_supports_color() gates every escape;\nwith COLOR False, paint() returns plain text,\nso output stays correct when piped/redirected."
```

## render.py — drawing primitives

Pure layout built from `theme` parts: boxes, banners, the progress bar, wrapped
text, fields. Stateless; takes data, returns strings. Re‑exports `paint`/`STAR`
so callers import one module.

```mermaid
classDiagram
    class render {
        <<module>>
        +PAD
        +cli(verb) / label(text) / rule(color, width)
        +deco_border(left, right, inner, orn)
        +box(title, color, tall) / banner(title, color)
        +bigbox(art_lines, border, ramp) / wordmark(color)
        +id_banner(pid, color) / header(title, color)
        +wrap(text, width) / field(label, value, lblcolor)
        +bar(done, total, width) / indent(text, prefix)
        +quote_block(value)
        +re-exports: paint, paint_code, STAR, ...
    }
    render ..> theme : paint / glyphs / LOGO
    render ..> config : WIDTH
```

## The rule the audit‑of‑intent protects

```mermaid
flowchart LR
    subgraph allowed["allowed to emit ANSI / glyphs / box chars"]
        theme2["theme.py"]
        render2["render.py"]
    end
    subgraph forbidden["everything else — content/state/logic"]
        x["app · commands · checker · toolkit · content · state · config"]
    end
    x -->|"calls paint()/box()/bar()"| allowed
    forbidden -. "must NOT contain raw \\033[ or box chars" .-> allowed
```

Because presentation is quarantined, a theme change is data (`themes/*.json` +
`THEMES`) and a re‑style is local: the learning logic never moves.
