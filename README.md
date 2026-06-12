# PyQuest

A Python course you run from the terminal. You **read** a short brief, **write**
code in your own editor, then run one command to **check** it and unlock the
next puzzle. Seven chapters and 74 puzzles take you from `print("hello")` to
functions and error handling — using only the Python standard library, so it
runs anywhere Python 3 does.

There is no TUI to learn. The only interactive screen is the optional `begin`
menu (pick a level, theme, or profile); everything else is a short, one-shot
command. The terminal is just a command runner — the learning happens in files
you open in your editor.

## Highlights

- **74 puzzles in 7 chapters** — basics, strings, decisions & loops,
  collections, power tools, functions, errors. One new idea per puzzle.
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

## Shell shortcuts (optional)

Typing `python3 play.py` every time gets old. PyQuest ships shortcuts so you
can type `check`, `hint`, `map`, and so on from any directory:

```
python3 play.py setup
```

`setup` checks for Python 3 and offers two ways in: a `source` line for **this
terminal only**, or `python3 play.py setup persist`, which adds one line to
your `~/.zshrc` (then `source ~/.zshrc` or open a new terminal). Persist is
safe to run more than once — it never duplicates anything and never touches
your code or progress. To uninstall, delete that line from `~/.zshrc`. (The
old `./setup.sh` still works; it forwards to `python3 play.py setup`.)

If you would rather do it by hand, add this line to the end of `~/.zshrc`,
replacing the path with wherever the folder actually lives:

```sh
[ -f "/path/to/pyquest/shell/pyquest.zsh" ] && source "/path/to/pyquest/shell/pyquest.zsh"
```

One quirk: `reset` is **context-aware**, because `reset` is also the terminal
command that reinitializes your session. Inside the PyQuest folder, `reset`
clears PyQuest progress (after a y/N prompt); anywhere else it does the normal
terminal reset. You can always be explicit — `start reset` for PyQuest,
`command reset` for the terminal.

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
| `python3 play.py retry` | blank the workspace to practice again (stays solved) |
| `python3 play.py revert` | fully reset this puzzle: blank code + clear its progress |
| `python3 play.py mode easy` | set difficulty: `easy` \| `normal` \| `hard` |
| `python3 play.py theme amber` | switch colour theme (or add your own in `themes/`) |
| `python3 play.py user alice` | switch or create a profile |
| `python3 play.py setup` | enable the short commands (local or persistent) |
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
  engine/            the implementation, split by concern (see ARCHITECTURE.md)
  audit.py           mechanical checks: conformance + anti-sidestep replay attack
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
| [ARCHITECTURE.md](ARCHITECTURE.md) | module map, design invariants, how validation works |
| [SCHEMA.md](SCHEMA.md) | file formats for authoring your own puzzles |
| [themes/README.md](themes/README.md) | creating custom colour themes |

## Requirements

Python 3.8+ — standard library only. No installation, no dependencies. The
shell shortcuts target zsh (the macOS default); everything also works by
prefixing commands with `python3 play.py` on any platform.

## License

[MIT](LICENSE)
