# 4.11 -- Conjuntos

## Conceito

Um **conjunto** é uma coleção não ordenada de itens **únicos** -- descarta
automaticamente duplicados. Escreve-se um com chavetas, ou constrói-se um a partir
de uma lista com `set(...)`:

```python
s = {1, 2, 2, 3}
print(s)              # {1, 2, 3}   (the duplicate 2 is gone)

nums = [1, 1, 2, 3, 3]
print(set(nums))      # {1, 2, 3}
print(len(set(nums))) # 3           how many *distinct* values
```

Os conjuntos são ótimos para "quantas coisas diferentes?" e para testes rápidos de
pertença com `in`:

```python
print(2 in s)         # True
```

(Os conjuntos não têm ordem nem indexação -- não podes fazer `s[0]`.)

## Exemplo

```python
words = ["a", "b", "a"]
print(len(set(words)))   # 2
```

## A tua tarefa

Lê uma contagem `n`, depois `n` palavras. Imprime quantas palavras **distintas**
existem.

Para a entrada `4`, `a`, `b`, `a`, `c`:

```
3
```

(`a` aparece duas vezes mas conta uma só vez.)

## Está feito quando

- `a, b, a, c` imprime `3`.
- Uma contagem de `0` imprime `0`.
