Generátor vypadá jako normální funkce, ale řekne `yield` tam, kde by normální
sestavila výsledek. Každý `yield` vyprodukuje jedno číslo.

---

Počítej cyklem od `n` dolů a `yield`ni každou hodnotu. Cyklus `while`: začni `i`
na `n`, `yield i`, pak `i = i - 1`, dokud `i >= 1`. (Funguje i
`for i in range(n, 0, -1):`.)

---

def count_down(n):
    i = n
    while i >= 1:
        yield i
        i = i - 1
