**`functools.reduce(func, iterable[, start])`** **složí** (fold) posloupnost do
jediné hodnoty tím, že kumulativně aplikuje dvouargumentovou `func`, zleva doprava:
`func(func(func(i0, i1), i2), i3)...`. Každý krok zkombinuje průběžný výsledek s
další položkou.

- **Počáteční** hodnota (`reduce(func, items, start)`) skládání nasadí a definuje
  výsledek pro **prázdnou** posloupnost; bez ní redukce prázdného iterovatelného
  objektu vyvolá `TypeError`.
- Zobecňuje akumulátorový cyklus na *libovolný* kombinátor: `+` dá součet, `*`
  součin, `max` největší. Vyhrazený `sum` je speciální případ `+` a `math.prod` ten
  pro `*` — ale `reduce` skládá s jakoukoli funkcí, kterou dodáš.
- `reduce` žije v `functools` (není vestavěný), takže se musí naimportovat.

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])      # 10
reduce(lambda a, b: a * b, [1, 2, 3, 4], 1)   # 24
reduce(lambda a, b: a if a > b else b, [3, 9, 2])   # 9  (max)
```
