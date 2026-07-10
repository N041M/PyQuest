Guarda `x` e `y` em `__init__`. O método recebe o outro vetor:
`def add(self, other):`.

---

Lê os dois vetores através do ponto (`self.x`, `other.x`) e **devolve um novo
Vector**: `return Vector(self.x + other.x, self.y + other.y)`. Não atribuas
de volta a `self`.

---

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
