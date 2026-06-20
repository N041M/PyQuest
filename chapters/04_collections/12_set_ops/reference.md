Sets support the algebra of collections:

- **`a & b`** (intersection) — items in **both**.
- **`a | b`** (union) — items in **either**.
- **`a - b`** (difference) — items in `a` but **not** in `b`.

Each returns a **new** set. (`^` is the symmetric difference — in exactly one.)
These express set questions directly, replacing hand-written loops that compare
two collections.

```python
a, b = {1, 2, 3}, {2, 3, 4}
a & b     # {2, 3}
a | b     # {1, 2, 3, 4}
a - b     # {1}
```
