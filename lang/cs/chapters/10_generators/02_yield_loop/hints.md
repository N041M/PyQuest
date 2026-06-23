Projdi čísla `0, 1, ..., n-1` cyklem a `yield`ni každé umocněné.

---

`for i in range(n):` pak `yield i * i`. Cyklus ti dá každé číslo; yield vydá jeho
druhou mocninu a pozastaví se, dokud není požádán o další.

---

def squares(n):
    for i in range(n):
        yield i * i
