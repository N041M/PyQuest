# 13.3 -- weekday: který den v týdnu

## Koncept

Daný datum, jaký je to den v týdnu? Spočítat to ručně znamená znát přestupné roky a
délku každého měsíce. Objekt `date` to už umí -- zeptej se ho:

```python
from datetime import date

date(2026, 6, 20).weekday()     # 5  (Saturday)
```

- **`.weekday()`** vrátí celé číslo: **pondělí je 0**, úterý 1, ... neděle 6.
- (`.isoweekday()` je tatáž myšlenka, ale pondělí=1 .. neděle=7.)

To je ten druh věci, který necháš dělat knihovnu: kóduje skutečný kalendář, takže
odpověď je správná pro libovolné datum, včetně přestupných roků.

## Příklad

```python
from datetime import date

def is_weekend(text):
    return date.fromisoformat(text).weekday() >= 5
```

## Tvůj úkol

Definuj `weekday(text)`, která bere řetězec `YYYY-MM-DD` a vrátí jeho den v týdnu
jako celé číslo, **pondělí=0 .. neděle=6**, pomocí `.weekday()` objektu data.

## Hotovo, když

- `weekday("2026-06-20")` vrátí `5` (sobota).
- `weekday("2000-01-01")` vrátí `5`.
- Odpověď pochází z `.weekday()` na rozparsovaném `date`.
