**`timedelta`** představuje **dobu trvání** — časový úsek, ne bod v něm. Přičtení
jedné k `date` vyprodukuje jiné `date`, se vším kalendářním účetnictvím (délky
měsíců, hranice roku, přestupné dny) zpracovaným automaticky.

- `timedelta(days=n)` je `n` dní; přijímá také `weeks=`, `hours=`, `minutes=`,
  `seconds=`. `n` může být **záporné**, aby se posunulo dozadu.
- `date + timedelta` a `date - timedelta` dají nové datum; odečtení dvou *dat* dá
  `timedelta` (13.5).
- Proto aritmetika dat jde přes knihovnu: `date(2026, 12, 25) + timedelta(days=10)`
  správně přejde do dalšího roku a délka února nikdy není tvůj problém.

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)    # date(2026, 7, 30)
date(2026, 1, 1) - timedelta(days=1)      # date(2025, 12, 31)
date(2026, 6, 20) + timedelta(weeks=2)    # date(2026, 7, 4)
```
