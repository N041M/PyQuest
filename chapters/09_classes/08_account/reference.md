The capstone is a **stateful class** that puts the chapter together: a default in
`__init__`, methods that **mutate** state, a **guard** that raises on invalid
operations, and `__str__` for display.

- `__init__` sets the starting balance (with a default); `deposit` and `withdraw`
  change `self.balance` in place.
- A guard protects the invariant: `withdraw` checks funds and
  `raise ValueError(...)` rather than allowing an impossible state.
- `__str__` renders the object for printing. Together these make an object that
  is reliable to use and pleasant to read.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
    def __str__(self):
        return f"balance: {self.balance}"
```
