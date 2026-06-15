# Engine core

The orchestration, content, input and state layers. Visuals are in
[visuals.md](visuals.md); the tester in [toolkit.md](toolkit.md); the verbs in
[commands.md](commands.md). ← [overview](README.md)

```mermaid
flowchart TB
    play["start.py «entry»"] --> session["session.py «launcher»"]
    play --> app["app.py «dispatch»"]
    app --> checker["checker.py"]
    app --> commands["commands/*"]
    checker --> toolkit["toolkit/"]
    checker --> content["content.py"]
    checker --> state["state.py"]
    checker --> render["render · theme"]
    content --> config["config.py"]
    state --> config
    toolkit --> config
    tests["tests.py «authoring»"] -. imports .-> inputs["inputs.py"]
    classDef seam fill:#efe,stroke:#575,stroke-dasharray:3 3;
    class tests,inputs seam;
```

> `inputs.py` is consumed by each puzzle's `tests.py` (loaded via
> `content.load_tests`), **not** by `toolkit` or `content` themselves: it is
> the authoring seam, not an engine dependency.

---

## start.py / app.py: entry & dispatch

`start.py` is a thin root entry point that only routes (version check, then
launch-or-dispatch). A cold bare run delegates to `engine.session`, which hosts
a session shell with the shortcuts loaded and opens the menu (the one place
that spawns a shell); given a verb it calls `engine.app.main()`. `app.main()`
is the **only** place argv becomes an action:
it builds the puzzle list once, loads progress, guarantees `work.py` exists,
then routes the verb to exactly one command function. Before routing it
consults `commands/registry`: canonicalize the verb (fold aliases), gate
puzzle-context verbs (`check`, `hint`, `next`, … redirect to `begin` when no
puzzle is loaded), and on an unknown verb suggest the closest match. Adding a
verb = one `elif` here + one function in `commands/` + one registry row.

The two ways in -- a cold bare launch versus running a verb -- and how a
session folds back into dispatch:

```mermaid
flowchart TB
    s["python3 start.py"] --> q{"a verb, or<br/>PYQUEST_SHELL set?"}
    q -- "no: cold + bare" --> sess["engine.session.launch_session()"]
    sess --> sh["detect shell · load shortcuts<br/>(throwaway rc) · spawn it · export PYQUEST_SHELL"]
    sh --> beg["start.py begin  (inside the session)"]
    q -- "yes" --> app["engine.app.main()"]
    beg --> app
    app --> reg["registry: canonical · gate · suggest"]
    reg --> h["one command handler"]
```

```mermaid
classDiagram
    class app {
        <<module>>
        +main()
    }
    app ..> registry : canonical · gate · suggest
    app ..> content : discover()
    app ..> state : load · current · ensure_workspace
    app ..> checker : cmd_check
    app ..> commands : cmd_*
```

`main()` maps each verb to one function:

| verb(s) | → function |
|---|---|
| status · current · progress | `cmd_status` |
| check · hint · solution · map | `cmd_check` · `cmd_hint` · `cmd_solution` · `cmd_map` |
| next · skip · retry · revert · goto | the navigation verbs (`navigate.py`) |
| theme · mode · user · reset | `cmd_theme` · `cmd_mode` · `cmd_user` · `cmd_reset` |
| export · import | `cmd_export` · `cmd_import` (portable profile bundle) |
| begin · menu · setup · uninstall · help | the rest |

## config.py: foundation

Pure constants + the atomic‑write primitive everything else builds on. Knows
no other engine module (the bottom of the dependency graph).

```mermaid
classDiagram
    class config {
        <<module>>
        +ROOT, CHAPTERS_DIR, USERS_DIR, THEMES_DIR
        +SETTINGS_PATH, WORK_FILENAME, PY, TIMEOUT
        +MODES, DEFAULT_SETTINGS, WIDTH
        +load_settings() dict
        +save_settings(settings)
        +set_setting(key, value)
        +write_json(path, data)
        +now() str
        +rel(path) str
    }
```

`write_json` is the single atomic JSON writer (write temp → `os.replace`), so a
crash mid‑write can never corrupt `progress.json` / `answers.json` / settings.

## content.py: the structured question

