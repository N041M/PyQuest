Funkce **skládají vestavěné funkce** do pojmenované, znovupoužitelné operace.
Funkce `average` je modelem: obalí `sum` a `len` za jedno jasné jméno.

- `return sum(nums) / len(nums)` spočítá průměr — ale `len(nums)` je pro prázdný
  seznam `0`, což vyvolá `ZeroDivisionError`, takže to ošetři časným returnem.
- Pojmenování operace (`average(scores)`) dělá volající kód čitelným jako záměr a
  oprava nebo vylepšení logiky se děje na jednom místě.

```python
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

average([2, 4, 9])    # 5.0
```
