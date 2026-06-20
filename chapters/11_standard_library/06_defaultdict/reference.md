**`defaultdict`** (from **`collections`**) is a `dict` that supplies a default for
a missing key automatically. You pass it a **factory** — a zero-argument callable
that builds the default — and the first time you read or touch an absent key, it
calls the factory, stores the result, and uses it.

- `defaultdict(list)` makes a fresh `[]` for each new key, so `d[k].append(x)`
  works with no "if key not in d" setup — the grouping idiom.
- `defaultdict(int)` makes `0` for each new key, so `d[k] += 1` tallies.
- Only **lookup** of a missing key triggers the factory; it's otherwise an
  ordinary dict. `dict(d)` converts to a plain dict, and a *genuinely* missing
  key still reads as the default rather than raising.

```python
from collections import defaultdict

groups = defaultdict(list)
groups[5].append("hello")    # key 5 auto-starts as []
groups                       # defaultdict(<class 'list'>, {5: ['hello']})
```
