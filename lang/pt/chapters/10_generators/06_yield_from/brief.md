# 10.6 -- yield from: passar um fluxo inteiro adiante

## Conceito

Quando queres que um gerador reemita **todos** os itens de outro iterável,
podias percorrê-lo e fazer `yield` de cada um:

```python
def both(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
```

O Python tem um atalho para exatamente esse ciclo interno: **`yield from`**.

```python
def both(a, b):
    yield from a        # yield every item of a, one by one
    yield from b        # then every item of b
```

`yield from iterável` significa "faz yield de cada valor que este iterável
produz". As duas versões acima comportam-se de forma idêntica; `yield from`
apenas o diz numa linha.

## Exemplo

```python
def repeat_each(items):
    for x in items:
        yield from (x, x)      # yield x, then x again

list(repeat_each([1, 2]))      # [1, 1, 2, 2]
```

## A tua tarefa

Define um gerador `chain(a, b)` que produz **todos** os itens de `a`, depois
**todos** os itens de `b`, por ordem. Usa `yield from`. Qualquer uma das
listas pode estar vazia.

## Está feito quando

- `list(chain([1, 2], [3, 4]))` é `[1, 2, 3, 4]`.
- `list(chain([], [9]))` é `[9]`; `list(chain([], []))` é `[]`.
- Usas `yield from`, portanto chamar `chain` devolve um gerador.
