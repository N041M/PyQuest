# Architecture

The design reference for PyQuest — read it before adding a feature, a puzzle,
a command, or a coat of paint. Its job is to keep PyQuest **modular** so it
never collapses back into one monolithic file, and so new capabilities
(randomized inputs, new themes, new question types) slot in cleanly. For file
formats, see [SCHEMA.md](SCHEMA.md); for usage, see the [README](README.md).

If a change you are about to make does not fit one of the modules below, that
is a signal to discuss the boundary — not to staple the code onto the nearest
file.

## 1. What PyQuest is (and is not)

PyQuest is a terminal-run Python course. The learner reads a brief, writes code
in a workspace file in their own editor, and runs short, stateless commands to
validate it and progress.

- It is **not** a full interactive TUI. The only interactive surface is the
  optional `begin` launcher menu (set up shortcuts, pick a level), shown
  *before* puzzles. The puzzle loop and every other command run once and exit.
- It validates **behavior**, never source text — with rare, explicit exceptions
  where the lesson *is* a construct (e.g. commenting a line out).
- Standard library only. No third-party dependencies. Runs on a fresh Python 3.

These are invariants. See §3.

## 2. Separation of concerns

Five concerns must never bleed into each other. Each owns one question:

| Concern | Owns the question | Module |
|---|---|---|
| **Content** | "What is this puzzle?" | `content.py` |
| **Input** | "What do we feed the solution?" | `inputs.py` |
| **Checker/Tester** | "Is the solution correct (and good)?" | `toolkit.py`, `checker.py` |
| **State** | "Where is the learner up to?" | `state.py` |
| **Visuals** | "How does it look on screen?" | `theme.py`, `render.py` |

The flow of a `check` reads left to right:

```
content (the question)  ->  inputs (provide stdin/args)  ->  checker + toolkit
(run the solution, validate)  ->  state (record progress)  ->  render (show result)
```

The **input provider** generates what the solution receives; the **same provider
hands the expected basis to the checker**, so a single source decides both the
question's inputs and the answer's validation. This is what makes randomized
inputs (§8) a drop-in: swap the provider, and both the run and the check follow.

Visuals are a separate layer end to end: no module outside `theme.py`/`render.py`
contains a colour code, a box character, or layout math. A restyle touches only
those two files.

## 3. Invariants (do not break these)

1. **Behavioral validation.** Check what the code *does*, not how it reads. The
   only exception is a puzzle whose concept is a source construct; it must use
   `toolkit` construct-checks (`prints_computed`, `reassigns_a_variable`, …) and
   say so in its brief.
2. **No feature before its lesson.** A puzzle may only require concepts taught in
   earlier puzzles. (Strings can't use lists; functions don't exist until Ch6.)
3. **One new idea per puzzle**, then 1–2 reinforce it.
4. **Every brief**: concept from scratch → tiny worked example → the task → what
   "done" looks like. Define a term the first time it appears.
5. **At least one edge case** in every puzzle's tests.
6. **Distinct, plain-language failures.** A missing function, a syntax error, a
   wrong result, and a crash each produce a different message that points at the
   concept. Never dump a raw traceback.
7. **Fresh load every check.** Re-read/re-import the solution each run so stale
   state can never cause a false pass or fail.
8. **Stateless commands, with two scoped exceptions.** Every command runs once
   and exits — no prompts, loops, or live redraw — *except* (a) the `begin`
   launcher menu, which is interactive by design (it loops reading a choice)
   and runs before puzzles, and (b) bare `goto`, which shows the puzzle list
   and reads ONE id before exiting. Both degrade to a plain print when stdin
   is not a terminal, so they never block pipes or tests. The shell-level
   `reset` confirmation (outside `play.py`) is the only other prompt.
9. **Stdlib only.**
10. **Progress is recoverable.** `reset` is a true reset; saving never silently
    destroys the learner's code without it living in `answers.json`. All JSON
    saves are atomic (temp file + rename), and an unreadable progress/answers
    file is moved aside as `<name>.corrupt` — never overwritten.

## 4. Module map

The package lives under `pyquest/`. `play.py` at the root is a thin launcher.
Dependencies only ever point **downward** in this list (no cycles):

