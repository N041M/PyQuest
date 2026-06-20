A generator **remembers** its local variables across `yield`s: execution freezes
at the `yield` and every local keeps its value until the next request resumes the
function. This lets a generator **carry state** as it streams.

- A variable updated in the loop (a running total, a previous value) persists
  between yields without any object or global.
- This is what makes a generator a natural **running accumulator** — a running
  sum, for instance, that emits the total so far each step.

```python
def running_sum(nums):
    total = 0
    for n in nums:
        total += n          # total survives across yields
        yield total

list(running_sum([1, 2, 3]))    # [1, 3, 6]
```
