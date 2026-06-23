# 13.4 -- timedelta: aritmetika dat

## Koncept

**`timedelta`** je **doba trvání** -- časový úsek. Přičti jednu k datu a dostaneš
jiné datum, se všemi kalendářními zmatky (délky měsíců, přechod roku, přestupné dny)
vyřešenými za tebe:

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)     # date(2026, 7, 30)
date(2026, 12, 25) + timedelta(days=10)    # date(2027, 1, 4)  -- crosses the year
```

- `timedelta(days=n)` je doba `n` dní (bere také `weeks=`, `hours=` atd.). `n` může
  být **záporné**, abys šel dozadu.
- `date + timedelta` dá nové `date`; `date - timedelta` jde opačně.
- Proto nikdy neděláš aritmetiku dat ručně: knihovna ví, že únor má v přestupném roce
  29 dní, a ty nemusíš.

## Příklad

```python
from datetime import date, timedelta

def tomorrow(text):
    return (date.fromisoformat(text) + timedelta(days=1)).isoformat()
```

## Tvůj úkol

Definuj `add_days(text, n)`, která bere řetězec `YYYY-MM-DD` a celé číslo `n` a vrátí
řetězec `YYYY-MM-DD` pro datum o `n` dní později (pomocí `timedelta`). `n` může být
záporné.

## Hotovo, když

- `add_days("2026-06-20", 40)` vrátí `"2026-07-30"`.
- `add_days("2026-01-01", -1)` vrátí `"2025-12-31"`.
- Posun používá `timedelta` na skutečném `date`, ne ručně psané počítání dní.
