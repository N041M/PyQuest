# PyQuest translations -- language 'example' -- chapter 08_files -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

"8.1 brief": r"""# 8.1 -- Opening a file

## Concept

So far every value came from a literal you typed or from `input()`. Real
programs also read **files** -- text already sitting on disk.

`open(name)` hands you a *file object*. The clean way to use one is a `with`
block:

```python
with open("note.txt") as f:
    text = f.read()
```

- `with open(...) as f:` opens the file and binds it to `f`;
- `f.read()` returns the file's **entire contents** as one string;
- when the block ends, Python **closes the file for you** -- even if the code
  inside raised. That automatic close is the whole reason to prefer `with`
  over a bare `open()`.

The file is found relative to where the program runs, so `"note.txt"` means "a
file called note.txt next to me".

## Example

If `note.txt` contains:

```
buy milk
call sam
```

then `text` is the string `"buy milk\ncall sam\n"` -- newlines and all.

## Your task

A file named `note.txt` sits beside your program. Read its whole contents and
print them.

## Done when

- The program prints exactly what `note.txt` contains.
- It works whatever the file holds -- one line, many lines, or nothing.
- You opened the file with a `with` statement.
""",

"8.1 hints": r"""A `with open(name) as f:` block gives you the file as `f`. Inside it, ask the
file for everything it holds.

---

`f.read()` returns the whole file as a single string. Store it, then print it
after (or inside) the block.

---

with open("note.txt") as f:
    text = f.read()
print(text)
""",

"8.1 reference": r"""**`open(name)`** connects to a file on disk; the **`with`** statement manages it
so the file is **closed automatically** when the block ends, even if an error
occurs. Inside the block, the file object `f` provides the contents.

- `with open(name) as f:` opens for **reading** text (the default mode `"r"`) and
  binds the open file to `f`.
- **`f.read()`** returns the entire contents as one string. (`f.read(n)` reads at
  most `n` characters.)
- Opening a path that doesn't exist raises `FileNotFoundError`. Always use `with`
  rather than a bare `open` — it guarantees the close.

```python
with open("notes.txt") as f:
    text = f.read()      # whole file as a string
# file is closed here
```
""",

"8.2 brief": r"""# 8.2 -- A file, line by line

## Concept

`f.read()` gives you everything at once. More often you want the file **one
line at a time** -- and a file object is *iterable*, so a `for` loop walks its
lines for you:

```python
with open("tasks.txt") as f:
    for line in f:
        ...
```

One catch: each `line` still carries the newline that ended it -- `"wash\n"`,
not `"wash"`. Strip it with `line.strip()` (3.7) before you use the text, or
your output grows blank lines.

## Example

For a `tasks.txt` of:

```
wash
cook
sleep
```

numbering each line gives:

```
1. wash
2. cook
3. sleep
```

`enumerate` (5.5) is the natural fit -- start it at `1`:

```python
for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")
```

## Your task

Read `tasks.txt` and print every line **numbered from 1**, in the form
`1. wash`. Drop the trailing newline so there are no stray blank lines.

## Done when

- Each line is printed as `<number>. <text>`, counting from 1.
- It works for a file of any length.
- You opened the file with `with` and looped over it with `for`.
""",

"8.2 hints": r"""A file object is iterable: `for line in f:` hands you one line per pass.

---

`enumerate(f, start=1)` gives `(1, firstline), (2, secondline), ...`. Each line
still ends in `\n` -- use `line.strip()` to drop it.

---

with open("tasks.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")
""",

"8.2 reference": r"""A file object is **iterable**: looping over it yields the file **one line at a
time**, without loading the whole thing into memory. This is the standard way to
process a file line by line.

- `for line in f:` binds `line` to each line **including its trailing newline**
  `"\n"`; call `line.strip()` (or `.rstrip("\n")`) to drop it.
- It reads lazily, so it handles large files comfortably.
- `f.readlines()` instead returns a **list** of all lines at once — fine for
  small files, wasteful for big ones.

```python
with open("log.txt") as f:
    for line in f:
        print(line.strip())   # one line per pass, newline removed
```
""",

