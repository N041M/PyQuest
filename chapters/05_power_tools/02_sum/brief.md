# 5.2 -- sum()

## Concept

In 3.12 you wrote the **accumulator pattern** by hand:

```python
total = 0
for x in nums:
    total = total + x
```

That pattern is so common Python ships it as a built-in function:

```python
total = sum(nums)
```

`sum(list_of_numbers)` adds every item and returns the total. On an empty list
it returns `0` -- exactly what your hand-written accumulator started with.

This chapter is full of such **power tools**: built-ins that replace a loop you
have already written yourself once. You earn the shortcut by knowing what it
replaces.

## Example

```python
nums = [3, 1, 4]
print(sum(nums))    # 8
print(sum([]))      # 0
```

## Your task

Read a count `n`, then `n` whole numbers (one per line). Print their total
using `sum()`.

For input `3`, then `3`, `1`, `4`:

```
8
```

## Done when

- `3, 1, 4` prints `8`; negatives work too.
- A count of `0` prints `0`.
- You used `sum()` -- not a hand-written loop this time.
