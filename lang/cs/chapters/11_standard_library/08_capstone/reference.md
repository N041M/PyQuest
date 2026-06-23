Závěrečná úloha je skutečným smyslem kapitoly: **skládání modulů standardní
knihovny** do malého potrubí, místo psaní každého kroku od nuly.

- **Čti** pomocí `json` — `json.loads(text)` promění JSON vstup na pythonovské
  hodnoty (zde seznam čísel).
- **Shrň** pomocí `statistics` a vestavěných funkcí — `statistics.mean(nums)` na
  průměr, `max(nums)` / `min(nums)` na extrémy, `len(nums)` na počet.
- **Vrať** prostý `dict`, takže volající dostane obyčejné pythonovské hodnoty k
  použití.

Každá fáze je modul, který někdo jiný napsal a otestoval; tvým úkolem je propojit
je. To je to, čím většina skutečných programů je — lepidlo mezi dobře udělanými
knihovnami.

```python
import json
import statistics

def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {"count": len(nums), "mean": statistics.mean(nums),
            "max": max(nums), "min": min(nums)}

summary("[2, 4, 6]")   # {'count': 3, 'mean': 4, 'max': 6, 'min': 2}
```