"8.3 brief": r"""# 8.3 -- Adding up a file

## Concept

A file is always **text**. A line that looks like `42` arrives as the string
`"42\n"`, not the number 42 -- so before you can do arithmetic you must convert
it with `int()` (1.11), exactly as you did with `input()`.

`int()` is happy to ignore the surrounding whitespace, so `int("42\n")` is
`42` -- you don't even need to strip first.

```python
total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
```

## Example

For a `prices.txt` of:

```
10
25
7
```

the total is `42`.

## Your task

`prices.txt` holds one whole number per line. Read them, add them all up, and
print the total.

## Done when

- The program prints the sum of every number in the file.
- Negative numbers and a single-line file both work.
- You opened the file with `with` and converted each line with `int()`.
""",

"8.3 hints": r"""Start a running total at 0, open the file, and loop over its lines.

---

Each line is a string like `"25\n"`. `int(line)` turns it into a number you can
add. Print the total after the loop.

---

total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
print(total)
""",

"8.3 reference": r"""File contents are always **text**, so a line like `"42\n"` is a *string*. To do
arithmetic you must convert each line to a number first.

- `int(line)` parses an integer; it tolerates surrounding whitespace (including
  the trailing newline), so `int("42\n")` is `42`. Use `float(line)` for
  decimals.
- A blank or non-numeric line raises `ValueError` — skip blanks
  (`if not line.strip(): continue`) or wrap the conversion in `try`.
- Accumulate as you go: keep a running total and add each parsed value.

```python
total = 0
with open("nums.txt") as f:
    for line in f:
        total += int(line)    # text -> number, then add
```
""",

"8.4 brief": r"""# 8.4 -- Writing a file

## Concept

Reading is half the story; programs also **create** files. Open with the mode
`"w"` (for *write*) and call `.write()`:

```python
with open("out.txt", "w") as f:
    f.write("hello\n")
```

Two things to know:

- `"w"` makes a brand-new file (or **empties** an existing one), then writes.
- `.write()` puts down **exactly** the text you give it -- no automatic
  newline like `print()` adds. If you want line breaks, include `"\n"`
  yourself.

A common shape is **read one file, write another**:

```python
with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
```

## Example

If `in.txt` contains `quiet please`, then `out.txt` should end up holding
`QUIET PLEASE`.

## Your task

Read `in.txt`, and write its contents **in upper case** (7.x `.upper()` from
2.7) into a new file called `out.txt`.

## Done when

- `out.txt` contains exactly the text of `in.txt`, uppercased.
- An empty `in.txt` produces an empty `out.txt` -- no crash.
- You used `with` and opened `out.txt` in `"w"` mode.
""",

"8.4 hints": r"""Two steps: first read in.txt into a string, then open out.txt in `"w"` mode and
write the uppercased string.

---

`open("out.txt", "w")` is the write half; `text.upper()` does the uppercasing.
`.write()` writes the string as-is.

---

with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
""",

"8.4 reference": r"""Opening with mode **`"w"`** opens a file for **writing**. It **creates** the file
if absent and **truncates** it (empties it) if it already exists, so existing
contents are lost.

- **`f.write(text)`** writes a string and, unlike `print`, adds **no** trailing
  newline — include `"\n"` yourself where you want line breaks.
- `f.write` takes strings only; convert numbers with `str()` or an f-string
  first.
- Use `with` so the data is flushed and the file closed properly.

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")   # newlines are explicit
```
""",

"8.5 brief": r"""# 8.5 -- Append, don't overwrite

## Concept

Mode `"w"` is ruthless: it **empties** the file before writing. That's wrong
when you want to *add* to a file -- a log you keep growing, say. For that there
is mode `"a"` (for *append*):

```python
with open("log.txt", "a") as f:
    f.write("another line\n")
```

`"a"` leaves everything already in the file untouched and writes your new text
**after** it (and if the file doesn't exist yet, `"a"` simply creates it).
Same `.write()`, same need to add your own `"\n"` -- only the mode letter
changes, and that one letter is the whole difference between "add to" and
"wipe and replace". The whole point of `"a"` is that you *don't* read the file
first -- you just write at the end.

## Example

If `log.txt` already contains:

```
woke up
ate
```

then appending the line `ran` leaves it holding `woke up`, `ate`, `ran` -- all
three, in order.

## Your task

A file `log.txt` already exists. Read one line of text from input (`input()`)
and **append** it to `log.txt` as a new line, keeping everything already there.

## Done when

- The original contents of `log.txt` are still present, in order.
- The new entry is added as its own line at the end.
- Using `"w"` would erase the old lines -- so you must use `"a"`.
""",

