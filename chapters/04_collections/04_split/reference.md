**`s.split()`** breaks a string into a **list of pieces**. With no argument it
splits on runs of **whitespace** and discards leading/trailing blanks — the usual
way to get the words of a line.

- `s.split(sep)` splits on the exact separator `sep`, keeping empty pieces
  between adjacent separators (`"a,,b".split(",")` is `["a", "", "b"]`).
- `s.split(sep, maxsplit)` splits at most `maxsplit` times — handy to peel off a
  prefix, e.g. `"key=a=b".split("=", 1)` is `["key", "a=b"]`.
- It is the inverse of `join` (next).

```python
"the quick fox".split()        # ['the', 'quick', 'fox']
"2024-01-15".split("-")        # ['2024', '01', '15']
```
