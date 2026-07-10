`from datetime import date`, depois `date(y, m, d)` cria o objeto. Tem um
método `.isoformat()` que devolve a cadeia YYYY-MM-DD.

---

Encadeia-os: `date(y, m, d).isoformat()`. O preenchimento com zeros é tratado
por ti.

---

from datetime import date


def iso(y, m, d):
    return date(y, m, d).isoformat()
