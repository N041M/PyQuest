File contents are always **text**, so a line like `"42\n"` is a *string*. To do
arithmetic you must convert each line to a number first.

- `int(line)` parses an integer; it tolerates surrounding whitespace (including
  the trailing newline), so `int("42\n")` is `42`. Use `float(line)` for
  decimals.
- A blank or non-numeric line raises `ValueError` — skip blanks
  (`if not line.strip(): continue`) or wrap the conversion in `try`.
- Accumulate as you go: keep a running total and add each parsed value.

```python
total = 0
with open("nums.txt") as f:
    for line in f:
        total += int(line)    # text -> number, then add
```
