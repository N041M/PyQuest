# PyQuest: Architecture (UML)

A UML view of PyQuest's design. The diagrams are written in [Mermaid](https://mermaid.js.org)
so they render directly on GitHub and in most Markdown/IDE viewers.

This page is the **overview**. Each module group has its own page with
module‑level class diagrams and the relevant sequences:

| Page | Covers |
|---|---|
| **[engine-core.md](engine-core.md)** | `app`, `config`, `content`, `inputs`, `state`, `checker` |
| **[toolkit.md](toolkit.md)** | the `T` tester: `Toolkit` facade, mixins, `ExecutionGuard`, liveness, errors |
| **[commands.md](commands.md)** | the verb package (`commands/`) and argv dispatch |
| **[visuals.md](visuals.md)** | `theme`, `render`, the isolated presentation layer |
| **[audit.md](audit.md)** | `audit.py`, conformance, the anti‑sidestep attack suite, engine self‑test |

> **Notation.** Python here is mostly module‑level functions, not classes, so a
> file is drawn as a UML class with the «module» stereotype: its functions are
> listed as operations and its module constants as attributes. Genuine classes
> (`Toolkit`, `ExecutionGuard`, the error hierarchy) are drawn as ordinary
> classes. Dependencies point **downward**: a box only knows about the boxes
> below it.

---

## 0. Master diagrams (every module & class)

The whole system as two clean panels — split so the layout stays untangled:
**0.1** the engine modules (the import graph) and **0.2** the tester
(`Toolkit`) class hierarchy. Together they cover every module and genuine class;
the per-area pages below add the per-verb and run/liveness detail. `─▷` (hollow
arrow) is inheritance, `┄▷` (dashed) a dependency (import/use).

### 0.1 Engine modules

«module» boxes and their import graph, reading left to right: entry → dispatch →
services → foundation. `i18n` localizes content and UI strings; `inputs` is the
authoring seam — no engine module imports it, a puzzle's `tests.py` does, building
`Case`s. Everything bottoms out at `config`. (`checker` → `toolkit/` is in §4.2.)

```mermaid
classDiagram
    direction LR
    class app {
        <<module>>
        +main()
    }
    class session {
        <<module>>
        +launch_session()
    }
    class commands {
        <<package>>
        +verbs · cards · registry
    }
    class checker {
        <<module>>
        +cmd_check()
    }
    class content {
        <<module>>
        +discover() category()
        +load_tests() load_reference()
    }
    class state {
        <<module>>
        +load_progress() current_puzzle()
        +ensure_workspace()
    }
    class i18n {
        <<module>>
        +t() localized()
    }
    class inputs {
        <<module>>
        +random_word() random_int()
    }
    class Case {
        +stdin args kwargs expect
    }
    class render {
        <<module>>
        +box() header() section()
    }
    class theme {
        <<module>>
        +paint() THEMES
    }
    class config {
        <<module>>
        +write_json() term_size()
        +ROOT WIDTH TIMEOUT
    }
    app ..> commands
    app ..> checker
    commands ..> content
    commands ..> state
    commands ..> render
    checker ..> content
    checker ..> state
    checker ..> render
    content ..> i18n
    content ..> config
    state ..> content
    state ..> config
    render ..> theme
    theme ..> config
    i18n ..> config
    session ..> config
    inputs ..> Case
```

### 0.2 The tester (`Toolkit`) classes

The genuine classes behind a `check`: the `Toolkit` facade composes six method
mixins; every run of learner code funnels through the one `ExecutionGuard`; and
failures are the translated `PuzzleError` hierarchy (`LessonNotUsedError` is a
`WrongResultError`, so its `except` must come first). `checker` is the only
module that touches this package.

