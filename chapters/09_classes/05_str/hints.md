Store `x` and `y` in `__init__` as usual, then add a `__str__(self)` method.

---

`__str__` must **return** the text (not print it). Build it with an f-string:
`return f"({self.x}, {self.y})"`. Mind the comma and the space.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
