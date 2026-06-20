**`zip(a, b)`** walks several iterables **in step**, yielding one tuple of
matching items per pass — the *i*-th from each. It pairs up parallel sequences
without indexing.

- `for x, y in zip(xs, ys):` binds `x` and `y` to the matching items each pass.
- It stops at the **shortest** input, so extra items in a longer one are ignored.
- Any number of iterables can be zipped; `dict(zip(keys, values))` builds a dict
  from two parallel lists.

```python
names, scores = ["Ada", "Linus"], [90, 85]
for n, s in zip(names, scores):
    print(n, s)           # Ada 90 / Linus 85
```
