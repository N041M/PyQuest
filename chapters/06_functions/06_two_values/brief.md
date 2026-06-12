# 6.6 -- Returning two values

## Concept

`return` can hand back **several values at once** -- separate them with a
comma and Python packs them into a **tuple** (4.7):

```python
def min_max(nums):
    return min(nums), max(nums)
```

The caller can keep the tuple, or unpack it straight into variables -- the
same unpacking you used for `a, b = b, a`:

```python
pair = min_max([3, 1, 4])     # (1, 4)  -- one tuple
lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4  -- unpacked
```

This is how Python functions return "two answers" -- there is no special
trick, just a tuple and unpacking.

## Example

```python
def split_name(full):
    parts = full.split()
    return parts[0], parts[-1]

first, last = split_name("Ada King Lovelace")
# first = "Ada", last = "Lovelace"
```

## Your task

Define `min_max(nums)` that returns the smallest and largest item of a
non-empty list, **in that order**, as a tuple. (`min()`/`max()` are from 5.3.)

## Done when

- `min_max([3, 1, 4])` returns `(1, 4)` -- a tuple, smallest first.
- `min_max([7])` returns `(7, 7)`.
- Negative numbers work.
