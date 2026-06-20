# 13.4 -- timedelta: date arithmetic

## Concept

A **`timedelta`** is a **duration** -- a span of time. Add one to a date and you
get another date, with all the calendar messiness (month lengths, year rollover,
leap days) handled for you:

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)     # date(2026, 7, 30)
date(2026, 12, 25) + timedelta(days=10)    # date(2027, 1, 4)  -- crosses the year
```

- `timedelta(days=n)` is a duration of `n` days (it also takes `weeks=`,
  `hours=`, etc.). `n` may be **negative** to go backwards.
- `date + timedelta` gives a new `date`; `date - timedelta` goes the other way.
- This is why you never do date maths by hand: the library knows February has 29
  days in a leap year, and you don't have to.

## Example

```python
from datetime import date, timedelta

def tomorrow(text):
    return (date.fromisoformat(text) + timedelta(days=1)).isoformat()
```

## Your task

Define `add_days(text, n)` that takes a `YYYY-MM-DD` string and an integer `n`,
and returns the `YYYY-MM-DD` string for the date `n` days later (using
`timedelta`). `n` may be negative.

## Done when

- `add_days("2026-06-20", 40)` returns `"2026-07-30"`.
- `add_days("2026-01-01", -1)` returns `"2025-12-31"`.
- The shift uses `timedelta` on a real `date`, not hand-rolled day counting.
