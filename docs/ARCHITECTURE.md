# Architecture

The design reference for PyQuest. Read it before adding a feature, a puzzle,
a command, or a coat of paint. Its job is to keep PyQuest **modular** so it
never collapses back into one monolithic file, and so new capabilities
(randomized inputs, new themes, new question types) slot in cleanly. For file
formats, see [SCHEMA.md](SCHEMA.md); for usage, see the [README](../README.md);
for the same design **as diagrams**, see [diagrams/](diagrams/README.md).

If a change you are about to make does not fit one of the modules below, that
is a signal to discuss the boundary, not to staple the code onto the nearest
file.

## 1. What PyQuest is (and is not)

PyQuest is a terminal-run Python course. The learner reads a brief, writes code
in a workspace file in their own editor, and runs short, stateless commands to
validate it and progress.

- It is **not** a full interactive TUI. Interactivity is confined to two
  opt-in surfaces that only engage on a key-capable TTY and otherwise degrade
  to the same typed commands: the `menu` launcher (set up shortcuts, pick a
  level), and the **play cockpit** -- the puzzle card's bottom nav row made
  arrow-selectable (engine/keys.py). Underneath, every command still runs once
  and exits; the cockpit is a thin selector that dispatches those same verbs.
- It validates **behavior**, never source text: with rare, explicit exceptions
  where the lesson *is* a construct (e.g. commenting a line out).
- Standard library only. No third-party dependencies. Runs on a fresh Python 3.

These are invariants. See §3.

## 2. Separation of concerns

Five concerns must never bleed into each other. Each owns one question:

| Concern | Owns the question | Module |
|---|---|---|
| **Content** | "What is this puzzle?" | `content.py` |
| **Input** | "What do we feed the solution?" | `inputs.py` |
| **Checker/Tester** | "Is the solution correct (and good)?" | `toolkit/`, `checker.py` |
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

## 3. Invariants

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
8. **Stateless commands, with scoped, opt-in interactive surfaces.** Every
   command runs once and exits, no prompts, loops, or live redraw, *except*
   (a) the `menu` launcher, which loops reading a choice and runs before
   puzzles; (b) bare `goto`, which shows the puzzle list and reads ONE id; and
   (c) the **play cockpit** (app._play), which makes the puzzle card's bottom
   nav row arrow-selectable, dispatching the same verbs in place until Esc.
   All three engage only on a key-capable TTY (engine/keys.py) and degrade to a
   plain print + the typed commands when stdin is not a terminal, so they never
   block pipes or tests. The destructive `wipe profile` needs no prompt at all
   -- its required second word is the confirmation, so it stays a one-shot.
9. **Stdlib only.**
10. **Progress is recoverable.** `wipe profile` is a true reset; saving never silently
    destroys the learner's code without it living in `answers.json`. All JSON
    saves are atomic (temp file + rename), and an unreadable progress/answers
    file is moved aside as `<name>.corrupt`, never overwritten.

## 4. Module map

The package lives under `pyquest/`. `start.py` at the root is a thin entry
point that only routes: a cold bare run delegates to `engine.session` (host a
session shell, open the menu); `start.py <verb>` delegates to
`engine.app.main()` (run one command).
Dependencies only ever point **downward** in this list (no cycles):

