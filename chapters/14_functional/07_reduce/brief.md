# 14.7 -- reduce: fold a sequence to one value

## Concept

**`reduce`** (from `functools`) **folds** a whole sequence into a single value by
applying a two-argument function cumulatively, left to right:

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])     # 10  ((((1+2)+3)+4))
reduce(lambda a, b: a * b, [1, 2, 3, 4])     # 24
```

- `reduce(func, items)` computes `func(func(func(i0, i1), i2), i3)...` -- each
  step combines the running result with the next item.
- A third argument is a **start** value: `reduce(func, items, start)` begins the
  fold from `start`, which also defines the answer for an **empty** sequence.
- It's the accumulator loop (chapter 3) as a higher-order function. (`sum` is the
  special case for `+`; `reduce` lets you fold with *any* combiner.)

## Example

```python
from functools import reduce

def total(nums):
    return reduce(lambda a, b: a + b, nums, 0)
```

## Your task

Using **`reduce`** from `functools`, define `product(nums)` that returns the
product of all the numbers (with a start of `1`, so the empty list gives `1`).

## Done when

- `product([1, 2, 3, 4])` returns `24`; `product([5])` returns `5`.
- `product([])` returns `1`.
- The fold uses `reduce`, not a manual accumulator loop.
