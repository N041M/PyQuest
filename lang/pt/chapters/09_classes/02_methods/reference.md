Um **método** é uma função definida dentro de uma classe. Recebe sempre
**`self`** primeiro e calcula a partir dos próprios atributos do objeto, para
que o comportamento viva junto dos dados sobre os quais atua.

- Chama-o com `instance.method()`; o Python passa a instância como `self`
  automaticamente, por isso `p.dist()` chama `dist(p)`.
- Lá dentro, alcança os dados do objeto através de `self`: `self.x`, `self.y`.
- Um método pode receber mais parâmetros depois de `self` e `return` um valor
  como qualquer função.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

Point(3, 4).dist()      # 5.0
```
