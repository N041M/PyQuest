Collect the words into a list, then join them. join is called on the separator.

---

Build the list, then `print("-".join(words))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print("-".join(words))
