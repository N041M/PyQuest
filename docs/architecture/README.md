# PyQuest — Architecture (UML)

A UML view of PyQuest's design. The diagrams are written in [Mermaid](https://mermaid.js.org)
so they render directly on GitHub and in most Markdown/IDE viewers.

This page is the **overview**. Each module group has its own page with
module‑level class diagrams and the relevant sequences:

| Page | Covers |
|---|---|
| **[engine-core.md](engine-core.md)** | `app`, `config`, `content`, `inputs`, `state`, `checker` |
| **[toolkit.md](toolkit.md)** | the `T` tester: `Toolkit` facade, mixins, `ExecutionGuard`, liveness, errors |
| **[commands.md](commands.md)** | the verb package (`commands/`) and argv dispatch |
| **[visuals.md](visuals.md)** | `theme`, `render` — the isolated presentation layer |
| **[audit.md](audit.md)** | `audit.py` — conformance, the anti‑sidestep attack suite, engine self‑test |

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
    fs[("Filesystem<br/>chapters/ · users/ · themes/ · settings.json")]
    editor["The learner's own editor"]

    learner -->|"runs python3 play.py ..."| pq
    learner -->|edits & saves| editor
    editor -->|work.py| fs
    author -->|"drops puzzle folders"| fs
    pq <-->|read content / read+write state| fs
    pq -->|"renders cards & feedback"| learner
```

PyQuest is a **stateless command runner**, not a TUI: every invocation is one
short `python3 play.py <verb>` that reads content + per‑user state from disk,
does one thing, prints, and exits. The only interactive surface is the `begin`
menu. There are **no third‑party dependencies** (Python 3.8+ stdlib only).

## 2. Containers & components (C4 level 2)

```mermaid
flowchart TB
    subgraph entry["entry point"]
        play["play.py<br/>«launcher»"]
    end

    subgraph engine["engine/ (the application)"]
        app["app.py<br/>«argv dispatch»"]
        subgraph cmds["commands/ — the verbs"]
            verbs["status · map · hint · solution<br/>goto/next/skip/retry/revert · mode<br/>theme · user · reset · setup · begin/menu · help"]
        end
        checker["checker.py<br/>«orchestrates one check»"]
        subgraph tk["toolkit/ — the T tester"]
            toolkit["Toolkit + ExecutionGuard<br/>+ liveness"]
        end
        content["content.py<br/>«discovery + loaders»"]
        inputs["inputs.py<br/>«input providers»"]
        state["state.py<br/>«progress / answers / work.py»"]
        config["config.py<br/>«paths · settings · atomic write»"]
        subgraph vis["presentation"]
            theme["theme.py"]
            render["render.py"]
        end
    end

    subgraph data["content & state on disk"]
        chapters[("chapters/NN/MM/<br/>brief·starter·tests·hints·solution·meta(+dodges)")]
        users[("users/<name>/<br/>progress.json·answers.json·work.py")]
        themes[("themes/*.json")]
        settings[("settings.json")]
    end

    audit["audit.py<br/>«conformance + anti-sidestep»<br/>(not part of engine)"]

    play --> app
    app --> verbs
    app --> checker
    verbs --> checker
    checker --> toolkit
    checker --> content
    checker --> state
    verbs --> content
    verbs --> state
    verbs --> render
    toolkit --> inputs
    content --> chapters
    state --> users
    theme --> themes
    config --> settings
    render --> theme
    audit --> content
    audit --> toolkit
    audit --> chapters
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

**Invariants** (verified by `audit.py` + the docs in `../../ARCHITECTURE.md`):

| Rule | Where it lives |
|---|---|
| A new **puzzle** is files on disk only — zero code change | `content.discover()` auto‑scans |
| A new **command** → one `commands/` module + one dispatch line | `app.main()` |
| A new **validation helper** → one `toolkit/` module | `Toolkit` mixins |
| All in‑process learner code runs through **one guard** | `ExecutionGuard.guarded()` |
| Colours/glyphs/boxes exist **only** in the visual layer | `theme.py` / `render.py` |
| Every JSON write is **atomic** (temp + rename); a corrupt file is moved aside | `config.write_json` · `state.backup_corrupt` |

## 4. Domain model (the data a check moves through)

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

## 5. Key runtime sequence — `python3 play.py check`

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

    L->>App: play.py check
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
learner‑facing screen — see [toolkit.md](toolkit.md) and [engine-core.md](engine-core.md).

## 6. Anti‑sidestep posture (why the grader is hard to cheat)

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
    dodges -.pins.-> attacks
```

Detailed in [audit.md](audit.md). The manual counterpart lives in the
(gitignored) `SIDESTEP_PLAYBOOK.md`.
