**`strftime(format)`** („string-format-time“) vykreslí datum nebo datetime do
řetězce, který popíšeš **formátovacími kódy**. Kde `.isoformat()` dá jedno pevné
rozvržení, `strftime` dá libovolné.

- Časté kódy: `%Y` čtyřmístný rok, `%m` měsíc, `%d` den — všechny doplněné nulami;
  `%H` hodina, `%M` minuta, `%S` sekunda. Jakékoli jiné znaky (`/`, `.`, mezery) se
  kopírují doslovně.
- Jmenné kódy jako `%A` (den v týdnu) a `%B` (měsíc) **závisí na lokalizaci**, takže
  pro výstup, který musí být stabilní, dej přednost číselným kódům.
- `strptime` je inverze — *parsuje* řetězec podle formátu (13.7).

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y%m%d")       # '20260620'
d.strftime("%d.%m.%y")     # '20.06.26'  -- %y is the 2-digit year
```
