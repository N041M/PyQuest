**`map(func, iterable)`** aplikuje `func` na každou položku a vydá výsledky — vzor
„transformuj každou položku“ jako funkce vyššího řádu (taková, která bere jinou
funkci jako argument).

- Vrátí **líný iterátor**, který počítá každý výsledek na vyžádání; obal ho do
  `list(...)` (nebo `tuple`, nebo napájej `for`), abys ho zkonzumoval.
- `func` může být `lambda`, pojmenovaný `def` nebo libovolný volatelný objekt —
  vestavěná jako `len`, `str.upper` nebo `int` je běžná.
- S několika iterovatelnými objekty `map(func, a, b)` volá `func(a_i, b_i)` v
  zákrytu a zastaví se u nejkratšího.
- Seznamová komprehenze `[func(x) for x in items]` vyjadřuje totéž a je často
  jasnější; `map` je funkcionálně stylový ekvivalent, který uvidíš všude.

```python
list(map(len, ["hi", "there"]))        # [2, 5]
list(map(lambda x: x * x, [1, 2, 3]))  # [1, 4, 9]
list(map(int, ["1", "2", "3"]))        # [1, 2, 3]
```
