**`__str__`** defines the human-readable text for an object. When you `print` an
instance or call `str()` on it, Python calls `__str__` and uses what it returns.

- Without it, printing an object shows an unhelpful default like
  `<Point object at 0x...>`; `__str__` replaces that with something meaningful.
- It must **return** a string (not print one), typically built with an f-string
  from the object's attributes.
- `__str__` is one of several **dunder** ("double-underscore") methods Python
  calls on your behalf, like `__init__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(3, 4))      # (3, 4)
```
