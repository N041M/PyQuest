Guarda `x` e `y` em `__init__` como habitualmente, depois acrescenta um
método `__str__(self)`.

---

`__str__` tem de **devolver** o texto (não imprimi-lo). Constrói-o com uma
f-string: `return f"({self.x}, {self.y})"`. Repara na vírgula e no espaço.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
