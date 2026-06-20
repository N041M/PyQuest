**`yield from iterable`** re-emits **every** item the iterable produces, as if you
had written a loop of `yield`s. It delegates a whole sub-stream in one line.

- `yield from sub` is equivalent to `for x in sub: yield x`, but shorter and
  faster — and it works with lists, ranges, other generators, any iterable.
- It's the tool for **flattening** or **chaining**: a generator can `yield from`
  several sources in turn to splice their streams together.

```python
def chain(a, b):
    yield from a
    yield from b            # splice two streams into one

list(chain([1, 2], [3, 4]))     # [1, 2, 3, 4]
```
