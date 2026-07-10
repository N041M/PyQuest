# 8.3 -- Somar um ficheiro

## Conceito

Um ficheiro é sempre **texto**. Uma linha que parece `42` chega como a cadeia
de caracteres `"42\n"`, não como o número 42 -- por isso, antes de poderes
fazer contas, tens de a converter com `int()` (1.11), exatamente como fizeste
com `input()`.

`int()` ignora de bom grado os espaços em branco à volta, por isso
`int("42\n")` é `42` -- nem sequer precisas de fazer `strip` primeiro.

```python
total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
```

## Exemplo

Para um `prices.txt` de:

```
10
25
7
```

o total é `42`.

## A tua tarefa

`prices.txt` contém um número inteiro por linha. Lê-os, soma-os todos, e
imprime o total.

## Está feito quando

- O programa imprime a soma de todos os números do ficheiro.
- Números negativos e um ficheiro de uma só linha funcionam ambos.
- Abriste o ficheiro com `with` e converteste cada linha com `int()`.
