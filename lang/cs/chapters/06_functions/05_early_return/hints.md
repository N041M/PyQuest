Každý případ je if s vlastním return. Jakmile return proběhne, funkce je u konce.

---

Nejprve zkontroluj `n < 0`, pak `n == 0`; pokud ani jeden nevrátil, musí být n
kladné -- prostě vrať "positive" bez podmínky.

---

def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
