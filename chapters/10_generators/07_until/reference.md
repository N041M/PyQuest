A bare **`return`** inside a generator — or simply reaching the end of the
function — **stops** it: iteration ends and no further values come. `return` in a
generator carries **no value**; it only signals "done".

- This lets a generator **stop early** on a condition: `if x == sentinel: return`
  ends the stream at that point.
- To a `for` loop, a stopped generator is just an iterable that has run out — the
  loop ends naturally (internally, the generator raises `StopIteration`).

```python
def until_zero(nums):
    for n in nums:
        if n == 0:
            return          # stop the stream here
        yield n

list(until_zero([3, 1, 0, 9]))  # [3, 1]
```
