Responde primeiro ao caso mais pequeno: se n é 0, devolve 1 -- não é preciso chamar nada.

---

Para todo o resto, confia na função que estás a escrever:
return n * fact(n - 1). O retorno antecipado (6.5) mantém o caso base limpo.

---

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
