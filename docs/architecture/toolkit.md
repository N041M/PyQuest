# toolkit/ — the `T` tester

`T`, the object handed to every puzzle's `check(T)`. It runs the learner's code
through one guard, asserts on behavior, and judges whether the lesson's
construct was actually *used* (liveness). ← [overview](README.md)

The package is composed by concern; dependencies point **down** this list, and
`Toolkit` is a thin facade that inherits each group as a mixin so `tests.py`
keeps a flat `T.eq(...)` / `T.uses_op(...)` surface.

```mermaid
flowchart TB
    facade["__init__.Toolkit (facade)"]
    facade --> runners
    facade --> asserts
    facade --> liveness
    facade --> constructs
    facade --> lines
    facade --> perf
    runners["runners.py"] --> guard
    liveness["liveness.py"] --> guard["guard.ExecutionGuard"]
    constructs["constructs.py"] --> liveness
    lines["lines.py"] --> liveness
    runners --> errors
    asserts["asserts.py"] --> errors
    guard --> errors["errors.py"]
    runners --> textutil
    liveness --> textutil["textutil.py"]
    perf["perf.py"]
```

---

## Composition — the facade and its mixins

```mermaid
classDiagram
    class Toolkit {
        +str path
        +str mode  "script | import"
        +ExecutionGuard guard
        -module _module
        -AST _tree
        -list _runs   "tape: (stdin, files, stdout)"
        -list _calls  "tape: (name, args, kwargs)"
        -_live_base
        -bool _live_base_done
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
        +uses_op/if/for/while/loop/break/continue
        +uses_try/raise/in/boolop/comprehension
        +uses_index/negative_index/slice/fstring
        +uses_call/dict/set/nested_if/unpacking
        +uses_with / uses_with_open
        +uses_import/class/yield/lambda/default_param
        +uses_print / print_uses_keyword / print_has_min_args
        +prints_computed/prints_name
        +assigns_a_variable / reassigns_a_variable
    }
    class LinesMixin {
        +print_expr(i)
        +line_uses_op(i, op)
        +line_shape(i, outer, inner)
        +line_only_literals(i, allowed)
    }
    class PerfMixin {
        +time_call(name, *a, runs) float
        +scales(name, make_input, n_small, n_big, slack)
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
runs that the behavior assertions recorded — **call behavior assertions before
construct checks**.

## The execution guard — the one place learner code runs

```mermaid
classDiagram
    class ExecutionGuard {
        +int timeout
        +str printed  "captured stdout"
        -str _sandbox
        +sandbox() str
        +put_file(name, content)
        +guarded(because, fn, *a, _stdin, **k)
    }
    note for ExecutionGuard "guarded() turns on every protection:\n• stdin blanked (stray input() fails fast)\n• stdout captured into .printed\n• SIGALRM wall-clock timeout (POSIX main thread)\n• exit()/SystemExit translated\n• cwd → throwaway sandbox (file I/O is contained)"
```

Script mode gets stronger isolation via a real subprocess (cross‑platform
timeout + sandbox cwd); import/liveness runs in‑process under the same guard.
**No learner code is ever invoked outside `guarded()`** — `audit.py --engine`
pins each guarantee.

## Translated failures — one type per learner screen

```mermaid
classDiagram
    class Exception
    class WrongResultError {
        +expected
        +actual
        +because
    }
    class LessonNotUsedError {
        "answer right, lesson skipped"
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

`LessonNotUsedError` **is‑a** `WrongResultError` — catch it first (the checker
does). It carries the wanted construct as `expected` and the offending code (or
the "decorative code doesn't count" note) as `actual`.

## Sequence — `T.run()` (script mode) records the tape

```mermaid
sequenceDiagram
    autonumber
    participant Test as tests.check(T)
    participant R as RunnersMixin.run
    participant G as ExecutionGuard
    participant P as subprocess(work.py)
    Test->>R: run(stdin, files)
    R->>G: put_file(...) seed fixtures
    R->>P: subprocess in sandbox cwd, stdin piped
    P-->>R: returncode, stdout, stderr
    alt non-zero exit
        R-->>Test: raise PuzzleSyntaxError / PuzzleCrashError
    else ok
        R->>R: normalize(stdout)
        R->>R: _runs.append((stdin, files, out))  %% the tape
        R-->>Test: normalized stdout
    end
```

## Sequence — liveness: "is this construct actually used?"

```mermaid
sequenceDiagram
    autonumber
    participant C as ConstructsMixin.uses_*
    participant L as LivenessMixin
    participant G as ExecutionGuard
    C->>L: _require_live(found nodes, kind)
    L->>L: _baseline() — replay the tape in-process → signature(stdout)
    alt no tape / not reproducible
        L-->>C: degrade to plain AST presence (never block on a harness quirk)
    else have baseline
        loop each candidate node
            L->>L: _ablate(node) — remove stmt / substitute expr with sentinel
            L->>G: re-run recorded inputs on the mutated AST
            G-->>L: ablated signature
            L->>L: live? stmt: crash/any change · expr: clean run, changed output
        end
        alt at least one live node
            L-->>C: pass
        else all decorative
            L-->>C: raise LessonNotUsedError("decorative code doesn't count")
        end
    end
```

Liveness signatures capture **stdout only**. For file/side‑effect lessons that
means a write‑only `with` looks dead — which is exactly why the files chapter
uses `uses_with_open` anchored on a *read* whose removal crashes downstream (see
[audit.md](audit.md) and `SIDESTEP_PLAYBOOK.md`).

## Three layers of construct strength

```mermaid
flowchart TB
    a["AST‑only presence<br/>(uses_yield/lambda/default_param)<br/>weakest — ablation is awkward"]
    b["liveness‑checked construct<br/>(most uses_*) — must change behavior"]
    c["expression‑scoped line_*<br/>strongest — pins the exact printed expression"]
    a --- b --- c
```

`require_live(want, missing, node_indices, kind, because)` is the public seam: a
complex puzzle composes a bespoke structural check from `T.tree()` + audited
liveness instead of hand‑rolling AST logic — and ships a `dodges.py` proving it
bites.
