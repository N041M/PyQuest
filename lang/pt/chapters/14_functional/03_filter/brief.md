# 14.3 -- filter: manter o que passa

## Conceito

Enquanto `map` transforma cada item, **`filter`** mantém apenas **alguns**
deles. Dás-lhe um **predicado** -- uma função que devolve verdadeiro ou falso --
e ele mantém cada item ao qual o predicado diz que sim:

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))     # [2, 4]
```

- `filter(pred, iterable)` produz cada item para o qual `pred(item)` é
  verdadeiro, descartando o resto, por ordem.
- Tal como `map`, devolve um **iterador preguiçoso**, por isso envolve-o em
  `list(...)`.

(A compreensão `[x for x in items if pred(x)]` faz o mesmo; este puzzle é
sobre o próprio `filter`.)

## Exemplo

```python
def nonempty(strings):
    return list(filter(lambda s: s != "", strings))
```

## A tua tarefa

Usando **`filter`**, define `evens(nums)` que devolve uma lista apenas com os
números pares em `nums`.

## Está feito quando

- `evens([1, 2, 3, 4])` devolve `[2, 4]`.
- `evens([1, 3, 5])` devolve `[]`.
- A seleção é feita com `filter`, não com uma compreensão ou um ciclo manual.
