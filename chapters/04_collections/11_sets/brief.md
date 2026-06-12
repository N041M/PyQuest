# 4.11 -- Sets

## Concept

A **set** is an unordered collection of **unique** items -- it automatically drops
duplicates. Write one with curly braces, or build one from a list with `set(...)`:

```python
s = {1, 2, 2, 3}
print(s)              # {1, 2, 3}   (the duplicate 2 is gone)

nums = [1, 1, 2, 3, 3]
print(set(nums))      # {1, 2, 3}
print(len(set(nums))) # 3           how many *distinct* values
```

Sets are great for "how many different things?" and for fast membership tests
with `in`:

```python
print(2 in s)         # True
```

(Sets have no order and no indexing -- you can't do `s[0]`.)

## Example

```python
words = ["a", "b", "a"]
print(len(set(words)))   # 2
```

## Your task

Read a count `n`, then `n` words. Print how many **distinct** words there are.

For input `4`, `a`, `b`, `a`, `c`:

```
3
```

(`a` appears twice but counts once.)

## Done when

- `a, b, a, c` prints `3`.
- A count of `0` prints `0`.
