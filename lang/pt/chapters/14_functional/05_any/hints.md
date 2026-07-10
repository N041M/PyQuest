`any(...)` recebe uma sequência de valores verdadeiro/falso e devolve True se
algum for verdadeiro. Constrói essa sequência com uma expressão geradora.

---

`any(n < 0 for n in nums)` -- para cada número, o teste `n < 0` é True ou
False, e `any` informa se pelo menos um foi True.

---

def has_negative(nums):
    return any(n < 0 for n in nums)
