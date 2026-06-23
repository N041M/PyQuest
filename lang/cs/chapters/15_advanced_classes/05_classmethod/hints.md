Napiš `__init__` jako obvykle. Pak přidej metodu dekorovanou `@classmethod`, jejíž
první parametr je `cls`, ne `self`.

---

Uvnitř `from_tuple` rozbal dvojici a postav objekt pomocí `cls`:
`return cls(pair[0], pair[1])`.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])
