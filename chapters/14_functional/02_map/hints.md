`map(func, nums)` applies `func` to each number. Your `func` squares its input:
`lambda x: x * x`.

---

`map` is lazy, so wrap it: `list(map(lambda x: x * x, nums))`.

---

def squares(nums):
    return list(map(lambda x: x * x, nums))
