# 12.1 -- re.search: is the pattern there?

## Concept

A **regular expression** ("regex") is a small language for describing patterns
in text. The **`re`** module matches them. The most basic question is "does this
pattern appear anywhere?" -- **`re.search`**:

```python
import re

re.search(r"\d", "abc4")     # a match object (truthy)
re.search(r"\d", "abc")      # None
```

- The pattern is written as a **raw string** `r"..."` so backslashes mean what
  regex expects (`r"\d"`, not `"\d"`).
- `\d` matches any single **digit**. Other shorthands: `\w` a word character,
  `\s` whitespace, `.` any character.
- `re.search` returns a **match object** if the pattern is found anywhere, or
  **`None`** if not -- so `re.search(...) is not None` is a clean yes/no.

## Example

```python
import re

def has_letter(text):
    return re.search(r"[a-z]", text) is not None
```

## Your task

Using **`re.search`**, define `has_digit(text)` that returns `True` if `text`
contains at least one digit, `False` otherwise.

## Done when

- `has_digit("abc4")` is `True`, `has_digit("abc")` is `False`.
- `has_digit("")` is `False`.
- The test uses `re.search` with `\d`, not a hand-written digit scan.
