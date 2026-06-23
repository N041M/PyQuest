Potřebuješ cyklus, který nikdy neskončí, yieldující počítadlo, které se pokaždé
zvýší o jedna. `yield` je to, co mu brání zamrznout.

---

Začni `i` na `0`. Pak `while True:` -- `yield i`, pak `i = i + 1`. Cyklus „nikdy
neskončí“, ale každý yield ho pozastaví, dokud se nechce další hodnota.

---

def naturals():
    i = 0
    while True:
        yield i
        i = i + 1
