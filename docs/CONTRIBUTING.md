# Contributing to PyQuest

Thanks for helping grow the course. PyQuest is a terminal-run Python tutorial:
a learner reads a brief, writes code in their own editor (`work.py`), and runs
one stateless command to check it. This guide is the detailed collaboration
reference — how the project is built, how to add and harden content, and the one
discipline that makes the whole thing work.

Read in this order:

| Doc | What it gives you |
|---|---|
| [README.md](../README.md) | the learner's view + the roadmap |
| [ARCHITECTURE.md](ARCHITECTURE.md) | the design and its layers |
| [SCHEMA.md](SCHEMA.md) | the exact file formats and every `T` helper |
| [architecture/toolkit.md](architecture/toolkit.md) | the checker (`T`), liveness, construct checks |
| [architecture/audit.md](architecture/audit.md) | the audit: conformance, the adversaries, the guards |
| **this file** | how to collaborate: setup, workflow, the anti-sidestep craft |

Most contributions are **new puzzles** — files on disk, zero engine code. A
smaller set touch the **engine/toolkit** (a new validation check, a command, a
visual). Both paths are covered below.

---

## The one idea behind everything

> A puzzle must make its **lesson** unavoidable, not just its **output**.

A program that prints the right answer while skipping the concept the puzzle
teaches is a **sidestep** (also "dodge"). Answering an order-of-operations task
with `print(7 * 2)` is correct output, absent reasoning. Closing sidesteps —
making the lesson the *only* way to pass — is the craft of this project, and
most of this guide.

Everything else follows five principles ([ARCHITECTURE.md](ARCHITECTURE.md) has
the long form):

1. **Stdlib only, Python 3.8+.** No third-party dependencies, ever.
2. **Behavioral checks by default.** Tests assert what code *does*, never its
   raw source text. The single sanctioned exception is the liveness-checked
   construct checks (`T.uses_*` / `T.line_*`), and a puzzle whose lesson *is* a
   construct must say so in its brief.
3. **The lesson is unavoidable.** Randomized inputs defeat hardcoding; liveness
   defeats dead-code decoration; anchored construct checks defeat "compute it a
   different way."
4. **Layers never bleed.** content (`chapters/`, `content.py`), input
   (`inputs.py`), checking (`toolkit/`, `checker.py`), state (`state.py`),
   visuals (`theme.py`, `render.py`). Colours and glyphs live *only* in the
   visual layer.
5. **State is recoverable.** Every JSON write is atomic; an unreadable file is
   moved aside, never overwritten.

---

## Setup

No installation. From the repo root:

```bash
python3 start.py              # session + menu (the entry point)
python3 start.py status       # progress + the learner verbs (begin, check, next, hint, ...)
python3 start.py setup        # optional: install the `pq ...` shell shortcuts
```

Open the repo in a **GitHub Codespace** (Code → Codespaces) to run with no local
setup — the devcontainer ships a recent Python. Shell shortcuts ship for zsh,
bash, and PowerShell; everything also works by prefixing `python3 start.py`.

---

## The audit *is* the test suite

There is no pytest layer. [`tools/audit.py`](../tools/audit.py) is the test
suite and the executable source of truth. It reports per-puzzle, so to focus on
one puzzle read its line.

| Command | What it checks | When to run |
|---|---|---|
| `python3 tools/audit.py` | conformance: every `solution.py` passes its `tests.py` | quick check |
| `python3 tools/audit.py --sidestep` | conformance **+** the adversaries **+** the static guards | **before every commit** |
| `python3 tools/audit.py --engine` | execution-guard & toolkit self-tests (`audit_selftest.py`) | after touching `engine/` |
| `python3 tools/audit.py --lessons` | coverage table: which construct each puzzle pins | auditing the attack surface |
| `python3 tools/audit.py --prove-checks` | strips the construct layer, confirms a pinned dodge then slips past (proves the check is load-bearing) | after adding/altering a check |

The current green bar:

```
142/142 conformance, 0/142 sidesteppable, 0/142 unguarded lessons,
40/40 engine self-tests
```

**Never weaken a check to make the audit pass.** Fix the root cause. A green
audit with a hollowed-out check is worse than a red one.

---

## Where each change goes

