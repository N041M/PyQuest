Putting **`yield` behind an `if`** filters a stream as it flows: the generator
emits only the items that pass the test and silently skips the rest — the lazy
counterpart of a comprehension's `if` clause.

- `for x in source: if test(x): yield x` produces a filtered stream without
  building any intermediate list.
- Because it's lazy, it composes cleanly: a filter generator can feed another
  generator, each handling one stage.

```python
def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n         # only the evens make it out

list(evens(range(10)))      # [0, 2, 4, 6, 8]
```
