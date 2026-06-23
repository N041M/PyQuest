Přidej do Temperature `__lt__(self, other)`. Python ho volá pro `<` a `sorted`
používá `<`.

---

Vrať porovnání hodnot: `return self.degrees < other.degrees`. Ta jediná metoda
stačí, aby byl seznam řaditelný.

---

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __lt__(self, other):
        return self.degrees < other.degrees
