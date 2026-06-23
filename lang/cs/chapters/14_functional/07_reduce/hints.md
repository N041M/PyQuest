`from functools import reduce`. Bere dvouargumentový kombinátor, položky a
počáteční hodnotu.

---

Kombinátor násobí průběžný výsledek dalším číslem:
`reduce(lambda a, b: a * b, nums, 1)`. Počátek `1` zařídí, že prázdný seznam dá 1.

---

from functools import reduce


def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)
