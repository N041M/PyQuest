# commands/: the verbs

The verb implementations, split by concern and re‑exported from a facade
`__init__` so `app.py` imports them from one place. Each verb is a plain
function `(puzzles, by_id, prog, ...)`; none of them touch colours directly,
they go through [render/theme](visuals.md). ← [overview](README.md)

```mermaid
flowchart TB
    app["app.py «dispatch»"] --> registry["registry «verb table»"]
    app --> init["commands/__init__ «facade»"]
    init --> views["views «status/map/hint/solution»"]
    init --> nav["navigate «goto/next/skip/retry/revert»"]
    init --> profiles["profiles «theme/mode/user/reset»"]
    init --> transfer["transfer «export/import»"]
    init --> shortcuts["shortcuts «installer»"]
    init --> menu["menu «begin/menu»"]
    init --> help["help"]
    views --> cards["cards «shared card/goto»"]
    nav --> cards
    menu --> cards
    menu --> profiles
    menu --> shortcuts
    help --> registry
```

Each verb also reads `content`/`state` and draws through `render` (the module
diagram below); those edges are left off here to keep the verb topology clear.
`checker.cmd_check` lives in `engine/checker.py` (not this package) because it
owns the toolkit run; everything else verb‑shaped is here.

`app.py` consults `registry` before dispatch: it canonicalizes aliases
(`load`→`goto`), redirects puzzle-context verbs (`check`, `hint`, `next`, …)
to `begin` when no puzzle is loaded, and offers a "did you mean?" suggestion on
an unknown verb. `help` renders its grouped list from the same table.

---

## Module responsibilities

```mermaid
classDiagram
    class registry {
        <<module>>
        +VERBS / CANONICAL / ALIASES / NEEDS_PUZZLE
        +canonical(cmd) / suggest(cmd)
    }
    class cards {
        <<module>>
        +status_marker(prog, pid, current_id)
        +print_current_card(prog, cur, arriving, puzzles)
        +chapter_tree(puzzles, prog, pickable)  "map + goto picker"
        +nav_strip(prog, cur, puzzles)  "registry-driven nav bar"
        -_goto_list(...) / _resolve_goto(arg,...)
        -_jump(target,...) / _advance_one(...,verb)
    }
    class views {
        <<module>>
        +cmd_status / cmd_map
        +cmd_hint / cmd_solution
    }
    class navigate {
        <<module>>
        +cmd_goto / cmd_next / cmd_skip
        +cmd_retry / cmd_revert
    }
    class profiles {
        <<module>>
        +cmd_theme(arg) / cmd_mode(prog, arg)
        +cmd_user(arg, puzzles, by_id, prog)
        +cmd_reset(puzzles, prog, arg)
        -_swatch() / _user_count(...)
    }
    class transfer {
        <<module>>
        +cmd_export(...) / cmd_import(...)
        -_export_dest(...)
        -_sanitize_progress / _sanitize_answers
    }
    class shortcuts {
        <<module>>
        +cmd_setup() / cmd_setup_persist()
        +cmd_uninstall()
        -_install_persistent / _uninstall_persistent
        -_is_persistent / _disclaimer
    }
    class menu {
        <<module>>
        +cmd_begin / cmd_menu
        -_menu_options / _menu_level
        -_menu_theme / _menu_users / _menu_shortcuts
    }
    class help {
        <<module>>
        +cmd_help()
    }
    views ..> cards : status marker + card
    navigate ..> cards : goto/advance helpers
    menu ..> cards
    menu ..> profiles
    menu ..> shortcuts
    cards ..> registry : NAV_CLUSTERS + NEEDS_PUZZLE
```

`cards.py` is the shared core: card rendering, the one chapter-tree renderer
(`chapter_tree`, used by both `map` and the goto picker), the registry-driven
bottom nav strip (`nav_strip`, the consistent footer on every pane), the goto
list, resolving a goto target, jumping, and advancing one puzzle. `views.py`,
`navigate.py`, and `menu.py` all build on it so navigation looks and behaves
identically from the CLI and the menu. `nav_strip` reads `NAV_CLUSTERS` +
`NEEDS_PUZZLE` from `registry`, so the strip can never list a verb dispatch
wouldn't accept.

## The only interactive surface: `begin` / `menu`

Every other verb is one‑shot. `cmd_begin`/`cmd_menu` are the lone read‑loop, and
they still delegate the real work to the same one‑shot verbs.

```mermaid
stateDiagram-v2
    [*] --> Menu : begin / menu
    Menu --> Level : pick level (easy/normal/hard)
    Menu --> Theme : pick a colour theme
    Menu --> Users : switch / create profile
    Menu --> Shortcuts : install pq shortcuts
    Menu --> Play : start / resume a puzzle
    Level --> Menu
    Theme --> Menu
    Users --> Menu
    Shortcuts --> Menu
    Play --> [*] : drops back to the one-shot loop
    Menu --> [*] : quit
```

## Difficulty modes gate navigation

`cmd_mode` sets `prog["mode"]`; the navigation helpers in `cards.py` read it to
decide whether `next`/`skip`/`goto` may move past an unsolved puzzle.

```mermaid
flowchart LR
    easy["easy, free roam"]
    normal["normal, forward only to unlocked"]
    hard["hard, must solve to advance"]
    easy -.-> normal -.-> hard
```

(See README's command table for the exact per‑mode rules.)
