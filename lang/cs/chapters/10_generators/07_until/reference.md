Holé **`return`** uvnitř generátoru — nebo prostě dosažení konce funkce — ho
**zastaví**: iterace skončí a žádné další hodnoty nepřijdou. `return` v generátoru
nenese **žádnou hodnotu**; jen signalizuje „hotovo“.

- To umožní generátoru **zastavit se brzy** při splnění podmínky:
  `if x == sentinel: return` ukončí stream v tom bodě.
- Pro cyklus `for` je zastavený generátor prostě iterovatelný objekt, který došel —
  cyklus přirozeně skončí (interně generátor vyvolá `StopIteration`).

```python
def until_zero(nums):
    for n in nums:
        if n == 0:
            return          # stop the stream here
        yield n

list(until_zero([3, 1, 0, 9]))  # [3, 1]
```
