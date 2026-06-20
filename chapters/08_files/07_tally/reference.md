A **frequency report** is a three-stage file pipeline: **read** the file, **tally**
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
