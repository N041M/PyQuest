Posbírej slova do seznamu, pak je spoj. join se volá na oddělovači.

---

Sestav seznam, pak `print("-".join(words))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print("-".join(words))
