Začni s `class Dog:` a dej mu metodu `__init__(self, name, age)`.

---

Uvnitř `__init__` zkopíruj každý parametr na objekt pomocí `self.`:
`self.name = name`. To je to, co hodnotu udrží.

---

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
