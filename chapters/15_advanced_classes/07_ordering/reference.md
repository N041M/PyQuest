**`__lt__(self, other)`** defines the **`<`** operator for your objects, and `<` is
exactly what **`sorted`**, **`min`**, and **`max`** use to order things. Without
it, comparing two of your objects raises `TypeError`; with it, a list of them
sorts directly.

- Python calls `a.__lt__(b)` for `a < b`; return whether `a` should come **before**
  `b`, usually by comparing the attribute you sort on.
- `sorted` needs only `<`, so `__lt__` alone makes objects sortable. The full set
  of ordering dunders is `__lt__`, `__le__`, `__gt__`, `__ge__`.
- `functools.total_ordering` is a class decorator that fills in the other three
  from `__lt__` and `__eq__`, if you want all comparisons.

```python
class Temperature:
    def __init__(self, degrees): self.degrees = degrees
    def __lt__(self, other): return self.degrees < other.degrees

sorted([Temperature(30), Temperature(10), Temperature(20)])   # 10, 20, 30
min([Temperature(30), Temperature(10)]).degrees               # 10
```
