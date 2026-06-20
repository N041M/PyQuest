An **`else`** clause gives an `if` a second branch: its block runs exactly when
the `if` condition is **false**. Together they are a two-way choice — one branch
or the other always runs, never both.

- `else` takes no condition; it is the catch-all for "the `if` was false".
- It must pair with an `if` at the same indentation, and its block is indented
  the same way.

```python
if n % 2 == 0:
    print("even")
else:
    print("odd")        # runs only when n % 2 == 0 is False
```