```mermaid
classDiagram
    direction TB
    class Toolkit {
        <<facade>>
        +path mode
        +_runs _calls
    }
    class RunnersMixin {
        +run() call() make() method()
    }
    class AssertsMixin {
        +eq() approx() raises()
    }
    class ConstructsMixin {
        +uses_op() uses_call() uses_class()
    }
    class LinesMixin {
        +line_uses_op() line_shape()
    }
    class LivenessMixin {
        +require_live() tree()
    }
    class PerfMixin {
        +time_call() scales()
    }
    class ExecutionGuard {
        +guarded() sandbox()
    }
    class PuzzleError {
        <<exception>>
    }
    class PuzzleSyntaxError
    class MissingSymbolError
    class WrongResultError
    class PuzzleCrashError
    class LessonNotUsedError
    RunnersMixin <|-- Toolkit
    AssertsMixin <|-- Toolkit
    ConstructsMixin <|-- Toolkit
    LinesMixin <|-- Toolkit
    LivenessMixin <|-- Toolkit
    PerfMixin <|-- Toolkit
    Toolkit ..> ExecutionGuard : runs code
    ConstructsMixin ..> LivenessMixin : judged by
    ExecutionGuard ..> PuzzleError : raises
    PuzzleError <|-- PuzzleSyntaxError
    PuzzleError <|-- MissingSymbolError
    PuzzleError <|-- WrongResultError
    PuzzleError <|-- PuzzleCrashError
    WrongResultError <|-- LessonNotUsedError
```
---

## 1. System context (C4 level 1)

```mermaid
flowchart TB
    learner["Learner<br/>(writes work.py)"]
    author["Author<br/>(adds puzzles)"]
    pq["PyQuest<br/>terminal Python course"]
    fs[("Filesystem<br/>chapters/ · users/ · themes/")]
    editor["The learner's own editor"]

    learner -->|"runs python3 start.py ..."| pq
    learner -->|edits & saves| editor
    editor -->|work.py| fs
    author -->|"drops puzzle folders"| fs
    pq <-->|read content / read+write state| fs
    pq -->|"renders cards & feedback"| learner
```

