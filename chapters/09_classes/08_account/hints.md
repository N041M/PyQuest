`__init__(self, balance=0)` stores the starting balance. `deposit` just adds to
`self.balance`.

---

`withdraw` needs a guard: `if amount <= self.balance:` subtract and
`return True`; otherwise change nothing and `return False`.

---

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
