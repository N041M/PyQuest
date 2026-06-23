`for i, w in enumerate(words, 1):` ti dá číslo a slovo dohromady, počínaje 1.

---

Uvnitř cyklu sestav řádek f-řetězcem: `f"{i}. {w}"`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i, w in enumerate(words, 1):
    print(f"{i}. {w}")
