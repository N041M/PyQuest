**`all(iterable)`** returns `True` only if **every** item is truthy — the partner
to `any`. It answers "do they all pass?" in one expression.

- It **short-circuits** on the first falsy item, returning `False` immediately.
- `all([])` is `True` — *vacuously*, since no item failed. This "all of nothing
  is true" rule is a common surprise; guard for the empty case if it matters.
- Same shape as `any`: `all(<test> for <item> in <iterable>)`. Together they
  express the universal ("for all") and existential ("there exists") questions
  over a sequence.

```python
all(n > 0 for n in [1, 2, 3])     # True
all(n > 0 for n in [1, -2, 3])    # False
all([])                           # True  -- vacuously
```
