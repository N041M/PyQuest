Lê um número antes do ciclo, e lê o seguinte no fim de cada passagem.

---

`total = 0`, lê n, depois `while n != 0:` soma ao total e lê o n seguinte.
Depois do ciclo, imprime total.

---

total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
