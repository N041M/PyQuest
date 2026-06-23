# 13.8 -- Závěrečná: posuň časové razítko

## Koncept

Tohle stáhne kapitolu do jednoho okruhu tam a zpět: **rozparsuj** časové razítko,
**posuň** ho o dobu, **naformátuj** výsledek zpět -- každý krok nástroj, který jsi
potkal.

```python
from datetime import datetime, timedelta

dt = datetime.strptime("2026-06-20 23:30", "%Y-%m-%d %H:%M")  # parse
dt = dt + timedelta(hours=2)                                  # shift
dt.strftime("%Y-%m-%d %H:%M")                                 # '2026-06-21 01:30'
```

Všimni si, že posun přešel přes půlnoc do dalšího dne -- knihovna to automaticky
sleduje, napříč dny, měsíci a roky. Udělat to ručně by znamenalo znovu implementovat
kalendář a hodiny.

## Tvůj úkol

Definuj `add_hours(timestamp, hours)`, která bere řetězec `"YYYY-MM-DD HH:MM"` a celé
číslo `hours` (které může být záporné) a vrátí časové razítko posunuté o tolik hodin,
ve **stejném formátu `"YYYY-MM-DD HH:MM"`**.

Použij `datetime.strptime` k parsování, `timedelta(hours=...)` k posunu a `strftime`
k formátování.

## Hotovo, když

- `add_hours("2026-06-20 23:30", 2)` vrátí `"2026-06-21 01:30"`.
- `add_hours("2026-01-01 00:30", -1)` vrátí `"2025-12-31 23:30"`.
- Posun používá `timedelta` na rozparsovaném `datetime`, naformátovaný pomocí
  `strftime` -- ne ruční aritmetiku na řetězci.
