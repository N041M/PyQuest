A **quantifier** controls how many times the pattern immediately before it
repeats:

- **`+`** one or more, **`*`** zero or more, **`?`** zero or one (optional),
- **`{n}`** exactly *n*, **`{n,m}`** between *n* and *m*, **`{n,}`** at least *n*.

`[A-Za-z]+` therefore matches a whole **word** — a run of one or more letters —
stopping at the first character that doesn't fit, which is how you tokenize text
while ignoring spaces and punctuation.

- Quantifiers are **greedy** by default: they match as much as possible. A
  trailing `?` makes one **lazy** (`\d+?` matches as few digits as it can).
- The quantifier applies to the single item before it — a character, a class, or
  a parenthesised group: `(ab)+` matches `ababab`.

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")   # ['Hello', 'world']
re.findall(r"\d{4}", "y2024 y2025")          # ['2024', '2025']
re.search(r"colou?r", "color")               # matches (the u is optional)
```
