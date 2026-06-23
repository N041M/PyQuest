`from datetime import date`, pak `date(y, m, d)` vytvoří objekt. Má metodu
`.isoformat()`, která vrátí řetězec YYYY-MM-DD.

---

Zřetěz je: `date(y, m, d).isoformat()`. Doplnění nulami se vyřeší za tebe.

---

from datetime import date


def iso(y, m, d):
    return date(y, m, d).isoformat()
