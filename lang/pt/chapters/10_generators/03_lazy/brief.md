# 10.3 -- os geradores são preguiçosos

## Conceito

Este é o superpoder. Um gerador só faz trabalho **quando pedes o próximo
valor**. Nunca constrói a sequência toda antecipadamente -- portanto um
gerador pode ser **infinito** e ainda assim custar quase nada até retirares
dele.

```python
def naturals():
    i = 0
    while True:        # never stops on its own...
        yield i
        i = i + 1
```

`while True` numa função normal ficaria pendurado para sempre. Num gerador
está tudo bem: cada `yield` **pausa** o ciclo até que quem chama queira mais
um. Retiras apenas quantos precisares:

```python
from itertools import islice
list(islice(naturals(), 4))     # [0, 1, 2, 3] -- then it just stops asking
```

`islice(gen, k)` retira os primeiros `k` itens de um gerador e nada mais. O
gerador produz exatamente esses quatro, depois fica pausado.

## Exemplo

O `naturals()` acima produz `0, 1, 2, 3, ...` sem fim. Retirar 3 itens dá
`[0, 1, 2]`; retirar 10 dá `[0, 1, ..., 9]`. O mesmo gerador infinito,
pedido em quantidades diferentes.

## A tua tarefa

Define um gerador **infinito** `naturals()` que produz os números inteiros a
começar em `0`: `0, 1, 2, 3, ...` para sempre. Nunca se pode parar sozinho; o
verificador só alguma vez retira um punhado de valores dele.

## Está feito quando

- Os primeiros 5 valores de `naturals()` são `[0, 1, 2, 3, 4]`.
- É infinito -- retirar mais valores dá simplesmente mais números; nunca se
  esgota.
- Usas `yield`, portanto chamar `naturals()` devolve um gerador.
