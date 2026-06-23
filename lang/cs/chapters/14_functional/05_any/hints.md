`any(...)` bere posloupnost hodnot pravda/nepravda a vrátí True, pokud je nějaká
pravda. Tu posloupnost sestav generátorovým výrazem.

---

`any(n < 0 for n in nums)` -- pro každé číslo je test `n < 0` True nebo False a
`any` nahlásí, zda byla alespoň jedna True.

---

def has_negative(nums):
    return any(n < 0 for n in nums)