```
config.py     constants & paths; terminal width; users/settings.json (current
              user + theme). Depends on nothing.
theme.py      selectable palettes (THEMES), glyphs, paint(), the logo. The
              visual identity; apply_theme() switches in place.
render.py     drawing primitives: box, banner, bar, header, wordmark, rule,
              field, wrap, indent, cli(). Pure look; depends on theme + config.
content.py    Puzzle/Chapter model + discovery + loaders (brief, hints, starter,
              meta, tests, reference) + category(). "The structured question."
i18n.py       human-language piping: English default + fallback, validated
              community packs under lang/<code>/. t() localizes a UI string,
              localized() a content file (brief/hints/reference). content + the
              read verbs route through it; depends only on config.
inputs.py     input providers: random_word/int + the Case seam. Hands the same
              data to the runner and the checker. "The input automizer."
state.py      per-user progress + answers (users/<name>/...) + workspace
              (work.py) lifecycle: seed, archive, switch, reset, users.
toolkit/      the T object handed to each tests.py. "The tester." A package
              composed by concern; internal dependencies point down:
                errors.py      the translated failure categories (incl.
                               LessonNotUsedError: right answer, wrong lesson)
                textutil.py    normalize / short_tb / fmt_args
                guard.py       ExecutionGuard -- the ONE place in-process
                               learner code runs (sandbox, alarm, capture)
                runners.py     script/import execution + the tape of every
                               recorded run/call
                asserts.py     behavior assertions (eq, approx, raises, ...)
                liveness.py    ablation engine -- judges constructs against
                               the tape
                constructs.py  uses_* / print_* / assigns_* checks
                lines.py       prescribed-expression checks (line_*)
                perf.py        bonus(T) timing helpers
              `__init__.py` assembles Toolkit as a facade over these mixins;
              the import path `engine.toolkit` and the flat T API are frozen.
checker.py    orchestrates one check: load tests, build T, run check()/bonus(),
              translate failures into their categories (a missed construct
              check renders its own "so close" screen), render pass/fail.
commands/     the verbs (status, map, stats, goto, next, skip, retry, hint,
              solution, mode, wipe, help), compose state + content + render + checker.
              A package split by concern, like toolkit/; internal dependencies
              point down and `__init__.py` re-exports every cmd_* as a facade so
              the import path `engine.commands` and the dispatcher stay frozen:
                registry.py   the command surface declared once: each verb's
                              aliases, context (always / needs a puzzle), and
                              one-line help, plus NAV_CLUSTERS (which verbs the
                              nav strip shows). app.py canonicalizes, gates, and
                              suggests from it; help renders from it.
                cards.py      shared composition: the puzzle card, status
                              marker, the one chapter tree (map + goto picker),
                              the registry-driven bottom nav strip, and the
                              goto/advance helpers (the layer the loop verbs and
                              the menu both build on)
                views.py      the read verbs (show, never move you): status,
                              map, stats (per-chapter completion + attempts/
                              hints/clean-solves read back from progress.json),
                              hint, solution, textbook (writes a per-user
                              syntax/tips markdown file from the `concept`/`why`
                              of puzzles that carry them -- reached vs full,
                              entry-less puzzles omitted -- and links to it; no
                              separate authoring, never drifts)
                navigate.py   navigation + workspace reset: goto, next, skip,
                              retry, restart
                profiles.py   settings: theme, mode, user (switch/create plus
                              the delete/rename subcommands), wipe
                transfer.py   export, import: portable profile bundles
                              (serialize + validate against current content)
                shortcuts.py  the ~/.zshrc shortcuts installer -- the only part
                              that edits the user's environment (setup/persist/
                              uninstall)
                help.py       the help screen
                menu.py       the interactive launcher (menu), one of two
                              interactive surfaces (§3 invariant 8; the other is
                              the play cockpit in cards.nav_select / app._play);
                              sits on top of cards + profiles + shortcuts. A hub
                              (play / learn / set up) whose numbered items run
                              the read verbs (textbook/stats/map) in place and
                              fold theme/mode/profiles/shortcuts behind one
                              `settings` sub-pane; typed status/help run inline
                              too. Every pane obeys one rule: `0` backs out.
app.py        argv dispatch + main().
session.py    cold-start launcher: detect the shell, host a session with the
              shortcuts loaded, open the menu. The one place that spawns a
              shell; depends only on config. (`start.py` calls it.)
```

Rules for the map:

- A new **command** → the matching `commands/` module (a read verb →
  `views.py`, a navigation verb → `navigate.py`, a setting → `profiles.py`,
  etc.; a new concern → a new module),
  re-export it from `commands/__init__.py`, add a row in `commands/registry.py`
  (aliases + context + help), plus one dispatch line in `app.py` and a shell
  shortcut — unless the bare word collides with a shell built-in (`export`),
  in which case it stays umbrella-only (`start export`) and `render.cli()`'s
  `UMBRELLA_ONLY` list shows it that way. Nowhere else. (`t_command_registry`
  fails the audit if dispatch and the registry drift apart.)
