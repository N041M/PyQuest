Guarda o lado em `__init__` como da última vez, depois acrescenta um segundo
método `area`.

---

Um método recebe `self` primeiro: `def area(self):`. Dentro, devolve
`self.side * self.side`.

---

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
