Os objetos **colaboram**: um método pode receber **outro objeto** da mesma
classe como parâmetro, ler os seus atributos, e **devolver um novo** objeto
com o resultado — deixando ambas as entradas inalteradas.

- `def add(self, other):` alcança `self.x` e `other.x`, depois
  `return Vector(self.x + other.x, ...)`. Devolver uma instância nova mantém
  os operandos imutáveis.
- É assim que os objetos do tipo valor se compõem (pontos, vetores, dinheiro).
  Definir o dunder `__add__` deixaria mesmo `a + b` chamá-lo.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

Vector(1, 2).add(Vector(3, 4)).x    # 4
```
