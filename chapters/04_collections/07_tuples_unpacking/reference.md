A **tuple** is an ordered, **immutable** sequence, written with commas (often in
parentheses): `(3, 4)`, or just `3, 4`. Once made it cannot be changed.

- **Unpacking** assigns the items of a sequence to several names at once:
  `a, b = point`. The count on each side must match.
- This enables the one-line **swap** `a, b = b, a`: the right side is built into
  a tuple first, then unpacked, so no temporary is needed.
- Use a tuple for a fixed group of related values (a coordinate, a record); use a
  list when the collection grows or changes.

```python
point = (3, 4)
x, y = point        # x = 3, y = 4
a, b = b, a         # swap in one line
```
