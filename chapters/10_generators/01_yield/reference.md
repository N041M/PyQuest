A function containing **`yield`** is a **generator function**. Calling it doesn't
run the body — it returns a **generator object** that produces values one at a
time, **pausing** at each `yield` and resuming where it left off when asked for
the next.

- Each `yield value` hands one value to whoever is iterating, then freezes the
  function's state until the next value is requested.
- You consume a generator by iterating it (`for x in gen:`) or with `next(gen)`.
- This differs from `return`, which hands back **one** value and ends the
  function for good.

```python
def two():
    yield 1
    yield 2

for n in two():
    print(n)            # 1, then 2
```
