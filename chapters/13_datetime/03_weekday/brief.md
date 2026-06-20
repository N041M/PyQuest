# 13.3 -- weekday: which day of the week

## Concept

Given a date, what day of the week is it? Working that out by hand means knowing
leap years and every month's length. The `date` object already does -- ask it:

```python
from datetime import date

date(2026, 6, 20).weekday()     # 5  (Saturday)
```

- **`.weekday()`** returns an integer: **Monday is 0**, Tuesday 1, ... Sunday 6.
- (`.isoweekday()` is the same idea but Monday=1 .. Sunday=7.)

This is the kind of thing you let the library do: it encodes the real calendar,
so the answer is correct for any date, leap years and all.

## Example

```python
from datetime import date

def is_weekend(text):
    return date.fromisoformat(text).weekday() >= 5
```

## Your task

Define `weekday(text)` that takes a `YYYY-MM-DD` string and returns its day of
the week as an integer, **Monday=0 .. Sunday=6**, using the date object's
`.weekday()`.

## Done when

- `weekday("2026-06-20")` returns `5` (a Saturday).
- `weekday("2000-01-01")` returns `5`.
- The answer comes from `.weekday()` on a parsed `date`.
