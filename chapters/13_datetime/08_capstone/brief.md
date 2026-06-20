# 13.8 -- Capstone: shift a timestamp

## Concept

This pulls the chapter together into one round trip: **parse** a timestamp,
**shift** it by a duration, **format** the result back -- each step a tool you've
met.

```python
from datetime import datetime, timedelta

dt = datetime.strptime("2026-06-20 23:30", "%Y-%m-%d %H:%M")  # parse
dt = dt + timedelta(hours=2)                                  # shift
dt.strftime("%Y-%m-%d %H:%M")                                 # '2026-06-21 01:30'
```

Notice the shift rolled past midnight into the next day -- the library tracks
that automatically, across days, months and years. Doing this by hand would mean
reimplementing the calendar and the clock.

## Your task

Define `add_hours(timestamp, hours)` that takes a `"YYYY-MM-DD HH:MM"` string and
an integer number of `hours` (which may be negative), and returns the timestamp
shifted by that many hours, in the **same `"YYYY-MM-DD HH:MM"` format**.

Use `datetime.strptime` to parse, `timedelta(hours=...)` to shift, and
`strftime` to format.

## Done when

- `add_hours("2026-06-20 23:30", 2)` returns `"2026-06-21 01:30"`.
- `add_hours("2026-01-01 00:30", -1)` returns `"2025-12-31 23:30"`.
- The shift uses `timedelta` on a parsed `datetime`, formatted with `strftime` --
  not hand arithmetic on the string.
