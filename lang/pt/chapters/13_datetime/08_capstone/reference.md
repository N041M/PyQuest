A tarefa final é a **viagem de ida e volta** completa através do módulo,
compondo três das suas ferramentas:

1. **Analisar** — `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` lê a
   cadeia e produz um `datetime`.
2. **Deslocar** — adicionar `timedelta(hours=h)` move-o por uma duração,
   avançando automaticamente ao longo de minutos, dias, meses e anos (e para
   trás no caso de `h` negativo).
3. **Formatar** — `.strftime("%Y-%m-%d %H:%M")` apresenta o resultado de
   volta no mesmo formato.

O objetivo do capítulo numa única função: cada caso complicado — uma hora que
atravessa a meia-noite, um dia que passa para um novo mês ou ano, um dia
bissexto — é tratado pelos tipos de `datetime`, não por ti. Tu descreves os
passos; a biblioteca mantém o calendário honesto.

```python
from datetime import datetime, timedelta

def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    return (dt + timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M")

add_hours("2026-06-20 23:30", 2)    # '2026-06-21 01:30'
```
