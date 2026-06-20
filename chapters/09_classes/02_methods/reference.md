A **method** is a function defined inside a class. It always takes **`self`**
first and computes from the object's own attributes, so behaviour lives with the
data it acts on.

- Call it with `instance.method()`; Python passes the instance as `self`
  automatically, so `p.dist()` calls `dist(p)`.
- Inside, reach the object's data through `self`: `self.x`, `self.y`.
- A method may take more parameters after `self` and `return` a value like any
  function.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

Point(3, 4).dist()      # 5.0
```
