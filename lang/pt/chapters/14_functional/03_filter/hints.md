`filter(pred, nums)` mantém cada número onde `pred` é verdadeiro. O teu
predicado testa a paridade: `lambda x: x % 2 == 0`.

---

Envolve-o em `list(...)`: `list(filter(lambda x: x % 2 == 0, nums))`.

---

def evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
