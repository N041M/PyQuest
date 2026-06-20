The capstone composes generators into a **streaming pipeline**: a **source**
generator feeds a **filter** generator, which feeds a **transform** generator.
Each stage is lazy, so values flow through one at a time and nothing is
materialised in full.

- Because each stage consumes the previous lazily, the pipeline processes huge or
  endless data with tiny memory — one item is in flight at a time.
- Stages stay small and independent: swap or add a stage without touching the
  others. This is the generator analogue of composing functions.

```python
def reader(nums):  yield from nums
def keep_pos(src): yield from (n for n in src if n > 0)
def doubled(src):  yield from (n * 2 for n in src)

list(doubled(keep_pos(reader([-1, 2, -3, 4]))))   # [4, 8]
```
