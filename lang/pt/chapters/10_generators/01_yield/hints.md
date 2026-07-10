Um gerador parece uma função normal, mas diz `yield` onde uma normal
construiria um resultado. Cada `yield` produz um número.

---

Conta com um ciclo de `n` para baixo e faz `yield` de cada valor. Um ciclo
`while`: começa `i` em `n`, `yield i`, depois `i = i - 1`, enquanto
`i >= 1`. (Um `for i in range(n, 0, -1):` também funciona.)

---

def count_down(n):
    i = n
    while i >= 1:
        yield i
        i = i - 1
