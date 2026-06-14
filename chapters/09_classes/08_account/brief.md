# 9.8 -- Capstone: a bank account

## Concept

Time to put the chapter together: a class with state, several methods, a
sensible default, and a rule it enforces.

A `BankAccount` keeps a `balance`. You can deposit (it grows) and withdraw (it
shrinks) -- but a withdrawal that would overdraw the account must be **refused**,
leaving the balance untouched.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

- `balance` defaults to `0`, so `BankAccount()` is an empty account.
- `deposit` and `withdraw` change the stored balance (state that persists).
- `withdraw` **returns `True`** when it succeeds and **`False`** when it refuses
  -- and on refusal the balance does not change.

```python
acc = BankAccount(100)
acc.deposit(50)       # balance 150
acc.withdraw(70)      # True,  balance 80
acc.withdraw(999)     # False, balance still 80
```

## Your task

Define `BankAccount` exactly as above: a `balance` that defaults to `0`, a
`deposit(amount)` method, and a `withdraw(amount)` method that subtracts and
returns `True` only when there's enough -- otherwise it changes nothing and
returns `False`.

## Done when

- `BankAccount()` starts at `0`; `BankAccount(100)` starts at `100`.
- `deposit` and `withdraw` update `balance`, and withdrawing too much returns
  `False` and leaves `balance` unchanged.
- Withdrawing exactly the balance is allowed.
