# 6.2 -- Two parameters

## Concept

A function can take several parameters -- list them with commas, and the
caller's values arrive **in the same order**:

```python
def rect_area(width, height):
    return width * height

rect_area(3, 4)     # 12  (width=3, height=4)
```

Inside the body, the parameters are ordinary variables. Everything you know
already works on them -- arithmetic, comparisons, f-strings, loops.

A subtlety worth meeting early: parameters are **local** to the function. The
`width` inside `rect_area` exists only while a call is running; it is not
visible (and does not clash with) anything outside.

## Example

```python
def diff(a, b):
    return a - b

print(diff(10, 4))   # 6
print(diff(4, 10))   # -6  -- order matters
```

## Your task

Define `rect_area(width, height)` that returns the area of a rectangle
(width times height).

## Done when

- `rect_area(3, 4)` returns `12`; `rect_area(4, 3)` does too.
- A zero side returns `0`.
- No `input()`, no `print()` -- the checker passes the values in.
