# 5.2 -- sum()

## Conceito

Em 3.12 escreveste o **padrão acumulador** à mão:

```python
total = 0
for x in nums:
    total = total + x
```

Esse padrão é tão comum que o Python o traz como função nativa:

```python
total = sum(nums)
```

`sum(list_of_numbers)` soma cada item e devolve o total. Numa lista vazia
devolve `0` -- exatamente o valor com que o teu acumulador escrito à mão começava.

Este capítulo está cheio destas **ferramentas poderosas**: funções nativas que substituem um
ciclo que já escreveste tu mesmo uma vez. Ganhas o atalho por saberes o que ele substitui.

## Exemplo

```python
nums = [3, 1, 4]
print(sum(nums))    # 8
print(sum([]))      # 0
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números inteiros (um por linha). Imprime o seu total
usando `sum()`.

Para a entrada `3`, depois `3`, `1`, `4`:

```
8
```

## Está feito quando

- `3, 1, 4` imprime `8`; negativos também funcionam.
- Uma contagem de `0` imprime `0`.
- Usaste `sum()` -- desta vez, não um ciclo escrito à mão.
