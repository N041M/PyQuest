# Getting started

A step-by-step first session with PyQuest. For the full command reference,
difficulty modes, and project layout, see the [README](README.md).

PyQuest is a Python course you run from the terminal. You read a short brief,
write code in a file in your own editor, then run one command to check it and
unlock the next puzzle. Nothing to install; it uses only Python 3.

> Don't want to set up Python locally? Open the repo in a **GitHub Codespace**
> (green *Code* button → *Codespaces*) and skip straight to step 2.

## 1. Go into the PyQuest folder

```
cd pyquest
```

If that says "no such file or directory", you are not in the folder that
*contains* `pyquest`. `cd` to wherever you keep it first. Tip: in your
editor, right-click the `pyquest` folder and "Open in Integrated Terminal".

## 2. Open the menu

```
python3 start.py
```

`start.py` is the easy way in: it checks your Python, turns on the short
commands (`check`, `hint`, ...) for this session, and opens the menu. (If you
would rather not use the shortcuts, `python3 start.py menu` just opens the
menu.)

This is the main menu, shown before any puzzles. Pick a number (arrow keys work
too, where your terminal supports them):

```
1  start          jump onto the current puzzle
2  select level   choose where to begin
3  textbook       the technical reference for what you've reached
4  stats          your numbers: attempts, hints, clean solves
5  map            the chapter tree (Core · Advanced · Projects)
6  settings       theme · difficulty · profiles · shortcuts · language
0  quit
```

Once you pick **1 start**, solving is done with short, one-shot commands. (The
card's bottom row is also arrow-selectable — the "play cockpit" — on a capable
terminal.)

## 3. Enable the short commands (recommended)

In the menu choose **6 settings → shortcuts**, then pick:

- **local**: works in this terminal only, nothing saved (run the `source …`
  line it shows you), or
- **persistent**: adds one line to your `~/.zshrc` (remove it any time with
  `uninstall`).

After that you can type `check` instead of `python3 start.py check`. Open a new
terminal, or run `source ~/.zshrc` once.

You never *have* to install the shortcuts, every command also works prefixed
with `python3 start.py` (so `python3 start.py hint`, `python3 start.py next`, and
so on). If a short command says `command not found`, the shortcuts just aren't
active in this terminal: run `source ~/.zshrc`, open a new terminal, or use
the long form.

## 4. The loop

Read the brief, write code, save, check, move on:

1. **Read** `brief.md` in your editor, it explains the idea and the task.
2. **Write** your code in `work.py`, your profile's single workspace file;
   PyQuest loads the current puzzle into it (`start` shows its path).
3. **Save** the file. Unsaved edits are the #1 reason a correct-looking
   answer fails the check.
4. **Check** it: `check`
5. When it passes, move on when ready: `next`

Run `start` any time to see where you are and the two file paths (`brief.md`
to read, `work.py` to edit).

Stuck? `hint` reveals up to three escalating hints, and `solution` shows the
reference answer with an explanation of why it works.

## 5. Good to know

- **Your work is always saved.** Every `check` archives your code; moving
  between puzzles (`next`, `goto 2.4`) saves the current draft and restores
  the target's saved code. Nothing is lost.
- **Difficulty.** `mode easy`, `mode normal`, or `mode hard`: see the
  [README](README.md#difficulty-modes) for what each changes.
- **Profiles.** `user <name>` switches or creates a profile; everyone's
  progress stays separate under `users/<name>/`.
- **Themes.** `theme <name>` recolours everything and remembers your choice.
  Make your own by dropping a JSON file in `themes/` (see
  [themes/README.md](themes/README.md)).
- **Clearing.** `restart` clears just the current puzzle (blank code + drop its
  progress); `retry` blanks the workspace but keeps it solved. To erase the
  whole profile, `wipe profile` -- the second word is required, so it can't go
  off by accident.
