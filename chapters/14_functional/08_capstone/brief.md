# 14.8 -- Capstone: a ranked shortlist

## Concept

The chapter's tools chain into a **pipeline**. Given a list of `(name, score)`
records, build a shortlist:

1. **`filter`** to the records that meet a threshold,
2. **`sorted`** with a `key=lambda` (and `reverse=True`) to rank them high to low,
3. **`map`** out just the names.

```python
records = [("Ada", 90), ("Linus", 70), ("Grace", 95)]
qualified = filter(lambda r: r[1] >= 80, records)
ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
list(map(lambda r: r[0], ranked))     # ['Grace', 'Ada']
```

Each record is a tuple, so `r[0]` is the name and `r[1]` the score.

## Your task

Define `passing(records, threshold)` that takes a list of `(name, score)` tuples
and returns the **names** of those with `score >= threshold`, ordered by score
**highest first**, built with `filter`, `sorted(key=lambda ...)`, and `map`.

## Done when

- `passing([("Ada", 90), ("Linus", 70), ("Grace", 95)], 80)` returns
  `["Grace", "Ada"]`.
- `passing([], 50)` returns `[]`; a threshold above every score returns `[]`.
- The result is built by filtering, sorting by a lambda key, and mapping -- a
  pipeline of the chapter's tools.
