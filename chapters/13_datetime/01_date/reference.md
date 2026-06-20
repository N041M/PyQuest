The **`datetime`** module provides types for calendar dates and clock times. Its
**`date`** type holds one day as a single object: `date(year, month, day)`.

- The constructor **validates** the values against the real calendar —
  `date(2026, 2, 30)` raises `ValueError`, so an impossible date can't slip
  through.
- Attributes `.year`, `.month`, `.day` read the parts back; **`.isoformat()`**
  renders the standard `YYYY-MM-DD` string, always zero-padded.
- A `date` knows the calendar, so it can compare (`<`, `==`), subtract (13.5),
  and report its weekday (13.3) — things three loose integers or a hand-built
  string cannot. `date.today()` returns the current day.

```python
from datetime import date

d = date(2026, 6, 20)
d.month          # 6
d.isoformat()    # '2026-06-20'
date(2026, 1, 5).isoformat()   # '2026-01-05'  -- padded
```
