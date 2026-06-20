A **negative** index counts from the end of the string: `s[-1]` is the last
character, `s[-2]` the second-to-last, and so on. It saves writing
`s[len(s) - 1]`.

- `s[-1]` and `s[len(s) - 1]` name the same character; the negative form just
  doesn't need the length.
- The valid negative range is `-1` down to `-len(s)`; going further (e.g.
  `s[-99]` on a short string) raises `IndexError`.
- `s[0]` is the first character; there is no `-0` (that's just `0`).

```python
word = "Python"
word[-1]   # 'n'
word[-2]   # 'o'
```
