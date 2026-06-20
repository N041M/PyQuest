Objects **collaborate**: a method can take **another object** of the same class
as a parameter, read its attributes, and **return a new** object holding the
result — leaving both inputs unchanged.

- `def add(self, other):` reaches `self.x` and `other.x`, then
  `return Vector(self.x + other.x, ...)`. Returning a fresh instance keeps the
  operands immutable.
- This is how value-like objects compose (points, vectors, money). Defining the
  dunder `__add__` would even let `a + b` call it.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

Vector(1, 2).add(Vector(3, 4)).x    # 4
```
