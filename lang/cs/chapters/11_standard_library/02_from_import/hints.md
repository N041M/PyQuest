Začni soubor s `from math import gcd`. Teď je `gcd` funkce, kterou můžeš volat
přímo, bez `math.` před ní.

---

Najdi `g = gcd(num, den)`, pak vrať n-tici `(num // g, den // g)`. Použij `//`
(celočíselné dělení), aby výsledek zůstal celými čísly.

---

from math import gcd


def simplify(num, den):
    g = gcd(num, den)
    return (num // g, den // g)
