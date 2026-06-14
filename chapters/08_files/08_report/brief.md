# 8.8 -- Capstone: a ranking report

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
