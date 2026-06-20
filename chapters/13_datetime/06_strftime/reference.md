**`strftime(format)`** ("string-format-time") renders a date or datetime into a
string you describe with **format codes**. Where `.isoformat()` gives one fixed
layout, `strftime` gives any layout.

- Common codes: `%Y` four-digit year, `%m` month, `%d` day — all zero-padded;
  `%H` hour, `%M` minute, `%S` second. Any other characters (`/`, `.`, spaces)
  are copied through literally.
- Name codes like `%A` (weekday) and `%B` (month) are **locale-dependent**, so
  prefer the numeric codes for output that must be stable.
- `strptime` is the inverse — it *parses* a string by a format (13.7).

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y%m%d")       # '20260620'
d.strftime("%d.%m.%y")     # '20.06.26'  -- %y is the 2-digit year
```
