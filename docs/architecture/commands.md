# commands/: the verbs

The verb implementations, split by concern and re‑exported from a facade
`__init__` so `app.py` imports them from one place. Each verb is a plain
function `(puzzles, by_id, prog, ...)`; none of them touch colours directly,
they go through [render/theme](visuals.md). ← [overview](README.md)

```mermaid
flowchart TB
    app["app.py «dispatch»"] --> registry["registry «verb table»"]
    app --> init["commands/__init__ «facade»"]
    init --> views["views «status/map/stats/hint/solution/textbook»"]
    init --> nav["navigate «goto/next/skip/retry/restart»"]
    init --> profiles["profiles «theme/mode/user/wipe»"]
    init --> transfer["transfer «export/import»"]
    init --> shortcuts["shortcuts «installer»"]
    init --> menu["menu «menu»"]
    init --> help["help"]
    views --> cards["cards «shared card/goto»"]
    nav --> cards
    menu --> cards
    menu --> profiles
    menu --> shortcuts
    menu --> views
    menu --> help
    menu --> registry
    help --> registry
```

The hub runs the read‑only inspection verbs (`help`/`status`/`map`/`stats`) and `mode`
in place, hence `menu → views`/`help`; the puzzle‑solving verbs still route the
learner to "pick 1 to start".

Each verb also reads `content`/`state` and draws through `render` (the module
diagram below); those edges are left off here to keep the verb topology clear.
`checker.cmd_check` lives in `engine/checker.py` (not this package) because it
owns the toolkit run; everything else verb‑shaped is here.

`app.py` consults `registry` before dispatch: it canonicalizes aliases
(`load`→`goto`, `back`→`menu`), opens the menu (`menu`) when a puzzle-context
verb (`check`, `hint`, `next`, …) is run with no puzzle loaded, and offers a
"did you mean?" suggestion on an unknown verb. A bare invocation also defaults
to the menu, so every entry point lands on the same home base. `help` renders its grouped list from the same table, taking
`prog` so it can highlight the set that is live in the current space (the puzzle
verbs are bright ▸ while solving, dimmed · otherwise).

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
        +cmd_status / cmd_map / cmd_stats / cmd_search
        +cmd_hint / cmd_solution
        +cmd_textbook(...,arg)  "writes textbook.md: reached vs full"
    }
    class navigate {
        <<module>>
        +cmd_goto / cmd_next / cmd_skip / cmd_resume
        +cmd_note / cmd_retry / cmd_restart
    }
    class profiles {
        <<module>>
        +cmd_theme(arg) / cmd_mode(prog, arg)
        +cmd_user(arg,...)  "switch/create · delete · rename"
        +cmd_wipe(puzzles, prog, arg)  "needs `wipe profile` to fire"
        -_swatch() / _user_count(...)
        -_user_delete(...) / _user_rename(...)
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
        +cmd_menu
        -_menu_options / _menu_level
        -_menu_theme / _menu_users / _menu_shortcuts
    }
    class help {
        <<module>>
        +cmd_help(prog)  "context-highlighted reference"
    }
    views ..> cards : status marker + card
    navigate ..> cards : goto/advance helpers
    menu ..> cards
    menu ..> profiles
    menu ..> shortcuts
    menu ..> views : numbered textbook/stats/map + status/help inline
    menu ..> help
    menu ..> registry : canonical · gate
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

## The only interactive surface: `menu`

Every other verb is one‑shot. `cmd_menu` is the lone read‑loop, and
they still delegate the real work to the same one‑shot verbs.

```mermaid
stateDiagram-v2
    [*] --> Menu : menu
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
decide whether `skip`/`goto` may move past an unsolved puzzle (`next` requires a solve).

```mermaid
flowchart LR
    easy["easy, free roam"]
    normal["normal, forward only to unlocked"]
    hard["hard, must solve to advance"]
    easy -.-> normal -.-> hard
```

(See README's command table for the exact per‑mode rules.)
