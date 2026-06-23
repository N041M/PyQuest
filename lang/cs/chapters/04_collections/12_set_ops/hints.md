Dej každou skupinu do množiny, pak použij jejich průnik.

---

Sestav množinu `a` a množinu `b`, pak `print(len(a & b))`.

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