- A new **screen/visual** or restyle → `theme.py` / `render.py` only.
- A new **validation helper** → the matching `toolkit/` module
  (assertion → `asserts.py`, construct check → `constructs.py`, …); the
  facade in `toolkit/__init__.py` only changes if a new mixin is added.
- A new **input strategy** (e.g. randomized) → `inputs.py`; nothing else changes.
- A new **puzzle** → files on disk only (see §6); zero code changes.

## 5. The visual layer

`theme.py` holds the swappable identity: the colour palette (named roles, not raw
codes scattered around), the glyph set (`OK`, `CUR`, `ARROW`, …), the logo, and
`paint()`. `render.py` holds reusable drawing primitives that consume the theme.

To restyle PyQuest you edit those two files and nothing else. Screen *composition*
(which fields a card shows) lives with the command that owns the screen, but it
must build that screen only from `render` primitives, never by emitting raw
escape codes or box characters itself.

Colour auto-disables when output is not a TTY or `NO_COLOR` is set. Frames size to
the live terminal width (capped for readability). Both behaviours live in the
visual layer; no other module knows about them.

## 6. Adding a puzzle (no code change)

A puzzle is a folder `chapters/NN_chapter/MM_title/` with these files:

- `brief.md`: what the learner reads (house style, §3.4).
- `starter.py`: the seed loaded into the chapter's `work.py`.
- `tests.py`: defines `check(T)` and optionally `bonus(T)` (§7).
- `hints.md`: three hints, escalating, separated by `---`.
- `solution.py`: reference answer (+ `why` lives in `meta.json`).
- `meta.json`: `id`, `title`, `chapter`, `mode`, and the optional `concept`,
  `why`, `category` (curriculum tier), and `kind` (marks a project puzzle).
- `reference.md` *(optional)*: the topic's detailed textbook entry; required
  when the puzzle carries a `concept`.
- `dodges.py` *(optional)*: known sidesteps pinned as regressions (§8).

