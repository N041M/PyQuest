# Contributing to PyQuest

Thanks for helping grow the course. PyQuest is a terminal-run Python tutorial:
learners read a brief, write code in their own editor, and run one command to
check it. Most contributions are **new puzzles**, which are just files on disk
(no engine changes needed).

Start with the [README](../README.md) for the learner's view, then
[ARCHITECTURE.md](ARCHITECTURE.md) for the design and [SCHEMA.md](SCHEMA.md) for
the exact file formats.

## Ground rules

- **Python 3.8+, standard library only.** No third-party dependencies, ever.
- **Behavioral checks only.** Tests validate what code *does*, not its source
  text. The single sanctioned exception is the liveness-checked construct
  checks (`T.uses_*` / `T.line_*`).
- **A puzzle must make its *lesson* unavoidable, not just its output.** A
  program that produces the right answer while skipping the concept is a
  *sidestep*, and closing those is the core of the project (see below).
- **The visual layer is isolated.** Colours, glyphs, and box characters live
  only in `engine/theme.py` and `engine/render.py`; nothing else emits them.

## Setup

No installation. From the repo root:

```bash
python3 start.py              # status / the learner loop (begin, check, next, ...)
python3 start.py setup        # optional: install the `pq ...` shell shortcuts
```

Open the repo in a **GitHub Codespace** (Code → Codespaces) and it runs with no
local setup, the devcontainer ships Python 3.12.

## The audit is the test suite

There is no pytest layer. [`audit.py`](../tools/audit.py) is the test suite, and it
must be green before any change is committed:

```bash
python3 tools/audit.py --sidestep   # conformance + the anti-sidestep attack suite
python3 tools/audit.py --engine     # execution-guard & toolkit self-tests
```

`--sidestep` is mutation testing aimed at the *grader*: it builds intentionally
wrong programs and requires them to fail. **Never weaken a check to make the
audit pass**, fix the root cause.

## Adding a puzzle

A puzzle is one folder under `chapters/NN_chapter/MM_title/` with six files
(`brief.md`, `starter.py`, `tests.py`, `hints.md`, `solution.py`, `meta.json`)
and an optional `dodges.py`. The engine discovers it automatically. See
[SCHEMA.md](SCHEMA.md) for every field and helper.

Checklist:

1. Write the brief in the house style: concept from scratch → a tiny worked
   example → the task → what "done" looks like.
2. Make `tests.py` validate **behavior** with `T` (`T.run`/`T.call`, then
   `T.eq`/`T.true`/...), and include at least one edge case.
3. Pin the lesson with a construct check (`T.uses_*` / `T.line_*`) so the answer
   can't be reached with a different tool. Run behavior assertions *before*
   construct checks (liveness replays the recorded inputs).
4. Randomize inputs where you can, so answers can't be hardcoded.
5. Confirm `solution.py` passes, then run `python3 tools/audit.py --sidestep`.

## Closing a sidestep

If you (or the audit) find a program that passes without using the lesson:

1. Tighten the defense, randomize inputs, choose a liveness-checked construct
   check, or pin the exact expression with a `line_*` check.
2. Add the sidestep to that puzzle's `dodges.py` as a `(label, source)` pair, so
   the audit fails forever if it ever passes again.
3. Re-run `python3 tools/audit.py --sidestep` and confirm it reports the puzzle
   robust.

## Pull requests

- Keep commits small with terse, imperative subjects.
- No decorative emojis in code, comments, or commit messages (the deliberate UI
  glyph set in `engine/theme.py` is the only exception).
- Green audit (`--sidestep` and `--engine`) is required.
- One new idea per puzzle; one concern per module.
