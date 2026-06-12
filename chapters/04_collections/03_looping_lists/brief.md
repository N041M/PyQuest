# 4.3 -- Looping over a list

## Concept

Just like a string, a list is a sequence -- so a `for` loop walks straight over
its items, one per pass:

```python
nums = [10, 20, 30]
for x in nums:
    print(x)        # 10, then 20, then 30
```

`len(nums)` gives the number of items, and slicing works too -- `nums[1:]` is all
but the first, `nums[:2]` is the first two:

```python
print(len(nums))    # 3
print(nums[:2])     # [10, 20]
```

## Example

```python
xs = [1, 2, 3]
for x in xs:
    print(x * 10)   # 10, 20, 30
```

## Your task

Read a count `n`, then `n` numbers, into a list. First print how many numbers
there are, then print each number **doubled**, one per line.

For input `3`, then `5`, `2`, `9`:

```
3
10
4
18
```

## Done when

- `5, 2, 9` prints `3`, then `10`, `4`, `18`.
- A count of `0` prints just `0` (no numbers to double).
