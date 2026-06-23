# 11.3 -- import as: přejmenuj při vstupu

## Koncept

Někdy je jméno modulu dlouhé, nebo se sráží s jedním z tvých. **`import ... as
...`** přinese modul pod jménem, které si **ty** zvolíš:

```python
import statistics as stats

stats.mean([1, 2, 3, 4])    # 2.5
```

- `import statistics as stats` naváže modul na `stats`; `stats.mean` je přesně
  `statistics.mean`.
- Alias je jen lokální přezdívka -- modul je beze změny a nové jméno vidí jen tvůj
  soubor.
- Proto všude uvidíš zaběhlé aliasy (`import numpy as np`); tady zkracujeme
  `statistics`.

Modul **`statistics`** za tebe dělá běžné průměry. `stats.mean(nums)` je
aritmetický průměr -- součet dělený počtem -- aniž bys psal `sum(nums) / len(nums)`.

## Příklad

```python
import statistics as stats

def midpoint(nums):
    return stats.median(nums)
```

## Tvůj úkol

Pomocí **`import statistics as stats`** definuj `average(nums)`, která vrátí průměr
seznamu `nums`, spočítaný pomocí `stats.mean`.

## Hotovo, když

- `average([2, 4, 6])` vrátí `4`, `average([1, 2])` vrátí `1.5`.
- `average([5])` vrátí `5`.
- Průměr pochází z `statistics.mean`, naimportované jako `stats`.
