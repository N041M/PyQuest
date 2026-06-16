# 10.4 -- a generator remembers

## Concept

Because a generator **pauses** instead of finishing, its local variables stay
alive between `yield`s. A value you build up survives every pause -- the
generator picks up exactly where it left off, accumulator and all.

```python
def tally(words):
    seen = 0
    for w in words:
        seen = seen + 1
        yield seen          # 1, then 2, then 3, ... -- `seen` is remembered
```

`list(tally(["a", "b", "c"]))` is `[1, 2, 3]`. The `seen` counter is not reset
on each pass; it keeps its value across the yields.

## Example

```python
def running_max(nums):
    best = None
    for n in nums:
        if best is None or n > best:
            best = n
        yield best
```

`list(running_max([3, 1, 5]))` is `[3, 3, 5]` -- each item is the largest seen
**so far**.

## Your task

Define a generator `running_total(nums)` that yields the **running sum** of
`nums`: each value is the total of every number up to and including the current
one. An empty list yields nothing.

## Done when

- `list(running_total([3, 1, 2]))` is `[3, 4, 6]`.
- `list(running_total([5]))` is `[5]`; `list(running_total([]))` is `[]`.
- You use `yield`, and a variable that carries the total across the yields.
