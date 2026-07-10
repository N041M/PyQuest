Cria um dicionário vazio, e depois guarda cada par como d[word] = number.

---

`d = {}`, percorre num ciclo lendo palavra + número com `d[word] = int(input())`,
depois lê a consulta e `print(d[query])`.

---

n = int(input())
d = {}
for _ in range(n):
    word = input()
    d[word] = int(input())
query = input()
print(d[query])
