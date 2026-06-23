Závěrečná úloha skládá generátory do **proudového potrubí**: **zdrojový** generátor
napájí **filtrovací** generátor, který napájí **transformační** generátor. Každá
fáze je líná, takže hodnoty tečou po jedné a nic se nezhmotní celé.

- Protože každá fáze líně konzumuje předchozí, potrubí zpracovává obrovská nebo
  nekonečná data s nepatrnou pamětí — v každém okamžiku je v letu jedna položka.
- Fáze zůstávají malé a nezávislé: vyměň nebo přidej fázi, aniž by ses dotkl
  ostatních. To je generátorová obdoba skládání funkcí.

```python
def reader(nums):  yield from nums
def keep_pos(src): yield from (n for n in src if n > 0)
def doubled(src):  yield from (n * 2 for n in src)

list(doubled(keep_pos(reader([-1, 2, -3, 4]))))   # [4, 8]
```
