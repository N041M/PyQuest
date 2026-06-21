# 15.6 -- __eq__: value equality

## Concept

By default, `==` on objects asks "are these the **same object**?" -- so two
separately-built objects with identical data are *not* equal. The **`__eq__`**
dunder method changes that to **value equality**:

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):
        return self.cents == other.cents

Money(500) == Money(500)     # True   -- same value
Money(500) == Money(750)     # False
```

- Python calls `a.__eq__(b)` for `a == b`. You return whether they should count as
  equal -- usually by comparing the attributes that define the value.
- `!=` is handled for you (it's the negation of `__eq__`).
- (Defining `__eq__` is also what lets your objects be compared in tests, lists,
  and `in` checks by value.)

## Your task

Define `Money` with `__init__(self, cents)` and an **`__eq__`** so two `Money`
objects are equal exactly when their `cents` match.

## Done when

- `Money(500) == Money(500)` is `True`.
- `Money(500) == Money(750)` is `False`.
- Equality compares `cents`, not object identity.
