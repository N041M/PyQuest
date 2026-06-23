# 13.7 -- strptime: parsuj podle formátu

## Koncept

`date.fromisoformat` čte jen jedno ISO rozvržení. Pro **libovolné** rozvržení --
datum s časem, vlastní pořadí -- použij **`datetime.strptime`** („parse time“). Dáš
mu řetězec **a** formát, který ho popisuje, se stejnými kódy jako `strftime`:

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.year     # 2026
dt.hour     # 14
dt.minute   # 30
```

- Formát musí odpovídat tvaru řetězce; neshoda vyvolá `ValueError`, takže při
  parsování validuje.
- Výsledek je **`datetime`** -- datum *a* čas -- s atributy `.year`, `.month`,
  `.day`, `.hour`, `.minute`, `.second`.

`strptime` parsuje, `strftime` formátuje: stejné kódy, opačné směry.

## Příklad

```python
from datetime import datetime

def year_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").year
```

## Tvůj úkol

Definuj `hour_of(text)`, která bere časové razítko jako `"2026-06-20 14:30"` a vrátí
**hodinu** jako celé číslo, tím, že ho rozparsuje pomocí `datetime.strptime` a
formátu `"%Y-%m-%d %H:%M"`.

## Hotovo, když

- `hour_of("2026-06-20 14:30")` vrátí `14`.
- `hour_of("1999-01-05 09:05")` vrátí `9`.
- Hodina pochází z rozparsovaného `datetime`, ne z řezání řetězce.
