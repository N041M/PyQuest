# 13.6 -- strftime: format a date your way

## Concept

`.isoformat()` always gives `YYYY-MM-DD`. When you need a different layout,
**`strftime`** ("string format time") renders a date using **format codes**:

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y.%m.%d")     # '2026.06.20'
```

- `%d` is the day, `%m` the month, `%Y` the four-digit year -- each zero-padded.
  Everything else in the format string (the `/`, `.`, spaces) is copied through
  literally.
- Other codes exist (`%H` hour, `%M` minute, and name codes like `%A`), but the
  numeric ones are the staples.

So one date object can present itself however a report or user expects.

## Example

```python
from datetime import date

def dotted(text):
    return date.fromisoformat(text).strftime("%Y.%m.%d")
```

## Your task

Define `pretty(text)` that takes a `YYYY-MM-DD` string and returns it in
**`DD/MM/YYYY`** form, using `strftime("%d/%m/%Y")` on the parsed date.

## Done when

- `pretty("2026-06-20")` returns `"20/06/2026"`.
- `pretty("1999-01-05")` returns `"05/01/1999"` (zero-padded).
- The formatting is done by `strftime`, not by rearranging split pieces.
