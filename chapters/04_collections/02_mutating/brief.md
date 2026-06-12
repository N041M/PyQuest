# 4.2 -- Changing a list

## Concept

Unlike strings, lists can be **changed in place** (they are *mutable*). A few ways:

- Replace an item by index: `nums[0] = 99`
- Remove and return the **last** item: `nums.pop()`
- Remove the first matching **value**: `nums.remove(20)`

```python
nums = [10, 20, 30]
nums[0] = 99      # [99, 20, 30]   replace by position
nums.pop()        # [99, 20]       drop the last item (returns 30)
print(nums)       # [99, 20]
```

These change the existing list -- the variable still points at the same list,
now modified.

## Example

```python
xs = [1, 2, 3]
xs[1] = 0
xs.pop()
print(xs)         # [1, 0]
```

## Your task

Read a count `n` (at least 1), then `n` numbers, into a list. Then:

1. **double the first item** (replace `nums[0]` with `nums[0] * 2`), and
2. **remove the last item** with `.pop()`.

Print the resulting list. For input `3`, then `5`, `2`, `9`:

```
[10, 2]
```

(`[5, 2, 9]` -> double first -> `[10, 2, 9]` -> pop -> `[10, 2]`.)

## Done when

- `5, 2, 9` gives `[10, 2]`.
- A single number `n=1` (e.g. just `4`) gives `[]` -- doubled to `[8]`, then the
  last (only) item is popped.
