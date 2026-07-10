Percorre os números. Assim que vires um `0`, para o gerador inteiro; caso
contrário faz `yield` do número.

---

`for n in nums:` -- primeiro `if n == 0: return` (isto termina o gerador),
depois `yield n` para tudo antes do zero.

---

def until_zero(nums):
    for n in nums:
        if n == 0:
            return
        yield n
