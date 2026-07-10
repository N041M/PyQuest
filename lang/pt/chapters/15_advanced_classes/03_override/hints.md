Dá a `Animal` tanto `__init__` como `speak` (a devolver "..."). Depois
`Cat(Animal)` define o seu próprio `speak`.

---

O `speak` de Cat simplesmente devolve "Meow". Não redefinas `__init__` em Cat
-- é herdado.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"
