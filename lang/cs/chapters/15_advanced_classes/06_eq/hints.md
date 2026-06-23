Přidej do Money metodu `__eq__(self, other)`. Python ji volá pro `==`.

---

Vrať porovnání hodnot: `return self.cents == other.cents`.

---

class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        return self.cents == other.cents
