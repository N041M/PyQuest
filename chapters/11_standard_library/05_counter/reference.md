**`Counter`** (from the **`collections`** module) is a `dict` subclass that
tallies an iterable in one call: `Counter(items)` returns a mapping of each
distinct item to how many times it appears — the `counts.get(k, 0) + 1` loop,
already written.

- Being a dict, it supports everything a dict does (`c[key]`, `c.items()`,
  `key in c`) and compares **equal** to a plain dict with the same counts.
- A **missing** key reads as `0` rather than raising `KeyError`, which suits
  counting.
- **`c.most_common(n)`** returns the `n` highest-count `(item, count)` pairs,
  already sorted — the report step for free. Counters also add and subtract
  (`c1 + c2`) to combine tallies.

```python
from collections import Counter

c = Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
c["a"]                    # 3
c["z"]                    # 0  -- no KeyError
c.most_common(1)          # [('a', 3)]
```
