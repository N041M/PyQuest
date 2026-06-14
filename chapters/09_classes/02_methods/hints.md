Store the side in `__init__` like last time, then add a second method `area`.

---

A method takes `self` first: `def area(self):`. Inside, return
`self.side * self.side`.

---

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
