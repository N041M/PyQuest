Acrescenta `__lt__(self, other)` a Temperature. O Python chama-o para `<`, e
o `sorted` usa `<`.

---

Devolve a comparação dos valores: `return self.degrees < other.degrees`. Esse
único método já chega para tornar uma lista ordenável.

---

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __lt__(self, other):
        return self.degrees < other.degrees
