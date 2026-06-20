By default a pattern can match **anywhere** in the string. Validating a *format*
means the **whole** string must conform — no leftover characters. Two ways to
require that:

- **Anchors** in the pattern: **`^`** matches the start of the string, **`$`** the
  end. `r"^[A-Z]{2}\d{4}$"` must span the entire input.
- **`re.fullmatch(pattern, text)`** demands the pattern cover the whole string
  for you — no anchors needed. It returns a match object or `None`.

The contrast: `re.search(r"[A-Z]{2}\d{4}", "AB1234x")` **matches** (the pattern
occurs), but `re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")` is **`None`** (the `x` is
left over). Use `search`/`findall` to *find* substrings, `fullmatch`/anchors to
*validate* a whole value.

```python
import re

bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234"))    # True
bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x"))   # False
bool(re.match(r"^\d{5}$", "12345"))               # True -- anchored form
```
