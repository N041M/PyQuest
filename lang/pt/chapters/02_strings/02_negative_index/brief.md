# 2.2 -- Indexação negativa

## Conceito

Também podes contar a partir do **fim** de uma cadeia de caracteres usando índices negativos. `-1` é
o último caractere, `-2` o penúltimo, e assim por diante.

```
character:   c   a   t
index:       0   1   2
from end:   -3  -2  -1
```

```python
word = "cat"
print(word[-1])   # t
print(word[-2])   # a
```

Isto é útil quando não queres contar o comprimento: `s[-1]` é sempre o
último caractere, seja qual for o comprimento da cadeia.

## Exemplo

```python
s = "python"
print(s[-1])   # n
```

## A tua tarefa

Lê uma palavra e depois imprime o seu **último** caractere.

Para a entrada `hello` a saída é:

```
o
```

## Está feito quando

- Para `hello` imprime `o`.
- Também funciona para uma palavra de uma só letra (`-1` aponta para esse único caractere).
