A function returns **one** object, but that object can be a **tuple**, so
`return a, b` hands back several values at once (Python packs them into a tuple).
The caller **unpacks** them with matching names.

- `return lo, hi` returns the tuple `(lo, hi)`; `low, high = bounds(xs)` unpacks
  it into two names.
- The counts must match on unpacking. Catch the whole tuple with one name if you
  prefer: `result = bounds(xs)` then `result[0]`, `result[1]`.

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4
```
