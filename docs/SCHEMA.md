# Authoring schema

The file formats for adding or editing puzzles. For the design rules behind
them, see [ARCHITECTURE.md](ARCHITECTURE.md). A puzzle is one folder under
`chapters/NN_title/MM_title/` containing six files: `brief.md`, `starter.py`,
`tests.py`, `hints.md`, `solution.py`, and `meta.json`, plus an optional
`dodges.py` of pinned sidesteps (see below). The engine discovers new puzzle
folders automatically, no code changes needed.

## The workspace model

The learner never edits files inside a puzzle folder. Instead each user has a
single `users/<name>/work.py` that the engine owns. When a puzzle becomes
current, the engine seeds `work.py` from that puzzle's `starter.py` (or from the
learner's previously saved code). `check` validates `work.py`. Every check
archives the workspace into that user's `answers.json` (see below). This is what
lets `reset` restore a truly clean slate, it deletes the profile's
`answers.json` and regenerates `work.py`.

So when authoring, the file you write as the starting point is `starter.py`; the
learner sees its contents in `work.py`.

## meta.json

```json
{
  "id": "1.1",
  "title": "Hello, output",
  "chapter": "Basics",
  "concept": "print() displays a line of text",
  "mode": "script",
  "why": "print() sends its arguments to the screen, then a newline."
}
```

- `mode` is `"script"` or `"import"`.
  - `script`: run the workspace `work.py` as a subprocess, compare stdout.
  - `import`: import the workspace `work.py` and call its functions, assert on returns.
- `id` must match the folder numbers: chapter `01_` + puzzle `01_` → `"1.1"`.
- `why` is printed by `play.py solution` under "Why it works".

## tests.py

Each `tests.py` defines exactly one required function:

```python
def check(T):
    ...
```

`T` is a toolkit provided by the engine. It both runs the learner's code and
raises *translated* failures, so a missing function, a syntax error, a wrong
return, and a crash each produce a different plain-language message.

### Script-mode helpers

```python
def check(T):
    out = T.run()                 # run work.py, return normalized stdout
    T.eq(out, "Hello, output",
         because="It should print exactly: Hello, output")

    out2 = T.run(stdin="Ada\n")   # feed predetermined stdin
    T.eq(out2, "Hello, Ada")
```

### Import-mode helpers

```python
def check(T):
    T.eq(T.call("double", 21), 42)
    T.eq(T.call("double", 0), 0, because="Zero is an easy case to forget.")
    T.eq(T.call("double", -5), -10)   # edge case
    obj = T.get("CONSTANT")           # fetch a non-callable symbol
    T.raises(ValueError, "parse", "abc")   # assert it raises
```

Every execution of the learner's code runs under the engine's guard: stdin is
blanked (a stray `input()` fails with a friendly message instead of hanging),
stdout is captured into `T.printed`, infinite loops hit the wall-clock timeout,
`exit()`/`sys.exit()` is translated, and the working directory is a throwaway
sandbox, so learner file I/O can never touch the project.

Available on `T`:

- `T.run(stdin="", files=None)` → normalized stdout (script mode). `files`
  seeds fixture files into the sandbox, e.g. `T.run(files={"in.txt": "abc"})`.
- `T.put_file(name, content)` / `T.file(name)` → create a fixture / read a
  file the learner's code wrote (missing file = translated failure).
- `T.printed` → stdout captured from the last import-mode load/call.
- `T.load()` → the imported module (fresh each check).
- `T.func(name)` → the callable, or a translated "missing piece" failure.
- `T.get(name)` → any module-level symbol.
- `T.call(name, *args, **kwargs)` → call it; crashes are translated.
- `T.make("ClassName", *args)` / `T.method(obj, "name", *args)` /
  `T.attr(obj, "name")` → instantiate and exercise the learner's classes.
- `T.does_not_mutate(name, *args)` → call and require the arguments back
  unchanged (for "return a NEW value" lessons); returns the result.
