Começa um total acumulado em 0, abre o ficheiro, e percorre as suas linhas.

---

Cada linha é uma cadeia de caracteres como `"25\n"`. `int(line)` transforma-a
num número que podes somar. Imprime o total depois do ciclo.

---

total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
print(total)
