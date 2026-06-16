# 10.3 -- generators are lazy

## Concept

This is the superpower. A generator only does work **when you ask for the next
value**. It never builds the whole sequence up front -- so a generator can be
**endless** and still cost almost nothing until you pull from it.

```python
def naturals():
    i = 0
    while True:        # never stops on its own...
        yield i
        i = i + 1
```

`while True` in a normal function would hang forever. In a generator it is
fine: each `yield` **pauses** the loop until the caller wants one more. You
take only as many as you need:

```python
from itertools import islice
list(islice(naturals(), 4))     # [0, 1, 2, 3] -- then it just stops asking
```

`islice(gen, k)` pulls the first `k` items from a generator and no more. The
generator produces exactly those four, then sits paused.

## Example

`naturals()` above yields `0, 1, 2, 3, ...` with no end. Pulling 3 items gives
`[0, 1, 2]`; pulling 10 gives `[0, 1, ..., 9]`. The same endless generator,
asked for different amounts.

## Your task

Define an **endless** generator `naturals()` that yields the whole numbers
starting at `0`: `0, 1, 2, 3, ...` forever. It must never stop on its own; the
checker only ever pulls a handful of values from it.

## Done when

- The first 5 values of `naturals()` are `[0, 1, 2, 3, 4]`.
- It is endless -- pulling more values just gives more numbers; it never runs
  out.
- You use `yield`, so calling `naturals()` returns a generator.
