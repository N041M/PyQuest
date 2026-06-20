`print` writes a textual representation of each argument to standard output (the
terminal), in order, and then writes `end` (a newline by default). It is the
primary way a program shows the user a result.

- Each value is converted to text with `str()` first, so `print(42)` and
  `print("42")` both show `42`.
- With several arguments, `sep` (default a single space) is placed *between*
  adjacent values — never before the first or after the last.
- `end` is appended once, after everything else. Because it defaults to `"\n"`,
  each `print` call ends the current line and the next output starts fresh.
- `print` returns `None`; it is called for its side effect, not its value.

```python
print("Hello, World!")        # Hello, World!
print("a", "b", "c")          # a b c
```
