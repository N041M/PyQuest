# 4.6 -- Lists inside lists

## Concept

A list can hold **other lists**. This is how you represent rows of data, pairs,
grids, and so on:

```python
pairs = [[1, 2], [3, 4], [5, 6]]
print(pairs)        # [[1, 2], [3, 4], [5, 6]]
print(pairs[0])     # [1, 2]        the first inner list
print(pairs[0][1])  # 2            first inner list, second item
```

Two indexes: the first picks an inner list, the second picks an item inside it.
Looping gives you each inner list in turn:

```python
for p in pairs:
    print(p[0] + p[1])   # 3, 7, 11
```

## Example

```python
grid = [[1, 1], [2, 2]]
for row in grid:
    print(row[0] + row[1])   # 2, 4
```

## Your task

Read a count `n`, then `n` **pairs** of numbers (each pair is two numbers, on two
lines). Build a list of `[a, b]` pairs. First print the whole nested list, then
print the **sum of each pair**, one per line.

For input `2`, then `1`, `2`, `3`, `4`:

```
[[1, 2], [3, 4]]
3
7
```

## Done when

- `1,2` and `3,4` print `[[1, 2], [3, 4]]` then `3` then `7`.
- A count of `0` prints `[]` and nothing else.
