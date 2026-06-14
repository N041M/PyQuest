Store `x` and `y` in `__init__`. The method takes the other vector:
`def add(self, other):`.

---

Read both vectors through the dot (`self.x`, `other.x`) and **return a new
Vector**: `return Vector(self.x + other.x, self.y + other.y)`. Don't assign back
onto `self`.

---

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
