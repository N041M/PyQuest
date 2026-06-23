# 14.7 -- reduce: slož posloupnost do jedné hodnoty

## Koncept

**`reduce`** (z `functools`) **složí** (fold) celou posloupnost do jediné hodnoty
tím, že kumulativně aplikuje dvouargumentovou funkci, zleva doprava:

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])     # 10  ((((1+2)+3)+4))
reduce(lambda a, b: a * b, [1, 2, 3, 4])     # 24
```

- `reduce(func, items)` spočítá `func(func(func(i0, i1), i2), i3)...` -- každý krok
  zkombinuje průběžný výsledek s další položkou.
- Třetí argument je **počáteční** hodnota: `reduce(func, items, start)` začne skládat
  od `start`, což také definuje odpověď pro **prázdnou** posloupnost.
- Je to akumulátorový cyklus (kapitola 3) jako funkce vyššího řádu. (`sum` je
  speciální případ pro `+`; `reduce` ti umožní skládat s *libovolným* kombinátorem.)

## Příklad

```python
from functools import reduce

def total(nums):
    return reduce(lambda a, b: a + b, nums, 0)
```

## Tvůj úkol

Pomocí **`reduce`** z `functools` definuj `product(nums)`, která vrátí součin všech
čísel (s počátkem `1`, takže prázdný seznam dá `1`).

## Hotovo, když

- `product([1, 2, 3, 4])` vrátí `24`; `product([5])` vrátí `5`.
- `product([])` vrátí `1`.
- Skládání používá `reduce`, ne ruční akumulátorový cyklus.
