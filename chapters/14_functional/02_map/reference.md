**`map(func, iterable)`** applies `func` to every item and yields the results —
the "transform each item" pattern as a higher-order function (one that takes
another function as an argument).

- It returns a **lazy iterator**, computing each result on demand; wrap it in
  `list(...)` (or `tuple`, or feed a `for`) to consume it.
- `func` can be a `lambda`, a named `def`, or any callable — a built-in like
  `len`, `str.upper`, or `int` is common.
- Given several iterables, `map(func, a, b)` calls `func(a_i, b_i)` in lockstep,
  stopping at the shortest.
- A list comprehension `[func(x) for x in items]` expresses the same thing and is
  often clearer; `map` is the functional-style equivalent you'll see widely.

```python
list(map(len, ["hi", "there"]))        # [2, 5]
list(map(lambda x: x * x, [1, 2, 3]))  # [1, 4, 9]
list(map(int, ["1", "2", "3"]))        # [1, 2, 3]
```
