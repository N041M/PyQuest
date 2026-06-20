A **default value** in the header makes a parameter optional: if the caller omits
that argument, the default is used.

- `def greet(name, greeting="hi"):` can be called `greet("Ada")` (uses `"hi"`) or
  `greet("Ada", "hello")` (overrides it).
- Parameters **with** defaults must come **after** those without.
- Use a *new* default each call for mutable types — write `def f(items=None):`
  then `if items is None: items = []`, never `def f(items=[]):` (one shared list
  persists between calls).

```python
def power(base, exp=2):
    return base ** exp

power(5)       # 25  -- exp defaults to 2
power(5, 3)    # 125
```
