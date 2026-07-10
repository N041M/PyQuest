# 3.5 -- and / or / not

## Conceito

Podes combinar booleanos com três palavras:

- `and` -- True apenas se **ambos** os lados forem True.
- `or` -- True se **qualquer um** dos lados for True.
- `not` -- inverte um booleano: `not True` é `False`.

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

age = 25
print(age >= 18 and age < 65)   # True  (both hold)
```

Isto permite que uma única condição teste várias coisas ao mesmo tempo.

## Exemplo

```python
n = 12
print(n % 2 == 0 and n % 3 == 0)   # True  (12 is divisible by both)
```

## A tua tarefa

Lê um número inteiro. Imprime se é divisível **tanto** por 2 como por 3 -- isto
é, imprime o resultado de `(n % 2 == 0) and (n % 3 == 0)` (que é `True` ou
`False`).

Para a entrada `12` a saída é:

```
True
```

## Está feito quando

- `12` e `6` imprimem `True`; `4` e `9` imprimem `False`.
- `0` imprime `True` (0 é divisível por tudo).
