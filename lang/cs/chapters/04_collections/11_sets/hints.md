Množina zahodí duplicity. Dej slova do množiny, pak ji spočítej.

---

Posbírej slova do seznamu, pak `print(len(set(words)))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(len(set(words)))
