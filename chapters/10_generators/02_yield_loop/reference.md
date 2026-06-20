Placing a **`yield` inside a loop** streams a whole sequence: the generator emits
one transformed value per pass, pausing after each and resuming on the next
request.

- `for x in source: yield f(x)` yields `f(x)` for every item — the generator form
  of building a list with a comprehension, but produced lazily.
- Nothing is computed until something iterates the generator, and only as far as
  it's consumed.

```python
def squares(nums):
    for n in nums:
        yield n * n

list(squares([1, 2, 3]))    # [1, 4, 9]
```
