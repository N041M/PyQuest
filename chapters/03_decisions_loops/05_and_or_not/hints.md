"Divisible by 2" is n % 2 == 0. You need that AND the same for 3.

---

Join the two checks with `and`, and print the whole thing:
`print(n % 2 == 0 and n % 3 == 0)`.

---

n = int(input())
print(n % 2 == 0 and n % 3 == 0)
