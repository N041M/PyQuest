Store both values in `__init__`: `self.width = width` and
`self.height = height`.

---

Add two methods. `area` returns `self.width * self.height`; `perimeter` returns
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
