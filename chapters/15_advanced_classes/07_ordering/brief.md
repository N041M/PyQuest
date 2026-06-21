# 15.7 -- __lt__: make objects sortable

## Concept

`sorted`, `min`, and `max` all order things using the **`<`** operator. By
default Python doesn't know how to compare two of your objects -- sorting them
raises `TypeError`. Define **`__lt__`** ("less than") and they become sortable:

```python
class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees
    def __lt__(self, other):
        return self.degrees < other.degrees

temps = [Temperature(30), Temperature(10), Temperature(20)]
sorted(temps)        # ordered 10, 20, 30 -- by degrees
```

- Python calls `a.__lt__(b)` for `a < b`. Return whether `a` should come **before**
  `b` -- usually by comparing the attribute you want to sort on.
- `sorted` only needs `<`, so `__lt__` alone makes a list of your objects
  sortable.

## Your task

Define `Temperature` with `__init__(self, degrees)` and an **`__lt__`** so
temperatures compare by `degrees`.

## Done when

- `Temperature(10) < Temperature(20)` is `True`.
- `sorted([Temperature(30), Temperature(10), Temperature(20)])` is ordered
  `10, 20, 30` by degrees.
- Comparison uses `degrees`.
