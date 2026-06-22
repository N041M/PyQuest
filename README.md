# PyQuest

**Learn Python by doing, one small puzzle at a time.**

PyQuest gives you a series of short, friendly puzzles. You read a quick
explanation, write a few lines of code in your own editor, and run one command
to check your answer. Get it right, and the next puzzle unlocks.

It starts at the very beginning, `print("hello")`, and builds up gently
through **142 puzzles in 16 chapters**, grouped into three tiers:

- **Core** (Ch 1–14): the basics, text, decisions and loops, lists and
  dictionaries, power tools, functions, errors, files, classes, generators, the
  standard library, regular expressions, dates and times, and functional tools.
- **Advanced** (Ch 15): inheritance, `super`, properties, and the special
  methods (`__eq__`, `__lt__`, …).
- **Projects** (Ch 16+): build a small app over a few steps — including
  fixing broken code — and finish a low-guidance capstone on your own.

Each puzzle adds just one new idea, so you're never thrown in the deep end.

There's nothing to install and no complicated setup. If you have Python 3, or
just a web browser (see **Run in a Codespace** below), you're ready, even if
you've never written code before.

> Works with any Python 3.8+ · nothing to install · free and open-source (MIT)

---

## What you get

- **142 bite-sized puzzles, one idea each**: from `print` all the way to
  inheritance and your own small project, in steps you can actually keep up with.
- **Friendly, plain-English feedback**: when something's wrong, you get a
  clear note about *what* went wrong, not a wall of scary red error text.
- **You can't fake it**: the checker runs your code and changes the numbers
  each time, so copying an answer or hard-coding the result won't work. The
  only way forward is to genuinely get it, which means you actually learn.
- **Help when you're stuck**: three hints per puzzle that get more specific,
  plus a full worked solution with a "why it works" explanation when you want it.
- **A built-in textbook**: `textbook` writes a technical reference for the
  topics you've reached, so the language is documented as you go.
- **Go at your own pace**: pick an easier or harder mode, and your progress
  saves automatically, so you can stop and pick up again any time.
- **Translatable**: the interface and textbook can be localized with drop-in
  community language packs (`lang/`), English being the default and fallback.

## Quick start

Open a terminal (the text window where you type commands), go into the PyQuest
folder, and run:

```
cd pyquest
python3 start.py
```

That one command checks your Python, turns on the short commands (`check`,
`hint`, `next`, ...) for this session, and drops you into the menu. Pick a level
and start solving. It works the same on macOS, Linux, Codespaces, and Windows:
`start.py` sets up whichever shell you have, just for this session, and changes
nothing permanently.