"8.5 hints": r"""Read the entry with `input()`, then open the file in a mode that *keeps* what
is already there.

---

Mode `"a"` appends instead of wiping. Don't forget the `"\n"` so the new entry
sits on its own line.

---

entry = input()
with open("log.txt", "a") as f:
    f.write(entry + "\n")
""",

"8.5 reference": r"""Mode **`"a"`** opens a file for **appending**: writes go to the **end**, and any
existing contents are kept. It's the non-destructive counterpart to `"w"`.

- `"a"` creates the file if it doesn't exist; if it does, `f.write` adds after
  what's already there — nothing is overwritten.
- `"w"` empties the file first; reach for `"a"` to grow a log or accumulate
  results across runs.
- As with `"w"`, newlines are not added for you.

```python
with open("log.txt", "a") as f:
    f.write("another entry\n")   # added at the end, old lines kept
```
""",

"8.6 brief": r"""# 8.6 -- Filtering lines into a new file

## Concept

Put reading and writing together and you get the everyday data chore: walk an
input file line by line, **decide** which lines to keep (3.2 `if`), and write
just those to an output file.

```python
with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if keep(line):
            f.write(line)
```

`f.readlines()` reads the whole file into a list of lines up front -- handy
when you want to finish reading before you start writing.

A line that is empty or only spaces is "blank": `line.strip()` returns `""` for
it, and an empty string is falsey (3.1), so `if line.strip():` is a tidy test
for "this line has real content".

## Example

From a `lines.txt` of:

```
keep me

and me
```

the blank middle line is dropped, leaving `keep me` and `and me`.

## Your task

Read `lines.txt` and write only its **non-blank** lines to `kept.txt`, in the
same order. Drop any line that is empty or just whitespace.

## Done when

- `kept.txt` holds exactly the non-blank lines of `lines.txt`, in order.
- A file with no blank lines is copied unchanged; an all-blank file yields an
  empty `kept.txt`.
- You used `with`, a loop, and an `if` to decide what to keep.
""",

"8.6 hints": r"""Read all the lines first, then open the output file in `"w"` mode and loop,
writing only the ones you want to keep.

---

`if line.strip():` is true only when the line has real content. Write the
original `line` (it already ends in `\n`), not a stripped copy.

---

with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)
""",

"8.6 reference": r"""A **filtering** pass reads one file, keeps only the lines an `if` accepts, and
writes them to another — the file form of the comprehension-with-`if` pattern.

- Open the source for reading and the destination for writing, loop the source,
  and `f_out.write(line)` only when the line passes your test.
- Lines from the input keep their newline, so writing them back reproduces line
  breaks without adding any.
- Reading and writing the **same** path at once is unsafe; write to a new file
  (or collect results, then write).

```python
with open("all.txt") as src, open("kept.txt", "w") as out:
    for line in src:
        if "ERROR" in line:
            out.write(line)       # keep only matching lines
```
""",

"8.7 brief": r"""# 8.7 -- A frequency report

## Concept

This puzzle puts the chapter together with the dictionary tally from 5.9: read
a file, **count** something across it, and write the result to another file.

Read the words in, then tally them with a dict (the `dict.get` pattern):

```python
with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

`f.read().split()` reads the whole file and splits on any whitespace, so it
hands you a flat list of words however they were spaced.

Then write the report, **sorted by count, highest first**, ties broken
alphabetically. `sorted` with a `key` (5.4) does both at once:

```python
for w in sorted(counts, key=lambda w: (-counts[w], w)):
    f.write(f"{w}: {counts[w]}\n")
```

The key `(-counts[w], w)` sorts by descending count (negate it) and then by the
word itself for ties.

## Example

A `words.txt` of `fig fig pear fig pear` becomes a `report.txt` of:

```
fig: 3
pear: 2
```

## Your task

Count how often each word appears in `words.txt`, and write `report.txt` with
one `word: count` line per distinct word -- ordered by count (highest first),
ties in alphabetical order.

## Done when

- Each distinct word appears once, as `word: count`.
- Lines are ordered by descending count, alphabetical within a tie.
- You used `with`, a dict to tally, and read the words from the file.
""",

