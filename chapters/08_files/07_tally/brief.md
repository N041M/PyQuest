# 8.7 -- A frequency report

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