> No Python on your computer, or new to all this? You can run PyQuest in your
> web browser instead: jump to [Run in a Codespace](#run-in-a-codespace) below.

Prefer to drive it by hand? Every command also works as
`python3 start.py <command>` (so `python3 start.py status` shows your progress,
`python3 start.py check` checks your work). For the current puzzle you work in
two files:

- `brief.md`: read this. It explains the concept and the task.
- `work.py`: edit this. One workspace file per profile (at
  `users/<name>/work.py`); PyQuest loads each puzzle's starter into it as you
  go (`status` shows the exact path).

Write your code, **save the file in your editor** (unsaved edits are the most
common reason a correct-looking answer fails), then check it:

```
python3 start.py check
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
   python3 start.py
   ```

Everything is already set up for you: the right version of Python, the editor's
Python support, and PyQuest itself. (The setup lives in the `.devcontainer`
folder, which you never have to touch.) Codespaces is free
for personal use within GitHub's monthly allowance, and you can delete your
Codespace whenever you're done.

New to the project? [GETTING_STARTED.md](GETTING_STARTED.md) walks through the
first session step by step.

## Terminal setup

PyQuest needs nothing beyond Python 3: `python3 start.py <command>` always
works in any shell, on any platform. The setup below is optional comfort.

### Short commands

Typing `python3 start.py` every time gets old. PyQuest ships shell shortcuts so
you can type `check`, `hint`, `map`, and so on from any directory:

```
python3 start.py setup
```

`setup` checks for Python 3 and offers two ways in:

- **local**: it prints a `source` line you run once; the shortcuts work in
  **this terminal only** and nothing on your system is changed.
- **persistent**: `python3 start.py setup persist` adds one line to your shell's
  startup file (`~/.zshrc`, or `~/.bashrc` on bash), so every new terminal has
  the shortcuts. It is safe to run more than once: it never duplicates the line
  and never touches your code or progress (it edits that one file and nothing
  else).

After persisting, open a new terminal or re-source that file once (e.g.
`source ~/.zshrc`). The same setup is also reachable from the `menu`
(option **6 settings → shortcuts**).

If you would rather do it by hand, add this line to the end of `~/.zshrc` (or
`~/.bashrc`, sourcing `shell/pyquest.bash`), replacing the path with wherever
the folder actually lives:

```sh
[ -f "/path/to/pyquest/shell/pyquest.zsh" ] && source "/path/to/pyquest/shell/pyquest.zsh"
```

The shortcuts file resolves its own location, so once that line points at it
you can move or rename the PyQuest folder without editing anything inside it.

Once the shortcuts are loaded, **Tab completion** comes with them: `goto <Tab>`
lists puzzle ids, `theme <Tab>` the themes, `user <Tab>` your profiles, and a
bare `pq <Tab>` (or `start <Tab>`) the verbs. The candidate lists are generated
from the live course, so they never go stale.

### Windows (PowerShell)

On Windows the same shortcuts ship as a PowerShell script. From the PyQuest
folder, load them into the current terminal:

```powershell
. .\shell\pyquest.ps1
```

Now `check`, `hint`, `map`, `next`, and the rest work, with `pq` as the umbrella
command (`pq`, `pq check`, `pq wipe profile`). To get them in every new terminal, run
`Install-PyQuest` once (it adds one line to your PowerShell profile); remove
them later with `uninstall`. If Windows blocks the script the first time, allow
local scripts once with `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
On any platform, `python start.py <command>` (or `py -3 start.py <command>`)
always works without any of this.

### Uninstalling

Run `uninstall` (or `python3 start.py uninstall`). It removes the line from
`~/.zshrc` **and** clears the shortcut functions from the current terminal,
or just delete the `# PyQuest shell shortcuts` line from `~/.zshrc` yourself.

### Clearing progress

Two separate verbs, deliberately named so they can't be confused:

- `restart` clears **just the current puzzle** (blank code + drop its progress),
  so you can solve it fresh. (`retry` is the gentler one: it blanks the
  workspace but keeps the puzzle marked solved.)
- `wipe profile` erases the **whole profile** — every completed puzzle, all
  saved code, the workspace. It is irreversible, so it only fires with that
  explicit second word; a bare `wipe` just explains what it would do.

### How PyQuest treats your terminal

- **Colour degrades gracefully.** Output is plain text whenever it is piped or
  redirected (not a TTY), and the [`NO_COLOR`](https://no-color.org/)
  convention is respected.
- **Frames fit your window.** Boxes and banners size themselves to the live
  terminal width (capped for readability) instead of assuming 80 columns.
- **Nothing blocks a pipe.** The interactive surfaces (the `menu`, bare `goto`,
  and the play cockpit — the card's arrow-selectable nav row) degrade to a plain
  print when stdin is not a terminal, so scripts and tests never hang.
- **Shell support.** The shortcuts ship for zsh (`shell/pyquest.zsh`, the macOS
  default), bash (`shell/pyquest.bash`, Linux and Codespaces), and Windows
  PowerShell (`shell/pyquest.ps1`, see above). `setup` installs the file that
  matches your shell. On anything else, the `python3 start.py` long form always
  works.

## Commands

Every command runs once, prints plain text, and exits. With the shortcuts
installed, drop the `python3 start.py` prefix (`export`/`import` keep the `start`
umbrella — `start export` — since the shell owns a bare `export`).

| Command | What it does |
|---|---|
| `python3 start.py` | open the menu — every session starts here (bare `start` / `pq` with the shortcuts on); a cold terminal also sets up the session |
| `python3 start.py status` | show progress and the current puzzle |
| `python3 start.py menu` | open the main menu — start here, or back out of a puzzle (alias `back`) |
| `python3 start.py help` | list every command, highlighting the ones available in your current space |
| `python3 start.py check` | validate your `work.py` against the puzzle |
| `python3 start.py hint` | reveal the next hint (three per puzzle, escalating) |
| `python3 start.py solution` | show the reference solution and why it works |
| `python3 start.py map` | show the chapter/puzzle tree with progress |
| `python3 start.py search <word>` | find a puzzle by a word in its title or concept (`find` alias) |
| `python3 start.py resume` | jump to the first puzzle you haven't solved yet |
| `python3 start.py stats` | your numbers: attempts, hints, clean first-try solves, per-chapter completion (`score` alias) |
| `python3 start.py textbook` | write a syntax & tips markdown file and link you to it — what you've reached (`textbook all` for the whole language; `ref` alias) |
| `python3 start.py next` | move on to the next puzzle — only once this one is solved |
| `python3 start.py goto` | pick a puzzle from a list (`goto 2` = first open puzzle of chapter 2) |
| `python3 start.py goto 2.4` | jump to a puzzle by id (restores your saved code) |
| `python3 start.py load 2.4` | same as `goto`, reload a puzzle's saved code |
| `python3 start.py skip` | give up and move on without solving (not in hard mode) |
| `python3 start.py note <text>` | jot a personal note on this puzzle (bare `note` shows it, `note clear` removes it); it appears on the card |
| `python3 start.py retry` | blank the workspace to practice again (stays solved; `replay` is an alias) |
| `python3 start.py restart` | start this puzzle over: blank code + clear its progress (`retry` keeps it solved) |
| `python3 start.py mode easy` | set difficulty: `easy` \| `normal` \| `hard` |
| `python3 start.py theme amber` | switch colour theme (or add your own in `themes/`) |
| `python3 start.py user alice` | switch or create a profile |
| `python3 start.py user rename alice bob` | rename a profile, keeping its progress |
| `python3 start.py user delete bob` | delete a profile (not the active one — switch away first) |
| `python3 start.py setup` | enable the short commands (local or persistent) |
| `python3 start.py uninstall` | remove the persistent shortcuts again |
| `python3 start.py wipe profile` | erase this whole profile: progress, saved code, workspace (needs the word `profile` to fire) |

## Difficulty modes

Set once with `mode <name>`; change it whenever you like.

| | Easy | Normal | Hard |
|---|---|---|---|
| Pointer shown automatically | yes | no | no |
| Hints | unlimited, anytime | on demand | only after 3 tries |
| `solution` | anytime | anytime | only after solving |
| `textbook` | anytime | anytime | sealed |
| `next` (needs a solve) | yes | yes | yes |
| `skip` past unsolved | yes | yes | no (must solve) |
| `goto` forward (ahead) | yes | back only | back only |

## How your work is saved

Every `check` archives your `work.py` into your profile's `answers.json`,
keyed by puzzle id. Switching puzzles (`next`, `skip`, `goto`) saves the
current draft and reloads the target puzzle's saved code, nothing is lost,
and `goto 1.1` brings back exactly what you wrote there. All saves are atomic.

`python3 start.py wipe profile` is the one true wipe: completed puzzles, attempts,
hints used (`progress.json`), all saved code (`answers.json`), and the
workspace files, which are regenerated from their starters. Your difficulty
mode is preserved. After a wipe you are genuinely back to a blank puzzle 1.1.
(For one puzzle instead of the whole profile, `restart` clears just that one.)

Each profile is its own folder under `users/`. `user <name>` switches or
creates one, `user rename <old> <new>` renames a profile keeping its progress,
and `user delete <name>` removes one (the active profile is protected — switch
away first). `stats` reflects any profile's numbers back at you: attempts,
hints, clean first-try solves, and per-chapter completion.

## Project layout

```
pyquest/
  start.py           the entry point: bare opens the session + menu;
                     start.py <command> runs one command (check, next, ...)
  engine/            the implementation, split by concern (see docs/ARCHITECTURE.md)
  tools/audit.py       mechanical checks: conformance + anti-sidestep replay attack
  docs/              ARCHITECTURE.md, SCHEMA.md, CONTRIBUTING.md, diagrams/ (UML)
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
  shell/             the zsh / bash / PowerShell shortcut scripts
  users/             local state (gitignored): per-profile dirs + settings.json
```

## Documentation

| Document | What it covers |
|---|---|
| [docs/](docs/README.md) | the documentation index — start here, organized by what you want to do |
| [GETTING_STARTED.md](GETTING_STARTED.md) | a learner's first session, step by step |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | module map, design invariants, how validation works |
| [docs/diagrams/](docs/diagrams/README.md) | UML architecture (Mermaid): overview + per‑module diagrams |
| [docs/SCHEMA.md](docs/SCHEMA.md) | file formats for authoring puzzles and projects |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | how to add a puzzle, the audit gate, project conventions |
| [themes/README.md](themes/README.md) | creating custom colour themes |
| [lang/README.md](lang/README.md) | translating the interface and textbook (language packs) |

## Roadmap

The course now runs through 16 chapters — the standard library, regular
expressions, dates and times, functional tools, and advanced classes all
shipped, and the first **project** chapter (build → debug → capstone) is in.
The detailed plan — ~300 more puzzles mapped out (new concept chapters, a
**data-structures & algorithms** track, real-world stdlib like sqlite/CLI/
concurrency, ten projects, and far more debug/extend/refactor puzzles) — is in
[docs/ROADMAP.md](docs/ROADMAP.md). In brief, what's next:

- **More projects.** The projects track (`kind` in `meta.json`: `build` /
  `debug` / `capstone`) is built for it — including debug puzzles that ship
  broken code to fix. Adding another is content-only.
- **More advanced chapters.** Context managers and `itertools` are natural next
  topics the construct-check machinery already covers (`uses_with` /
  `uses_with_open`, `uses_call` / `uses_call_over_param`). Decorators and type
  hints need a new check first: a liveness-anchored `uses_decorator(name)` (today
  `@property` is forced with a runtime reflection oracle, as in 15.4), and an
  AST-based hint check (type hints are erased at runtime, so behavior can't see
  them).
- **Community translations.** The i18n plumbing is done (`lang/`, with a
  `tools/check_pack.py` validator); language packs are welcome — nothing is
  translated yet.

Adding a chapter is content-only — puzzle folders on disk, zero engine
changes — which is exactly what the architecture was shaped for.

## Requirements

Python 3.8+, standard library only. No installation, no dependencies. The
shell shortcuts ship for zsh, bash, and Windows PowerShell; everything also
works by prefixing commands with `python3 start.py` on any platform.

## License

[MIT](LICENSE), © 2026 Ronald Karel Grant
