„Sudé“ znamená, že zbytek po dělení 2 je nula: `x % 2 == 0`.

---

Dej ten test na konec komprehenze:
`evens = [x for x in nums if x % 2 == 0]` -- pak vypiš každou položku.

---

n = int(input())
nums = [int(input()) for _ in range(n)]
evens = [x for x in nums if x % 2 == 0]
for e in evens:
    print(e)
