**`datetime.strptime(text, format)`** rozparsuje řetězec na **`datetime`** pomocí
stejných formátovacích kódů jako `strftime` — je to opačný směr. Kde
`date.fromisoformat` čte jen jedno ISO rozvržení, `strptime` čte **libovolné**
rozvržení, které umíš popsat.

- `format` musí přesně odpovídat tvaru řetězce (`"%Y-%m-%d %H:%M"` pro
  `"2026-06-20 14:30"`); neshoda vyvolá `ValueError`, čímž při parsování validuje.
- Výsledek je `datetime` — datum **a** čas — zpřístupňující `.year`, `.month`,
  `.day`, `.hour`, `.minute`, `.second`. (`.date()` a `.time()` vytáhnou jen jednu
  část.)
- Pamatuj si dvojici: **strptime** parsuje (řetězec → datetime), **strftime**
  formátuje (datetime → řetězec).

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.hour                      # 14
datetime.strptime("05/01/1999", "%d/%m/%Y").year   # 1999
```
