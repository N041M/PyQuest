# 13.2 -- fromisoformat: text to date

## Concept

Dates usually arrive as **text** -- from a file, a form, an API. **`date.from
isoformat`** parses a standard `YYYY-MM-DD` string into a real `date` object,
the inverse of `.isoformat()`:

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
d.year      # 2026
d.month     # 6
d.day       # 20
```

- It returns a `date`, so you can then read `.year` / `.month` / `.day`, compare
  it, or do arithmetic -- everything a date can do.
- It expects the exact `YYYY-MM-DD` shape; a malformed string raises `ValueError`.

Parsing into a real date (rather than slicing the string yourself) means the
value is validated and ready for calendar work.

## Example

```python
from datetime import date

def month_of(text):
    return date.fromisoformat(text).month
```

## Your task

Using **`date.fromisoformat`**, define `parts(text)` that parses a `YYYY-MM-DD`
string and returns the tuple of integers `(year, month, day)` read from the date
object's attributes.

## Done when

- `parts("2026-06-20")` returns `(2026, 6, 20)`.
- `parts("1999-01-05")` returns `(1999, 1, 5)`.
- The values come from a parsed `date`'s attributes, not `text.split("-")`.
