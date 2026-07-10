# 14.4 -- sorted(key=lambda): ordenar por um valor derivado

## Conceito

`sorted` (capítulo 5) ordena os itens pela sua ordem natural. O seu argumento
**`key=`** muda *aquilo* por que ordena: uma função que faz corresponder cada
item ao valor a comparar. Uma **lambda** em linha é a forma habitual de a
escrever:

```python
words = ["pear", "fig", "apple"]
sorted(words, key=len)                  # ['fig', 'pear', 'apple']
sorted(words, key=lambda w: w[-1])      # by last letter
```

- `key` é chamada uma vez por item; `sorted` ordena então os itens por esses
  valores-chave.
- A lambda permite ordenar por qualquer coisa **derivada** de um item -- o
  seu comprimento, um campo, uma pontuação calculada -- sem alterar os próprios
  itens.
- `sorted` é **estável**: itens com chaves iguais mantêm a sua ordem
  original.

## Exemplo

```python
def by_size(nums):
    return sorted(nums, key=lambda n: abs(n))   # by distance from zero
```

## A tua tarefa

Usando **`sorted`** com um **`key=lambda`**, define `by_last(words)` que
devolve as palavras ordenadas pelo seu **último caráter**.

## Está feito quando

- `by_last(["pear", "fig", "kiwi"])` devolve `["fig", "kiwi", "pear"]`
  (as últimas letras g, i, r estão por ordem).
- `by_last([])` devolve `[]`.
- A ordem vem de `sorted(..., key=lambda ...)`, não de uma ordenação manual.