```
start.py            # entry point
engine/             # the app (see architecture/engine-core.md)
  toolkit/          # the T tester: a new validation helper goes here
  commands/         # the verbs: a new command goes here + a registry row + a dispatch line
chapters/NN_x/MM_y/ # one puzzle per folder — pure data, no engine code
tools/audit.py      # conformance + anti-sidestep + the guards + the self-test driver
docs/architecture/  # hand-maintained diagrams — keep in sync when you rewire structure
```

A **new puzzle** is files on disk, nothing else. A **new check / command /
visual** touches the matching area plus its self-test and diagram (below).

---

## Anatomy of a puzzle

One folder under `chapters/NN_chapter/MM_title/`:

| File | Required? | Purpose |
|---|---|---|
| `brief.md` | yes | the prompt the learner reads |
| `starter.py` | yes | seeds `work.py` |
| `tests.py` | yes | `check(T)` — runs the code, asserts behavior, judges the construct |
| `hints.md` | yes | exactly **3** hints for a lesson puzzle (a project puzzle may carry **0–3**) |
| `solution.py` | yes | the reference answer; must pass `tests.py` (conformance) |
| `meta.json` | yes | `id`, `title`, `chapter`, `mode` (`script`\|`import`), optional `concept`/`why`, optional `kind` |
| `reference.md` | if `concept` | the textbook entry (the audit requires it when a `concept` is set) |
| `dodges.py` | optional | `DODGES = [(label, source), ...]` — known sidesteps pinned as permanent regressions |

`mode` drives checking: **`script`** runs `work.py` as a subprocess and compares
stdout; **`import`** imports it and calls its functions/classes. A puzzle with a
`concept` teaches a construct and appears in the textbook; a drill or capstone
omits `concept` and stays out of both. Full field reference:
[SCHEMA.md](SCHEMA.md).

---

## Authoring a puzzle, step by step

1. **Name the one lesson** the puzzle must force — the construct, not the
   output. Write it down; every later decision serves it.
2. **Write the brief** in house style: concept from scratch → a tiny worked
   example → the task → a "Done when" list of observable outcomes.
3. **Assert behavior first.** In `tests.py`, drive the code (`T.run` / `T.call`
   / `T.make`+`T.method`) and check results (`T.eq` / `T.approx` / `T.true` /
   `T.raises`, ...). Include at least one edge case (empty, zero, negative,
   absent).
4. **Randomize inputs** wherever you can, with `engine.inputs`
   (`random_int`, `random_word`, `Case`). Randomization is what stops a lookup
   table; make outputs vary across cases so a stale value can't match.
5. **Pin the lesson with a construct check** — *after* the behavior asserts
   (liveness replays the recorded runs, so they must exist first). Choose the
   narrowest check that fits (next section).
6. **Write `reference.md`** if the puzzle carries a `concept`.
7. **Confirm `solution.py` passes**, then run `python3 tools/audit.py
   --sidestep`. Green or it doesn't ship.

The starter for a **`debug`** puzzle must really fail the tests (the audit
rejects a starter that already passes — no bug, no lesson).

---

## Choosing a construct check

Reach for a construct check only when the answer can be produced with a
*different tool* than the lesson. Prefer the strongest available, in this order:

**1 — A behavioral assert, if the lesson is observable.** Most lessons are. A
`__str__` that must format a certain way, a generator that must be lazy
(`T.is_generator`), an exception that must be raised (`T.raises`), a function
that must not mutate its input (`T.does_not_mutate`). No construct check needed.

**2 — A liveness-anchored construct check, if the lesson is a construct.** These
only count a node that is *live* — ablating it must change behavior on the
recorded inputs, so dead-code decoration can't satisfy them
([liveness](architecture/toolkit.md) explains the model):

| Group | Checks |
|---|---|
| control flow | `uses_if`, `uses_nested_if`, `uses_for`, `uses_while`, `uses_loop`, `uses_break`, `uses_continue`, `uses_try`, `uses_raise`, `uses_with`, `uses_with_open`, `uses_unpacking` |
| expressions / data | `uses_op`, `uses_in`, `uses_boolop`, `uses_comprehension`, `uses_index`, `uses_negative_index`, `uses_slice`, `uses_fstring`, `uses_dict`, `uses_set`, `assigns_a_variable`, `reassigns_a_variable`, `uses_print` |
| calls / imports | `uses_call`, `uses_import` |
| fixed-output shape | `line_only_literals`, `line_shape`, `line_uses_op`, `print_expr`, `print_has_min_args`, `print_uses_keyword`, `prints_computed`, `prints_name` |

