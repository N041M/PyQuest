`Dog` bere dva argumenty. První, `name`, patří `Animal` -- předej ho nahoru pomocí
`super().__init__(name)`.

---

Po řádku `super().__init__(name)` nastav `self.breed = breed` pro vlastní část Doga.

---

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
