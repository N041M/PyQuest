„Dělitelné 2“ je n % 2 == 0. Potřebuješ to A totéž pro 3.

---

Spoj obě kontroly pomocí `and` a vypiš to celé:
`print(n % 2 == 0 and n % 3 == 0)`.

---

n = int(input())
print(n % 2 == 0 and n % 3 == 0)
