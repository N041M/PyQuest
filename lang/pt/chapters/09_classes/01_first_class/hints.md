Começa com `class Dog:` e dá-lhe um método `__init__(self, name, age)`.

---

Dentro de `__init__`, copia cada parâmetro para o objeto com `self.`:
`self.name = name`. É isso que faz o valor ficar guardado.

---

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
