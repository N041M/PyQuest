Dá a `__init__` um parâmetro com valor por omissão:
`def __init__(self, greeting="Hello"):`, depois guarda-o em `self`.

---

`greet` constrói a mensagem: `return f"{self.greeting}, {name}!"`. O valor
por omissão pertence à assinatura, por isso não escrevas um
`if greeting is None` em vez disso.

---

class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
