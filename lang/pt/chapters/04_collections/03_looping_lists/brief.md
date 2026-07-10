# 4.3 -- Percorrer uma lista num ciclo

## Conceito

Tal como uma cadeia de caracteres, uma lista é uma sequência -- por isso um ciclo
`for` percorre diretamente os seus itens, um por cada passagem:

```python
nums = [10, 20, 30]
for x in nums:
    print(x)        # 10, then 20, then 30
```

`len(nums)` dá o número de itens, e o slicing também funciona -- `nums[1:]` é tudo
menos o primeiro, `nums[:2]` são os dois primeiros:

```python
print(len(nums))    # 3
print(nums[:2])     # [10, 20]
```

## Exemplo

```python
xs = [1, 2, 3]
for x in xs:
    print(x * 10)   # 10, 20, 30
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números, para uma lista. Primeiro imprime quantos
números existem, depois imprime cada número **duplicado**, um por linha.

Para a entrada `3`, seguida de `5`, `2`, `9`:

```
3
10
4
18
```

## Está feito quando

- `5, 2, 9` imprime `3`, depois `10`, `4`, `18`.
- Uma contagem de `0` imprime apenas `0` (não há números para duplicar).
