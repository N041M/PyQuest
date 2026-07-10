`Dog` recebe dois argumentos. O primeiro, `name`, pertence a `Animal` -- passa-o
para cima com `super().__init__(name)`.

---

Depois da linha `super().__init__(name)`, define `self.breed = breed` para a
parte própria de Dog.

---

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
