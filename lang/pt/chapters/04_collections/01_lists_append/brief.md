# 4.1 -- Listas e append

## Conceito

Uma **lista** guarda vários valores por ordem, numa única variável. Escreve-se uma
lista com parênteses retos, com os itens separados por vírgulas:

```python
nums = [10, 20, 30]
print(nums)        # [10, 20, 30]
print(nums[0])     # 10   (index like a string -- from 0)
print(len(nums))   # 3
```

Uma lista pode começar vazia e crescer. `.append(x)` adiciona `x` ao **fim**:

```python
nums = []
nums.append(10)
nums.append(20)
print(nums)        # [10, 20]
```

Este padrão de "começar vazia e acrescentar num ciclo" é a forma como se constrói
uma lista a partir da entrada.

## Exemplo

```python
items = []
items.append(1)
items.append(2)
print(items)       # [1, 2]
```

## A tua tarefa

Lê um número inteiro `n`, depois lê mais `n` números inteiros (um por linha). Junta-os
numa lista com `.append()`, e imprime a lista final.

Para a entrada `3`, seguida de `1`, `2`, `3`:

```
[1, 2, 3]
```

## Está feito quando

- `3` com `1, 2, 3` imprime `[1, 2, 3]`.
- Uma contagem de `0` imprime `[]` (uma lista vazia).
