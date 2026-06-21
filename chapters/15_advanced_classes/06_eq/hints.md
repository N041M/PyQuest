Add a method `__eq__(self, other)` to Money. Python calls it for `==`.

---

Return the comparison of the values: `return self.cents == other.cents`.

---

class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        return self.cents == other.cents