**3 — Anchor a higher-order function to its role.** A bare `uses_call("map")`
is satisfied by a *live but decorative* wrapper — `map(lambda v: v, [x*x for x
in nums])`, where a comprehension did the work and `map` is a no-op the ablation
still calls live. Use the anchored variants instead:

| Check | Forces |
|---|---|
| `uses_call_over_param(name)` | the HOF runs over the input parameter, not a comprehension/literal that pre-computed the answer (map/filter/reduce) |
| `uses_call_on_collection(name)` | script-mode variant (no parameter): the arg is a real collection, not `sum([total])` |
| `uses_predicate_over_param(name)` | `any`/`all` consume a comprehension over the input, not `any([flag])` |
| `uses_lambda_arg(name, keyword/pos)` | a lambda sits in the sort key / predicate / map slot, not a decoy lambda elsewhere |

**4 — Pin an AST-only check to a name or role.** A few constructs have no
sentinel liveness can substitute (a lambda isn't callable when ablated; a
default value, a `yield`, a `class` don't have a clean stand-in). These fall
back to AST presence, which a *decoy* satisfies — so always pin them:

- `uses_lambda` → pair it with a behavioral or `uses_lambda_arg` anchor (a
  returned lambda's `__name__` is `"<lambda>"`; a nested `def`'s is its name).
- `uses_default_param("__init__")`, `uses_yield("gen")`, `uses_class("Dog")` →
  name the function/class the lesson lives in, so a decoy elsewhere can't stand
  in.

**5 — A runtime reflection / spy oracle, when no check fits.** Some lessons are
a *mechanism* with no construct check and no plain behavioral difference — the
class hierarchy chapter is full of them. Inspect the runtime objects instead of
the source:

- `@property` → `isinstance(getattr(Cls, "area"), property)`.
- inheritance over copying → `Sub.method is Base.method`.
- `super().__init__` actually runs → spy on the parent `__init__` and assert it
  was called.
- `classmethod` uses `cls(...)` → a subclass's factory returns the subclass.

This is reflection on runtime objects, not source text, so it stays within the
behavioral rule.

**6 — A prescribed-expression `line_*` check, for fixed-output puzzles** whose
lesson is a specific expression shape (where synth — see below — could otherwise
re-derive the constant a different way).

When you need something none of these express, compose it in `tests.py` from
`T.tree()` + `T.require_live(...)` (audited parts; see SCHEMA), and ship a
`dodges.py` entry alongside it.

---

## The anti-sidestep discipline

This is the heart of the project. Three layers defend every puzzle.

### The automated suite (`--sidestep`)

Four **generic adversaries** build intentionally-wrong programs from a recording
of the solution and require them to fail:

- **replay / chaff-replay** — answer from a lookup table, computing nothing
  (chaff adds a dead function stuffed with every construct). *Beaten by:*
  randomized inputs; liveness.
- **synth / named-synth** — for a fixed-output script, re-derive the constant
  with arithmetic the brief never asked for. *Beaten by:* a `line_*` check.

Two **static guards** cover what the adversaries structurally can't model on
varying-output puzzles:

- **lesson-guard** — flags a puzzle that teaches a `concept`, varies its output,
  and pins *no* construct check. Clear it by adding a check, or record the id in
  `GUARDED_OK` (in `audit.py`) with a written reason.
- **wrapper-guard** — flags a bare `uses_call` for a wrappable HOF
  (`sum`/`min`/`max`/`any`/`all`/`map`/`filter`/`reduce`) with no anchored
  variant; such a call is defeatable by the live no-op wrapper above. Clear it
  with an anchored check (group 3), or record it in `WRAPPER_OK`.

### The manual pass

The generic suite can't imagine hand-crafted dodges. After adding or changing a
puzzle, attack it yourself: name the lesson, write candidate impostors that
reach the right output a *different* way, and run each against the real tests
with fresh randomness over several attempts (a dodge that passes even once is a
breach). Common hand-dodges: the wrong tool with the right answer (`n % 6 == 0`
for "divisible by 2 *and* 3"); the required construct parked in dead code; a
broad check satisfied by an unrelated instance; the lesson's shortcut
re-implemented by hand.

### Closing and pinning a sidestep

When you (or the audit) find a passing impostor:

1. **Tighten the defense** — randomize inputs, switch to a liveness-anchored or
   anchored-HOF check, pin the expression with `line_*`, or add a reflection
   oracle. Prefer the *narrowest* fix that closes the hole without rejecting an
   honest variant.
2. **Pin the exact dodge** in that puzzle's `dodges.py` as a `(label, source)`
   pair, so the audit fails forever if it ever passes again.
3. **Re-run** `--sidestep` (green) and `--prove-checks` (your new check is shown
   load-bearing, or the dodge is caught behaviorally and you understand why).

Don't pin a dodge you can't actually block — if a variant is a legitimate,
equivalent alternative, accept it and say so in `dodges.py` rather than shipping
a red audit.

### Object / OOP puzzles

`make` / `method` / `attr` record an **object tape** that liveness replays, so
`uses_class` and in-method checks are liveness-judged there too. If a test
touches an object the tape never made (built via an operator, a subclass, or a
direct `Cls.method(...)`), the tape marks itself unreplayable and liveness
degrades safely to AST presence — so those puzzles lean on `uses_class(name)`,
randomized arguments, and the reflection/spy oracles from group 5.

---

## Hardening an existing puzzle

The same loop, applied to content already in the tree:

1. Read its `brief.md` + `solution.py` + `tests.py`; name the one lesson.
2. Write impostors to a scratch file and run them against the real tests with
   fresh randomness. The audit's `impostor_passes(p, src)` is the harness.
3. For each breach: tighten the check, then pin the dodge.
4. Re-run `--sidestep`, `--prove-checks`, and `--engine`. All green.

---

## Contributing to the engine / toolkit

A new validation helper is the most common engine contribution. Adding one is a
five-point change, each pinned against drift:

1. **The check** → a method on the matching mixin in `engine/toolkit/`
   (construct checks live in `constructs.py`; assert it through liveness via
   `self._require_live(...)` unless the construct genuinely can't be ablated).
2. **The self-test** → a `t_*` case in `tools/audit_selftest.py` proving it
   passes honest code and rejects the sidestep, then add it to the run list.
   Verify with `--engine`.
3. **The lesson-guard registry** → add the method name to `LESSON_CHECKS` in
   `audit.py`, so the guard counts it and `--prove-checks` strips it.
4. **The wrapper-guard** → if it anchors a HOF, add it to `_ANCHORED_CHECKS`.
5. **The diagrams** → update `docs/architecture/toolkit.md` (and `audit.md` if
   you touched the guards). A diagram that lies is worse than none.

A new **command** follows the same shape: a `commands/` module + a
`commands/registry.py` row + one `app.py` dispatch line + a self-test; see
[architecture/commands.md](architecture/commands.md).

---

## Projects and translations

- **Projects** (`chapters/NN_project_*/`) apply the lessons instead of teaching
  a construct: a few steps building an app to a low-guidance capstone, including
  `debug` puzzles that ship broken code to fix. Their puzzles set `kind`
  (`build`/`debug`/`capstone`), omit `concept`, and keep tests behavioral with
  randomized inputs — that, not a construct check, is what keeps them
  sidestep-proof. See [SCHEMA.md#projects](SCHEMA.md).
- **Translations** — the i18n plumbing is done (`lang/`, validated by
  `python3 tools/check_pack.py`). Language packs are welcome; nothing is
  translated yet.

---

## Commits and pull requests

- Small commits, **terse imperative subjects** ("Harden ch.14 graders", not "I
  hardened the graders"). One idea per puzzle, one concern per module.
- **No decorative emojis** in code, comments, or commit messages — the
  deliberate UI glyph set in `engine/theme.py` is the only exception, and those
  characters live only in the visual layer.
- Work is attributed to its **human author**; no AI co-author trailers or
  generated-with lines.
- Keep the `docs/architecture/` diagrams in sync in the *same* change that
  rewires structure.
- A **green audit** — `--sidestep` and `--engine` — is required to merge.

### Pre-submit checklist

- [ ] `solution.py` passes; behavior asserts cover an edge case.
- [ ] Inputs randomized; outputs vary across cases.
- [ ] The lesson is pinned with the narrowest fitting check (or justified in
      `GUARDED_OK` / `WRAPPER_OK`).
- [ ] You attacked it by hand; every breach is closed and pinned in `dodges.py`.
- [ ] `--sidestep` green; `--engine` green if you touched `engine/`;
      `--prove-checks` shows new checks load-bearing.
- [ ] `reference.md` present if the puzzle has a `concept`.
- [ ] Diagrams updated if structure changed.
