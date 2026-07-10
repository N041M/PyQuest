Percorre os números `0, 1, ..., n-1` com um ciclo, e faz `yield` de cada um
elevado ao quadrado.

---

`for i in range(n):` depois `yield i * i`. O ciclo dá-te cada número; o
yield emite o seu quadrado e pausa até que o próximo seja pedido.

---

def squares(n):
    for i in range(n):
        yield i * i
