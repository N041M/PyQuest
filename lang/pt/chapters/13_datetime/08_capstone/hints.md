Três passos, três ferramentas: `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")`
para analisar, `+ timedelta(hours=hours)` para deslocar, `.strftime("%Y-%m-%d %H:%M")`
para formatar.

---

Importa `datetime` e `timedelta`. Analisa para um datetime, adiciona o
timedelta, e depois devolve o strftime do resultado. Horas negativas
funcionam da mesma forma.

---

from datetime import datetime, timedelta


def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    dt = dt + timedelta(hours=hours)
    return dt.strftime("%Y-%m-%d %H:%M")