- `T.eq(actual, expected, because="")` → assert equal. String outputs are
  whitespace-normalized and compared **case-sensitively** by default (this is a
  Python course; capitalisation is part of the answer); pass `match_case=False`
  for the rare puzzle where any casing is fine.
- `T.true(cond, because="")`, `T.is_a(value, type, because="")`.
- `T.raises(ExcType, name, *args, **kwargs)`.

### Construct checks (integrity)

`T.uses_op("+")`, `T.uses_if/for/while/loop/break/continue`, `T.uses_try`,
`T.uses_raise`, `T.uses_in`, `T.uses_boolop(op=)`, `T.uses_call(name)`,
`T.uses_with`, `T.uses_with_open` (the files chapter: the FILE must be opened
by a `with`, a generic `uses_with` is satisfied by any live `with`, even a
`with io.StringIO()` wrapping a print, so use `uses_with_open` for file
lessons), `T.uses_dict/set`, `T.uses_nested_if`,
`T.uses_index/negative_index/slice(step=)`, `T.uses_fstring`,
`T.uses_comprehension(with_if=)`, `T.uses_unpacking`, `T.uses_default_param(name)`,
`T.uses_class(name)` (the OOP chapters: pass the class name the tests
instantiate, object puzzles run through `make`/`method`/`attr`, which aren't on
the tape, so this is an AST presence check and the name stops a decoy
`class X: pass` standing in for a namedtuple/`type()`),
`T.uses_print`, `T.print_uses_keyword(kw)`, `T.print_has_min_args(n)`,
`T.prints_computed(min_calls=)`, `T.prints_name(min_calls=, same=)`,
`T.assigns_a_variable(value=)`, `T.reassigns_a_variable(values=)`.

Most of these are **liveness-checked**: a construct only counts if mutating it
away changes the program's behavior on the inputs the tests already ran. Dead
decorations (`q = 1 * 1`, `if False: pass`, a print routed into a StringIO)
don't satisfy anything, so call the behavior assertions (`T.run`/`T.call`)
**before** the construct checks, liveness replays those recorded inputs.
(`uses_default_param`, like `uses_yield`/`uses_lambda`, is AST-only: ablating a
default is awkward.) A failed construct check raises `LessonNotUsedError`, the
answer was right but the lesson's tool was skipped, which the checker shows as
its own "so close" screen, distinct from a plain wrong-result failure.

Use these to pin the lesson against a *different tool* that gets the same
answer: `uses_boolop()` (not `n % 6 == 0` for "divisible by 2 and 3"; accepts a
De Morgan `not(a or b)`), `uses_nested_if` (a real body nest, not a flat `elif`
chain, an `elif` is AST-identical to `else: if`), `uses_default_param("greet")`
(the `name=value` default, not `*args`), `uses_call("int")` (not `eval`).

For fixed-output puzzles (no input to randomize) where the lesson IS one
specific expression, pin the printed expression itself:

- `T.line_uses_op(i, op)` → print #i computes with `op` *inside its own
  argument* (defeats `print(7*2)` + `print(10+10)` answering an
  order-of-operations task).
- `T.line_shape(i, outer, inner)` → print #i contains `inner` evaluated
  before `outer` (`(2 + 3) * 4` is a Mult with an Add operand, a shape only
  parentheses can write).
- `T.line_only_literals(i, {2, 3, 4})` → print #i is built only from the
  task's own literals (type-strict; no variables, calls, or other numbers).

For a complex puzzle that needs a structural check none of the above covers,
compose one from audited parts instead of hand-rolling AST logic:
`T.tree()` for the AST, then `T.require_live(want, missing, node_indices,
kind, because=)` to demand the found nodes be live (`kind`: `"stmt"`,
`"expr"`, `"bool"`, `"container"`, `"trim"`, `"kw:<name>"`). Any bespoke
check must ship with a `dodges.py` entry proving it bites.

### dodges.py (optional)

Known sidesteps, pinned forever. A puzzle folder may include a `dodges.py`:

