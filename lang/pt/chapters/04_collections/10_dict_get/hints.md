d[key] falha se a chave não existir. d.get(key, 0) devolve 0 em vez disso.

---

Depois de construir o dicionário e ler a consulta, `print(d.get(query, 0))`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
query = input()
print(d.get(query, 0))
