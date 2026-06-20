A **dictionary** (`dict`) maps **keys** to **values**: `{"a": 1, "b": 2}`. It is
the tool for lookup by name rather than by position.

- **`d[key]`** reads the value for a key; **`d[key] = value`** adds the key (if
  new) or updates it (if present). Keys are unique — assigning an existing key
  overwrites.
- Reading a **missing** key with `d[key]` raises `KeyError` (see `.get`, 4.10).
- Keys must be immutable (strings, numbers, tuples); values can be anything.
  `len(d)` counts the pairs; `key in d` tests for a key.

```python
ages = {"Ada": 36}
ages["Ada"]          # 36
ages["Linus"] = 21   # add a new pair
```
