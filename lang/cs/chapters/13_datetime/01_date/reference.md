Modul **`datetime`** poskytuje typy pro kalendářní data a hodinové časy. Jeho typ
**`date`** drží jeden den jako jeden objekt: `date(year, month, day)`.

- Konstruktor hodnoty **validuje** proti skutečnému kalendáři — `date(2026, 2, 30)`
  vyvolá `ValueError`, takže nemožné datum neproklouzne.
- Atributy `.year`, `.month`, `.day` přečtou části zpět; **`.isoformat()`** vykreslí
  standardní řetězec `YYYY-MM-DD`, vždy doplněný nulami.
- `date` zná kalendář, takže se umí porovnat (`<`, `==`), odečíst (13.5) a nahlásit
  svůj den v týdnu (13.3) — věci, které tři volná celá čísla nebo ručně sestavený
  řetězec neumějí. `date.today()` vrátí aktuální den.

```python
from datetime import date

d = date(2026, 6, 20)
d.month          # 6
d.isoformat()    # '2026-06-20'
date(2026, 1, 5).isoformat()   # '2026-01-05'  -- padded
```
