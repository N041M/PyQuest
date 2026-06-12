# 1.9 -- Three kinds of division

## Concept

Dividing has three useful operators in Python:

- `/`  normal division -- always gives a decimal number (Python calls these
  `float`). `7 / 2` is `3.5`.
- `//` floor division -- divides and throws away the fractional part, giving a
  whole number. `7 // 2` is `3`.
- `%`  modulo -- gives the **remainder** after division. `7 % 2` is `1`
  (because 2 goes into 7 three times with 1 left over).

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
```

A number with a decimal point, like `3.5`, is a `float`. A whole number with no
point, like `3`, is an `int`. Notice `/` gives `3.5` even when it divides
evenly-looking numbers: `4 / 2` is `2.0`, not `2`.

`%` is surprisingly handy: a number is even exactly when `n % 2` is `0`.

## Common misconception

`/` does not round to a whole number. `7 / 2` is `3.5`, never `3`. If you want the
whole-number part, that is what `//` is for.

## Your task

Using the number 7 and 2, print these three lines in order:

```
3.5
3
1
```

Use `/` for the first, `//` for the second, and `%` for the third.

## Done when

- Output is exactly `3.5`, then `3`, then `1`.
- Each line uses the matching operator (`/`, `//`, `%`).
