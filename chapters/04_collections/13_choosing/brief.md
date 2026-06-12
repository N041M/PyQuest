# 4.13 -- Choosing the right collection

## Concept

You now have four collections. Picking the right one makes a problem easy:

- **list** -- ordered items, duplicates allowed (`[1, 2, 2]`). Use for sequences.
- **tuple** -- like a list but fixed/immutable. Use for fixed groups.
- **set** -- unordered, **unique** items. Use for "distinct" and fast membership.
- **dict** -- key -> value lookup. Use for "given X, find its Y".

This puzzle combines a few:

- `len(nums)` -- how many items (a **list** keeps every value, including repeats).
- `len(set(nums))` -- how many **distinct** values (a **set** drops duplicates).
- the **sum** -- a loop with an accumulator (or `sum(nums)`).

## Example

```python
nums = [1, 2, 2, 3]
print(len(nums))        # 4
print(len(set(nums)))   # 3
```

## Your task

Read a count `n`, then `n` numbers. Print three lines:

1. how many numbers there are,
2. how many **distinct** numbers there are,
3. their **total**.

For input `4`, then `1`, `2`, `2`, `3`:

```
4
3
8
```

## Done when

- `1, 2, 2, 3` prints `4`, `3`, `8`.
- A count of `0` prints `0`, `0`, `0`.
