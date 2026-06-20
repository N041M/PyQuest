`int` converts a value to an **integer**. Its most common use is turning the
**string** that `input()` returns into a number you can compute with.

- `int("42")` is `42`. Surrounding whitespace is ignored (`int(" 42 ")` works);
  a leading sign is allowed (`int("-5")`).
- Text that isn't a whole number raises `ValueError` — `int("3.5")` and
  `int("ten")` both fail. For decimals, use `float("3.5")`.
- Called on a `float`, `int` truncates *toward zero* (`int(3.9)` is `3`,
  `int(-3.9)` is `-3`).

Because `input()` always yields text, reading a number is a two-step idiom:

```python
n = int(input("How many? "))   # read text, then parse it to an int
print(n * 2)
```
