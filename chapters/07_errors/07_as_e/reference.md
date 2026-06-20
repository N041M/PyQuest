**`except ValueError as e:`** binds the caught exception **object** to a name, so
you can inspect it — most simply by printing it to show what went wrong.

- The exception object carries the detail; `str(e)` (or `print(e)`) yields its
  message. `type(e).__name__` gives the error's class name.
- The name `e` exists only inside the `except` block.
- One handler can catch a family by naming a base class: `except Exception as e:`
  binds any of its subclasses (use sparingly — broad catches hide bugs).

```python
try:
    int("xyz")
except ValueError as e:
    print("bad input:", e)    # bad input: invalid literal for int()...
```
