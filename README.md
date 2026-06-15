# PyQuest

**A Python course you run from the terminal: read a short brief, write code in your own editor, then run one command to check it and unlock the next puzzle.**

Nine chapters and 90 puzzles take you from `print("hello")` to functions,
error handling, files, and classes — using only the Python standard library,
so it runs anywhere Python 3 does.

There is no TUI to learn. The only interactive screen is the optional `begin`
menu (pick a level, theme, or profile); everything else is a short, one-shot
command. The terminal is just a command runner — the learning happens in files
you open in your editor.

> Python 3.8+ · standard library only · zero dependencies · MIT licensed

---

## Features

- **90 puzzles in 9 chapters** — basics, strings, decisions & loops,
  collections, power tools, functions, errors, files & I/O, classes & objects.
  One new idea per puzzle.
- **Behavioral checking** — tests validate what your code *does*, with
  plain-language failure messages instead of raw tracebacks.
- **Hard to cheat, easy to learn** — randomized inputs defeat hardcoded
  answers, and an automated replay-attack audit (`audit.py --sidestep`) proves
  every puzzle's lesson is unavoidable.
- **Three difficulty modes**, escalating hints, reference solutions with a
  "why it works" explanation.
- **Profiles, colour themes, and safe progress** — atomic saves, nothing is
  ever silently lost, and `reset` gives a true clean slate.
- **Zero dependencies** — Python 3.8+ standard library only. Nothing to
  install.

## Quick start

```
cd pyquest
python3 play.py
```

That prints your progress and points you at two files for the current puzzle:

- `brief.md` — read this. It explains the concept and the task.
- `work.py` — edit this. One workspace file per profile (at
  `users/<name>/work.py`); PyQuest loads each puzzle's starter into it as you
  go (`start` shows the exact path).

Write your code, **save the file in your editor** (unsaved edits are the most
common reason a correct-looking answer fails), then check it:

```
python3 play.py check
```

When it passes, your code is saved and you stay put so you can keep tinkering.
Move on whenever you're ready with `next`. That is the whole loop:

> **read `brief.md` → edit `work.py` → save → `check` → `next`**

New to the project? [GETTING_STARTED.md](GETTING_STARTED.md) walks through the
first session step by step.

## Terminal setup

PyQuest needs nothing beyond Python 3 — `python3 play.py <command>` always
works, in any shell, on any platform. The setup below is optional comfort.

### Short commands

Typing `python3 play.py` every time gets old. PyQuest ships shell shortcuts so
you can type `check`, `hint`, `map`, and so on from any directory:

```
python3 play.py setup
```

`setup` checks for Python 3 and offers two ways in:

- **local** — it prints a `source` line you run once; the shortcuts work in
  **this terminal only** and nothing on your system is changed.
- **persistent** — `python3 play.py setup persist` adds one line to your
  `~/.zshrc`, so every new terminal has the shortcuts. It is safe to run more
  than once: it never duplicates the line and never touches your code or
  progress (it edits `~/.zshrc` and nothing else).

After persisting, open a new terminal or run `source ~/.zshrc` once. The same
setup is also reachable from the `begin` menu (option **5 → shortcuts**), and
the old `./setup.sh` still works — it forwards to `python3 play.py setup`.

If you would rather do it by hand, add this line to the end of `~/.zshrc`,
replacing the path with wherever the folder actually lives:

```sh
[ -f "/path/to/pyquest/shell/pyquest.zsh" ] && source "/path/to/pyquest/shell/pyquest.zsh"
```

The shortcuts file resolves its own location, so once that line points at it
you can move or rename the PyQuest folder without editing anything inside it.

### Uninstalling

Run `uninstall` (or `python3 play.py uninstall`). It removes the line from
`~/.zshrc` **and** clears the shortcut functions from the current terminal —
or just delete the `# PyQuest shell shortcuts` line from `~/.zshrc` yourself.

### The context-aware `reset`

`reset` is also a real terminal command that reinitializes your session, and
the shortcuts deliberately don't steal it. Inside the PyQuest folder, `reset`
clears PyQuest progress (after a y/N prompt); anywhere else it falls through
to the normal terminal reset. You can always be explicit — `start reset` for
PyQuest, `command reset` for the terminal.

### How PyQuest treats your terminal

