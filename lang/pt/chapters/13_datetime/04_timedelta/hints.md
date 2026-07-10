Importa `date` e `timedelta`. Analisa o texto e depois adiciona
`timedelta(days=n)` à data.

---

`date.fromisoformat(text) + timedelta(days=n)` dá uma nova data; chama
`.isoformat()` nessa data para obteres a cadeia. `n` negativo simplesmente
funciona.

---

from datetime import date, timedelta


def add_days(text, n):
    return (date.fromisoformat(text) + timedelta(days=n)).isoformat()
