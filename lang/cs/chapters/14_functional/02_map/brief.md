# 14.2 -- map: aplikuj na každou položku

## Koncept

**`map(func, iterable)`** spustí `func` na **každé** položce a vydá výsledky. Je to
vzor „aplikuj na každou“ jako funkce vyššího řádu -- funkce, která bere jinou funkci:

```python
list(map(str.upper, ["a", "b"]))     # ['A', 'B']
list(map(lambda x: x * x, [1, 2, 3])) # [1, 4, 9]
```

- `map` vrátí **líný iterátor**, takže ho obal do `list(...)`, abys dostal seznam.
- Funkce může být `lambda`, `def` nebo vestavěná jako `str.upper` nebo `int`.

(Seznamová komprehenze `[f(x) for x in items]` dělá totéž a často se čte
přirozeněji; tato úloha je o naučení se samotného `map`, nástroje, který potkáš v
hromadě kódu.)

## Příklad

```python
def lengths(words):
    return list(map(len, words))
```

## Tvůj úkol

Pomocí **`map`** definuj `squares(nums)`, která vrátí seznam každého čísla v `nums`
umocněného.

## Hotovo, když

- `squares([1, 2, 3])` vrátí `[1, 4, 9]`.
- `squares([])` vrátí `[]`.
- Mapování dělá `map`, ne komprehenze nebo ruční cyklus.
