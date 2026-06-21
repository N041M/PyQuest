# PyQuest content roadmap

The detailed planning companion to the public roadmap in the
[README](../README.md#roadmap). It maps the next **~150–200 puzzles** across new
concept chapters, more projects, and — deliberately — far more **debug** and
**extend** puzzles than the course has today.

> Numbers (`17.x`, `PR-A`, …) are a **proposal**, not a commitment. Chapters can
> be reordered and projects slotted between them; the engine ties ids to folder
> order, so renumbering is free until a puzzle ships.

## Where we are

142 puzzles, 16 chapters. **Variety is the gap:** 141 are `concept` lessons,
there is exactly **one** debug puzzle (16.3) and **no** standalone "extend
existing code" puzzle. One project chapter (16, the cart). This roadmap fixes
that imbalance as much as it adds new material.

## Puzzle archetypes (the variety we want)

| Tag | Kind in `meta.json` | What it is |
|---|---|---|
| **[C] concept** | `concept` set | teaches one new construct (the staple) |
| **[drill]** | neither | practice, no new syntax, out of the textbook |
| **[D] debug** | `kind: debug` | `starter.py` ships broken code to fix (audit enforces it fails) |
| **[X] extend** | `kind: build` *(or a concept with a full starter)* | given working code, add a method/feature |
| **[B] build** | `kind: build` | one component step of a project |
| **[K] capstone** | `kind: capstone` | low-guidance final assembly |

Mix across the ~201 additions: **~53%** concept (106), **~15%** build (30),
**~14%** capstone (28), **~10%** debug (21), **~8%** extend (16) — so "find a
bug" and "add to existing code" stop being rare (today: 1 debug, 0 extend).

## Design rules (unchanged, see [CONTRIBUTING](CONTRIBUTING.md))

- One new idea per puzzle; behaviour-first tests; randomized inputs.
- Every concept puzzle pins its lesson with a construct check, and is attacked by
  hand for sidesteps before it ships (`--sidestep` green).
- Each new **concept chapter carries at least one [D] and one [X]**, not only a
  [K] — that is how the variety lands throughout, not just inside projects.
- Debug puzzles ship genuinely failing starters; extend puzzles ship genuinely
  working starters with a missing feature.

---

## Tier A — intermediate language depth (ch. 17–24)

Build on functions (6), classes (9), generators (10), functional (14).

### 17 · Closures & scope (8)
- 17.1 Local vs global scope [C]
- 17.2 Functions remember: closures [C]
- 17.3 `nonlocal`: write the enclosing scope [C]
- 17.4 A counter factory (stateful closure) [C]
- 17.5 The late-binding loop trap [D]
- 17.6 Function factories (configurable functions) [C]
- 17.7 Add `reset()` to the counter factory [X]
- 17.8 Capstone: a memoize-by-hand cache [K]

### 18 · Decorators (10)  ⚠ needs `uses_decorator`
- 18.1 A function is a value [C]
- 18.2 Wrapping a function by hand [C]
- 18.3 `@decorator` syntax [C]
- 18.4 `functools.wraps`: keep the identity [C]
- 18.5 A timing decorator [C]
- 18.6 A decorator that takes arguments [C]
- 18.7 A decorator with state (call counter) [C]
- 18.8 Debug: the decorator drops the return value [D]
- 18.9 Add caching to an existing function via a decorator [X]
- 18.10 Capstone: a `@retry` decorator [K]

### 19 · Context managers (8)
- 19.1 `with`, revisited [C]
- 19.2 Why `with`: guaranteed cleanup [C]
- 19.3 `__enter__` / `__exit__` [C]
- 19.4 A timer context manager [C]
- 19.5 `contextlib.contextmanager` [C]
- 19.6 `suppress` / `closing` [C]
- 19.7 Debug: cleanup that never runs (bare open, no `with`) [D]
- 19.8 Capstone: a transaction (commit/rollback) context manager [K]

### 20 · Iterators & the protocol (8)
- 20.1 Iterable vs iterator [C]
- 20.2 `iter()` and `next()` [C]
- 20.3 `__iter__` / `__next__` [C]
- 20.4 A range-like iterator [C]
- 20.5 `StopIteration` [C]
- 20.6 Infinite iterators, taken finitely [C]
- 20.7 Make an existing class iterable [X]
- 20.8 Capstone: a paginator [K]

### 21 · itertools (10)
- 21.1 `chain`: glue iterables [C]
- 21.2 `count` / `cycle` / `repeat` [C]
- 21.3 `islice`: slice any iterable [C]
- 21.4 `takewhile` / `dropwhile` [C]
- 21.5 `groupby` [C]
- 21.6 `combinations` / `permutations` [C]
- 21.7 `product` [C]
- 21.8 `accumulate` [C]
- 21.9 Debug: `groupby` without sorting first [D]
- 21.10 Capstone: a run-length encoder [K]

### 22 · The collections module (10)
- 22.1 `namedtuple` [C]
- 22.2 namedtuple methods (`_replace`, `_asdict`) [C]
- 22.3 `deque`: fast at both ends [C]
- 22.4 `deque` as a queue / a stack [C]
- 22.5 `Counter`, deep (`most_common`, arithmetic) [C]
- 22.6 `defaultdict`, deep (list / int / set factories) [C]
- 22.7 `ChainMap` [C]
- 22.8 `OrderedDict` (`move_to_end`) [C]
- 22.9 Swap a hand-rolled tally for a `Counter` in existing code [X]
- 22.10 Capstone: an LRU cache with `OrderedDict` [K]

### 23 · dataclasses (8)
- 23.1 `@dataclass` basics [C]
- 23.2 Defaults and `field()` [C]
- 23.3 Generated `__repr__` / `__eq__` [C]
- 23.4 `order=True`: sortable for free [C]
- 23.5 `frozen=True`: immutable [C]
- 23.6 `__post_init__` validation [C]
- 23.7 Debug: the mutable default trap (`default_factory`) [D]
- 23.8 Capstone: model a small domain [K]

### 24 · Enums (6)
- 24.1 `Enum` basics [C]
- 24.2 `auto()` [C]
- 24.3 Access by name and by value [C]
- 24.4 `IntEnum` & comparisons [C]
- 24.5 Iterating members [C]
- 24.6 Capstone: a state machine driven by an `Enum` [K]

---

## Tier B — standard library & data (ch. 25–30)

### 25 · Type hints (8)  ⚠ needs an AST hint check
- 25.1 Annotating variables and functions [C]
- 25.2 `Optional` / `None` [C]
- 25.3 `list[int]`, `dict[str, int]` [C]
- 25.4 `Union` / `|` [C]
- 25.5 `Callable` and type aliases [C]
- 25.6 Hints don't run: clarity, not enforcement [C]
- 25.7 Annotate an existing untyped module [X]
- 25.8 Capstone: a typed config loader [K]

### 26 · pathlib & the filesystem (8)
- 26.1 `Path` basics [C]
- 26.2 Read / write text with `Path` [C]
- 26.3 Joining paths with `/` [C]
- 26.4 Parts: `name`, `suffix`, `parent` [C]
- 26.5 Listing & globbing [C]
- 26.6 `exists` / `is_file` / `mkdir` [C]
- 26.7 Debug: string paths that break on the OS separator [D]
- 26.8 Capstone: a directory report [K]

### 27 · More standard library (10)
- 27.1 `math` (sqrt, ceil, gcd) [C]
- 27.2 `statistics` (mean, median, stdev) [C]
- 27.3 `csv.reader` [C]
- 27.4 `csv.DictReader` / `DictWriter` [C]
- 27.5 `textwrap` [C]
- 27.6 `string` (constants, `Template`) [C]
- 27.7 `functools.partial` [C]
- 27.8 `functools.lru_cache` [C]
- 27.9 Speed up a slow function with `lru_cache` [X]
- 27.10 Capstone: a CSV summary tool [K]

### 28 · Numbers, decimals & bits (8)
- 28.1 int / float / `round` pitfalls [C]
- 28.2 Floating-point surprises [C]
- 28.3 `decimal.Decimal` for money [C]
- 28.4 `fractions.Fraction` [C]
- 28.5 Bitwise operators [C]
- 28.6 Bit flags [C]
- 28.7 Debug: the float-money rounding bug [D]
- 28.8 Capstone: a fixed-point money type [K]

### 29 · Sorting & comparison, deep (6)
- 29.1 `key` functions, revisited [C]
- 29.2 `operator.itemgetter` / `attrgetter` [C]
- 29.3 Multi-key sort (tuple keys) [C]
- 29.4 `reverse` and stability [C]
- 29.5 `functools.cmp_to_key` [C]
- 29.6 Capstone: a leaderboard sorter [K]

### 30 · Recursion & backtracking (8)
- 30.1 Recursion, revisited (base / recursive case) [C]
- 30.2 Sum & factorial recursively [C]
- 30.3 Recursion over nested lists [C]
- 30.4 Memoized recursion (Fibonacci) [C]
- 30.5 Tree traversal [C]
- 30.6 Backtracking: all subsets [C]
- 30.7 Debug: the missing base case (infinite recursion) [D]
- 30.8 Capstone: a recursive maze solver [K]

---

## Tier C — advanced (ch. 31–34)

### 31 · Bytes, text & encoding (6)
- 31.1 `str` vs `bytes` [C]
- 31.2 `encode` / `decode` [C]
- 31.3 UTF-8 & non-ASCII [C]
- 31.4 bytes: slicing & integer values [C]
- 31.5 Debug: mojibake (decoded with the wrong codec) [D]
- 31.6 Capstone: a hex dump [K]

### 32 · Testing your code (6)
- 32.1 `assert` & invariants [C]
- 32.2 Writing a test function [C]
- 32.3 `unittest.TestCase` [C]
- 32.4 Testing for exceptions (`assertRaises`) [C]
- 32.5 Debug: a test that can never fail [D]
- 32.6 Capstone: test a small module [K]

### 33 · Special methods, deep (8)
- 33.1 `__repr__` vs `__str__` [C]
- 33.2 `__len__` / `__getitem__` (sequence protocol) [C]
- 33.3 `__contains__` [C]
- 33.4 `__call__` [C]
- 33.5 `__hash__` & hashability [C]
- 33.6 Arithmetic dunders (`__add__`, `__mul__`) [C]
- 33.7 Make an existing class indexable [X]
- 33.8 Capstone: a small `Vector` type [K]

### 34 · Descriptors & attribute access (6, optional/expert)
- 34.1 `__getattr__` vs `__getattribute__` [C]
- 34.2 `property` recap as a descriptor [C]
- 34.3 A validating descriptor [C]
- 34.4 `__set_name__` [C]
- 34.5 Debug: a property with no setter that's assigned to [D]
- 34.6 Capstone: a typed-field descriptor [K]

**Concept-track subtotal (17–34): 142 puzzles** — 106 [C], 11 [D], 7 [X], 18 [K]
(136 without the optional ch.34).

---

## Tier D — projects (full apps; build / debug / extend / capstone heavy)

Each project is a short chapter that builds an app and ends in a low-guidance
capstone. Suggested placement reinforces a recently-taught topic. Every project
includes at least one **[D]** and one **[X]** step.

| | Project | Place after | Steps | Reinforces |
|---|---|---|---|---|
| **PR-A** | Task manager (CLI to-do, JSON store) | ch.18 | 6 | functions, json, dicts |
| **PR-B** | Text adventure (rooms, a state machine) | ch.24 | 6 | enums, dicts, control flow |
| **PR-C** | Sales report from CSV | ch.27 | 6 | csv, collections, sorting |
| **PR-D** | RPN calculator → expression evaluator | ch.21 | 6 | stacks/deque, errors |
| **PR-E** | Log-file analyzer | ch.26 | 5 | files, regex, Counter |
| **PR-F** | Card game: deck & hand ranking | ch.23 | 6 | dataclasses, sorting, enums |
| **PR-G** | Contact book (CRUD + persistence) | ch.26 | 6 | pathlib, json, classes |
| **PR-H** | Markdown → HTML mini-converter | ch.21 | 6 | strings, regex, state |
| **PR-I** | Bank II: accounts, transfers, statements | ch.22 | 6 | classes, errors, collections |
| **PR-J** | Inventory / warehouse | ch.23 | 6 | dataclasses, dicts, reports |

### PR-A · Task manager (6)
- A.1 `Task` (title, done flag) [B]
- A.2 `TaskList`: add / list [B]
- A.3 Mark done & filter by status [B]
- A.4 Add due dates and sort by them [X]
- A.5 Debug: the "completed" filter returns everything [D]
- A.6 Capstone: save / load the list as JSON [K]

### PR-B · Text adventure (6)
- B.1 `Room` with exits (a `dict` of direction → room) [B]
- B.2 Move between rooms [B]
- B.3 Game state as an `Enum` (PLAYING / WON / LOST) [B]
- B.4 Add a pick-up-able inventory [X]
- B.5 Debug: a one-way door (exits not symmetric) [D]
- B.6 Capstone: a scripted adventure loop [K]

### PR-C · Sales report from CSV (6)
- C.1 Parse rows with `csv.DictReader` [B]
- C.2 Revenue per product (`Counter` / `defaultdict`) [B]
- C.3 Top-N sellers (sorted) [B]
- C.4 Add a date-range filter [X]
- C.5 Debug: totals off by the header row [D]
- C.6 Capstone: a formatted summary report [K]

### PR-D · RPN calculator → expression evaluator (6)
- D.1 Tokenize an RPN string [B]
- D.2 Evaluate with a stack (`deque`) [B]
- D.3 Operators + errors (empty stack, div-by-zero) [B]
- D.4 Add `**` and unary minus [X]
- D.5 Debug: operands popped in the wrong order (`a-b` vs `b-a`) [D]
- D.6 Capstone: infix → RPN (shunting-yard), then evaluate [K]

### PR-E · Log-file analyzer (5)
- E.1 Read lines, parse each with a regex [B]
- E.2 Count by status code (`Counter`) [B]
- E.3 Busiest hour [B]
- E.4 Debug: a regex that silently misses 404s [D]
- E.5 Capstone: a top-paths + errors report [K]

### PR-F · Card game: deck & hand ranking (6)
- F.1 `Card` (rank, suit) as an ordered dataclass [B]
- F.2 `Deck`: build & shuffle [B]
- F.3 Deal & sort a hand [B]
- F.4 Add straight detection to the ranker [X]
- F.5 Debug: ace-low straight (A-2-3-4-5) miscounted [D]
- F.6 Capstone: rank & compare two hands [K]

### PR-G · Contact book (6)
- G.1 `Contact` (name, email, phone) [B]
- G.2 `Book`: add / find by name [B]
- G.3 Update & delete (full CRUD) [B]
- G.4 Add partial-name search [X]
- G.5 Debug: delete removes the wrong contact [D]
- G.6 Capstone: persist to JSON on disk (`pathlib`) [K]

### PR-H · Markdown → HTML mini-converter (6)
- H.1 Headings (`#` → `<h1>`) [B]
- H.2 Bold & italic (inline regex) [B]
- H.3 Unordered lists [B]
- H.4 Add links `[text](url)` [X]
- H.5 Debug: nested emphasis mangled [D]
- H.6 Capstone: convert a whole document [K]

### PR-I · Bank II: accounts, transfers, statements (6)
- I.1 `Account` with balance & history [B]
- I.2 Deposit / withdraw (raise on overdraft) [B]
- I.3 `Bank`: open accounts, look up by id [B]
- I.4 Add a transfer between accounts [X]
- I.5 Debug: transfer credits the payee but never debits the payer [D]
- I.6 Capstone: a printed statement per account [K]

### PR-J · Inventory / warehouse (6)
- J.1 `Product` (sku, name, qty, price) [B]
- J.2 `Warehouse`: stock in / out [B]
- J.3 Low-stock report [B]
- J.4 Add reorder thresholds & suggestions [X]
- J.5 Debug: stock can go negative (no guard) [D]
- J.6 Capstone: a valuation + reorder report [K]

**Projects subtotal: 59 puzzles** — 30 [B], 9 [X], 10 [D], 10 [K].

---

## Totals

| Source | Puzzles | of which [D] | of which [X] | of which [K] |
|---|---:|---:|---:|---:|
| Concept chapters 17–34 | 142 | 11 | 7 | 18 |
| Projects PR-A…PR-J | 59 | 10 | 9 | 10 |
| **New total** | **201** | **21** | **16** | **28** |

Course after: **142 → ~343 puzzles, 16 → 44 chapters** (18 concept + 10 project
chapters added). A ~100-puzzle first slice ≈ Tier A (68) + ~5 projects; the full
set is ~201 (195 without the optional ch.34).

## Engine work this unlocks (do before the chapter that needs it)

- **`uses_decorator(name)`** — liveness-anchored, for ch.18 (today `@property` is
  forced with a reflection oracle; decorators in general have no check). Without
  it, the decorator lesson is sidesteppable (wrap by hand, no `@`).
- **An AST hint check** for ch.25 — type hints are erased at runtime, so behaviour
  can't see them; needs a `tests.py` AST check via `T.tree()`/`require_live`'s
  static seam (annotations aren't ablatable, so AST-presence like `uses_lambda`).
- **`uses_call`/behavioural oracles already cover** itertools, collections,
  dataclasses (`is_a` + generated dunders), enums, pathlib, recursion
  (`uses_call(self)` liveness, as in 6.9). Confirm per puzzle with `--sidestep`.
- Consider promoting **[X] "extend"** to a first-class `kind` (vs. reusing
  `build`) if standalone extend puzzles outside projects become common — small
  `PROJECT_KINDS` + audit change, plus a SCHEMA note.

## Sidestep watch (per tricky chapter)

The new topics each have an obvious dodge. Plan the defense **before** authoring,
and pin it in `dodges.py` (the workflow in [CONTRIBUTING](CONTRIBUTING.md)).

| Chapter | The obvious dodge | Defense |
|---|---|---|
| 17 closures | a global / instance attribute instead of a closure | two factory instances must be independent (behavioural) |
| 18 decorators | wrap by hand, never write `@` | `uses_decorator(name)` (new, liveness-anchored) |
| 19 context managers | `try/finally` instead of `with`; bare `__exit__` that no-ops | `uses_with` + a probe that `__exit__` runs **on an exception** |
| 20 iterators | return a `list`, not an iterator | behavioural `iter(x) is x` + `next()` advances; reject a list |
| 21 itertools | re-implement the tool by hand | `uses_call_over_param("chain"/"groupby"/…)` over the input |
| 22 collections | a plain `dict`/`list` doing `Counter`/`deque`'s job | `is_a(Counter)` / `uses_call("deque")` + the type's own methods |
| 23 dataclasses | a hand-written class with the same fields | reflection: `dataclasses.is_dataclass(cls)` + generated `__eq__` |
| 24 enums | plain module constants / ints | members must be `Enum` instances (`is_a`) |
| 25 type hints | omit the hints (no runtime effect) | AST check: annotations present on params/return |
| 28 decimals | `float` instead of `Decimal` | `is_a(Decimal)` + exact-equality cases `float` can't represent |
| 30 recursion | an iterative loop | `uses_call(self)` liveness (as in 6.9) |
| 33 dunders | an external function instead of the dunder | drive it through the operator (`len(x)`, `x[i]`, `x + y`) |

## Sequencing & dependencies

```
6 functions ─┬─> 17 closures ─> 18 decorators ─> PR-A
             └─> 14 functional
9 classes ───┬─> 15 advanced ─> 23 dataclasses ─> PR-F / PR-J
             ├─> 33 dunders ─> 34 descriptors
             └─> 20 iterators
10 generators ─> 21 itertools ─> PR-D / PR-H
11 stdlib ───> 22 collections / 24 enums / 27 stdlib+ ─> PR-B / PR-C / PR-I
8 files ─────> 26 pathlib ─> PR-E / PR-G
```

Roughly: ship Tier A first (it has the highest "new language power" per puzzle
and unlocks the most projects), interleave PR-A/PR-D early for variety, then
Tiers B–C as breadth.

## Open decisions

1. **Scope:** ~100 (Tier A + ~5 projects) vs the full ~201? 
2. **`extend` kind:** new `meta.kind`, or keep using `build`/full-starter lessons?
3. **Tier C depth:** is ch.34 (descriptors) too advanced for this course's
   audience, or a good "expert" capstone chapter?
4. **Async / concurrency:** intentionally omitted (the script/import runner and
   stdlib-only constraint make it awkward) — keep omitted?
