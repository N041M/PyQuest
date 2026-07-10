Mantém uma variável `total` fora do ciclo, soma-lhe cada número dentro do
ciclo, e faz `yield` do total após cada adição.

---

`total = 0` antes do ciclo. Depois `for n in nums:` -- `total = total + n`,
depois `yield total`. O total é recordado ao longo dos yields, por isso
continua a crescer.

---

def running_total(nums):
    total = 0
    for n in nums:
        total = total + n
        yield total
