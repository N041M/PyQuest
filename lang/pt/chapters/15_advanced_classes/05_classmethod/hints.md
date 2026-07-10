Escreve `__init__` como habitualmente. Depois acrescenta um método decorado
com `@classmethod` cujo primeiro parâmetro é `cls`, não `self`.

---

Dentro de `from_tuple`, desempacota o par e constrói o objeto com `cls`:
`return cls(pair[0], pair[1])`.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])
