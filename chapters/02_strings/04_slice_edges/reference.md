Slice bounds can be **negative**, counting from the end, and the two styles mix
freely. `s[1:-1]` drops the first and last character — start at index 1, stop
just before the last.

- A slice whose start is at or past its stop is **empty**, not an error:
  `s[3:3]` and `s[5:2]` both give `""`.
- Out-of-range bounds are clamped, so slicing is forgiving where plain indexing
  raises: `s[1:99]` is fine.
- Because the stop is exclusive, `s[:-1]` removes exactly the last character and
  `s[1:]` removes the first.

```python
s = "Python"
s[1:-1]   # 'ytho'  -- both ends trimmed
s[2:2]    # ''      -- empty, not an error
```
