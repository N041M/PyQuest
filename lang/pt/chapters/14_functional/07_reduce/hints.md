`from functools import reduce`. Recebe um combinador de dois argumentos, os
itens, e um valor inicial.

---

O combinador multiplica o resultado corrente pelo próximo número:
`reduce(lambda a, b: a * b, nums, 1)`. O valor inicial `1` faz com que a lista
vazia dê 1.

---

from functools import reduce


def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)
