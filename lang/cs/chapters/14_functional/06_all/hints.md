`all(...)` vrátí True jen tehdy, když je každá hodnota v posloupnosti pravda.
Posloupnost testů sestav generátorovým výrazem.

---

`all(n > 0 for n in nums)` -- každé `n > 0` je True nebo False a `all` je True jen
tehdy, když žádná nebyla False.

---

def all_positive(nums):
    return all(n > 0 for n in nums)
