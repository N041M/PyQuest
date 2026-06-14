Give `__init__` a parameter with a default: `def __init__(self,
greeting="Hello"):`, then store it on `self`.

---

`greet` builds the message: `return f"{self.greeting}, {name}!"`. The default
belongs in the signature, so don't write an `if greeting is None` instead.

---

class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
