Guarda os dois valores em `__init__`: `self.width = width` e
`self.height = height`.

---

Acrescenta dois métodos. `area` devolve `self.width * self.height`;
`perimeter` devolve `2 * (self.width + self.height)`.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
