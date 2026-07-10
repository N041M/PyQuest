# 4.6 -- Listas dentro de listas

## Conceito

Uma lista pode conter **outras listas**. É assim que se representam linhas de
dados, pares, grelhas, etc.:

```python
pairs = [[1, 2], [3, 4], [5, 6]]
print(pairs)        # [[1, 2], [3, 4], [5, 6]]
print(pairs[0])     # [1, 2]        the first inner list
print(pairs[0][1])  # 2            first inner list, second item
```

Dois índices: o primeiro escolhe uma lista interna, o segundo escolhe um item
dentro dela. Um ciclo dá-te cada lista interna, uma de cada vez:

```python
for p in pairs:
    print(p[0] + p[1])   # 3, 7, 11
```

## Exemplo

```python
grid = [[1, 1], [2, 2]]
for row in grid:
    print(row[0] + row[1])   # 2, 4
```

## A tua tarefa

Lê uma contagem `n`, depois `n` **pares** de números (cada par são dois números, em
duas linhas). Constrói uma lista de pares `[a, b]`. Primeiro imprime a lista
aninhada completa, depois imprime a **soma de cada par**, uma por linha.

Para a entrada `2`, seguida de `1`, `2`, `3`, `4`:

```
[[1, 2], [3, 4]]
3
7
```

## Está feito quando

- `1,2` e `3,4` imprimem `[[1, 2], [3, 4]]`, depois `3`, depois `7`.
- Uma contagem de `0` imprime `[]` e mais nada.
