Write `area` as a normal method that returns `self.width * self.height`, then put
`@property` on the line directly above `def area`.

---

With `@property`, callers write `r.area` (no parentheses) and the method runs each
time, so it always reflects the current width and height.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
