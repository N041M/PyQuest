# PyQuest

**Learn Python by doing, one small puzzle at a time.**

PyQuest gives you a series of short, friendly puzzles. You read a quick
explanation, write a few lines of code in your own editor, and run one command
to check your answer. Get it right, and the next puzzle unlocks.

It starts at the very beginning, `print("hello")`, and builds up gently
through **90 puzzles in 9 chapters**: the basics, text, decisions and loops,
lists and dictionaries, functions, handling errors, files, and classes. Each
puzzle adds just one new idea, so you're never thrown in the deep end.

There's nothing to install and no complicated setup. If you have Python 3, or
just a web browser (see **Run in a Codespace** below), you're ready, even if
you've never written code before.

> Works with any Python 3.8+ · nothing to install · free and open-source (MIT)

---

## What you get

- **90 bite-sized puzzles, one idea each**: from `print` all the way to
  classes, in small steps you can actually keep up with.
- **Friendly, plain-English feedback**: when something's wrong, you get a
  clear note about *what* went wrong, not a wall of scary red error text.
- **You can't fake it**: the checker runs your code and changes the numbers
  each time, so copying an answer or hard-coding the result won't work. The
  only way forward is to genuinely get it, which means you actually learn.
- **Help when you're stuck**: three hints per puzzle that get more specific,
  plus a full worked solution with a "why it works" explanation when you want it.
- **Go at your own pace**: pick an easier or harder mode, and your progress
  saves automatically, so you can stop and pick up again any time.

## Quick start

Open a terminal (the text window where you type commands), go into the PyQuest
folder, and run it:

```
cd pyquest
python3 play.py
```

> No Python on your computer, or new to all this? You can run PyQuest in your
> web browser instead: jump to [Run in a Codespace](#run-in-a-codespace) below.

That prints your progress and points you at two files for the current puzzle:

- `brief.md`: read this. It explains the concept and the task.
- `work.py`: edit this. One workspace file per profile (at
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

## Run in a Codespace

Don't want to install Python or use a terminal on your own machine? **GitHub
Codespaces** gives you a ready-to-go PyQuest that runs in your web browser, no
setup at all.

1. On this project's page on GitHub, click the green **Code** button.
2. Open the **Codespaces** tab and click **Create codespace on main**.
3. Wait a moment while it gets ready. A code editor opens in your browser, with
   a terminal panel at the bottom.
4. In that terminal, type the command and press Enter:

   ```
   python3 play.py
   ```

Everything is already set up for you: the right version of Python, the editor's
Python support, and PyQuest itself. (The setup lives in the `.devcontainer`
folder, which you never have to touch.) Codespaces is free
for personal use within GitHub's monthly allowance, and you can delete your
Codespace whenever you're done.

New to the project? [GETTING_STARTED.md](GETTING_STARTED.md) walks through the
first session step by step.

## Terminal setup

PyQuest needs nothing beyond Python 3: `python3 play.py <command>` always
works in any shell, on any platform. The setup below is optional comfort.

### Short commands

Typing `python3 play.py` every time gets old. PyQuest ships shell shortcuts so
you can type `check`, `hint`, `map`, and so on from any directory:

```
python3 play.py setup
```

`setup` checks for Python 3 and offers two ways in:

- **local**: it prints a `source` line you run once; the shortcuts work in
  **this terminal only** and nothing on your system is changed.
- **persistent**: `python3 play.py setup persist` adds one line to your
  `~/.zshrc`, so every new terminal has the shortcuts. It is safe to run more
  than once: it never duplicates the line and never touches your code or
  progress (it edits `~/.zshrc` and nothing else).

After persisting, open a new terminal or run `source ~/.zshrc` once. The same
setup is also reachable from the `begin` menu (option **5 → shortcuts**), and
the old `./setup.sh` still works and forwards to `python3 play.py setup`.

If you would rather do it by hand, add this line to the end of `~/.zshrc`,
replacing the path with wherever the folder actually lives:

```sh
[ -f "/path/to/pyquest/shell/pyquest.zsh" ] && source "/path/to/pyquest/shell/pyquest.zsh"
```

The shortcuts file resolves its own location, so once that line points at it
you can move or rename the PyQuest folder without editing anything inside it.

### Uninstalling

Run `uninstall` (or `python3 play.py uninstall`). It removes the line from
`~/.zshrc` **and** clears the shortcut functions from the current terminal,
or just delete the `# PyQuest shell shortcuts` line from `~/.zshrc` yourself.

### The context-aware `reset`

`reset` is also a real terminal command that reinitializes your session, and
the shortcuts deliberately don't steal it. Inside the PyQuest folder, `reset`
clears PyQuest progress (after a y/N prompt); anywhere else it falls through
to the normal terminal reset. You can always be explicit, `start reset` for
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
  default. On other shells, use the `python3 play.py` long form for now; bash
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
| `python3 play.py load 2.4` | same as `goto`, reload a puzzle's saved code |
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
current draft and reloads the target puzzle's saved code, nothing is lost,
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
  chapters/          the course content, one folder per puzzle, no code
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
  users/             local state (gitignored): per-profile dirs + settings.json
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

Adding a chapter is content-only, puzzle folders on disk, zero engine
changes, which is exactly what the architecture was shaped for.

## Requirements

Python 3.8+, standard library only. No installation, no dependencies. The
shell shortcuts target zsh (the macOS default); everything also works by
prefixing commands with `python3 play.py` on any platform.

## License

[MIT](LICENSE), © 2026 Ronald Karel Grant
