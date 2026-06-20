A **class** defines a new type of object, bundling related data into one value.
**`__init__`** is the initialiser: Python calls it automatically when you create
an instance, to set up its starting data.

- `class Point:` opens the definition; calling `Point(3, 4)` makes an
  **instance** and runs `__init__`.
- **`self`** is the instance being built; `self.x = x` stores a value as an
  **attribute** on it, where every method can later reach it.
- `__init__`'s first parameter is always `self`; the rest are the arguments the
  caller passes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x          # store data on the instance
        self.y = y

p = Point(3, 4)
p.x                         # 3
```
