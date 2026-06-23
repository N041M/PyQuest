# 3.9 -- for a range

## Koncept

**Cyklus `for`** spustí svůj blok jednou pro každou položku v posloupnosti. Ve
spojení s **`range`** je to obvyklý způsob, jak něco zopakovat určitý počet krát.

`range(n)` vytvoří čísla `0, 1, 2, ..., n-1` (zastaví se *před* `n`):

```python
for i in range(4):
    print(i)
# prints 0, 1, 2, 3
```

Při každém průchodu vezme řídicí proměnná (zde `i`) další hodnotu. Počítadlo si
nespravuješ sám -- `range` to dělá za tebe, takže nehrozí nekonečný cyklus.

`range` může mít také start a krok: `range(1, 5)` je `1,2,3,4`; `range(0, 10, 2)`
je `0,2,4,6,8`.

## Příklad

```python
for i in range(3):
    print(i)
# prints 0, 1, 2
```

## Tvůj úkol

Přečti celé číslo `n` a pak vypiš každé číslo od `0` do `n-1`, každé na vlastním
řádku, pomocí cyklu `for` s `range`.

Pro vstup `4` je výstup:

```
0
1
2
3
```

## Hotovo, když

- `4` vypíše `0,1,2,3` (každé na řádku). `1` vypíše jen `0`.
- `0` nevypíše nic.
