Start with `class Dog:` and give it an `__init__(self, name, age)` method.

---

Inside `__init__`, copy each parameter onto the object with `self.`:
`self.name = name`. That's what makes the value stick.

---

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
