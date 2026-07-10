**`datetime.strptime(text, format)`** analisa uma cadeia e produz um
**`datetime`** usando os mesmos códigos de formato que `strftime` — é o
sentido inverso. Onde `date.fromisoformat` só lê o único formato ISO,
`strptime` lê **qualquer** formato que consigas descrever.

- O `format` tem de corresponder exatamente à forma da cadeia
  (`"%Y-%m-%d %H:%M"` para `"2026-06-20 14:30"`); uma incompatibilidade gera
  `ValueError`, validando enquanto analisa.
- O resultado é um `datetime` — uma data **e** uma hora — expondo `.year`,
  `.month`, `.day`, `.hour`, `.minute`, `.second`. (`.date()` e `.time()`
  extraem apenas uma parte.)
- Lembra-te do par: **strptime** analisa (cadeia → datetime), **strftime**
  formata (datetime → cadeia).

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.hour                      # 14
datetime.strptime("05/01/1999", "%d/%m/%Y").year   # 1999
```
