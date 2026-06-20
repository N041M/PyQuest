A **slice** `s[start:stop]` returns a new string containing the characters from
position `start` up to **but not including** `stop` — a *half-open* range. The
length of the result is `stop - start` (when both are in range).

- `s[2:5]` gives the characters at indexes 2, 3, 4 — three characters.
- Either bound may be omitted: `s[:3]` starts at the beginning, `s[3:]` runs to
  the end, and `s[:]` copies the whole string.
- Slicing never raises for out-of-range bounds — it clamps. `s[:100]` on a short
  string just returns all of it.

```python
s = "Python"
s[0:3]    # 'Pyt'
s[:2]     # 'Py'
s[2:]     # 'thon'
```
