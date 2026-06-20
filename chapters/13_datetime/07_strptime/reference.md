**`datetime.strptime(text, format)`** parses a string into a **`datetime`** using
the same format codes as `strftime` — it's the inverse direction. Where
`date.fromisoformat` reads only the one ISO layout, `strptime` reads **any**
layout you can describe.

- The `format` must match the string's shape exactly (`"%Y-%m-%d %H:%M"` for
  `"2026-06-20 14:30"`); a mismatch raises `ValueError`, validating as it parses.
- The result is a `datetime` — a date **and** a time — exposing `.year`,
  `.month`, `.day`, `.hour`, `.minute`, `.second`. (`.date()` and `.time()`
  extract just one part.)
- Remember the pair: **strptime** parses (string → datetime), **strftime**
  formats (datetime → string).

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.hour                      # 14
datetime.strptime("05/01/1999", "%d/%m/%Y").year   # 1999
```
