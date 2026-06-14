# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("no overdraft guard -- withdraw always succeeds and overdraws",
     "class BankAccount:\n"
     "    def __init__(self, balance=0):\n"
     "        self.balance = balance\n"
     "    def deposit(self, amount):\n"
     "        self.balance += amount\n"
     "    def withdraw(self, amount):\n"
     "        self.balance -= amount\n"
     "        return True\n"),
    ("refuses correctly but still mutates the balance on refusal",
     "class BankAccount:\n"
     "    def __init__(self, balance=0):\n"
     "        self.balance = balance\n"
     "    def deposit(self, amount):\n"
     "        self.balance += amount\n"
     "    def withdraw(self, amount):\n"
     "        self.balance -= amount\n"
     "        return amount <= self.balance + amount\n"),
]
