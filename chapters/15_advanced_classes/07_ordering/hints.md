Add `__lt__(self, other)` to Temperature. Python calls it for `<`, and `sorted`
uses `<`.

---

Return the comparison of the values: `return self.degrees < other.degrees`. That
single method is enough to make a list sortable.

---

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __lt__(self, other):
        return self.degrees < other.degrees
