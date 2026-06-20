The **tally** pattern counts how many times each distinct thing appears, using a
dict whose keys are the things and whose values are running counts.

- For each item, `counts[k] = counts.get(k, 0) + 1` reads the current count
  (`0` the first time the key is seen, via `.get`'s default) and writes one more.
- Start from an empty dict `{}`; keys appear as they're first encountered.
- The standard-library `collections.Counter` does this in one step, but the
  `.get(k, 0) + 1` idiom shows exactly what's happening.

```python
counts = {}
for w in ["a", "b", "a"]:
    counts[w] = counts.get(w, 0) + 1   # {'a': 2, 'b': 1}
```
