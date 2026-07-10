`map(func, nums)` aplica `func` a cada número. A tua `func` eleva a entrada ao
quadrado: `lambda x: x * x`.

---

`map` é preguiçoso, por isso envolve-o: `list(map(lambda x: x * x, nums))`.

---

def squares(nums):
    return list(map(lambda x: x * x, nums))
