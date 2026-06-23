Úplně první řádek souboru zpřístupní modul: `import math`. Poté můžeš použít
cokoli, co poskytuje, jako `math.něco`.

---

`math.sqrt(x)` vrátí odmocninu z `x`. Chceš odmocninu z `a*a + b*b`. Dej `import
math` nahoru, pak napiš funkci.

---

import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)
