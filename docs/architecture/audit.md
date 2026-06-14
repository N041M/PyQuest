# audit.py — conformance, anti‑sidestep, engine self‑test

`audit.py` is the project's executable reality check. It is **not part of the
engine** (safe to delete) and is the test suite: there is no pytest layer.
← [overview](README.md)

```bash
python3 audit.py            # every solution.py passes its own tests.py
python3 audit.py --sidestep # ALSO attack every puzzle with the adversaries
python3 audit.py --engine   # self-test the execution guard & toolkit APIs
```

It reuses the real engine (`content.discover/load_tests`, the `Toolkit`), so it
grades against exactly what learners run.

```mermaid
flowchart TB
    main["main()"] --> conf["conformance_issues<br/>«default»"]
    main --> side["sidestep_report<br/>«--sidestep»"]
    main --> eng["_engine_selftest<br/>«--engine»"]
    conf --> tk["Toolkit.check"]
    side --> rec["Recorder «records the tape»"]
    side --> adv["adversaries → impostor_passes"]
    side --> dod["load_dodges"]
    rec --> tk
```

---

## Structure

```mermaid
classDiagram
    class Toolkit
    class Recorder {
        +list stdin_runs
        +list fn_calls
        +run(stdin, files)
        +call(name, ...)
    }
    Toolkit <|-- Recorder

    class audit {
        <<module>>
        +ALLOWED · CHAFF
        +build_impostor(rec)
        +build_synth(rec, named)
        +load_dodges(pdir)
        +impostor_passes(p, src, attempts)
        +sidestep_report(p)
        +conformance_issues(p)
        +_engine_selftest()
        +main()
    }
    audit ..> Recorder
    audit ..> content : discover · load_tests
```

`ALLOWED` whitelists puzzles where the cheapest passing program is a legitimate
answer; `CHAFF` is dead code holding every construct (to test that liveness
ignores it). `build_impostor`/`build_synth` synthesize the adversaries;
`sidestep_report` returns `(breaches, dodge_passes)` per puzzle.

`Recorder` subclasses the real `Toolkit` so it grades identically while also
capturing the **tape** of every `(stdin → stdout)` and `(call → result)` — the
raw material every adversary is built from.

## The four generic adversaries (mutation testing of the grader)

```mermaid
flowchart LR
    rec["Recorder → tape"] --> r1["replay"] --> d1{{"randomized inputs"}}
    rec --> r2["chaff-replay"] --> d2{{"liveness checks"}}
    rec --> r3["synth"] --> d3{{"line_* checks"}}
    rec --> r4["named-synth"] --> d4{{"pin the stored value"}}
```

The Recorder runs the reference solution to capture the **tape**, then four
adversaries answer from it: **replay** (a lookup table, computing nothing),
**chaff-replay** (the table plus `CHAFF` — a never-called function holding every
construct), **synth** (re-derive a fixed output via arithmetic the brief never
asked for), and **named-synth** (the same constants parked in a variable). Each
hexagon is the defense that defeats it.

**A passing impostor is a hole.** Each puzzle should be saved by at least one
defense per adversary. `ALLOWED` whitelists the rare puzzle where the cheapest
passing program *is* a legitimate answer (e.g. 1.1 "print one literal").

## Per‑puzzle pinned regressions — `dodges.py`

```mermaid
flowchart LR
    dfile["puzzle/dodges.py<br/>DODGES = [(label, source), ...]"]
    dfile --> ip["impostor_passes(p, src, attempts=1)"]
    ip -->|"any passes"| fail["!! DODGE PASSES → audit FAILS"]
    ip -->|"all fail"| ok["green"]
```

Every known hand‑found sidestep is pinned here with the check that now blocks
it; the audit fails forever if one ever passes again.

## Sequence — `--sidestep` against one puzzle

```mermaid
sequenceDiagram
    autonumber
    participant M as main
    participant SR as sidestep_report
    participant Rec as Recorder
    participant B as builders
    participant IP as impostor_passes
    participant D as load_dodges

    M->>SR: sidestep_report(p)
    SR->>Rec: run reference solution, record the tape
    SR->>B: build replay / chaff / synth / named-synth
    loop each adversary
        SR->>IP: impostor_passes(p, src, attempts=2)
        IP->>IP: temp file · fresh tests · Toolkit.check
        IP-->>SR: passed? — a breach if yes
    end
    SR->>D: load_dodges(dir)
    loop each pinned dodge
        SR->>IP: impostor_passes(p, src, attempts=1)
        IP-->>SR: must be False
    end
    SR-->>M: breaches, dodge_passes
    M-->>M: weak++ on any breach or passing dodge
```

## `--engine` — the guard's guarantees, pinned

`_engine_selftest()` runs ~25 direct cases asserting each promise the
[ExecutionGuard](toolkit.md) and toolkit make: `exit()`/hang/stray‑`input()`
translation, stdout capture, the file sandbox never leaking into the project,
class/mutation/`approx`/case‑sensitive‑`eq` behavior, liveness killing dead
chaff while honest constructs pass, the `line_*` checks, the structural checks
(`uses_nested_if`, `uses_default_param`, `uses_with_open`), atomic JSON writes,
corrupt‑file backup, username validation, and discovery tolerating bad meta.

```mermaid
flowchart LR
    sub["learner(code) → temp file + Toolkit"]
    sub --> cases["case(label, fn): run, classify ok/FAIL"]
    cases --> report["N/N engine self-tests pass"]
```

Run order in CI‑of‑one: `--engine` after touching `toolkit/`, `--sidestep`
before any commit; both must be green (current bar: **82/82 conformance,
0/82 sidesteppable, 25/25 engine self‑tests**).
