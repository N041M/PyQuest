A set drops duplicates. Put the words in a set, then count it.

---

Collect the words in a list, then `print(len(set(words)))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(len(set(words)))
