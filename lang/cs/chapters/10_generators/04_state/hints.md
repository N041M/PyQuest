Drž proměnnou `total` mimo cyklus, uvnitř cyklu k ní přičítej každé číslo a po
každém přičtení `yield`ni total.

---

`total = 0` před cyklem. Pak `for n in nums:` -- `total = total + n`,
pak `yield total`. Total se pamatuje napříč yieldy, takže pořád roste.

---

def running_total(nums):
    total = 0
    for n in nums:
        total = total + n
        yield total
