**Returning** a value and **printing** it are different acts, and confusing them
is a common bug.

- **`return`** hands a value back to the calling code, which can store it, do
  arithmetic on it, or pass it on. The value travels.
- **`print`** writes text to the screen and returns `None`. The value is shown but
  not captured — `x = print(5)` makes `x` be `None`.
- A function that prints instead of returning can't be built on. Prefer to
  `return` the result and let the **caller** decide whether to print it.

```python
def double(n):
    return n * 2        # caller can use it
print(double(5) + 1)    # 11  -- works because double returned
```
