"Divisível por 2" é n % 2 == 0. Precisas disso E do mesmo para o 3.

---

Junta as duas verificações com `and`, e imprime tudo:
`print(n % 2 == 0 and n % 3 == 0)`.

---

n = int(input())
print(n % 2 == 0 and n % 3 == 0)
