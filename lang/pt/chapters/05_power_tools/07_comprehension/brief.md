# 5.7 -- Compreensões de listas

## Conceito

Uma forma de ciclo muito comum é *"construir uma nova lista fazendo algo a cada
item"*:

```python
doubled = []
for x in nums:
    doubled.append(x * 2)
```

O Python tem uma forma de uma linha exatamente para isso, chamada **compreensão de
lista**:

```python
doubled = [x * 2 for x in nums]
```

Lê-a de dentro para fora: *"para cada `x` em `nums`, coloca `x * 2` numa lista nova"*. Os
parênteses retos dizem "estou a construir uma lista"; a expressão antes de `for` é
aquilo em que cada item se transforma.

Funciona com qualquer coisa que possas percorrer -- incluindo `range`. Ler `n`
números (o que já fizeste uma dúzia de vezes) reduz-se a:

```python
nums = [int(input()) for _ in range(n)]
```

## Exemplo

```python
nums = [1, 2, 3]
squares = [x * x for x in nums]
print(squares)    # [1, 4, 9]
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números inteiros. Constrói uma nova lista onde cada
número está **duplicado**, depois imprime os seus itens um por linha.

Para a entrada `3`, depois `4`, `-1`, `0`:

```
8
-2
0
```

## Está feito quando

- `4, -1, 0` imprime `8, -2, 0` -- cada um duplicado, ordem mantida.
- Uma contagem de `0` não imprime nada.
- Usaste uma compreensão de lista para construir uma lista.
