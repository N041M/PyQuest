# 13.1 -- date: kalendářní den

## Koncept

Modul **`datetime`** modeluje skutečná kalendářní data a hodinové časy. Jeho typ
**`date`** drží jediný den -- rok, měsíc, den -- jako jeden objekt:

```python
from datetime import date

d = date(2026, 6, 20)
d.year      # 2026
d.isoformat()   # '2026-06-20'
```

- `date(year, month, day)` objekt sestaví a **validuje** ho: `date(2026, 13, 1)`
  vyvolá chybu, protože měsíc 13 neexistuje.
- `.isoformat()` ho vykreslí jako standardní řetězec `YYYY-MM-DD`, doplněný nulami.
- `date` je mnohem lepší než tři volná celá čísla: zná kalendář, takže se umí
  porovnat, odečíst a naformátovat.

## Příklad

```python
from datetime import date

def new_year(year):
    return date(year, 1, 1).isoformat()
```

## Tvůj úkol

Pomocí **`date`** z `datetime` definuj `iso(y, m, d)`, která datum sestaví a vrátí
jeho řetězec `YYYY-MM-DD` přes `.isoformat()`.

## Hotovo, když

- `iso(2026, 6, 20)` vrátí `"2026-06-20"`.
- `iso(1999, 1, 5)` vrátí `"1999-01-05"` (všimni si doplnění nulami).
- Řetězec pochází z `.isoformat()` objektu `date`, ne z ručního formátování.
