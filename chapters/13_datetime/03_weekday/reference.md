**`date.weekday()`** returns the day of the week as an integer, **Monday = 0**
through **Sunday = 6**. Because a `date` encodes the real calendar — leap years,
varying month lengths — it computes this correctly for any date, which is exactly
the kind of work you delegate to the library rather than derive by hand.

- `.isoweekday()` is the same but **Monday = 1 .. Sunday = 7** (the ISO
  convention).
- A common use is `weekday() >= 5` to test for a weekend.
- The companion `.strftime("%A")` formats the weekday's **name**, but that's
  locale-dependent; the numeric `.weekday()` is stable everywhere.

```python
from datetime import date

date(2026, 6, 20).weekday()      # 5  (Saturday)
date(2026, 6, 22).weekday()      # 0  (Monday)
date(2026, 6, 20).weekday() >= 5 # True -- it's the weekend
```