"8.7 hints": r"""Read the words into a list, then build a dict of counts with the
`counts[w] = counts.get(w, 0) + 1` pattern from 5.9.

---

To order the report, sort the dict's keys with a key function:
`sorted(counts, key=lambda w: (-counts[w], w))` gives highest count first,
alphabetical within ties. Write each `f"{w}: {counts[w]}\n"`.

---

with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as f:
    for w in sorted(counts, key=lambda w: (-counts[w], w)):
        f.write(f"{w}: {counts[w]}\n")
""",

"8.7 reference": r"""A **frequency report** is a three-stage file pipeline: **read** the file, **tally**
into a dict, then **write** a sorted summary.

- Loop the lines (or words), counting with `counts[k] = counts.get(k, 0) + 1`.
- Order the result with `sorted(counts.items(), ...)` — by key, or by count with
  `key=lambda kv: kv[1]` (add `reverse=True` for most-frequent first).
- Write each pair as a formatted line, e.g. `out.write(f"{word}: {n}\n")`.

It composes the file I/O of this chapter with the dict and `sorted` tools from
earlier ones.

```python
counts = {}
with open("words.txt") as f:
    for line in f:
        w = line.strip()
        counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as out:
    for w, n in sorted(counts.items()):
        out.write(f"{w}: {n}\n")
```
""",

"8.8 brief": r"""# 8.8 -- Capstone: a ranking report

## Concept

This capstone is a real little program: read a file of records, rank them, and
write a formatted report -- using split (4.4), unpacking (4.7), `int()` (1.11),
`sorted` with a key (5.4), f-strings (2.10), and files (this chapter) together.

`scores.txt` has one record per line, a name and a score separated by a space:

```
alice 40
bob 25
cara 40
```

Each line splits into its two fields:

```python
name, score = line.split()
score = int(score)
```

You want `ranking.txt` to list players from highest score to lowest (ties in
alphabetical order), then a final total line:

```
alice - 40
cara - 40
bob - 25
Total: 105
```

Note the exact format: `name - score` per player (spaces around the dash), and
a closing `Total: <sum>` line.

## Your task

Read `scores.txt`, and write `ranking.txt` with one `name - score` line per
player ordered by score (highest first, ties alphabetical), followed by a final
`Total: <sum of all scores>` line.

## Done when

- Players are listed `name - score`, highest score first, ties alphabetical.
- The last line is `Total: ` followed by the sum of every score.
- A single-player file works, and you used `with` for both files.
""",

"8.8 hints": r"""Read the lines, and for each one `name, score = line.split()`; convert the
score with `int()`. Collect the pairs into a list.

---

Sort with `key=lambda p: (-p[1], p[0])` for highest score first, ties
alphabetical. Write each `f"{name} - {score}\n"`, then a final
`f"Total: {sum_of_scores}\n"`.

---

with open("scores.txt") as f:
    lines = f.read().splitlines()
players = []
for line in lines:
    name, score = line.split()
    players.append((name, int(score)))
players.sort(key=lambda p: (-p[1], p[0]))
total = sum(score for name, score in players)
with open("ranking.txt", "w") as f:
    for name, score in players:
        f.write(f"{name} - {score}\n")
    f.write(f"Total: {total}\n")
""",

"8.8 reference": r"""The capstone reads **records**, parses each into usable fields, ranks them, and
writes a **formatted report** — the shape of real data work.

- **Parse**: split each line into fields and convert types (e.g.
  `name, score = line.split(","); score = int(score)`), collecting the records
  into a list.
- **Rank**: `sorted(records, key=..., reverse=True)` orders by the field that
  matters.
- **Format**: write aligned, human-readable lines, using f-string field widths
  (`f"{name:<12}{score:>5}"`) so columns line up.

```python
records = []
with open("scores.csv") as f:
    for line in f:
        name, score = line.strip().split(",")
        records.append((name, int(score)))
with open("ranked.txt", "w") as out:
    for name, score in sorted(records, key=lambda r: r[1], reverse=True):
        out.write(f"{name:<12}{score:>5}\n")
```
""",
}
