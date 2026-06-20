The **boolean operators** combine conditions:

- **`and`** is true only when **both** sides are true.
- **`or`** is true when **at least one** side is true.
- **`not`** inverts a single value.

They **short-circuit**: `and` stops at the first false operand, `or` at the first
true one, so the right side isn't evaluated when the left already decides the
result. Precedence is `not` > `and` > `or`; parentheses make intent obvious.

```python
0 < x and x < 100      # True only inside the range
done or out_of_time    # True if either holds
not finished           # flips the flag
```
