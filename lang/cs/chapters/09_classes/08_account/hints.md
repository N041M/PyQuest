`__init__(self, balance=0)` uloží počáteční zůstatek. `deposit` jen přičte k
`self.balance`.

---

`withdraw` potřebuje stráž: `if amount <= self.balance:` odečti a
`return True`; jinak nic neměň a `return False`.

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
