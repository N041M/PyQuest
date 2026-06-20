A single `try` can be followed by **several `except` clauses**, each handling a
different failure with its own response. They're tested top to bottom; the
**first** matching type runs, and the rest are skipped.

- This builds robust input handling: one `try` around the work, then an `except`
  per thing that can go wrong (`ValueError` for a bad number,
  `ZeroDivisionError` for `/0`), each giving a tailored message.
- Order from specific to general if types are related, since the first match
  wins.

```python
try:
    a, b = int(x), int(y)
    print(a / b)
except ValueError:
    print("please enter whole numbers")
except ZeroDivisionError:
    print("cannot divide by zero")
```
