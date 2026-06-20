Two search-and-survey methods:

- **`s.replace(old, new)`** returns a new string with **every** non-overlapping
  occurrence of `old` swapped for `new`. It replaces all matches, not just the
  first; if `old` doesn't occur, the string comes back unchanged.
- **`s.count(sub)`** returns how many times `sub` appears, counting
  non-overlapping matches left to right. `"aaa".count("aa")` is `1`, not 2.

Both only read `s` and return new information; the original string is untouched.

```python
"a-b-c".replace("-", "_")   # 'a_b_c'  -- every match
"banana".count("a")          # 3
```
