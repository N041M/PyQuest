**`@property`** is a decorator that turns a method into a **computed, read-only
attribute**. `obj.area` (no parentheses) runs the method and returns its result,
so a derived value is recomputed on every access and never goes stale.

- It hides the fact that work happens: callers use `obj.area`, not `obj.area()`,
  exactly as for a stored attribute — but the value always reflects the current
  state.
- A bare `@property` is read-only; assigning to it raises `AttributeError`. Add a
  matching `@area.setter` to allow assignment with validation.
- Prefer a property over a value stored in `__init__` whenever the value *depends*
  on other attributes that can change.

```python
class Rectangle:
    def __init__(self, w, h): self.width, self.height = w, h
    @property
    def area(self): return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12
r.width = 5
r.area        # 20  -- recomputed
```
