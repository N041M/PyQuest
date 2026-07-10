`__init__(self, balance=0)` guarda o saldo inicial. `deposit` limita-se a
somar a `self.balance`.

---

`withdraw` precisa de uma guarda: `if amount <= self.balance:` subtrai e
`return True`; caso contrário não muda nada e `return False`.

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
