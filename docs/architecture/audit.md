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
    main["main()"] --> conf["conformance_issues(p)"]
    main --> side["sidestep_report(p)  (--sidestep)"]
    main --> eng["_engine_selftest()  (--engine)"]
    conf --> tk["Toolkit(solution, mode).check"]
    side --> rec["Recorder (records the tape)"]
    side --> adv["adversaries → impostor_passes"]
    side --> dod["load_dodges(dir)"]
    rec --> tk
```

---

## Structure

```mermaid
classDiagram
    class Toolkit
    class Recorder {
        +list stdin_runs  "(stdin, stdout)"
        +list fn_calls    "(name, args, kwargs, result)"
        +run(stdin, files)
        +call(name, *a, **k)
    }
    Toolkit <|-- Recorder

    class audit {
        <<module>>
        +ALLOWED  "passing impostor is the accepted ceiling"
        +CHAFF    "dead code with every construct"
        +build_impostor(rec)  "replay lookup table"
        +build_synth(rec, named)  "compute fixed output another way"
        -_synth_expr(line)
        +load_dodges(pdir)  "per-puzzle pinned sidesteps"
        +impostor_passes(p, src, attempts)
        +sidestep_report(p) (breaches, dodge_passes)
        +conformance_issues(p) list
        +_engine_selftest() int
        +main() int
    }
    audit ..> Recorder
    audit ..> content : discover / load_tests
```

`Recorder` subclasses the real `Toolkit` so it grades identically while also
capturing the **tape** of every `(stdin → stdout)` and `(call → result)` — the
raw material every adversary is built from.

## The four generic adversaries (mutation testing of the grader)

```mermaid
flowchart TB
    rec["Recorder runs the reference solution<br/>→ tape (stdin_runs / fn_calls)"]
    rec --> r1["replay<br/>answer from a lookup table,<br/>compute nothing"]
    rec --> r2["chaff-replay<br/>table + CHAFF: a never-called fn<br/>stuffed with every construct"]
    rec --> r3["synth (fixed-output scripts)<br/>print each constant via arithmetic<br/>the brief never asked for"]
    rec --> r4["named-synth<br/>same constants parked in a var<br/>and reused"]
    r1 --> defeat1{{"defeated by:<br/>randomized inputs"}}
    r2 --> defeat2{{"defeated by:<br/>liveness checks"}}
    r3 --> defeat3{{"defeated by:<br/>line_* expression checks"}}
    r4 --> defeat4{{"defeated by:<br/>pinning the stored value"}}
```

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
it; the audit fails forever if one ever passes again. (The manual hunting
process is documented in the gitignored `SIDESTEP_PLAYBOOK.md`.)

## Sequence — `--sidestep` against one puzzle

```mermaid
sequenceDiagram
    autonumber
    participant M as main()
    participant SR as sidestep_report
    participant Rec as Recorder
    participant B as build_impostor / build_synth
    participant IP as impostor_passes
    participant D as load_dodges

    M->>SR: sidestep_report(p)
    SR->>Rec: load_tests(dir).check(Recorder)  %% record the tape
    SR->>B: build replay / chaff / synth / named-synth
    loop each adversary
        SR->>IP: impostor_passes(p, src, attempts=2)
        IP->>IP: write src to temp · load_tests fresh · Toolkit().check
        IP-->>SR: passed? (breach if yes)
    end
    SR->>D: load_dodges(dir)
    loop each pinned dodge
        SR->>IP: impostor_passes(p, src, attempts=1)
        IP-->>SR: must be False
    end
    SR-->>M: (breaches, dodge_passes)
    M-->>M: weak++ if any breach (not ALLOWED) or any dodge passes
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
