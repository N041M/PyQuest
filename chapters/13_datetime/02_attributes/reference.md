**`date.fromisoformat(text)`** parses a standard `YYYY-MM-DD` string into a `date`
object — the inverse of `.isoformat()`. The result is a real date, so you can read
its attributes, compare it, or do arithmetic on it.

- It expects the exact ISO shape; a malformed or impossible string raises
  `ValueError`, which validates the input as a side effect.
- `.year`, `.month`, `.day` read the components back as integers.
- Parsing into a date (rather than slicing the text yourself) is the point: the
  value is checked and immediately ready for calendar work. For non-ISO layouts,
  `datetime.strptime` parses by an explicit format (13.7).

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
(d.year, d.month, d.day)     # (2026, 6, 20)
d < date.fromisoformat("2026-12-31")   # True
```
