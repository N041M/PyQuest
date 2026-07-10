# 5.4 -- sorted()

## Conceito

`sorted(nums)` devolve uma **nova lista** com os mesmos itens por ordem, do mais pequeno
primeiro:

```python
nums = [3, 1, 2]
print(sorted(nums))    # [1, 2, 3]
print(nums)            # [3, 1, 2]  -- the original is untouched
```

Duas coisas a saber:

- Devolve uma *cópia*; a lista original mantém a sua ordem. (Também existe
  `nums.sort()`, um método que reordena a lista **no próprio local** -- útil mais tarde,
  mas `sorted()` é a opção mais segura por omissão porque nada é alterado às escondidas.)
- Do maior para o mais pequeno é só uma palavra-chave de distância: `sorted(nums, reverse=True)`.

Os duplicados mantêm-se -- ordenar reorganiza, nunca remove.

## Exemplo

```python
for x in sorted([3, 1, 2]):
    print(x)
# 1
# 2
# 3
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números inteiros. Imprime-os do mais pequeno ao maior,
um por linha.

Para a entrada `4`, depois `3`, `1`, `3`, `2`:

```
1
2
3
3
```

## Está feito quando

- `3, 1, 3, 2` imprime `1, 2, 3, 3` -- o `3` duplicado aparece duas vezes.
- Uma contagem de `0` não imprime nada.
- Usaste `sorted()`.