```
config.py     constants & paths; terminal width; settings.json (current user +
              theme). Depends on nothing.
theme.py      selectable palettes (THEMES), glyphs, paint(), the logo. The
              visual identity; apply_theme() switches in place.
render.py     drawing primitives: box, banner, bar, header, wordmark, rule,
              field, wrap, indent, cli(). Pure look; depends on theme + config.
content.py    Puzzle/Chapter model + discovery + loaders (brief, hints,
              solution, starter, meta, tests). "The structured question."
inputs.py     input providers: random_word/int + the Case seam. Hands the same
              data to the runner and the checker. "The input automizer."
state.py      per-user progress + answers (users/<name>/...) + workspace
              (work.py) lifecycle: seed, archive, switch, reset, users.
toolkit.py    the T object handed to each tests.py: run/import, behavior
              assertions, construct checks, performance helpers. "The tester."
checker.py    orchestrates one check: load tests, build T, run check()/bonus(),
              translate failures into the four categories, render pass/fail.
commands.py   the verbs (status, map, goto, next, skip, retry, hint, solution,
              mode, reset, help) — compose state + content + render + checker.
app.py        argv dispatch + main().
```

Rules for the map:

- A new **command** → `commands.py` (+ one dispatch line in `app.py`, + a shell
  shortcut). Nowhere else.
- A new **screen/visual** or restyle → `theme.py` / `render.py` only.
- A new **validation helper** → `toolkit.py`.
- A new **input strategy** (e.g. randomized) → `inputs.py`; nothing else changes.
- A new **puzzle** → files on disk only (see §6); zero code changes.

## 5. The visual layer

`theme.py` holds the swappable identity: the colour palette (named roles, not raw
codes scattered around), the glyph set (`OK`, `CUR`, `ARROW`, …), the logo, and
`paint()`. `render.py` holds reusable drawing primitives that consume the theme.

To restyle PyQuest you edit those two files and nothing else. Screen *composition*
(which fields a card shows) lives with the command that owns the screen, but it
must build that screen only from `render` primitives — never by emitting raw
escape codes or box characters itself.

Colour auto-disables when output is not a TTY or `NO_COLOR` is set. Frames size to
the live terminal width (capped for readability). Both behaviours live in the
visual layer; no other module knows about them.

## 6. Adding a puzzle (no code change)

A puzzle is a folder `chapters/NN_chapter/MM_title/` with six files:

- `brief.md` — what the learner reads (house style, §3.4).
- `starter.py` — the seed loaded into the chapter's `work.py`.
- `tests.py` — defines `check(T)` and optionally `bonus(T)` (§7).
- `hints.md` — three hints, escalating, separated by `---`.
- `solution.py` — reference answer (+ `why` lives in `meta.json`).
- `meta.json` — `id`, `title`, `chapter`, `concept`, `mode`, `why`.

The engine discovers it automatically. See [SCHEMA.md](SCHEMA.md) for exact
formats.

## 7. How validation works (the tester contract)

`tests.py` defines `def check(T)`. `T` (from `toolkit.py`) both runs the learner's
code and raises *translated* failures, so messages stay friendly.

