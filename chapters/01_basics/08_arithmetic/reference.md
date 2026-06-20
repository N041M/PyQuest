The arithmetic operators are `+` (add), `-` (subtract), `*` (multiply),
`/` (divide), `//` (floor-divide), `%` (remainder), and `**` (power).

They follow **precedence** (order of operations), highest to lowest:

1. `**`
2. unary `-` (negation)
3. `*`, `/`, `//`, `%`
4. `+`, `-`

Operators of equal precedence evaluate **left to right**, except `**`, which is
right-associative (`2 ** 3 ** 2` is `2 ** 9`). **Parentheses** override all of
this — evaluate them first.

```python
2 + 3 * 4      # 14   -- * before +
(2 + 3) * 4    # 20   -- parentheses first
-3 ** 2        # -9   -- ** before unary minus
```
