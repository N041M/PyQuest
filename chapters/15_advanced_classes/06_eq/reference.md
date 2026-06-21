By default, `==` between objects tests **identity** — whether they are the very
same object — so two independently built objects with identical data compare
unequal. Defining **`__eq__(self, other)`** redefines `==` as **value equality**.

- Python calls `a.__eq__(b)` to evaluate `a == b`; return whether they should
  count as equal, normally by comparing the defining attributes. `!=` follows
  automatically as its negation.
- Value equality is what makes objects work intuitively in `==` tests, in `list`
  membership (`in`), and when comparing results.
- If you define `__eq__`, the class becomes **unhashable** (its `__hash__` is set
  to `None`), so it can't go in a `set` or `dict` key until you also define
  `__hash__` — often `return hash(self.cents)`.

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other): return self.cents == other.cents

Money(500) == Money(500)     # True
Money(500) == Money(750)     # False
```