- **The execution guard.** Every execution of learner code — importing the
  file, calling a function, timing it — goes through one guard in `toolkit.py`
  that blanks stdin (a stray `input()` fails fast instead of hanging), captures
  stdout into `T.printed`, enforces the wall-clock timeout (infinite loops fail,
  even inside the learner's own `except Exception`), translates `exit()` /
  `sys.exit()` (learner code cannot kill the checker), and chdirs into a
  throwaway sandbox (file I/O cannot touch the project). Script mode gets the
  same isolation via its subprocess (timeout + sandbox cwd). Never invoke
  learner code outside this guard; `python3 audit.py --engine` pins these
  guarantees.
- **Behavior:** `T.run(stdin=..., files=...)` (script mode) or
  `T.call(name, ...)` (import mode), then `T.eq / T.true / T.is_a / T.raises`.
- **Files (Ch8+):** seed fixtures with `T.run(files={...})` or `T.put_file`;
  assert what the learner's code wrote with `T.file(name)` — all inside the
  sandbox, never the project tree.
- **Objects (OOP chapters):** `T.make("ClassName", args)` instantiates,
  `T.method(obj, "name", args)` calls, `T.attr(obj, "name")` reads — each with
  translated failures.
- **Mutation lessons:** `T.does_not_mutate(name, *args)` calls the function and
  requires the arguments back unchanged (the `sorted` vs `.sort()` distinction).
- **Many valid answers:** assert properties, not one value — `T.approx` (works
  inside lists/tuples/dicts), `T.any_of`, `T.unordered`, or `T.true(<invariant>)`.
- **Integrity:** when output alone could be typed in — or the topic construct
  dodged with another tool — require the real thing. `T.prints_computed(min_calls=)`,
  `T.uses_op("+"/"*"/...)`, `T.uses_print`, `T.print_uses_keyword`,
  `T.print_has_min_args`, `T.assigns_a_variable`, `T.reassigns_a_variable`,
  `T.uses_if/uses_while/uses_for/uses_loop/uses_break/uses_continue`,
  `T.uses_fstring`, `T.uses_index/uses_negative_index/uses_slice(step=)`,
  `T.uses_in`, `T.uses_comprehension(with_if=)`, `T.uses_call(name)`,
  `T.uses_dict/uses_set/uses_unpacking`, `T.uses_try`, `T.uses_raise`,
  `T.uses_with`, `T.uses_import(module)`, `T.uses_class`, `T.uses_yield`,
  `T.uses_lambda` (staged for Ch8+),
  `T.source()`. Require the *kind* of construct, not one exact spelling, so
  legitimate variations still pass (e.g. an `elif` puzzle accepts nested `if`s).
- **Performance (optional, advisory):** a `def bonus(T)` runs only after the answer
  is accepted and never blocks progress — a `⚡` line. Use `T.time_call` or, better,
  `T.scales` (a doubling experiment). Timing is best-effort; keep budgets loose.
  You cannot prove big-O automatically; this catches gross inefficiency, which is
  what LeetCode-style timing does too.

Authoring rules: never inspect source except via the integrity helpers; include an
edge case; prefer `because=` to name the concept; for non-unique answers assert
properties, not a fixed value.

## 8. Randomized inputs

The seam is `inputs.py`. The shape:

- A puzzle (or its `tests.py`) asks an **input provider** for one or more cases.
- The provider returns a structured case: the `stdin`/args to feed the solution
  **and** the data the checker needs to compute the expected result.
- `check(T)` feeds the case to `T.run`/`T.call` and validates against the
  provider's expectation — so hardcoding the answer is impossible because the
  inputs change per run.

Because the provider feeds both the run and the check from one place (§2), turning
a fixed puzzle into a randomized one means writing a provider and pointing the test
at it — no engine change. Fixed-output, no-input puzzles keep using construct
checks (§7) for integrity instead.

**In use now.** `inputs.py` provides `random_word` / `random_int`, and every
input-reading puzzle in Chapters 1–2 (e.g. 1.10, 1.11, all of Ch2) feeds
randomized cases and computes the expected result in `tests.py`. Hardcoding the
answer is therefore impossible there. The structured-provider/`Case` flow is
live in Chapter 6+: import-mode tests build a list of `Case`s (fixed edge cases
plus randomized ones), feed `case.args` to `T.call`, and validate against
`case.expect` — one source for both the input and the expectation.

**Anti-sidestep policy.** Every puzzle must make its *lesson* unavoidable, not
just its output: randomized inputs defeat hardcoding; construct checks (§7)
defeat solving with a different tool (e.g. `.find()` instead of `in`, an
`if b == 0` instead of `except ZeroDivisionError`, a loop instead of
recursion); and behavioral traps catch over-broad code (e.g. 7.2 calls
`safe_int([1, 2])` expecting `TypeError` to escape, so a bare `except` fails).
When adding a puzzle, ask: "could I pass this without using the concept?" —
and close the hole with the narrowest matching check.

This is verified **mechanically**, not by inspection: `python3 audit.py
--sidestep` runs a *replay attack* on every puzzle. It records each
(stdin → stdout) or (call → return) the tests exercise against the reference
solution, generates an impostor program that answers from that lookup table
(computing nothing), and runs the tests against the impostor twice. A puzzle
the impostor can pass is flagged SIDESTEPPABLE: either its inputs need
randomizing or its construct check is too weak. The handful of puzzles where
the replay is *equivalent to a legitimate answer* (e.g. 1.1, whose entire
lesson is printing one fixed literal) are whitelisted in `audit.py` with a
written reason. Run the sidestep audit whenever a puzzle or toolkit check
changes; plain `python3 audit.py` (conformance only) is the quick pass.

## 9. Coding conventions

- Stdlib only; Python 3.8+ compatible.
- Keep modules small and single-purpose; if a file starts owning two concerns,
  split it.
- Dependencies point downward through the §4 list; no import cycles.
- No raw ANSI/box characters outside the visual layer.
- No `print()` of internal state for debugging left in commands; failures are
  rendered, not dumped.
- Functions over classes unless state genuinely clusters (the `T` toolkit does).
- Name things for the concern they serve, not the mechanism.

When in doubt, re-read §2. The whole point is that visuals, content, input,
checking, and state can each change without touching the others.
