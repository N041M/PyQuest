Um **`@classmethod`** está ligado à **classe**, não a uma instância: o seu
primeiro parâmetro é **`cls`** (a própria classe) em vez de `self`. Como tem a
classe, pode construir instâncias — o uso clássico é um **construtor
alternativo**.

- Chama-se na classe: `Point.from_tuple((3, 4))`. O Python passa `Point` como
  `cls`.
- Construir com `cls(...)` em vez do nome literal da classe significa que uma
  **subclasse** que chame o classmethod herdado recebe uma instância de *si
  própria*.
- Contrasta com **`@staticmethod`**, que não recebe nem `self` nem `cls` —
  apenas uma função simples colocada no espaço de nomes da classe, usada
  quando o método não precisa de acesso à instância nem à classe.

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    @classmethod
    def from_tuple(cls, pair): return cls(pair[0], pair[1])

Point.from_tuple((3, 4)).x     # 3
```
