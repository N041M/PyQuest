Give `Animal` both `__init__` and `speak` (returning "..."). Then `Cat(Animal)`
defines its own `speak`.

---

Cat's `speak` simply returns "Meow". Don't redefine `__init__` in Cat -- it's
inherited.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"
