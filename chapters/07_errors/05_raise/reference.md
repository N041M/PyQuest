**`raise`** triggers an exception **yourself**, stopping the function and
signalling that something is wrong. It lets your code reject bad input at the
point it's detected, the same way built-ins do.

- `raise ValueError("amount must be positive")` constructs an exception with a
  message and throws it; execution stops unless a `try` up the call chain catches
  it.
- Choose the type that fits: `ValueError` for a wrong value, `TypeError` for a
  wrong type. The message explains what was expected.
- Raising at the boundary (as input arrives) keeps the rest of the code able to
  trust its data.

```python
def withdraw(amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    ...
```
