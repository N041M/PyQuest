**`sum(numbers)`** sečte iterovatelný objekt čísel a vrátí součet — akumulátorový
cyklus z 3.12 jako jedno vestavěné volání.

- Funguje na libovolném iterovatelném objektu čísel (seznam, n-tice, range,
  generátor). `sum([])` je `0`.
- Volitelný druhý argument je **počáteční** hodnota: `sum(nums, 100)` začne součet
  na 100.
- Sčítá jen čísla; abys sečetl něco odvozeného z každé položky, předej mu
  komprehenzi nebo generátor, např. `sum(len(w) for w in words)`.

```python
sum([3, 1, 4])              # 8
sum(range(1, 101))          # 5050
sum(len(w) for w in words)  # total characters
```
