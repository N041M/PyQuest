Functions **call other functions**, so a larger task is built from small, tested
pieces. The result of one becomes the argument or building block of the next.

- A helper does one job well; a higher-level function calls several helpers and
  combines their results. This is the core of structuring a program.
- `f(g(x))` feeds `g`'s result straight into `f`. Each function stays simple and
  independently checkable.

```python
def clean(s):  return s.strip().lower()
def is_yes(s): return clean(s) == "yes"

is_yes("  YES ")   # True  -- is_yes builds on clean
```
