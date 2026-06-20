# 13.7 -- strptime: parse by a format

## Concept

`date.fromisoformat` only reads the one ISO layout. For **any** layout -- a date
with a time, a custom order -- use **`datetime.strptime`** ("parse time"). You
give it the string **and** a format describing it, with the same codes as
`strftime`:

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.year     # 2026
dt.hour     # 14
dt.minute   # 30
```

- The format must match the string's shape; a mismatch raises `ValueError`, so
  it validates as it parses.
- The result is a **`datetime`** -- a date *and* a time -- with `.year`,
  `.month`, `.day`, `.hour`, `.minute`, `.second` attributes.

`strptime` parses, `strftime` formats: same codes, opposite directions.

## Example

```python
from datetime import datetime

def year_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").year
```

## Your task

Define `hour_of(text)` that takes a timestamp like `"2026-06-20 14:30"` and
returns the **hour** as an integer, by parsing it with `datetime.strptime` and
the format `"%Y-%m-%d %H:%M"`.

## Done when

- `hour_of("2026-06-20 14:30")` returns `14`.
- `hour_of("1999-01-05 09:05")` returns `9`.
- The hour comes from a parsed `datetime`, not string slicing.
