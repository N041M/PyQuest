# 7.3 -- ZeroDivisionError: ask forgiveness

## Concept

Dividing by zero raises `ZeroDivisionError`. There are two ways to write a
division that survives it:

```python
# "look before you leap": test first
if b == 0:
    return None
return a / b

# "easier to ask forgiveness": just try it
try:
    return a / b
except ZeroDivisionError:
    return None
```

Both behave the same *here* -- but Python style strongly favours the second,
and this puzzle requires it. Why:

- The `try` names the actual event ("the division failed") instead of a
  pre-condition you must keep in sync with it.
- Pre-checks don't scale: real operations can fail a dozen ways
  (file missing, permission denied, connection dropped...). You cannot
  pre-test them all -- but one `except` can catch the failure itself.

This style is called **EAFP**: *easier to ask forgiveness than permission*.

## Example

```python
safe_div(10, 4)    # 2.5
safe_div(5, 0)     # None  -- handled, no crash
```

## Your task

Define `safe_div(a, b)` that returns `a / b`, or `None` when `b` is zero --
using `try`/`except`, not an `if`.

## Done when

- `safe_div(10, 4)` is `2.5`; `safe_div(5, 0)` is `None`.
- `safe_div(0, 5)` is `0.0` -- zero on TOP is a fine division.
- You caught `ZeroDivisionError` -- an if-test dodges the lesson and fails.
