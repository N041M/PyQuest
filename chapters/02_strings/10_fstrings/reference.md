An **f-string** (formatted string literal) is a string prefixed with `f` in which
`{ }` holds a Python **expression**; the expression is evaluated and its value
inserted, converted to text.

- Any expression fits inside the braces: `f"{name}"`, `f"{a + b}"`,
  `f"{nums[0]}"`.
- A literal brace is written by doubling it: `f"{{literal}}"` shows `{literal}`.
- A format spec after a colon controls presentation, e.g. `f"{price:.2f}"` shows
  two decimal places and `f"{n:>5}"` right-aligns in a 5-wide field.

f-strings are the clearest way to build text from values, replacing chains of
`+` and `str()`.

```python
name, n = "Ada", 3
f"{name} solved {n} puzzles"   # 'Ada solved 3 puzzles'
f"{1/3:.2f}"                    # '0.33'
```
