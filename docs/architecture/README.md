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
does one thing, prints, and exits. The only interactive surface is the `menu`
menu. There are **no third‑party dependencies** (Python 3.8+ stdlib only).

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

The wiring *inside* the `engine/` container, shown as one coarse view plus
three focused slices so each stays small. Arrows point **toward the dependency**
(A → B means "A imports B"); verify the edges with
`grep -rE "^from \.\.?" engine`. `config` is the universal foundation imported
widely, so it appears only where a slice needs it. The per‑verb edges into the
data and visual layers live in [commands.md](commands.md); the tester in
[toolkit.md](toolkit.md).

### 4.1 At a glance

```mermaid
flowchart TB
    play["start.py «entry»"] --> app["app.py «argv dispatch»"]
    app --> verbs["commands/ «verbs»"]
    app --> checker["checker.py «one check»"]

    subgraph services["engine services"]
        direction LR
        data["content + state «data»"]
        vis["render + theme «visuals»"]
        toolkit["toolkit/ «T tester»"]
    end

    verbs --> services
    checker --> services
    services --> config["config.py «foundation»"]

    classDef base fill:#eef,stroke:#557;
    class config base;
```

Four tiers, no cycles: the **entry** starts **dispatch**, which routes each
command to the **verbs** or the **checker**; both lean on the shared **services**
(data, visuals, the tester), and everything bottoms out at **config**. The three
slices below zoom in, including which services each branch imports.

### 4.2 Dispatch & verbs

```mermaid
flowchart TB
    app["app.py"] --> creg["registry «verb table»"]
    app --> cinit["commands/__init__ «facade»"]
    cinit --> cviews["views «status/map/hint/solution»"]
    cinit --> cnav["navigate «goto/next/skip/retry/revert»"]
    cinit --> cmenu["menu «menu»"]
    cinit --> cprof["profiles «theme/mode/user/reset»"]
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

### 4.3 The check path

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
this path end to end.

### 4.4 Data, visuals & foundation

```mermaid
flowchart TB
    state["state.py «progress/answers/work.py»"] --> content["content.py «discovery + loaders»"]
    state --> config["config.py «paths · atomic write · WIDTH»"]
    content --> config
    render["render.py «primitives»"] --> theme["theme.py «palette · glyphs · paint»"]
    theme --> config
    inputs["inputs.py «input seam»"]
    tests["a puzzle's tests.py"] -. imports .-> inputs
    classDef base fill:#eef,stroke:#557;
    class config base;
    classDef seam fill:#efe,stroke:#575,stroke-dasharray:3 3;
    class inputs seam;
    class tests seam;
```

The bottom layers. `inputs` is intentionally an island, no engine module
imports it; only a puzzle's `tests.py` does (the authoring seam, dashed).

### 4.5 Inside the toolkit

The `toolkit/` box is itself a small package: a thin `Toolkit` facade that
composes method groups (mixins) over one shared sandbox. Coarse shape here; the
class‑level composition and the run/liveness sequences are in
[toolkit.md](toolkit.md).

```mermaid
flowchart TB
    facade["Toolkit «facade»<br/>composes the mixins, owns the tape"]
    facade --> behavior["runners + asserts<br/>«run code · assert behavior»"]
    facade --> integrity["constructs + lines<br/>«was the lesson used?»"]
    facade --> perf["perf «bonus timing»"]
    integrity --> liveness["liveness<br/>«ablation engine»"]
    behavior --> guard["ExecutionGuard<br/>«the one in-process sandbox»"]
    liveness --> guard
    guard --> base["errors + textutil<br/>«translated failures · helpers»"]
    classDef found fill:#eef,stroke:#557;
    class base found;
```

The dependency spine runs downward: the integrity checks lean on `liveness`
(does ablating the construct change behavior?), and every run of learner code,
behavior assertion or liveness re‑run, funnels through the single
`ExecutionGuard`. `perf` is the optional, advisory `bonus(T)` branch.

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

A puzzle is just seven files on disk; each has exactly one job and one reader.
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
        dodges["dodges.py"]
    end

    subgraph loop["engine, the learner loop"]
        direction TB
        discover["content.discover()"]
        ws["state → work.py"]
        check["checker → Toolkit.check"]
        hint["cmd_hint"]
        sol["cmd_solution"]
    end

    editor["the learner's editor"]
    audit["audit.py"]

    meta -->|always| discover
    starter -->|"seed work.py on start"| ws
    tests -->|on check| check
    hints -->|on hint| hint
    solution -->|on solution| sol
    brief -->|"path shown, never parsed"| editor
    tests --> audit
    solution --> audit
    dodges -->|"--sidestep only"| audit
```

`meta.json` is the only file loaded for *every* puzzle (discovery reads id,
mode, why); `brief.md` is never parsed, the engine just shows its path and the
learner opens it; `tests.py`, `solution.py`, and `dodges.py` are also what
`audit.py` grades against. Adding a puzzle is dropping these files on disk,
zero code changes.

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
