Lê primeiro a contagem. Começa um total em 0 e depois repete esse número de
vezes, somando cada número.

---

`n = int(input())`, `total = 0`, depois `for _ in range(n):` soma `int(input())`
ao total. Imprime total depois do ciclo.

---

n = int(input())
total = 0
for _ in range(n):
    total = total + int(input())
print(total)
