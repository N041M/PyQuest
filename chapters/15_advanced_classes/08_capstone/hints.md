Start with `Shape`: `__init__(self, name)` and `describe` returning
`"%s with area %d" % (self.name, self.area)`. It refers to `self.area`, which the
subclass will provide.

---

`Rectangle(Shape)`: in `__init__` call `super().__init__("rectangle")`, store
width/height; add `@property area` returning `width * height`; add `__eq__` and
`__lt__` that compare `self.area` to `other.area`.

---

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "%s with area %d" % (self.name, self.area)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area
