Dej `Animal` jak `__init__`, tak `speak` (vracející "..."). Pak `Cat(Animal)`
definuje svůj vlastní `speak`.

---

`speak` Cata prostě vrátí "Meow". Nepředefinovávej `__init__` v Cat -- je zděděný.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"
