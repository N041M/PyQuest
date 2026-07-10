# 4.5 -- join: de lista para texto

## Conceito

`.join()` é o oposto de `split`: cola uma **lista de cadeias de caracteres** numa só
cadeia, colocando um separador entre cada parte. Chama-se este método *sobre o
separador*:

```python
words = ["a", "b", "c"]
print("-".join(words))    # a-b-c
print(", ".join(words))   # a, b, c
print("".join(words))     # abc   (no separator)
```

Lê-se como "junta estas palavras com este separador entre elas". A lista tem de
conter cadeias de caracteres.

## Erro comum

`join` escreve-se com o separador primeiro: `"-".join(words)`, **não**
`words.join("-")`.

## Exemplo

```python
parts = ["2024", "12", "25"]
print("/".join(parts))    # 2024/12/25
```

## A tua tarefa

Lê uma contagem `n`, depois `n` palavras (uma por linha), para uma lista. Imprime-as
juntas com um traço `-`.

Para a entrada `3`, seguida de `a`, `b`, `c`:

```
a-b-c
```

## Está feito quando

- `a, b, c` imprime `a-b-c`; uma única palavra imprime apenas essa palavra.
- Uma contagem de `0` imprime uma linha vazia (nada para juntar).
