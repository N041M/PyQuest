# 9.7 -- Objects working together

## Concept

A method can take **another object** as an argument and build a **new** object
as its result. This is how objects combine without losing their own identity.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

`add` reaches into `other` (another Vector) for its data, and **returns a brand
new `Vector`** -- it does not change `self` or `other`:

```python
a = Vector(1, 2)
b = Vector(3, 4)
c = a.add(b)      # Vector(4, 6)
a.x               # still 1 -- a is untouched
```

Building a `Vector(...)` *inside* `Vector`'s own method is normal: the class can
use itself.

## Your task

Define a class `Vector` storing `x` and `y`, with a method `add(other)` that
returns a **new** `Vector` whose coordinates are the two vectors' coordinates
added together. The originals must be left unchanged.

## Done when

- `Vector(1, 2).add(Vector(3, 4))` is a Vector with `.x == 4` and `.y == 6`.
- The two input vectors are unchanged afterwards.
- `add` returns a new `Vector` object (not a tuple), built inside the method.
