A string is an ordered sequence of characters, and `s[index]` reads the one at a
given position. Positions are **zero-based**: the first character is `s[0]`, the
second `s[1]`, and so on.

- The result is itself a one-character string (Python has no separate character
  type).
- An index at or past the length raises `IndexError`; for a string of length
  *n*, the valid positions are `0` through `n - 1`.
- Strings are **immutable** — indexing reads a character, but `s[0] = "x"` is an
  error. To change text you build a new string.

```python
word = "Python"
word[0]    # 'P'
word[3]    # 'h'
```
