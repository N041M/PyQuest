# 5.3 -- min() and max()

## Concept

Finding the smallest or largest item is another loop you could write by hand
("keep a best-so-far, compare each item") -- and another loop Python ships as
a built-in:

```python
nums = [3, 7, 1]
print(min(nums))    # 1
print(max(nums))    # 7
```

`min()` and `max()` take a list (any non-empty collection, in fact) and return
its smallest / largest item. They also work on strings -- "smallest" then means
earliest in alphabetical order:

```python
min("cab")     # "a"
```

One caution: on an **empty** list they crash (there is no smallest of
nothing), so this puzzle guarantees at least one number.

## Example

```python
nums = [4, -2, 9]
print(min(nums))    # -2
print(max(nums))    # 9
```

## Your task

Read a count `n` (always at least 1), then `n` whole numbers. Print two lines:
the smallest, then the largest.

For input `3`, then `4`, `-2`, `9`:

```
-2
9
```

## Done when

- `4, -2, 9` prints `-2` then `9`.
- A single number prints itself twice (it is both the min and the max).
- You used `min()` and `max()`.
