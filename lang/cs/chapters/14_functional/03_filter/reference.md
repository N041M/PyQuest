**`filter(pred, iterable)`** ponechá položky, pro které je **predikát** `pred`
(funkce vracející pravda nebo nepravda) pravdivý, a zbytek zahodí — protějšek
„ponech, pokud“ k „transformuj každou“ od `map`.

- Vrátí **líný iterátor** v původním pořadí; obal ho do `list(...)`, abys posbíral.
- `pred` je libovolný volatelný objekt vracející pravdivou/nepravdivou hodnotu —
  `lambda`, `def` nebo vestavěná. Předání **`None`** jako predikátu
  (`filter(None, items)`) ponechá položky, které jsou samy pravdivé, a zahodí `0`,
  `""`, `None` atd.
- Komprehenze `[x for x in items if pred(x)]` je ekvivalent a často se čte lépe;
  `filter` je funkcionální tvar.

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))   # [2, 4]
list(filter(None, [0, 1, "", "a", None]))        # [1, 'a']
list(filter(str.isalpha, "a1b2"))                # ['a', 'b']
```
