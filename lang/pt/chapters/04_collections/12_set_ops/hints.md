Coloca cada grupo num conjunto, depois usa a interseção dos dois.

---

Constrói o conjunto `a` e o conjunto `b`, depois `print(len(a & b))`.

---

n = int(input())
a = set()
for _ in range(n):
    a.add(input())
m = int(input())
b = set()
for _ in range(m):
    b.add(input())
print(len(a & b))
