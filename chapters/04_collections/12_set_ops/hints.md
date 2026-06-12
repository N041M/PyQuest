Put each group in a set, then use the intersection of the two.

---

Build set `a` and set `b`, then `print(len(a & b))`.

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
