Napiš `area` jako normální metodu, která vrací `self.width * self.height`, pak dej
`@property` na řádek přímo nad `def area`.

---

S `@property` volající píší `r.area` (bez závorek) a metoda běží pokaždé, takže vždy
odráží aktuální šířku a výšku.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
