# 15.5 -- @classmethod: an alternative constructor

## Concept

A normal method takes `self` (an instance). A **`@classmethod`** takes **`cls`**
(the class itself), so it can build and return a **new instance** -- a handy way
to offer an alternative, named constructor:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

p = Point.from_tuple((3, 4))     # called on the class, not an instance
p.x, p.y                          # (3, 4)
```

- `@classmethod` makes `cls` the first parameter -- the class the method is called
  on (`Point` here).
- `cls(...)` is the same as `Point(...)`, but using `cls` means subclasses get an
  instance of *their* type for free.
- You call it on the **class**: `Point.from_tuple(...)`.

## Your task

Define `Point` with `__init__(self, x, y)`, and a **classmethod** `from_tuple(cls,
pair)` that builds a `Point` from a `(x, y)` tuple.

## Done when

- `Point.from_tuple((3, 4)).x` is `3` and `.y` is `4`.
- `from_tuple` is a `@classmethod` taking `cls`, and builds the point with
  `cls(...)`.
