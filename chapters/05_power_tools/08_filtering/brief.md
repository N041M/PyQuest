# 5.8 -- Filtering with comprehensions

## Concept

A comprehension can also **choose** which items to keep. Add an `if` at the
end:

```python
evens = [x for x in nums if x % 2 == 0]
```

Read it: *"each `x` from `nums` -- but only if `x % 2 == 0`"*. Items that fail
the test are simply left out.

The two parts are independent and combine freely:

```python
[x * 2 for x in nums]                 # transform every item   (5.7)
[x for x in nums if x > 0]            # keep some, unchanged   (this puzzle)
[x * 2 for x in nums if x > 0]        # keep some AND transform
```

Reminder from 1.9: `x % 2` is the remainder of dividing by 2, so it is `0`
exactly for even numbers -- and that includes `0` itself and negatives like
`-4`.

## Example

```python
nums = [1, 2, 3, 4]
print([x for x in nums if x % 2 == 0])    # [2, 4]
```

## Your task

Read a count `n`, then `n` whole numbers. Keep only the **even** ones (in
their original order) and print them one per line.

For input `5`, then `1`, `2`, `3`, `4`, `-6`:

```
2
4
-6
```

## Done when

- `1, 2, 3, 4, -6` prints `2, 4, -6` -- negatives and zero count as even.
- If no number is even, nothing is printed.
- You used a comprehension with an `if` clause.
