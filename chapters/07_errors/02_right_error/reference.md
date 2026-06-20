An `except` should name the **specific** exception you expect. Catching exactly
the right type lets unexpected errors surface as bugs instead of being silently
swallowed.

- `except ValueError:` catches only that type; an unrelated failure (a typo'd
  name raising `NameError`) still propagates, which is what you want.
- A bare `except:` (or `except Exception:`) catches **everything**, including bugs
  you'd rather see — avoid it unless you genuinely mean "any failure".
- Match the type to the operation: `int()` raises `ValueError`, indexing raises
  `IndexError`, dict lookup raises `KeyError`.

```python
try:
    value = data[key]
except KeyError:         # only a missing key, not other bugs
    value = None
```
