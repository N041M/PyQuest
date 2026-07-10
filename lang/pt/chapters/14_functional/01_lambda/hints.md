Uma lambda é `lambda args: expression`. Queres uma que receba um `x` e devolva
`x * n`.

---

`multiplier` devolve essa lambda. A lambda captura `n`, por isso cada chamada a
`multiplier` cria uma função ligada ao seu próprio `n`.

---

def multiplier(n):
    return lambda x: x * n
