Three core string operations:

- **`len(s)`** returns the number of characters in `s` as an `int`; `len("")`
  is `0`.
- **`+` concatenates**: `"ab" + "cd"` is `"abcd"`. Both operands must be strings
  — `"n" + 5` raises `TypeError`; convert with `str(5)` first.
- **`*` repeats**: `s * n` (or `n * s`) joins `n` copies. `"ab" * 3` is
  `"ababab"`; `n <= 0` gives the empty string `""`.

All three produce **new** strings and leave the originals unchanged (strings are
immutable).

```python
s = "ab"
len(s)    # 2
s + "c"   # 'abc'
s * 3     # 'ababab'
```
