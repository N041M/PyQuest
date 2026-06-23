`sorted(words, key=...)` řadí podle toho, co vrátí klíčová funkce. Chceš řadit podle
posledního znaku každého slova.

---

Poslední znak `w` je `w[-1]`, takže klíč je `lambda w: w[-1]`:
`sorted(words, key=lambda w: w[-1])`.

---

def by_last(words):
    return sorted(words, key=lambda w: w[-1])
