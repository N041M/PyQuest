Ulož stranu v `__init__` jako minule, pak přidej druhou metodu `area`.

---

Metoda bere `self` první: `def area(self):`. Uvnitř vrať
`self.side * self.side`.

---

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
