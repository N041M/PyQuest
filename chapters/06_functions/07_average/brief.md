# 6.7 -- Building on built-ins

## Concept

Functions shine when they bundle a small *recipe* behind a good name. The
recipe for an average:

> the total, divided by how many there are

You own every ingredient: `sum()` (5.2), `len()` (2.6), and `/` (1.9).
Remember from 1.9 that `/` **always returns a float** -- `4 / 2` is `2.0`,
not `2`. That is correct here: an average is naturally a decimal number.

```python
def average(nums):
    return sum(nums) / len(nums)
```

One function, one line, instantly reusable -- and the name says what the line
means.

## Example

```python
average([1, 2])        # 1.5
average([10, 20, 30])  # 20.0
```

## Your task

Define `average(nums)` that returns the average of a non-empty list of
numbers.

## Done when

- `average([1, 2])` returns `1.5`; `average([10, 20, 30])` returns `20.0`.
- The result is a **float** even when the division is exact (use `/`,
  not `//`).
- A one-item list returns that item (as a float).
