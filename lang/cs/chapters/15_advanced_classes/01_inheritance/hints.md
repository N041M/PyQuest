Nejprve napiš `Animal`, s `__init__` ukládajícím `self.name` a `describe`
vracejícím větu. Pak `class Dog(Animal):` -- to `(Animal)` je to, co dělá Doga
dědícím.

---

Uvnitř `Dog` píšeš jen `speak`; `describe` přijde zadarmo z `Animal`. Nepředefinovávej
`describe` v `Dog`.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name + " the animal"


class Dog(Animal):
    def speak(self):
        return "Woof"
