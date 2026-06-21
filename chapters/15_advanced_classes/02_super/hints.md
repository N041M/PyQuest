`Dog` takes two arguments. The first, `name`, belongs to `Animal` -- hand it up
with `super().__init__(name)`.

---

After the `super().__init__(name)` line, set `self.breed = breed` for Dog's own
part.

---

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
