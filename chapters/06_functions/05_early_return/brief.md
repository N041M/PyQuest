# 6.5 -- return ends the function

## Concept

`return` doesn't just hand back a value -- it **stops the function on the
spot**. Nothing after an executed `return` runs. That makes branching
functions read cleanly: settle each case and leave.

```python
def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
```

Notice there is no `else` -- none is needed. If the first `return` fired, the
function is already over; reaching the last line *means* `n` was positive.
This style is called an **early return**.

A function with several `return` statements still returns exactly **one**
value per call: whichever `return` runs first.

## Example

```python
sign(-3)    # "negative"
sign(0)     # "zero"
sign(42)    # "positive"
```

## Your task

Define `sign(n)` that returns `"negative"`, `"zero"`, or `"positive"` for a
whole number `n`.

## Done when

- `sign(-3)`, `sign(0)`, `sign(42)` return the three words above.
- The boundary cases `-1` and `1` are right too.
