# 3.5 -- and / or / not

## Concept

You can combine booleans with three words:

- `and` -- True only if **both** sides are True.
- `or` -- True if **either** side is True.
- `not` -- flips a boolean: `not True` is `False`.

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

age = 25
print(age >= 18 and age < 65)   # True  (both hold)
```

These let one condition test several things at once.

## Example

```python
n = 12
print(n % 2 == 0 and n % 3 == 0)   # True  (12 is divisible by both)
```

## Your task

Read a whole number. Print whether it is divisible by **both** 2 and 3 -- that
is, print the result of `(n % 2 == 0) and (n % 3 == 0)` (which is `True` or
`False`).

For input `12` the output is:

```
True
```

## Done when

- `12` and `6` print `True`; `4` and `9` print `False`.
- `0` prints `True` (0 is divisible by everything).
