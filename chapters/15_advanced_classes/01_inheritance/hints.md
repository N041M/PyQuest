Write `Animal` first, with `__init__` storing `self.name` and `describe`
returning the sentence. Then `class Dog(Animal):` -- the `(Animal)` is what makes
Dog inherit.

---

Inside `Dog` you only write `speak`; `describe` comes for free from `Animal`.
Don't redefine `describe` in `Dog`.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name + " the animal"


class Dog(Animal):
    def speak(self):
        return "Woof"
