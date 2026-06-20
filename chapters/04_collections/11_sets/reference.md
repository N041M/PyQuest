A **set** is an unordered collection of **unique** items: `{1, 2, 3}`. It models
"a group of distinct things" and tests membership fast.

- Building a set from a sequence **drops duplicates**: `set([1, 1, 2])` is
  `{1, 2}`. The empty set is `set()` — `{}` is an empty *dict*.
- **`x in s`** tests membership and is much faster than scanning a list, because
  sets are hash-based.
- Sets are unordered (no indexing, no slicing) and hold only immutable items.
  Add with `.add(x)`, remove with `.discard(x)`.

```python
seen = set()
seen.add("a"); seen.add("a")   # {'a'} -- duplicate ignored
"a" in seen                    # True
set([3, 1, 3, 2])              # {1, 2, 3}
```