```python
DODGES = [
    ("right constants via the wrong arithmetic",
     'print(7*2)\nprint(10+10)\n'),
]
```

`python3 tools/audit.py --sidestep` runs every entry against the puzzle's tests and
fails the audit if any of them ever passes. Add an entry whenever a real
sidestep is discovered, together with the check that now blocks it.

### Many valid answers

The engine checks behavior, so any implementation that produces the right result
already passes. When the *answer itself* is not unique, assert a **property**
instead of one canonical value:

- `T.approx(actual, expected, tol=1e-9)` → floats within a tolerance, also
  recursively inside lists/tuples/dicts.
- `T.any_of(actual, [a, b, c])` → accept any of several valid outputs.
- `T.unordered(actual, expected)` → equal ignoring order (lists/tuples).
- `T.true(cond, because=...)` → any custom invariant, e.g.
  `T.true(all(12 % f == 0 for f in result), "every item divides 12")`.

### Performance check (optional, advisory)

A puzzle's `tests.py` may also define `bonus(T)`. It runs **only after** the
answer is already accepted and **never blocks** progress; it prints a separate
`⚡` line (LeetCode-style "correct, and also fast?"). Use it for an efficiency or
elegance target:

```python
def bonus(T):
    # wall-clock budget (generous -- timings are machine-dependent)
    T.true(T.time_call("dedupe", list(range(5000))) < 0.05,
           because="aim for O(n) -- try a set instead of repeated `in` on a list")

    # or a doubling experiment: confirm it scales ~linearly, not O(n^2)
    T.scales("dedupe", lambda n: list(range(n)), 2000, 16000,
             because="O(n^2) blows up as the input grows")
```

Timing is best-effort: keep budgets loose, prefer `T.scales` (relative growth)
over absolute time, and never gate correctness on it. There is no way to *prove*
big-O automatically, this catches gross inefficiency (accidental O(n^2)/O(2^n)),
which is what LeetCode-style timing does in practice too.

Rules to follow when authoring tests:

- Never inspect the learner's source text; only check behavior. (The
  construct checks are the sanctioned exception, and liveness makes even
  them behavioral.)
- Include at least one edge case per puzzle.
- Prefer `because=` to name the concept being tested; it shows up on failure.
- For non-unique answers, assert properties (`any_of`/`unordered`/`true`), not
  one fixed value.
- Run behavior assertions before construct checks (liveness replays the
  recorded runs/calls).
- After adding or changing a puzzle, run `python3 tools/audit.py --sidestep`: the
  attack suite must report it robust (see ARCHITECTURE §8).

## progress.json

Created on first run; you normally never edit it.

```json
{
  "version": 1,
  "mode": "normal",
  "current": "1.1",
  "completed": ["1.1", "1.2"],
  "highest": 2,
  "stats": { "1.3": { "attempts": 2, "hints_used": 1 } },
  "created_at": "2026-01-01T00:00:00"
}
```

- `current`: id of the active puzzle.
- `completed`: ids that have passed `check`.
- `highest`: furthest puzzle index unlocked (gates forward `goto`).
- `stats[id]`: per-puzzle attempts and hints used.

## answers.json

The learner's saved code, one entry per puzzle. Created/updated automatically;
deleted by `reset`. You never edit this by hand.

```json
{
  "1.1": { "solved": true,  "code": "print(\"Hello, output\")\n" },
  "1.2": { "solved": false, "code": "print(\"Counting:\")\n" }
}
```

- `code`: the contents of `work.py` last time this puzzle was the active one.
- `solved`: whether a `check` has ever passed for it.

## hints.md

Three hints, escalating from gentle nudge to near-answer, separated by a line
containing only `---`:

```
Think about which function puts text on the screen.

---

You want print(), and the text goes inside the parentheses in quotes.

---

print("Hello, output")
```

## brief.md

Free-form markdown the learner reads. The house style is:
concept from scratch → a tiny worked example → the task → what "done" looks like.
