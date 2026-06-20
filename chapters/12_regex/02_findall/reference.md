**`re.findall(pattern, text)`** returns a **list of every** non-overlapping match
of the pattern, left to right — the extract-them-all counterpart to `re.search`'s
find-the-first.

- A **quantifier** makes one pattern match a run: `\d+` is "one or more digits",
  so each match is a whole number rather than a single digit. (`+` one-or-more,
  `*` zero-or-more, `?` optional, `{n}` exactly n.)
- Each item in the returned list is the **matched text** (a string); no match
  gives `[]`. Convert with `int(...)` when you want numbers.
- If the pattern has capture groups, `findall` returns the groups instead of the
  whole match (see 12.5); with one group it's a list of that group's text.

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
re.findall(r"[a-z]+", "Hi there!")  # ['i', 'there']
[int(n) for n in re.findall(r"\d+", "p1 p22")]   # [1, 22]
```