- **Colour degrades gracefully.** Output is plain text whenever it is piped or
  redirected (not a TTY), and the [`NO_COLOR`](https://no-color.org/)
  convention is respected.
- **Frames fit your window.** Boxes and banners size themselves to the live
  terminal width (capped for readability) instead of assuming 80 columns.
- **Nothing blocks a pipe.** The two interactive moments (`begin` and bare
  `goto`) degrade to a plain print when stdin is not a terminal, so scripts
  and tests never hang.
- **Shell support.** The shortcut functions are written for zsh, the macOS
  default. On other shells, use the `python3 play.py` long form for now — bash
  support is on the roadmap below.

## Commands

Every command runs once, prints plain text, and exits. With the shortcuts
installed, drop the `python3 play.py` prefix.

| Command | What it does |
|---|---|
| `python3 play.py` | show progress and the current puzzle (`start` / `pq` as a shortcut) |
| `python3 play.py begin` | open the main menu (start here) |
| `python3 play.py menu` | return to the main menu from anywhere |
| `python3 play.py check` | validate your `work.py` against the puzzle |
| `python3 play.py hint` | reveal the next hint (three per puzzle, escalating) |
| `python3 play.py solution` | show the reference solution and why it works |
| `python3 play.py map` | show the chapter/puzzle tree with progress |
| `python3 play.py next` | move on to the next puzzle |
| `python3 play.py goto` | pick a puzzle from a list (`goto 2` = first open puzzle of chapter 2) |
| `python3 play.py goto 2.4` | jump to a puzzle by id (restores your saved code) |
| `python3 play.py load 2.4` | same as `goto` — reload a puzzle's saved code |
| `python3 play.py skip` | move on without solving (not in hard mode) |
| `python3 play.py retry` | blank the workspace to practice again (stays solved; `replay` is an alias) |
| `python3 play.py revert` | fully reset this puzzle: blank code + clear its progress |
| `python3 play.py mode easy` | set difficulty: `easy` \| `normal` \| `hard` |
| `python3 play.py theme amber` | switch colour theme (or add your own in `themes/`) |
| `python3 play.py user alice` | switch or create a profile |
| `python3 play.py setup` | enable the short commands (local or persistent) |
| `python3 play.py uninstall` | remove the persistent shortcuts again |
| `python3 play.py reset` | wipe progress, saved answers, and workspaces |

## Difficulty modes

Set once with `mode <name>`; change it whenever you like.

| | Easy | Normal | Hard |
|---|---|---|---|
| Pointer shown automatically | yes | no | no |
| Hints | unlimited, anytime | on demand | only after 3 tries |
| `solution` | anytime | anytime | only after solving |
| `next`/`skip` past unsolved | yes | yes | no (must solve) |
| `goto` forward (ahead) | yes | back only | back only |

## How your work is saved

Every `check` archives your `work.py` into your profile's `answers.json`,
keyed by puzzle id. Switching puzzles (`next`, `skip`, `goto`) saves the
current draft and reloads the target puzzle's saved code — nothing is lost,
and `goto 1.1` brings back exactly what you wrote there. All saves are atomic.

`python3 play.py reset` is the one true wipe: completed puzzles, attempts,
hints used (`progress.json`), all saved code (`answers.json`), and the
workspace files, which are regenerated from their starters. Your difficulty
mode is preserved. After a reset you are genuinely back to a blank puzzle 1.1.

## Project layout

```
pyquest/
  play.py            the thin launcher you run
  engine/            the implementation, split by concern (see docs/ARCHITECTURE.md)
  audit.py           mechanical checks: conformance + anti-sidestep replay attack
  docs/              ARCHITECTURE.md, SCHEMA.md, CONTRIBUTING.md, architecture/ (UML)
  chapters/          the course content — one folder per puzzle, no code
    01_basics/
      01_hello/
        brief.md     concept + task (read)
        starter.py   the seed PyQuest loads into work.py
        hints.md     three escalating hints
        solution.py  reference solution
        tests.py     behavioral checks
        meta.json    puzzle metadata
  themes/            optional JSON colour presets (see themes/README.md)
  shell/             the zsh shortcuts sourced by setup
  users/<name>/      per profile: progress.json, answers.json, work.py (generated)
  settings.json      current user + colour theme (created on first run)
```

## Documentation

| Document | What it covers |
|---|---|
| [GETTING_STARTED.md](GETTING_STARTED.md) | a learner's first session, step by step |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | module map, design invariants, how validation works |
| [docs/architecture/](docs/architecture/README.md) | UML architecture (Mermaid): overview + per‑module diagrams |
| [docs/SCHEMA.md](docs/SCHEMA.md) | file formats for authoring your own puzzles |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | how to add a puzzle, the audit gate, project conventions |
| [themes/README.md](themes/README.md) | creating custom colour themes |

## Roadmap

The course currently ends at Chapter 9 (classes & objects). The engine was
built ahead of the content, so the groundwork for what comes next is already in
place:

- **Generators, lambdas, and the standard library.** Construct checks for
  `yield`, `lambda`, and per-module `import` are staged for these chapters.
- **Randomized inputs everywhere.** The structured `Case` provider flow
  (see [ARCHITECTURE.md §8](docs/ARCHITECTURE.md)) is live in Chapters 1–2 and 6+;
  remaining fixed-input puzzles will migrate to it where it strengthens the
  lesson.
- **bash support for the shortcuts.** `setup` already detects `~/.bashrc`;
  a bash-compatible version of the shortcut functions is planned so the short
  commands work beyond zsh.

Adding a chapter is content-only — puzzle folders on disk, zero engine
changes — which is exactly what the architecture was shaped for.

## Requirements

Python 3.8+ — standard library only. No installation, no dependencies. The
shell shortcuts target zsh (the macOS default); everything also works by
prefixing commands with `python3 play.py` on any platform.

## License

[MIT](LICENSE) — © 2026 Ronald Karel Grant
