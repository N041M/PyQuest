# 4.13 -- Escolher a coleção certa

## Conceito

Já tens quatro coleções. Escolher a certa torna um problema fácil:

- **lista** -- itens ordenados, duplicados permitidos (`[1, 2, 2]`). Usa para sequências.
- **tuplo** -- como uma lista mas fixo/imutável. Usa para grupos fixos.
- **conjunto** -- itens não ordenados e **únicos**. Usa para "distintos" e pertença rápida.
- **dicionário** -- consulta chave -> valor. Usa para "dado X, encontra o seu Y".

Este puzzle combina algumas:

- `len(nums)` -- quantos itens (uma **lista** guarda todos os valores, incluindo repetidos).
- `len(set(nums))` -- quantos valores **distintos** (um **conjunto** descarta duplicados).
- a **soma** -- um ciclo com um acumulador (ou `sum(nums)`).

## Exemplo

```python
nums = [1, 2, 2, 3]
print(len(nums))        # 4
print(len(set(nums)))   # 3
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números. Imprime três linhas:

1. quantos números existem,
2. quantos números **distintos** existem,
3. o seu **total**.

Para a entrada `4`, seguida de `1`, `2`, `2`, `3`:

```
4
3
8
```

## Está feito quando

- `1, 2, 2, 3` imprime `4`, `3`, `8`.
- Uma contagem de `0` imprime `0`, `0`, `0`.
