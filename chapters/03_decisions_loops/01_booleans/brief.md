# 3.1 -- Booleans and comparison

## Concept

A **boolean** is a value that is either `True` or `False` -- a yes/no answer.
It is its own type (`bool`), written with a capital letter.

You get booleans by **comparing** values:

| operator | means |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `<`  | less than |
| `>`  | greater than |
| `<=` | less than or equal |
| `>=` | greater than or equal |

```python
print(3 < 5)      # True
print(3 == 5)     # False
print(7 >= 7)     # True
```

Note `==` (compare) is **two** equals signs. A single `=` *assigns* a variable;
`==` *asks "are these equal?"*.

## Example

```python
a = 4
b = 9
print(a > b)      # False
```

## Your task

Read two whole numbers (each on its own line). Print whether the **first is
greater than the second** -- that is, print the result of `first > second`
(which will be `True` or `False`).

For input `8` then `3`, the output is:

```
True
```

## Done when

- For `8` then `3` it prints `True`; for `2` then `5` it prints `False`.
- When the two numbers are equal it prints `False` (equal is not "greater").
