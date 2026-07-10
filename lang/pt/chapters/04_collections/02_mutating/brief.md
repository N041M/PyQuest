# 4.2 -- Alterar uma lista

## Conceito

Ao contrário das cadeias de caracteres, as listas podem ser **alteradas no próprio
local** (são *mutáveis*). Algumas formas:

- Substituir um item pelo índice: `nums[0] = 99`
- Remover e devolver o **último** item: `nums.pop()`
- Remover o primeiro **valor** correspondente: `nums.remove(20)`

```python
nums = [10, 20, 30]
nums[0] = 99      # [99, 20, 30]   replace by position
nums.pop()        # [99, 20]       drop the last item (returns 30)
print(nums)       # [99, 20]
```

Estas alterações mudam a lista já existente -- a variável continua a apontar para a
mesma lista, agora modificada.

## Exemplo

```python
xs = [1, 2, 3]
xs[1] = 0
xs.pop()
print(xs)         # [1, 0]
```

## A tua tarefa

Lê uma contagem `n` (pelo menos 1), depois `n` números, para uma lista. Depois:

1. **duplica o primeiro item** (substitui `nums[0]` por `nums[0] * 2`), e
2. **remove o último item** com `.pop()`.

Imprime a lista resultante. Para a entrada `3`, seguida de `5`, `2`, `9`:

```
[10, 2]
```

(`[5, 2, 9]` -> duplica o primeiro -> `[10, 2, 9]` -> pop -> `[10, 2]`.)

## Está feito quando

- `5, 2, 9` dá `[10, 2]`.
- Um único número `n=1` (por exemplo, apenas `4`) dá `[]` -- duplicado para `[8]`,
  e depois o último (e único) item é removido com pop.
