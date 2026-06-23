Umístění **`yield` za `if`** filtruje stream, jak teče: generátor vydá jen
položky, které projdou testem, a zbytek tiše přeskočí — líný protějšek klauzule
`if` v komprehenzi.

- `for x in source: if test(x): yield x` vyprodukuje filtrovaný stream, aniž by
  stavěl jakýkoli mezilehlý seznam.
- Protože je líný, čistě se skládá: filtrovací generátor může napájet další
  generátor, každý zpracovává jednu fázi.

```python
def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n         # only the evens make it out

list(evens(range(10)))      # [0, 2, 4, 6, 8]
```
