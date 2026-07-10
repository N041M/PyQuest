`__init__` define o ponto de partida: `self.count = 0`. Depois `tick`
altera-o.

---

Dentro de `tick`, faz `self.count = self.count + 1` (ou `self.count += 1`),
depois `return self.count`. Mantém a contagem em `self` para que cada
contador tenha a sua própria.

---

class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1
        return self.count
