Percorre cada número, mas faz `yield` apenas dos que passam um teste de
paridade.

---

`for n in nums:` depois `if n % 2 == 0:` e, indentado sob o if, `yield n`.
Os números ímpares simplesmente passam sem serem produzidos.

---

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
