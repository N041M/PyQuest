**`functools.reduce(func, iterable[, start])`** **dobra** uma sequência num
único valor, aplicando uma `func` de dois argumentos cumulativamente, da
esquerda para a direita: `func(func(func(i0, i1), i2), i3)...`. Cada passo
combina o resultado corrente com o próximo item.

- Um valor **inicial** (`reduce(func, items, start)`) semeia a dobragem e
  define o resultado para uma sequência **vazia**; sem ele, reduzir um
  iterável vazio lança `TypeError`.
- Generaliza o ciclo acumulador para *qualquer* combinador: `+` dá uma soma,
  `*` um produto, `max` o maior. O `sum` dedicado é o caso especial de `+`, e
  `math.prod` o de `*` — mas `reduce` dobra com a função que fornecires.
- `reduce` vive em `functools` (não é uma função nativa), por isso tem de ser
  importada.

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])      # 10
reduce(lambda a, b: a * b, [1, 2, 3, 4], 1)   # 24
reduce(lambda a, b: a if a > b else b, [3, 9, 2])   # 9  (max)
```
