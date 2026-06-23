`map(func, nums)` aplikuje `func` na každé číslo. Tvá `func` umocní svůj vstup:
`lambda x: x * x`.

---

`map` je líný, takže ho obal: `list(map(lambda x: x * x, nums))`.

---

def squares(nums):
    return list(map(lambda x: x * x, nums))
