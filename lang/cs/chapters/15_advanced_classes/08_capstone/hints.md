Začni se `Shape`: `__init__(self, name)` a `describe` vracející
`"%s with area %d" % (self.name, self.area)`. Odkazuje na `self.area`, který poskytne
podtřída.

---

`Rectangle(Shape)`: v `__init__` zavolej `super().__init__("rectangle")`, ulož
width/height; přidej `@property area` vracející `width * height`; přidej `__eq__` a
`__lt__`, které porovnávají `self.area` s `other.area`.

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
