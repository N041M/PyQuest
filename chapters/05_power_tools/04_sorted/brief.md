# 5.4 -- sorted()

## Concept

`sorted(nums)` returns a **new list** with the same items in order, smallest
first:

```python
nums = [3, 1, 2]
print(sorted(nums))    # [1, 2, 3]
print(nums)            # [3, 1, 2]  -- the original is untouched
```

Two things to know:

- It returns a *copy*; the original list keeps its order. (There is also
  `nums.sort()`, a method that reorders the list **in place** -- handy later,
  but `sorted()` is the safer default because nothing is changed behind your
  back.)
- Largest-first is one keyword away: `sorted(nums, reverse=True)`.

Duplicates are kept -- sorting reorders, it never removes.

## Example

```python
for x in sorted([3, 1, 2]):
    print(x)
# 1
# 2
# 3
```

## Your task

Read a count `n`, then `n` whole numbers. Print them smallest to largest,
one per line.

For input `4`, then `3`, `1`, `3`, `2`:

```
1
2
3
3
```

## Done when

- `3, 1, 3, 2` prints `1, 2, 3, 3` -- the duplicate `3` appears twice.
- A count of `0` prints nothing.
- You used `sorted()`.
