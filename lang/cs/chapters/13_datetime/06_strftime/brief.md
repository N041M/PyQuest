# 13.6 -- strftime: naformátuj datum po svém

## Koncept

`.isoformat()` vždy dá `YYYY-MM-DD`. Když potřebuješ jiné rozvržení, **`strftime`**
(„string format time“) vykreslí datum pomocí **formátovacích kódů**:

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y.%m.%d")     # '2026.06.20'
```

- `%d` je den, `%m` měsíc, `%Y` čtyřmístný rok -- každý doplněný nulami. Vše ostatní
  ve formátovacím řetězci (ta `/`, `.`, mezery) se zkopíruje doslovně.
- Existují i další kódy (`%H` hodina, `%M` minuta a jmenné kódy jako `%A`), ale ty
  číselné jsou základ.

Takže jeden objekt data se umí prezentovat, jakkoli zpráva nebo uživatel očekává.

## Příklad

```python
from datetime import date

def dotted(text):
    return date.fromisoformat(text).strftime("%Y.%m.%d")
```

## Tvůj úkol

Definuj `pretty(text)`, která bere řetězec `YYYY-MM-DD` a vrátí ho ve tvaru
**`DD/MM/YYYY`**, pomocí `strftime("%d/%m/%Y")` na rozparsovaném datu.

## Hotovo, když

- `pretty("2026-06-20")` vrátí `"20/06/2026"`.
- `pretty("1999-01-05")` vrátí `"05/01/1999"` (doplněné nulami).
- Formátování dělá `strftime`, ne přeskupování rozdělených kousků.
