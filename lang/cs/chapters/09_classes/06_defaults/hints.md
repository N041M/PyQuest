Dej `__init__` parametr s výchozí hodnotou: `def __init__(self,
greeting="Hello"):`, pak ho ulož na `self`.

---

`greet` sestaví zprávu: `return f"{self.greeting}, {name}!"`. Výchozí hodnota
patří do signatury, takže nepiš místo toho `if greeting is None`.

---

class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
