# 13.2 -- fromisoformat: text na datum

## Koncept

Data obvykle dorazí jako **text** -- ze souboru, z formuláře, z API.
**`date.fromisoformat`** rozparsuje standardní řetězec `YYYY-MM-DD` na skutečný
objekt `date`, inverze k `.isoformat()`:

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
d.year      # 2026
d.month     # 6
d.day       # 20
```

- Vrátí `date`, takže pak můžeš číst `.year` / `.month` / `.day`, porovnat ho nebo s
  ním počítat -- vše, co datum umí.
- Očekává přesný tvar `YYYY-MM-DD`; chybně utvořený řetězec vyvolá `ValueError`.

Parsování na skutečné datum (místo abys řetězec sám řezal) znamená, že hodnota je
zvalidovaná a připravená pro kalendářní práci.

## Příklad

```python
from datetime import date

def month_of(text):
    return date.fromisoformat(text).month
```

## Tvůj úkol

Pomocí **`date.fromisoformat`** definuj `parts(text)`, která rozparsuje řetězec
`YYYY-MM-DD` a vrátí n-tici celých čísel `(year, month, day)` přečtenou z atributů
objektu data.

## Hotovo, když

- `parts("2026-06-20")` vrátí `(2026, 6, 20)`.
- `parts("1999-01-05")` vrátí `(1999, 1, 5)`.
- Hodnoty pocházejí z atributů rozparsovaného `date`, ne z `text.split("-")`.
