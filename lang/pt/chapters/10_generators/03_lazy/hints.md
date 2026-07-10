Precisas de um ciclo que nunca termina, produzindo um contador que sobe um
de cada vez. O `yield` é o que o impede de ficar pendurado.

---

Começa `i` em `0`. Depois `while True:` -- `yield i`, depois `i = i + 1`. O
ciclo "nunca termina", mas cada yield pausa-o até que o próximo valor seja
pedido.

---

def naturals():
    i = 0
    while True:
        yield i
        i = i + 1
