Subtracting one `date` from another yields a **`timedelta`** — the span between
them — and its **`.days`** attribute is the whole number of days, computed exactly
across months, years, and leap days.

- `date_b - date_a` measures from `a` to `b`: if `b` is **earlier**, `.days` is
  **negative**, so the sign tells you the direction.
- The result is a duration, so it composes: add it back to a date, multiply it,
  compare two spans.
- This is the counting counterpart to adding a `timedelta` (13.4) — together they
  make dates a small algebra: `date + duration = date`, `date - date = duration`.

```python
from datetime import date

(date(2026, 7, 1) - date(2026, 6, 20)).days     # 11
(date(2026, 6, 20) - date(2026, 7, 1)).days     # -11
(date(2026, 3, 1) - date(2024, 3, 1)).days      # 730  -- 2024 was a leap year
```
