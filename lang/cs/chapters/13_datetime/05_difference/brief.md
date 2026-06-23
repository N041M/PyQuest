# 13.5 -- Odčítání dat: počet dní mezi

## Koncept

Přičtení doby k datu dá datum. Funguje i opak: **odečti jedno datum od druhého** a
dostaneš **`timedelta`** -- úsek mezi nimi:

```python
from datetime import date

gap = date(2026, 7, 1) - date(2026, 6, 20)
gap            # timedelta(days=11)
gap.days       # 11
```

- `date_b - date_a` je `timedelta`; jeho **`.days`** je celý počet dní mezi nimi.
- Pokud je `date_b` **dříve** než `date_a`, `.days` je **záporné**.
- Je to přesné napříč měsíci, roky a přestupnými dny -- počítá knihovna, ty ne.

## Příklad

```python
from datetime import date

def days_old(born, today):
    return (date.fromisoformat(today) - date.fromisoformat(born)).days
```

## Tvůj úkol

Definuj `days_between(a, b)`, která bere dva řetězce `YYYY-MM-DD` a vrátí počet dní
**od `a` do `b`** (takže pozdější `b` dá kladné číslo), pomocí odčítání dat.

## Hotovo, když

- `days_between("2026-06-20", "2026-07-01")` vrátí `11`.
- `days_between("2026-07-01", "2026-06-20")` vrátí `-11`.
- `days_between("2026-06-20", "2026-06-20")` vrátí `0`.
- Počet pochází z odečtení dvou objektů `date`, ne z ruční aritmetiky.
