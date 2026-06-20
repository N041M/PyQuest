Generators are **lazy**: each value is computed only when requested, so a
generator can describe an **endless** sequence and still be useful — you just
take the values you need.

- An infinite `while True: yield n; n += 1` never finishes on its own, but a
  consumer can stop early (a `break`, or `next` called a few times).
- Laziness means a generator holds essentially **no memory** for the sequence — it
  keeps only its current state, not every value — unlike a list that materialises
  all of them.

```python
def naturals():
    n = 0
    while True:
        yield n             # endless, but only as far as asked
        n += 1

g = naturals(); next(g), next(g)   # (0, 1)
```
