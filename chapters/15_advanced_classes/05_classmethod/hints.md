Write `__init__` as usual. Then add a method decorated with `@classmethod` whose
first parameter is `cls`, not `self`.

---

Inside `from_tuple`, unpack the pair and build the object with `cls`:
`return cls(pair[0], pair[1])`.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])
