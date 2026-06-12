# 1.11 -- A number from input

## Concept

`input()` always gives back **text**, even when the person types digits. If you
try to do math on it, `+` will join instead of add -- remember puzzle 1.7:

```python
n = input()      # user types 21  ->  n is the string "21"
print(n + n)     # "2121", not 42
```

To do arithmetic, first **convert** the text to a number with `int(...)`:

```python
n = int(input())   # "21" -> 21, a real number now
print(n * 2)       # 42
```

`int(...)` takes text that looks like a whole number and turns it into an `int`
you can compute with. This pattern -- `int(input())` -- is extremely common.

## Common misconception

`int` does not just "remove the quotes"; it produces a different type. After
`int(input())` the value is a number, so `+`, `*`, `//`, and friends do real math.

## Your task

Read a whole number from input, then print **double** it. Examples:

- input `21` -> output `42`
- input `0`  -> output `0`
- input `-5` -> output `-10`

So: read with `input()`, convert with `int(...)`, multiply by 2, print the result.

## Done when

- For input `21` the output is `42`.
- It also works for `0` and for a negative number like `-5` (the checker tries
  these).
