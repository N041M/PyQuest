`__init__` is an ordinary function, so its parameters can have **default
values** — letting an object be created with or without certain arguments.

- `def __init__(self, balance=0):` allows `Account()` (starts at 0) or
  `Account(100)` (starts at 100).
- The same rules apply: defaulted parameters follow non-defaulted ones, and a
  mutable default needs the `None` sentinel trick
  (`def __init__(self, items=None): self.items = items or []`).
- Defaults make the common case effortless while keeping the option open.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance

Account().balance        # 0
Account(100).balance     # 100
```
