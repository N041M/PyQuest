**`__lt__(self, other)`** define o operador **`<`** para os teus objetos, e
`<` é exatamente o que **`sorted`**, **`min`** e **`max`** usam para ordenar
as coisas. Sem ele, comparar dois dos teus objetos levanta `TypeError`; com
ele, uma lista deles ordena-se diretamente.

- O Python chama `a.__lt__(b)` para `a < b`; devolve se `a` deve vir
  **antes** de `b`, normalmente comparando o atributo pelo qual ordenas.
- `sorted` só precisa de `<`, por isso só `__lt__` já torna os objetos
  ordenáveis. O conjunto completo dos dunders de ordenação é `__lt__`,
  `__le__`, `__gt__`, `__ge__`.
- `functools.total_ordering` é um decorador de classe que preenche os outros
  três a partir de `__lt__` e `__eq__`, se quiseres todas as comparações.

```python
class Temperature:
    def __init__(self, degrees): self.degrees = degrees
    def __lt__(self, other): return self.degrees < other.degrees

sorted([Temperature(30), Temperature(10), Temperature(20)])   # 10, 20, 30
min([Temperature(30), Temperature(10)]).degrees               # 10
```
