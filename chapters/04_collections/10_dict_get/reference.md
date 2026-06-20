**`d.get(key, default)`** looks a key up safely: it returns the value if the key
is present, otherwise the `default` — without raising. With no default it returns
`None` for a missing key.

- Use it instead of `d[key]` whenever a missing key is a normal, expected case
  rather than a bug.
- It powers the **tally** idiom: `counts[k] = counts.get(k, 0) + 1` reads the
  running count (0 the first time) and writes the new one.
- `.get` only reads; it never inserts the key (unlike `setdefault`).

```python
ages = {"Ada": 36}
ages.get("Ada", 0)     # 36
ages.get("Nobody", 0)  # 0  -- no KeyError
```
