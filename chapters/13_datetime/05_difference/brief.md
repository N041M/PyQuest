# 13.5 -- Subtracting dates: days between

## Concept

Adding a duration to a date gives a date. The reverse also works: **subtract one
date from another** and you get a **`timedelta`** -- the span between them:

```python
from datetime import date

gap = date(2026, 7, 1) - date(2026, 6, 20)
gap            # timedelta(days=11)
gap.days       # 11
```

- `date_b - date_a` is a `timedelta`; its **`.days`** is the whole number of days
  between them.
- If `date_b` is **earlier** than `date_a`, `.days` is **negative**.
- It's exact across months, years and leap days -- the library counts, you don't.

## Example

```python
from datetime import date

def days_old(born, today):
    return (date.fromisoformat(today) - date.fromisoformat(born)).days
```

## Your task

Define `days_between(a, b)` that takes two `YYYY-MM-DD` strings and returns the
number of days **from `a` to `b`** (so later `b` gives a positive number), using
date subtraction.

## Done when

- `days_between("2026-06-20", "2026-07-01")` returns `11`.
- `days_between("2026-07-01", "2026-06-20")` returns `-11`.
- `days_between("2026-06-20", "2026-06-20")` returns `0`.
- The count comes from subtracting two `date` objects, not manual arithmetic.
