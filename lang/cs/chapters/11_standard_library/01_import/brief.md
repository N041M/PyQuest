# 11.1 -- import: přines modul

## Koncept

Python dodává rozsáhlou **standardní knihovnu**: hotové nástroje seskupené do
**modulů**. Nedostaneš je zadarmo v každém souboru -- modul, který potřebuješ,
**naimportuješ**, pak sáhneš na jeho obsah skrz jeho jméno.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
```

- `import math` proběhne jednou nahoře v souboru a naváže jméno `math` na celý
  modul.
- Poté `math.sqrt` je funkce odmocniny a `math.pi` konstanta -- `modul.jméno` sáhne
  na cokoli, co modul poskytuje.

Smysl importování je, že tohle už někdo napsal a otestoval, takže zavoláš
`math.sqrt` místo toho, abys znovu odvozoval odmocninu sám.

## Příklad

```python
import math

def diagonal(side):
    return math.sqrt(2) * side
```

## Tvůj úkol

Definuj `hypotenuse(a, b)`, která vrátí délku přepony pravoúhlého trojúhelníku s
odvěsnami `a` a `b` -- odmocninu z `a*a + b*b` -- pomocí **`math.sqrt`** z
naimportovaného modulu `math`.

## Hotovo, když

- `hypotenuse(3, 4)` vrátí `5.0`, `hypotenuse(5, 12)` vrátí `13.0`.
- `hypotenuse(0, 0)` vrátí `0.0`.
- Odmocnina pochází z `math.sqrt`, přes `import math`.
