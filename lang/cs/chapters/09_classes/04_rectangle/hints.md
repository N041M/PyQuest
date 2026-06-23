Ulož obě hodnoty v `__init__`: `self.width = width` a
`self.height = height`.

---

Přidej dvě metody. `area` vrací `self.width * self.height`; `perimeter` vrací
`2 * (self.width + self.height)`.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
