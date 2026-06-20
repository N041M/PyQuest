A **regular expression** is a pattern describing a set of strings; the **`re`**
module matches them against text. **`re.search(pattern, text)`** scans the whole
string for the **first** place the pattern matches and returns a **match object**
(which is truthy) or **`None`**.

- Write patterns as **raw strings** — `r"\d"` — so the backslashes reach the
  regex engine instead of being interpreted by Python first.
- Shorthand classes: `\d` a digit, `\w` a word character `[A-Za-z0-9_]`, `\s`
  whitespace, and `.` any character but newline.
- `re.search` looks **anywhere** in the string; `re.match` only checks the start.
  Because the result is a match object or `None`, `re.search(...) is not None` is
  a clean membership test.

```python
import re

re.search(r"\d", "abc4")     # <re.Match object; match='4'>
re.search(r"\d", "abc")      # None
bool(re.search(r"\s", "a b"))  # True -- contains whitespace
```
