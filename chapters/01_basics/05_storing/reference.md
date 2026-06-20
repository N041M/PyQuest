Assignment with `=` binds a **name** to a value. Afterwards the name *refers to*
that value, and using the name anywhere evaluates to it. Reading code, `=` is
"becomes", not "equals" (equality is `==`).

- Names are not declared and have no fixed type — the first assignment creates
  the name, and it simply points at whatever object you assign.
- A name must start with a letter or underscore and contain letters, digits, or
  underscores; it is case-sensitive (`total` and `Total` are different).
- The right-hand side is fully evaluated first, then the result is bound to the
  name on the left.

```python
greeting = "Hello"
print(greeting)        # Hello  -- the name stands in for the value
```
