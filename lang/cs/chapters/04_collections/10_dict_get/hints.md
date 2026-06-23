d[key] spadne, pokud klíč chybí. d.get(key, 0) místo toho vrátí 0.

---

Po sestavení slovníku a přečtení dotazu `print(d.get(query, 0))`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
query = input()
print(d.get(query, 0))
