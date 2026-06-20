# 13.1 -- date: a calendar day

## Concept

The **`datetime`** module models real calendar dates and clock times. Its
**`date`** type holds a single day -- year, month, day -- as one object:

```python
from datetime import date

d = date(2026, 6, 20)
d.year      # 2026
d.isoformat()   # '2026-06-20'
```

- `date(year, month, day)` builds the object and **validates** it: `date(2026,
  13, 1)` raises, because there is no month 13.
- `.isoformat()` renders it as the standard `YYYY-MM-DD` string, zero-padded.
- A `date` is far better than three loose integers: it knows the calendar, so it
  can compare, subtract, and format itself.

## Example

```python
from datetime import date

def new_year(year):
    return date(year, 1, 1).isoformat()
```

## Your task

Using **`date`** from `datetime`, define `iso(y, m, d)` that builds the date and
returns its `YYYY-MM-DD` string via `.isoformat()`.

## Done when

- `iso(2026, 6, 20)` returns `"2026-06-20"`.
- `iso(1999, 1, 5)` returns `"1999-01-05"` (note the zero-padding).
- The string comes from a `date` object's `.isoformat()`, not hand-formatting.
