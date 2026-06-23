Nejprve přečti počet. Začni total na 0, pak se tolikrát zatoč a každé číslo
přičti.

---

`n = int(input())`, `total = 0`, pak `for _ in range(n):` přičti `int(input())`
k total. Po cyklu vypiš total.

---

n = int(input())
total = 0
for _ in range(n):
    total = total + int(input())
print(total)
