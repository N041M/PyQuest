Acrescenta um método `__eq__(self, other)` a Money. O Python chama-o para
`==`.

---

Devolve a comparação dos valores: `return self.cents == other.cents`.

---

class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        return self.cents == other.cents
