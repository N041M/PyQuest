The capstone reads **records**, parses each into usable fields, ranks them, and
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
