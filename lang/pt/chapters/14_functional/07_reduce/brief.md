# 14.7 -- reduce: dobrar uma sequência num único valor

## Conceito

**`reduce`** (de `functools`) **dobra** uma sequência inteira num único valor,
aplicando uma função de dois argumentos cumulativamente, da esquerda para a
direita:

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])     # 10  ((((1+2)+3)+4))
reduce(lambda a, b: a * b, [1, 2, 3, 4])     # 24
```

- `reduce(func, items)` calcula `func(func(func(i0, i1), i2), i3)...` -- cada
  passo combina o resultado corrente com o próximo item.
- Um terceiro argumento é um valor **inicial**: `reduce(func, items, start)`
  começa a dobragem a partir de `start`, que também define a resposta para uma
  sequência **vazia**.
- É o ciclo acumulador (capítulo 3) como função de ordem superior. (`sum` é o
  caso especial para `+`; `reduce` permite-te dobrar com *qualquer*
  combinador.)

## Exemplo

```python
from functools import reduce

def total(nums):
    return reduce(lambda a, b: a + b, nums, 0)
```

## A tua tarefa

Usando **`reduce`** de `functools`, define `product(nums)` que devolve o
produto de todos os números (com um valor inicial de `1`, para que a lista
vazia dê `1`).

## Está feito quando

- `product([1, 2, 3, 4])` devolve `24`; `product([5])` devolve `5`.
- `product([])` devolve `1`.
- A dobragem usa `reduce`, não um ciclo acumulador manual.
