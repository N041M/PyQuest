Ulož `x` a `y` v `__init__` jako obvykle, pak přidej metodu `__str__(self)`.

---

`__str__` musí text **vrátit** (ne ho vypsat). Sestav ho f-řetězcem:
`return f"({self.x}, {self.y})"`. Dej pozor na čárku a mezeru.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
