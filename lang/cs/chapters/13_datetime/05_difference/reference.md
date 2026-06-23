Odečtení jednoho `date` od druhého dá **`timedelta`** — úsek mezi nimi — a jeho
atribut **`.days`** je celý počet dní, spočítaný přesně napříč měsíci, roky a
přestupnými dny.

- `date_b - date_a` měří od `a` do `b`: je-li `b` **dříve**, `.days` je **záporné**,
  takže znaménko ti řekne směr.
- Výsledek je doba trvání, takže se skládá: přičti ji zpět k datu, vynásob ji,
  porovnej dva úseky.
- To je počítací protějšek přičítání `timedelta` (13.4) — dohromady dělají z dat
  malou algebru: `datum + doba = datum`, `datum - datum = doba`.

```python
from datetime import date

(date(2026, 7, 1) - date(2026, 6, 20)).days     # 11
(date(2026, 6, 20) - date(2026, 7, 1)).days     # -11
(date(2026, 3, 1) - date(2024, 3, 1)).days      # 730  -- 2024 was a leap year
```
