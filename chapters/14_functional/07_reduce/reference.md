**`functools.reduce(func, iterable[, start])`** **folds** a sequence into a single
value by applying a two-argument `func` cumulatively, left to right:
`func(func(func(i0, i1), i2), i3)...`. Each step combines the running result with
the next item.

- A **start** value (`reduce(func, items, start)`) seeds the fold and defines the
  result for an **empty** sequence; without it, reducing an empty iterable raises
  `TypeError`.
- It generalises the accumulator loop to *any* combiner: `+` gives a sum, `*` a
  product, `max` the largest. The dedicated `sum` is the `+` special case, and
  `math.prod` the `*` one — but `reduce` folds with whatever function you supply.
- `reduce` lives in `functools` (it's not a built-in), so it must be imported.

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])      # 10
reduce(lambda a, b: a * b, [1, 2, 3, 4], 1)   # 24
reduce(lambda a, b: a if a > b else b, [3, 9, 2])   # 9  (max)
```