PyQuest is a **stateless command runner**, not a TUI: every invocation is one
short `python3 start.py <verb>` that reads content + per‑user state from disk,
does one thing, prints, and exits. The interactive surfaces are the `menu`
launcher and the **play cockpit** (the card's arrow‑selectable nav row); both
engage only on a key‑capable TTY and degrade to plain prints otherwise. There
are **no third‑party dependencies** (Python 3.8+ stdlib only).

## 2. Containers (C4 level 2)

The runnable units and the stores they read/write, kept deliberately coarse.
The engine's internal **components** are the next level down: see §3 (layers)
and the per‑module pages.

```mermaid
flowchart TB
    play["start.py<br/>«entry»"]
    engine["engine/<br/>«the application»<br/>dispatch · verbs · checker · toolkit ·<br/>content · inputs · state · visuals"]
    audit["audit.py<br/>«test harness, not shipped»"]
    chapters[("chapters/<br/>puzzle content")]
    users[("users/<br/>profiles (progress · answers · work.py)<br/>+ settings.json")]
    themes[("themes/<br/>colour presets")]

    play --> engine
    engine -->|read| chapters
    engine -->|read/write| users
    engine -->|read| themes
    audit -->|reuses| engine
    audit -->|grades| chapters
```

## 3. Layered architecture (the five concerns that never bleed)

```mermaid
flowchart TB
    V["Visuals<br/>theme.py · render.py"]
    CK["Checking / orchestration<br/>checker.py · toolkit/"]
    CO["Content<br/>content.py"]
    IN["Input<br/>inputs.py"]
    ST["State<br/>state.py"]
    CF["Foundation<br/>config.py"]

    CK --> CO
    CK --> IN
    CK --> ST
    CK --> V
    CO --> CF
    ST --> CF
    V --> CF
    classDef f fill:#eef,stroke:#557;
    class CF f;
```

**Invariants** (verified by `audit.py` + the docs in `../ARCHITECTURE.md`):

| Rule | Where it lives |
|---|---|
| A new **puzzle** is files on disk only, zero code change | `content.discover()` auto‑scans |
| A new **command** → one `commands/` module + one dispatch line | `app.main()` |
| A new **validation helper** → one `toolkit/` module | `Toolkit` mixins |
| All in‑process learner code runs through **one guard** | `ExecutionGuard.guarded()` |
| Colours/glyphs/boxes exist **only** in the visual layer | `theme.py` / `render.py` |
| Every JSON write is **atomic** (temp + rename); a corrupt file is moved aside | `config.write_json` · `state.backup_corrupt` |

## 4. Engine components (C4 level 3)

The wiring *inside* the `engine/` container. §0 (the master diagram) is the full
structural picture; the two flows here add the direction and edge labels a class
diagram can't carry. Arrows point **toward the dependency** (A → B means "A
imports B"); verify with `grep -rE "^from \.\.?" engine`. The per‑verb edges into
the data and visual layers live in [commands.md](commands.md); the tester in
[toolkit.md](toolkit.md).

### 4.1 Dispatch & verbs

```mermaid
flowchart TB
    app["app.py"] --> creg["registry «verb table»"]
    app --> cinit["commands/__init__ «facade»"]
    cinit --> cviews["views «status/map/hint/solution»"]
    cinit --> cnav["navigate «goto/next/skip/retry/restart»"]
    cinit --> cmenu["menu «menu»"]
    cinit --> cprof["profiles «theme/mode/user/wipe»"]
    cinit --> ctrans["transfer «export/import»"]
    cinit --> cshort["shortcuts «shell installer»"]
    cinit --> chelp["help"]
    cviews --> ccards["cards «shared card/goto»"]
    cnav --> ccards
    cmenu --> ccards
    cmenu --> cprof
    cmenu --> cshort
    chelp --> creg
```

Only `cards` is shared and `menu` composes the other verbs, so adding a verb
touches one module plus one `elif` in `app.main()`. (Each verb's edges to
`content`/`state`/`render` are in [commands.md](commands.md).)

### 4.2 The check path

```mermaid
flowchart LR
    app["app.py"] --> checker["checker.py"]
    checker -->|load_tests| content["content.py"]
    checker -->|workspace + progress| state["state.py"]
    checker -->|"runs check(T)"| toolkit["toolkit/"]
    checker -->|cards + feedback| render["render.py"]
    toolkit --> config["config.py «TIMEOUT»"]
    classDef base fill:#eef,stroke:#557;
    class config base;
```

`checker` is the only module that touches the `toolkit`; the §6 sequence traces
this path end to end. The data, visual, and foundation wiring (`state`→`content`,
`content`→`i18n`/`config`, `render`→`theme`, the `inputs` seam) and the toolkit's
internal composition are in §0's master diagram; [toolkit.md](toolkit.md) zooms
into the tester.

## 5. Domain model (the data a check moves through)

```mermaid
classDiagram
    class Puzzle {
        +str id  "e.g. 8.4"
        +int ch_num
        +int pz_num
        +str ch_title
        +str dir
        +dict meta
    }
    class Meta {
        +str id
        +str title
        +str chapter
        +str concept
        +str mode  "script | import"
        +str why
        +str category  "Core | Advanced | Projects"
        +str kind  "projects: build | debug | capstone"
    }
    class Progress {
        +int version
        +str mode  "easy|normal|hard"
        +str current
        +list completed
        +int highest
        +dict stats
        +bool active
    }
    class Answers {
        +dict~id, Entry~ byId
    }
    class Entry {
        +bool solved
        +str code
    }
    class Case {
        +str stdin
        +tuple args
        +dict kwargs
        +any expect
        +dict meta
    }
    Puzzle "1" o-- "1" Meta : meta.json
    Progress "1" --> "1" Puzzle : current/highest
    Answers "1" o-- "*" Entry : per puzzle id
    Puzzle ..> Case : tests build cases
```

### How the system consumes a puzzle

A puzzle is a handful of files on disk; each has exactly one job and one reader.
This is the whole interaction surface between the engine and the content.

```mermaid
flowchart LR
    subgraph puzzle["a puzzle folder · chapters/NN/MM/"]
        direction TB
        meta["meta.json"]
        starter["starter.py"]
        tests["tests.py"]
        hints["hints.md"]
        solution["solution.py"]
        brief["brief.md"]
        reference["reference.md (opt)"]
        dodges["dodges.py (opt)"]
    end

    subgraph loop["engine, the learner loop"]
        direction TB
        discover["content.discover()"]
        ws["state → work.py"]
        check["checker → Toolkit.check"]
        hint["cmd_hint"]
        sol["cmd_solution"]
        book["cmd_textbook"]
    end

    editor["the learner's editor"]
    audit["audit.py"]

    meta -->|always| discover
    starter -->|"seed work.py on start"| ws
    tests -->|on check| check
    hints -->|on hint| hint
    solution -->|on solution| sol
    reference -->|on textbook| book
    brief -->|"path shown, never parsed"| editor
    tests --> audit
    solution --> audit
    starter -->|"--sidestep: debug must fail"| audit
    dodges -->|"--sidestep only"| audit
```

`meta.json` is the only file loaded for *every* puzzle (discovery reads id, mode,
category, kind); `brief.md` is never parsed — the engine shows its path and the
learner opens it; `reference.md` feeds the textbook; `tests.py`, `solution.py`,
`starter.py` (for debug puzzles), and `dodges.py` are what `audit.py` grades
against. Adding a puzzle is dropping these files on disk, zero code changes.

## 6. Key runtime sequence: `python3 start.py check`

```mermaid
sequenceDiagram
    autonumber
    actor L as Learner
    participant App as app.main()
    participant Ck as checker.cmd_check
    participant St as state
    participant Co as content.load_tests
    participant T as Toolkit (T)
    participant G as ExecutionGuard
    participant Sol as work.py (learner code)

    L->>App: start.py check
    App->>App: discover() · load_progress()
    App->>Ck: cmd_check(puzzles, by_id, prog)
    Ck->>St: ensure_workspace() · archive_work()
    Ck->>Co: load_tests(dir).check(T)
    activate T
    Note over T,G: behavior assertions first (run/call),<br/>then construct checks (liveness replays the tape)
    T->>G: guarded(run/import work.py)
    G->>Sol: subprocess (script) / exec (import)
    Sol-->>G: stdout / return / raise
    G-->>T: normalized result (or translated crash)
    T-->>Ck: pass · or raises a translated failure
    deactivate T
    alt passed
        Ck->>St: mark completed · archive solved · save_progress
        Ck-->>L: ✓ solved card (+ optional ⚡ bonus)
    else translated failure
        Ck-->>L: ✗ / "so close" screen by error type
    end
```

The five translated failure types (`toolkit/errors.py`) each map to a distinct
learner‑facing screen, see [toolkit.md](toolkit.md) and [engine-core.md](engine-core.md).

## 7. Anti‑sidestep posture (why the grader is hard to cheat)

```mermaid
flowchart LR
    subgraph defenses
        rnd["randomized inputs<br/>(inputs.py)"]
        live["liveness‑checked<br/>constructs (liveness.py)"]
        linex["expression‑scoped<br/>line_* checks (lines.py)"]
        beh["behavioral file checks<br/>(runners.put_file/file)"]
    end
    subgraph attacks["audit.py adversaries"]
        replay["replay"]
        chaff["chaff‑replay"]
        synth["synth / named‑synth"]
        dodges["per‑puzzle dodges.py"]
    end
    rnd -.defeats.-> replay
    live -.defeats.-> chaff
    linex -.defeats.-> synth
```

Each generic adversary has a structural defense (the dashed pairs).
**Behavioral file checks** add cover for write puzzles, the impostors
reproduce stdout, not files, and **per‑puzzle `dodges.py`** pins every
hand‑found sidestep as a permanent regression. Detailed in [audit.md](audit.md).
