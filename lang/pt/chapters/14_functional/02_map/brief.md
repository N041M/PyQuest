# 14.2 -- map: aplicar a cada item

## Conceito

**`map(func, iterable)`** executa `func` em **cada** item e produz os
resultados. É o padrão "aplicar a cada" como função de ordem superior -- uma
função que recebe outra função:

```python
list(map(str.upper, ["a", "b"]))     # ['A', 'B']
list(map(lambda x: x * x, [1, 2, 3])) # [1, 4, 9]
```

- `map` devolve um **iterador preguiçoso**, por isso envolve-o em `list(...)`
  para obteres uma lista.
- A função pode ser uma `lambda`, um `def`, ou uma função nativa como
  `str.upper` ou `int`.

(Uma compreensão de lista `[f(x) for x in items]` faz a mesma coisa e muitas
vezes lê-se de forma mais natural; este puzzle é sobre aprender o próprio `map`,
a ferramenta que vais encontrar em imenso código.)

## Exemplo

```python
def lengths(words):
    return list(map(len, words))
```

## A tua tarefa

Usando **`map`**, define `squares(nums)` que devolve uma lista com cada
número de `nums` elevado ao quadrado.

## Está feito quando

- `squares([1, 2, 3])` devolve `[1, 4, 9]`.
- `squares([])` devolve `[]`.
- O mapeamento é feito com `map`, não com uma compreensão ou um ciclo manual.
