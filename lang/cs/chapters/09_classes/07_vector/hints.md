Ulož `x` a `y` v `__init__`. Metoda bere druhý vektor:
`def add(self, other):`.

---

Přečti oba vektory tečkou (`self.x`, `other.x`) a **vrať nový Vector**:
`return Vector(self.x + other.x, self.y + other.y)`. Nepřiřazuj zpět na `self`.

---

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
