# 11.8 -- Závěrečná: statistický souhrn z JSON

## Koncept

Skutečnou lekcí této kapitoly je, že každodenní práce je **skládání knihovních
nástrojů**: nech jeden modul přečíst data, druhý je zpracovat a vrátit výsledek. Tady
zkombinuješ dva z modulů, které jsi právě potkal.

Vstup je **JSON řetězec** držící seznam čísel, např. `"[4, 8, 15, 16]"`. Ty:

1. ho rozparsuješ pomocí **`json.loads`** na pythonovský seznam,
2. ho shrneš pomocí **`statistics`** a vestavěných `max` / `min`,
3. vrátíš prostý slovník výsledků.

```python
import json
import statistics

data = json.loads("[4, 8, 15, 16]")     # [4, 8, 15, 16]
statistics.mean(data)                    # 10.75
```

## Tvůj úkol

Definuj `summary(numbers_json)`, která bere JSON řetězec seznamu čísel a vrátí
slovník s těmito klíči:

- `"count"` -- kolik čísel (`len`),
- `"mean"` -- jejich průměr (`statistics.mean`),
- `"max"` -- největší (`max`),
- `"min"` -- nejmenší (`min`).

Vstup rozparsuj pomocí `json.loads`. Předpokládej alespoň jedno číslo.

## Hotovo, když

- `summary("[2, 4, 6]")` se rovná
  `{"count": 3, "mean": 4, "max": 6, "min": 2}`.
- `summary("[5]")` se rovná `{"count": 1, "mean": 5, "max": 5, "min": 5}`.
- Vstup je rozparsován pomocí `json.loads`, ne ručně.
