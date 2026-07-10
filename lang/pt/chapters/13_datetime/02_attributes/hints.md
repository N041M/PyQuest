`date.fromisoformat(text)` transforma a cadeia num objeto de data. Guarda-o
numa variável.

---

Lê `d.year`, `d.month`, `d.day` desse objeto e devolve-os como um tuplo.

---

from datetime import date


def parts(text):
    d = date.fromisoformat(text)
    return (d.year, d.month, d.day)
