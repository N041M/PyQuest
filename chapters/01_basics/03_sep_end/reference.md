`sep` and `end` are keyword-only arguments that control the spacing around a
`print`'s output.

- **`sep`** is the string inserted between each pair of adjacent values. The
  default is `" "`. It never appears before the first value or after the last,
  so *N* values produce *N − 1* separators.
- **`end`** is the string written once after the final value. The default is
  `"\n"`, which is why each `print` ends its line. Set `end=""` to leave the
  cursor on the same line so the next `print` continues it.

```python
print("2024", "01", "15", sep="-")   # 2024-01-15
print("loading", end="")
print("...")                          # loading... (one line)
```
