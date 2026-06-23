Procházej čísla. Jakmile uvidíš `0`, zastav celý generátor; jinak číslo yieldni.

---

`for n in nums:` -- nejprve `if n == 0: return` (to ukončí generátor), pak
`yield n` pro vše před nulou.

---

def until_zero(nums):
    for n in nums:
        if n == 0:
            return
        yield n
