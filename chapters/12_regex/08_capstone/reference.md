The capstone composes the chapter: a single pattern with **multiple capture
groups**, handed to **`re.findall`**, extracts structured records in one step.

- With more than one group, `re.findall` returns a list of **tuples** — one per
  match, holding each group's text: `re.findall(r"(\w+)=(\w+)", s)` yields
  `[(key, value), ...]`.
- A list of `(key, value)` pairs is exactly what **`dict(...)`** consumes, so
  `dict(re.findall(...))` is a complete mini-parser.
- `\w+` matches a run of word characters (letters, digits, underscore); the `=`
  between the groups is matched **literally**. No match gives `[]`, so an empty
  input cleanly yields `{}`.

This is the regex payoff: describe the shape of one record, and the engine finds
and dissects every occurrence for you.

```python
import re

dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```
