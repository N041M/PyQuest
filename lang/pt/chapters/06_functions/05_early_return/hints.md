Cada caso é um if com o seu próprio return. Assim que um return executa, a função
termina.

---

Verifica `n < 0` primeiro, depois `n == 0`; se nenhum devolveu, n tem de ser positivo --
basta devolver "positive" sem condição nenhuma.

---

def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
