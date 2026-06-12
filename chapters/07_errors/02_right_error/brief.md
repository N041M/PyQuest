# 7.2 -- Catch the RIGHT error

## Concept

`except` can name which error it handles -- and it should. Errors you did not
expect are **information**, and swallowing them hides bugs.

```python
try:
    n = int(text)
except ValueError:        # exactly the error int() raises for bad TEXT
    n = None
```

The tempting shortcut is a bare `except:` (or `except Exception:`) -- "catch
everything, can't crash!" But *everything* includes errors that mean **your
code is being misused**. `int([1, 2])` doesn't raise `ValueError` -- it raises
`TypeError` ("wrong kind of thing entirely"), and that one *should* crash
loudly so the caller's bug gets found, not papered over.

The rule: **catch exactly what you expect; let everything else escape.**

## Example

```python
safe_int("42")      # 42
safe_int("nope")    # None         (ValueError, handled)
safe_int([1, 2])    # TypeError!   (NOT handled -- a misuse, let it crash)
```

## Your task

Define `safe_int(text)` that returns `int(text)`, or `None` when the text
isn't a valid number. Catch **only** `ValueError` -- a `TypeError` from a
non-string must escape.

## Done when

- `safe_int("42")` is `42`; `safe_int("-7")` is `-7`.
- `safe_int("nope")` and `safe_int("")` are `None`.
- `safe_int([1, 2])` raises `TypeError` -- the checker calls it with a list
  on purpose, so catching too much fails.
