# 12.5 -- Groups: capture the parts

## Concept

Parentheses **`(...)`** in a pattern mark a **capture group**: a piece of the
match you want to pull out. The match object then hands each one back:

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.group(1)     # '2026'
m.group(2)     # '06'
m.groups()     # ('2026', '06', '20')
```

- `re.match` matches from the **start** of the string and returns a match object
  (or `None`).
- `m.group(n)` returns the text the *n*-th group captured (`group(0)` is the
  whole match); `m.groups()` returns them all as a tuple.
- The captured text is still a string -- `int(m.group(1))` if you want a number.

One pattern thus both checks the shape and extracts the fields.

## Example

```python
import re

def split_pair(text):
    m = re.match(r"(\w+):(\w+)", text)
    return (m.group(1), m.group(2))
```

## Your task

Using **`re.match`** with capture groups, define `parse_date(text)` that takes a
date like `"2026-06-20"` and returns the tuple of **integers**
`(year, month, day)`.

## Done when

- `parse_date("2026-06-20")` returns `(2026, 6, 20)`.
- `parse_date("1999-01-05")` returns `(1999, 1, 5)`.
- The fields come from capture groups, not `text.split("-")`.
