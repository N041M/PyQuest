# toolkit/: the `T` tester

`T`, the object handed to every puzzle's `check(T)`. It runs the learner's code
through one guard, asserts on behavior, and judges whether the lesson's
construct was actually *used* (liveness). ← [overview](README.md)

The package is composed by concern; dependencies point **down** this list, and
`Toolkit` is a thin facade that inherits each group as a mixin so `tests.py`
keeps a flat `T.eq(...)` / `T.uses_op(...)` surface.

```mermaid
flowchart TB
    facade["Toolkit «facade»"]
    facade --> ra["runners · asserts<br/>«run code · assert»"]
    facade --> cl["constructs · lines<br/>«integrity checks»"]
    facade --> perf["perf «timing»"]
    cl --> liveness["liveness «ablation»"]
    ra --> guard["ExecutionGuard «sandbox»"]
    liveness --> guard
    guard --> base["errors · textutil"]
    classDef found fill:#eef,stroke:#557;
    class base found;
```

---

## Composition: the facade and its mixins

```mermaid
classDiagram
    class Toolkit {
        +str path
        +str mode
        +ExecutionGuard guard
        -_module · _tree
        -_runs · _calls «the tape»
        -_live_base · _live_base_done
        +__init__(path, mode, timeout)
    }
    class RunnersMixin {
        +run(stdin, files) str
        +call(name, *a, **k)
        +load() module
        +func/get(name)
        +make/method/attr(...)
        +put_file/file(name)
        +source() str
        +does_not_mutate(name, *a)
    }
    class AssertsMixin {
        +eq(actual, expected, because, match_case=True)
        +true/is_a/raises(...)
        +approx/any_of/unordered(...)
    }
    class LivenessMixin {
        +tree() AST
        +require_live(want, missing, idx, kind, ...)
        -_baseline() / _is_live(idx, kind)
        -_signature/_ablate/_tripwire(...)
    }
    class ConstructsMixin {
        +uses_op / uses_if / uses_for / uses_while ...
        +uses_with / uses_with_open / uses_call ...
        +uses_class(name) / uses_default_param ...
        +print_* · prints_* · assigns_* checks
        +30+ checks (liveness-judged where it can)
    }
    class LinesMixin {
        +print_expr(i)
        +line_uses_op(i, op)
        +line_shape(i, outer, inner)
        +line_only_literals(i, allowed)
    }
    class PerfMixin {
        +time_call(name, ...) float
        +scales(name, make_input, ...)
    }
    Toolkit --|> RunnersMixin
    Toolkit --|> AssertsMixin
    Toolkit --|> LivenessMixin
    Toolkit --|> ConstructsMixin
    Toolkit --|> LinesMixin
    Toolkit --|> PerfMixin
    Toolkit *-- ExecutionGuard
```

The mixins share state through the facade (`self.path`, `self.guard`, the tape
`self._runs`/`self._calls`, the AST/liveness caches). Method‑resolution order is
fixed in the `Toolkit(...)` base list, so the tape‑aware liveness checks see the
runs that the behavior assertions recorded, **call behavior assertions before
construct checks**.

## The execution guard: the one place learner code runs

```mermaid
classDiagram
    class ExecutionGuard {
        +int timeout
        +str printed
        -str _sandbox
        +sandbox() str
        +put_file(name, content)
        +guarded(because, fn, ...)
    }
```

`guarded()` turns on every protection at once: stdin blanked (a stray `input()`
fails fast), stdout captured into `.printed`, a SIGALRM wall‑clock timeout (on
the POSIX main thread), `exit()`/`SystemExit` translated, and the cwd moved to a
throwaway sandbox so file I/O is contained.

Script mode gets stronger isolation via a real subprocess (cross‑platform
timeout + sandbox cwd); import/liveness runs in‑process under the same guard.
**No learner code is ever invoked outside `guarded()`**, `audit.py --engine`
pins each guarantee.

## Translated failures: one type per learner screen

```mermaid
classDiagram
    class Exception
    class WrongResultError {
        +expected
        +actual
        +because
    }
    class LessonNotUsedError {
        +answer right, lesson skipped
    }
    class PuzzleSyntaxError { +detail }
    class MissingSymbolError { +name }
    class PuzzleCrashError { +detail; +because }
    Exception <|-- WrongResultError
    WrongResultError <|-- LessonNotUsedError
    Exception <|-- PuzzleSyntaxError
    Exception <|-- MissingSymbolError
    Exception <|-- PuzzleCrashError
```

`LessonNotUsedError` **is‑a** `WrongResultError`, catch it first (the checker
does). It carries the wanted construct as `expected` and the offending code (or
the "decorative code doesn't count" note) as `actual`.

## Sequence: `T.run()` (script mode) records the tape

```mermaid
sequenceDiagram
    autonumber
    participant Test as tests.py
    participant R as RunnersMixin
    participant G as ExecutionGuard
    participant P as work.py subprocess
    Test->>R: run(stdin, files)
    R->>G: put_file, seed fixtures
    R->>P: run in sandbox cwd, stdin piped
    P-->>R: returncode, stdout, stderr
    alt non-zero exit
        R-->>Test: raise PuzzleSyntaxError / PuzzleCrashError
    else ok
        R->>R: normalize stdout
        R->>R: append to the tape (_runs)
        R-->>Test: normalized stdout
    end
```

## Sequence: liveness: "is this construct actually used?"

```mermaid
sequenceDiagram
    autonumber
    participant C as uses_* check
    participant L as LivenessMixin
    participant G as ExecutionGuard
    C->>L: _require_live(found nodes, kind)
    L->>L: _baseline, replay the tape, signature is stdout
    alt no tape / not reproducible
        L-->>C: degrade to plain AST presence
    else have baseline
        loop each candidate node
            L->>L: _ablate, remove stmt / sentinel-swap expr
            L->>G: re-run recorded inputs on the mutated AST
            G-->>L: ablated signature
            L->>L: live? stmt = crash/any change · expr = clean+changed
        end
        alt at least one live node
            L-->>C: pass
        else all decorative
            L-->>C: raise LessonNotUsedError
        end
    end
```

Liveness signatures capture **stdout only**. For file/side‑effect lessons that
means a write‑only `with` looks dead, which is exactly why the files chapter
uses `uses_with_open` anchored on a *read* whose removal crashes downstream (see
[audit.md](audit.md)).

A second gap: `make`/`method`/`attr` (the object helpers) are **not on the
tape**, so the OOP chapters have no liveness at all. There, construct checks
degrade to plain AST presence, which a decoy `class X: pass` could satisfy, so
`uses_class(name)` takes the class name the tests instantiate, and the lessons
lean on randomized `make`/`method` arguments plus hand‑pinned `dodges.py`.
Recording the object tape (and replaying it in liveness) is the remaining work
flagged in `runners.py`.

## Three layers of construct strength

```mermaid
flowchart TB
    a["AST‑only presence<br/>(uses_yield/lambda/default_param)<br/>weakest, ablation is awkward"]
    b["liveness‑checked construct<br/>(most uses_*), must change behavior"]
    c["expression‑scoped line_*<br/>strongest, pins the exact printed expression"]
    a --- b --- c
```

`require_live(want, missing, node_indices, kind, because)` is the public seam: a
complex puzzle composes a bespoke structural check from `T.tree()` + audited
liveness instead of hand‑rolling AST logic, and ships a `dodges.py` proving it
bites.
