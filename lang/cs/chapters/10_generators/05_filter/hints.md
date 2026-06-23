Procházej každé číslo, ale `yield`ni jen ta, která projdou testem sudosti.

---

`for n in nums:` pak `if n % 2 == 0:` a, odsazené pod if, `yield n`.
Lichá čísla prostě propadnou bez yieldnutí.

---

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
