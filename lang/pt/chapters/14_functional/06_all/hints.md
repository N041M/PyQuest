`all(...)` devolve True apenas se todos os valores na sequência forem
verdadeiros. Constrói a sequência de testes com uma expressão geradora.

---

`all(n > 0 for n in nums)` -- cada `n > 0` é True ou False, e `all` é True
apenas se nenhum for False.

---

def all_positive(nums):
    return all(n > 0 for n in nums)
