The capstone is the full **round trip** through the module, composing three of its
tools:

1. **Parse** — `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` reads the string
   into a `datetime`.
2. **Shift** — adding `timedelta(hours=h)` moves it by a duration, rolling across
   minutes, days, months, and years automatically (and backwards for negative
   `h`).
3. **Format** — `.strftime("%Y-%m-%d %H:%M")` renders the result back to the same
   layout.

The point of the chapter in one function: every awkward edge — a time crossing
midnight, a day crossing into a new month or year, a leap day — is handled by the
`datetime` types, not by you. You describe the steps; the library keeps the
calendar honest.

```python
from datetime import datetime, timedelta

def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    return (dt + timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M")

add_hours("2026-06-20 23:30", 2)    # '2026-06-21 01:30'
```
