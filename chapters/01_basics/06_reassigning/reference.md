A variable is a name, not a box: assigning again **rebinds** the name to a new
value. The name always holds its most recent assignment; the previous value is
simply no longer reachable through it.

- Each `=` replaces what the name points to. Order matters — later assignments
  win.
- The right-hand side is evaluated using the name's *current* value, then the
  result is rebound, so `x = x + 1` reads the old `x` and stores the new one.
- The augmented forms (`x += 1`, `x *= 2`, …) are shorthand for exactly that:
  read, combine, rebind.

```python
score = 10
score = 25        # score is now 25
score = score + 5 # reads 25, stores 30
```
