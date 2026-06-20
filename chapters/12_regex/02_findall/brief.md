# 12.2 -- re.findall: every match

## Concept

`re.search` finds the *first* match. **`re.findall`** returns **all** of them, as
a list of strings:

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
```

- `\d+` means "one or more digits" -- the `+` makes the pattern grab a whole run
  of digits, not just one. So each match is a full number.
- `re.findall` returns a **list of strings** (the matched text), left to right,
  non-overlapping. No match gives the empty list `[]`.
- The matches are still text; convert with `int(...)` if you want numbers.

## Example

```python
import re

def words(text):
    return re.findall(r"[a-z]+", text)
```

## Your task

Using **`re.findall`**, define `all_numbers(text)` that returns a list of every
run of digits in `text`, as strings.

## Done when

- `all_numbers("a12b3c456")` returns `["12", "3", "456"]`.
- `all_numbers("nothing")` returns `[]`.
- The extraction uses `re.findall` with `\d+`, not a hand-written scan.
