`for i, w in enumerate(words, 1):` dá-te o número e a palavra juntos,
a começar em 1.

---

Dentro do ciclo, constrói a linha com uma f-string: `f"{i}. {w}"`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i, w in enumerate(words, 1):
    print(f"{i}. {w}")
