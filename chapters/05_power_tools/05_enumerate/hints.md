`for i, w in enumerate(words, 1):` gives you the number and the word together,
starting at 1.

---

Inside the loop, build the line with an f-string: `f"{i}. {w}"`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i, w in enumerate(words, 1):
    print(f"{i}. {w}")
