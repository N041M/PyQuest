Constrói o dicionário, depois percorre d.items() num ciclo para obter cada chave e valor.

---

`for k, v in d.items(): print(f"{k}={v}")`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
for k, v in d.items():
    print(f"{k}={v}")
