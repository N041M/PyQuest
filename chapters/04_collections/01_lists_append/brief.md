# 4.1 -- Lists and append

## Concept

A **list** holds several values in order, in one variable. You write a list with
square brackets, items separated by commas:

```python
nums = [10, 20, 30]
print(nums)        # [10, 20, 30]
print(nums[0])     # 10   (index like a string -- from 0)
print(len(nums))   # 3
```

A list can start empty and grow. `.append(x)` adds `x` to the **end**:

```python
nums = []
nums.append(10)
nums.append(20)
print(nums)        # [10, 20]
```

This "start empty, append in a loop" pattern is how you build a list from input.

## Example

```python
items = []
items.append(1)
items.append(2)
print(items)       # [1, 2]
```

## Your task

Read a whole number `n`, then read `n` more whole numbers (one per line). Collect
them into a list with `.append()`, and print the finished list.

For input `3`, then `1`, `2`, `3`:

```
[1, 2, 3]
```

## Done when

- `3` with `1, 2, 3` prints `[1, 2, 3]`.
- A count of `0` prints `[]` (an empty list).
