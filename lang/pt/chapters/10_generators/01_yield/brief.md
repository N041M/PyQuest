# 10.1 -- yield: uma função que pausa

## Conceito

Uma função normal faz `return` **uma vez** e está feita. Um **gerador** é uma
função que usa `yield` em vez disso: cada `yield` devolve **um** valor e
**pausa** a função exatamente ali. Pede o próximo valor e ela **retoma**
a partir de onde parou.

```python
def two_words():
    yield "hello"
    yield "world"
```

Chamá-la **não** executa o corpo. Dá-te um **gerador** -- um objeto de onde
retiras valores, um de cada vez, normalmente com um ciclo `for`:

```python
for w in two_words():
    print(w)        # hello, then world
```

A recompensa: um gerador produz uma sequência **sem construir a lista toda
em memória**. Vais sentir isso em 10.3.

## Exemplo

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1
```

`list(count_up(3))` é `[1, 2, 3]` -- cada passagem do ciclo produz um número,
depois pausa até que o próximo seja pedido.

## A tua tarefa

Define um gerador `count_down(n)` que **produz** os números inteiros de `n`
até `1`, por essa ordem. Se `n` for `0` (ou menos), não produz nada.

## Está feito quando

- `list(count_down(5))` é `[5, 4, 3, 2, 1]`.
- `list(count_down(1))` é `[1]`; `list(count_down(0))` é `[]`.
- Usas `yield` -- portanto chamar `count_down` devolve um gerador, não uma
  lista.
