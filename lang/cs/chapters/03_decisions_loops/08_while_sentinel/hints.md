Přečti jedno číslo před cyklem a další čti na konci každého průchodu.

---

`total = 0`, přečti n, pak `while n != 0:` přičti k total a přečti další n.
Po cyklu vypiš total.

---

total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
