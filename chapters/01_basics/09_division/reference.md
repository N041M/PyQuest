Python has three division operators:

- **`/` true division** always produces a **`float`**, even when the result is
  whole: `7 / 2 == 3.5`, and `4 / 2 == 2.0` (note the `.0`).
- **`//` floor division** divides and rounds *down* toward negative infinity,
  giving an `int` for two ints: `7 // 2 == 3`. With a negative operand it still
  rounds down, so `-7 // 2 == -4`, not `-3`.
- **`%` remainder (modulo)** is what's left over: `7 % 2 == 1`. In Python the
  result takes the **sign of the divisor**, so `-7 % 2 == 1`.

For any integers, `a == (a // b) * b + (a % b)` holds. `divmod(a, b)` returns the
pair `(a // b, a % b)` at once. Dividing by zero raises `ZeroDivisionError`.

```python
17 / 5    # 3.4
17 // 5   # 3
17 % 5    # 2   -- 3*5 + 2 == 17
```
