Functions **compose built-ins** into a named, reusable operation. An `average`
function is the model: it wraps `sum` and `len` behind one clear name.

- `return sum(nums) / len(nums)` computes the mean — but `len(nums)` is `0` for an
  empty list, which raises `ZeroDivisionError`, so guard it with an early return.
- Naming the operation (`average(scores)`) makes calling code read as intent, and
  fixing or improving the logic happens in one place.

```python
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

average([2, 4, 9])    # 5.0
```
