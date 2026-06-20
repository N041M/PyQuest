A **`timedelta`** represents a **duration** — a span of time, not a point in it.
Adding one to a `date` produces another `date`, with all the calendar bookkeeping
(month lengths, year boundaries, leap days) handled automatically.

- `timedelta(days=n)` is `n` days; it also accepts `weeks=`, `hours=`,
  `minutes=`, `seconds=`. `n` may be **negative** to move backwards.
- `date + timedelta` and `date - timedelta` give a new date; subtracting two
  *dates* gives a `timedelta` (13.5).
- This is why date arithmetic goes through the library: `date(2026, 12, 25) +
  timedelta(days=10)` correctly rolls into the next year, and February's length
  is never your problem.

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)    # date(2026, 7, 30)
date(2026, 1, 1) - timedelta(days=1)      # date(2025, 12, 31)
date(2026, 6, 20) + timedelta(weeks=2)    # date(2026, 7, 4)
```
