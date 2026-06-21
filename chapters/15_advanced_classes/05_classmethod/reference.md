A **`@classmethod`** is bound to the **class**, not an instance: its first
parameter is **`cls`** (the class itself) instead of `self`. Because it has the
class, it can build instances — the classic use is an **alternative constructor**.

- Call it on the class: `Point.from_tuple((3, 4))`. Python passes `Point` as
  `cls`.
- Building with `cls(...)` rather than the literal class name means a **subclass**
  that calls the inherited classmethod gets an instance of *itself*.
- Contrast with **`@staticmethod`**, which takes neither `self` nor `cls` — just a
  plain function namespaced under the class, used when the method needs no access
  to the instance or class.

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    @classmethod
    def from_tuple(cls, pair): return cls(pair[0], pair[1])

Point.from_tuple((3, 4)).x     # 3
```