**Projects** (`chapters/NN_project_*/`) are chapters that build an app over a few
steps to a low-guidance capstone. Their puzzles set `kind`
(`build` / `debug` / `capstone`) and omit `concept`, so they stay out of the
textbook and the lesson-guard; a `debug` puzzle ships broken code in `starter.py`
that the audit requires to *fail* its tests. See [SCHEMA.md](SCHEMA.md#projects).

The engine discovers it automatically. See [SCHEMA.md](SCHEMA.md) for exact
formats.

## 7. How validation works

`tests.py` defines `def check(T)`. `T` (from `engine/toolkit/`) both runs the learner's
code and raises *translated* failures, so messages stay friendly.

- **The execution guard.** Every execution of learner code: importing the
  file, calling a function, timing it, goes through one guard in `toolkit/guard.py`
  that blanks stdin (a stray `input()` fails fast instead of hanging), captures
  stdout into `T.printed`, enforces the wall-clock timeout (infinite loops fail,
  even inside the learner's own `except Exception`), translates `exit()` /
  `sys.exit()` (learner code cannot kill the checker), and chdirs into a
  throwaway sandbox so **relative**-path file I/O lands there, not in the
  project. Script mode gets stronger isolation via its subprocess (timeout +
  sandbox cwd). Never invoke learner code outside this guard; `python3 tools/audit.py
  --engine` pins these guarantees.
  *Isolation caveat:* the sandbox is a convenience boundary, not a security
  one. A chdir contains an honest mistake (a stray `open("out.txt", "w")`); it
  does **not** stop a determined absolute-path write (`open("/etc/…")`),
  `os.system`, or `shutil.rmtree`. The threat model is a learner's accident on
  their own machine, not malicious code, do not run untrusted submissions
  through it. (`--engine`'s `t_sandbox_files` only exercises relative paths,
  i.e. exactly the property the chdir provides.) The in-process guard also
  mutates global state (`os.chdir`, `sys.stdin/stdout`), so it is correct only
  single-threaded.
  *Portability caveat:* the **in-process** timeout uses `signal.alarm`
  (`guard.py`), so it only fires on the POSIX main thread, integer-second
  granularity, and a silent no-op on Windows or off the main thread. There it
  degrades open: an infinite-loop solution run via **import mode** would hang.
  Script mode is unaffected (its subprocess timeout is cross-platform), and the
  primary target is a POSIX terminal, so this is an accepted stdlib-only limit
  rather than a bug, but import-mode timeouts are not a guarantee off POSIX.
- **Behavior:** `T.run(stdin=..., files=...)` (script mode) or
  `T.call(name, ...)` (import mode), then `T.eq / T.true / T.is_a / T.raises`.
- **Files (Ch8+):** seed fixtures with `T.run(files={...})` or `T.put_file`;
  assert what the learner's code wrote with `T.file(name)`, all inside the
  sandbox, never the project tree.
- **Objects (OOP chapters):** `T.make("ClassName", args)` instantiates,
  `T.method(obj, "name", args)` calls, `T.attr(obj, "name")` reads, each with
  translated failures.
- **Mutation lessons:** `T.does_not_mutate(name, *args)` calls the function and
  requires the arguments back unchanged (the `sorted` vs `.sort()` distinction).
- **Many valid answers:** assert properties, not one value: `T.approx` (works
  inside lists/tuples/dicts), `T.any_of`, `T.unordered`, or `T.true(<invariant>)`.
- **Integrity:** when output alone could be typed in: or the topic construct
  dodged with another tool, require the real thing. `T.prints_computed(min_calls=)`,
  `T.prints_name(min_calls=, same=)`, `T.uses_op("+"/"*"/...)`, `T.uses_print`,
  `T.print_uses_keyword`, `T.print_has_min_args`,
  `T.assigns_a_variable(value=)`, `T.reassigns_a_variable(values=)`,
  `T.uses_if/uses_while/uses_for/uses_loop/uses_break/uses_continue`,
  `T.uses_fstring`, `T.uses_index/uses_negative_index/uses_slice(step=)`,
  `T.uses_in`, `T.uses_boolop(op=)`, `T.uses_comprehension(with_if=)`,
  `T.uses_call(name)`, `T.uses_dict/uses_set/uses_unpacking`,
  `T.uses_nested_if`, `T.uses_default_param(name)`, `T.uses_try`, `T.uses_raise`,
  `T.uses_with`/`T.uses_with_open` (the latter requires the FILE itself to be
  opened by the `with`, not merely some live `with` elsewhere),
  `T.uses_import(module)`, `T.uses_class(name)` (name the class the tests
  instantiate; AST-only for object puzzles, which have no tape, see runners.py),
  `T.uses_yield` (live in Chapter 10, generators), `T.uses_lambda` (live in
  Chapter 14, functional tools), `T.source()`. The object/dunder lessons of
  Chapter 15 (advanced classes) are forced behaviorally — `isinstance` for
  inheritance, `==`/`<` for `__eq__`/`__lt__`, a mutate-then-read for `@property`
  — backed by `uses_class`. Require the *kind* of construct, not one exact
  spelling, so
  legitimate variations still pass (e.g. an `elif` puzzle accepts nested `if`s,
  and `uses_boolop()` accepts a De Morgan `not(a or b)` for an `and`). The
  inverse, a *nesting* puzzle that must reject a flat `elif`, needs
  `uses_nested_if` (an `elif` is AST-identical to `else: if`, so only a body
  nest counts). A failed construct check is a `LessonNotUsedError`: the output
  was right but the taught tool was skipped, shown as its own screen.
- **Liveness (how construct checks judge).** A construct check is itself
  behavioral: a candidate node only counts if ablating it, removing the
  statement, substituting the expression with a sentinel value, dropping the
  keyword, trimming the extra print arguments, *changes the program's
  behavior* when re-run against the inputs the tests already exercised. Dead
  decorations (`q = 1 * 1`, `if False: pass`, a print routed into a StringIO)
  no longer satisfy anything. Judgment is deliberately learner-protective:
  statement removal counts a crash as live; expression substitution needs a
  clean run with different output (so crash-engineered chaff stays dead), and
  falls back to a reachability tripwire when every sentinel crashes
  (accumulator dicts/sets, `sorted()` feeding lookups); if the baseline can't
  be reproduced in-process, the check degrades to the plain AST scan rather
  than ever blocking honest code. The implementation lives in `toolkit/liveness.py`
  (`_require_live`, `_is_live`, `_ablate`), and `T.require_live(...)` is the
  public seam for a capstone's bespoke structural check, pair any use of
  it with a `dodges.py` entry.
  *Liveness exceptions (AST-only checks).* Three construct checks cannot be
  ablated and so are **plain AST scans, not liveness-judged**:
  `uses_yield` (substituting a yield flips the function's generator-ness and
  crashes callers), `uses_lambda` (a sentinel stand-in isn't callable), and
  `uses_default_param` (a default may legitimately go unexercised). For these,
  "dead-code chaff defeats it", a never-called function containing a lambda /
  yield / default would satisfy a *file-level* AST scan. Two backstops: (a)
  **scope the check to the lesson's function** -- `uses_yield(name)`,
  `uses_class(name)`, `uses_default_param(name)` require the construct in *that*
  function's own body, so a decoy parked in an unrelated (or nested) function no
  longer counts; and (b) the sidestep audit plus behavioral traps. So when you
  write a puzzle on generators, lambdas, or default params, do **not** lean on a
  bare construct check: scope it by name, pair it with behavior that forces the
  construct to run (call the generator and assert it streams via
  `is_generator`; call the default-using function both ways), and pin a
  `dodges.py` chaff entry. Ch10 (generators) does exactly this -- the file-level
  `uses_yield()` was breachable by a genexpr target plus a decoy yield, closed
  by `uses_yield("fn")` and pinned dodges (the `uses_yield_scoped` self-test).
- **Prescribed expressions (fixed-output puzzles):** a puzzle with no input
  can never randomize, and liveness can't tell `print(7*2)` from
  `print(2+3*4)`, both compute. Where the lesson IS a specific expression,
  pin it with `T.line_uses_op(i, op)`, `T.line_shape(i, outer, inner)` (the
  parentheses-grouping shape: a BinOp(outer) with a BinOp(inner) operand),
  and `T.line_only_literals(i, {...})` (built only from the task's own
  values, type-strict). These three made 1.7–1.9 airtight.
- **Performance (optional, advisory):** a `def bonus(T)` runs only after the answer
  is accepted and never blocks progress, a `⚡` line. Use `T.time_call` or, better,
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
  provider's expectation, so hardcoding the answer is impossible because the
  inputs change per run.

Because the provider feeds both the run and the check from one place (§2), turning
a fixed puzzle into a randomized one means writing a provider and pointing the test
at it, no engine change. Fixed-output, no-input puzzles keep using construct
checks (§7) for integrity instead.

**In use now.** `inputs.py` provides `random_word` / `random_int`, used across
the course. Script-mode, input-reading puzzles (Ch1–2) feed randomized stdin
and compute the expected result in `tests.py`. The structured-provider/`Case`
flow is the norm from Chapter 6 on (functions, and every import-mode chapter
since): tests build a list of `Case`s (fixed edge cases plus randomized ones),
feed `case.args` to `T.call`, and validate against `case.expect` — one source for
both the input and the expectation. Randomized inputs are also what keep the
**project** chapters robust: they carry no construct check, so changing inputs
each run is the whole anti-hardcode defense.

**Anti-sidestep policy.** Every puzzle must make its *lesson* unavoidable, not
just its output. The defenses stack, one per attack class:

| attack | example | defense |
|---|---|---|
| hardcode / replay the answers | `print("Hello, World")`, a lookup table | randomized inputs (this section) |
| park the construct in dead code | `q = 1 * 1`, `if False: pass`, a silenced print | liveness-checked construct checks (§7) |
| compute the constants another way | `print(7*2)` for the 2 + 3 * 4 puzzle | prescribed-expression checks `line_*` (§7) |
| solve with a different tool | `.find()` instead of `in`, a loop instead of recursion, an `if b == 0` instead of `except` | construct checks + behavioral traps (e.g. 7.2 calls `safe_int([1, 2])` expecting `TypeError` to escape, so a bare `except` fails) |

When adding a puzzle, ask: "could I pass this without using the concept?",
and close the hole with the narrowest matching check.

This is verified **mechanically**, not by inspection: `python3 tools/audit.py
--sidestep` is mutation testing aimed at the grader, intentionally wrong
programs must fail. It attacks every puzzle with four generic adversaries
(`replay`: answer from a recorded lookup table; `chaff-replay`: the table
plus a never-called function stuffed with every construct the toolkit can
require; `synth`: each constant output line recomputed via live arithmetic
the brief never asked for; `named-synth`: the constants parked in a reused
variable), and additionally runs every pinned dodge from a puzzle's optional
`dodges.py`, a regression list of known sidesteps (each must fail forever;
1.8's `print(7*2)` lives there). A puzzle any impostor passes is flagged
SIDESTEPPABLE unless whitelisted in `ALLOWED` with a written reason, which
is reserved for puzzles where the cheapest passing program *is* a legitimate
answer (1.1: the lesson is printing one fixed literal). Run the sidestep
audit whenever a puzzle or toolkit check changes; plain `python3 tools/audit.py`
(conformance only) is the quick pass.

**Two static meta-audits cover the adversaries' blind spot.** The generic
adversaries cannot model the bottom row of the table above — *solving with a
different tool* — on a **varying-output** puzzle: `synth` only fires on
fixed-output scripts, so a program that computes the right answer with the
wrong construct sails past. That gap used to be hunted by hand; it is now two
mechanical checks read from each `tests.py` source (`--sidestep` runs the first;
`--lessons` / `--prove-checks` are the standalone reports):

- **lesson-guard** flags any puzzle that teaches a construct (has a `concept`),
  varies its output, and pins *no* construct check — it is unguarded against the
  alternative-construct class. Acceptable residuals are whitelisted in
  `GUARDED_OK` with a written reason (mirroring `ALLOWED`): 3.1 (a varying
  boolean is unobtainable without *some* comparison, and `<`/`>`/`>=` are all
  valid, so there is nothing single to pin), and 6.1/6.2/6.3/6.5 (import mode —
  the grader calls the function by name, so `def`/params/`return` are forced and
  there is no *internal* construct to pin). Anything else is a hard failure.
- **prove-checks** is the converse: for every puzzle with both a construct check
  and a `dodges.py`, it strips the construct layer and confirms a pinned dodge
  then slips through — proving the *check*, not some behavioral assert, is what
  stops that dodge. A dodge caught behaviorally is surfaced (informational), not
  failed; it remains a valid hardcode/replay regression.

`check_inventory`, `lesson_guard`, and the AST construct-stripper are themselves
pinned by the `meta_audit` engine self-test, so the audit's own reasoning can't
silently rot.

**Known residual risks** (accepted, documented): liveness proves a construct
*matters*, not that it's idiomatic, an `if True:` wrapped around a trick
expression, or an executed-but-pointless decoy dict (containers are judged
by reachability, see §7), still passes the generic checks. The `GUARDED_OK`
entries above are the lesson-guard's documented residuals. These require a
learner to deliberately out-engineer the grader rather than stumble past it;
pin any that show up in the wild as `dodges.py` entries backed by a narrower
test, and remember the audit is fail-open by design, if liveness ever
degrades, impostors start passing and the audit flags it.

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