Discovers puzzle folders and loads their files. **Stateless**: no learner data
here. `discover()` returns the ordered `Puzzle` dicts the whole app keys on.

```mermaid
classDiagram
    class content {
        <<module>>
        +discover() list~Puzzle~
        +by_id_lookup(puzzles, pid) Puzzle
        +starter_path(puzzle) str
        +read_starter(puzzle) str
        +load_hints(dirpath) list~str~
        +load_tests(dirpath) module
    }
    content ..> config : CHAPTERS_DIR
```

`discover()` tolerates a broken `meta.json`, it logs to stderr and skips that
folder rather than failing the whole scan. `load_tests` re‑imports each
`tests.py` fresh per call, which is what gives the audit fresh randomness on
every attempt.

## inputs.py: the input seam ("input automizer")

Where a single source decides **both** the value fed to the solution and the
data needed to validate it, so answers can't be hardcoded.

```mermaid
classDiagram
    class Case {
        +str stdin
        +tuple args
        +dict kwargs
        +any expect
        +dict meta
    }
    class inputs {
        <<module>>
        +fixed(*cases) list~Case~
        +random_ints(count, low, high, seed) list~int~
        +random_word(min, max, rng) str
        +random_int(low, high, rng) int
    }
    inputs ..> Case : builds
```

A `tests.py` builds fixed + randomized `Case`s: script puzzles feed
`case.stdin`, import puzzles feed `case.args`, and both validate against
`case.expect`, one source decides input *and* expected result, so answers
can't be hardcoded.

## state.py: per‑user progress & the work.py lifecycle

Owns everything mutable and per‑user. All writes go through `config.write_json`;
an unreadable file is moved aside as `<name>.corrupt`, never overwritten.

```mermaid
classDiagram
    class state {
        <<module>>
        +valid_username(name) bool
        +current_user() str
        +user_dir / progress_path / answers_path(user)
        +list_users() · ensure_user() · migrate_legacy()
        +backup_corrupt(path) str
        +default_progress(puzzles) dict
        +load_progress(...) prog, fresh
        +save_progress(prog) · stat(prog, pid)
        +current_puzzle(...) Puzzle
        +load_answers() · save_answers()
        +work_path() · read_work() · write_work(code)
        +archive_work(...) · archive_current(...)
        +ensure_workspace(...) · activate(...) · switch_to(...)
    }
    state ..> config : write_json · paths
```

### The `work.py` lifecycle

```mermaid
stateDiagram-v2
    [*] --> Welcome : first run
    Welcome --> Seeded : begin / goto, seed from starter
    Seeded --> Edited : learner edits
    Edited --> Archived : check / switch, archive to answers.json
    Archived --> Seeded : switch_to next
    Archived --> Welcome : reset
```

## checker.py: one check, end to end

Translates the toolkit's typed failures into learner‑facing screens. It is the
bridge between the tester (`toolkit/`) and the presentation (`render`/`theme`).

```mermaid
classDiagram
    class checker {
        <<module>>
        +SAVE_TIP
        +cmd_check(puzzles, by_id, prog)
        +fail_nudge(prog, cur)
        -_run_bonus(tests, T)
        -_fail(title, body, prog, cur)
        -_almost(title, body, prog, cur)
        -_solved(cur, prog, puzzles)
    }
    checker ..> content : load_tests
    checker ..> state : ensure_workspace / archive_work / save_progress
    checker ..> Toolkit : runs check(T)
    checker ..> render : cards & feedback
```

### Failure → screen mapping

```mermaid
flowchart LR
    chk["tests.check(T)"] -->|PuzzleSyntaxError| f1["_fail: syntax"]
    chk -->|MissingSymbolError| f2["_fail: missing piece"]
    chk -->|LessonNotUsedError| a1["_almost: right answer,<br/>wrong lesson"]
    chk -->|WrongResultError| f3["_fail: wrong result"]
    chk -->|PuzzleCrashError| f4["_fail: crash"]
    chk -->|no error| ok["_solved + _run_bonus"]
```

`LessonNotUsedError` subclasses `WrongResultError`, so its **more specific**
`except` must come first in `cmd_check` (and does), this is the "so close"
screen that distinguishes a wrong answer from a right answer that skipped the
lesson.
