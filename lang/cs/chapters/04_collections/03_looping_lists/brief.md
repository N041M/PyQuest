# 4.3 -- Procházení seznamu

## Koncept

Stejně jako řetězec je seznam posloupnost -- takže cyklus `for` prochází přímo jeho
položky, jednu na průchod:

```python
nums = [10, 20, 30]
for x in nums:
    print(x)        # 10, then 20, then 30
```

`len(nums)` dá počet položek a funguje i řez -- `nums[1:]` je vše kromě první,
`nums[:2]` jsou první dvě:

```python
print(len(nums))    # 3
print(nums[:2])     # [10, 20]
```

## Příklad

```python
xs = [1, 2, 3]
for x in xs:
    print(x * 10)   # 10, 20, 30
```

## Tvůj úkol

Přečti počet `n`, pak `n` čísel, do seznamu. Nejprve vypiš, kolik čísel je, pak
vypiš každé číslo **zdvojnásobené**, jedno na řádek.

Pro vstup `3`, pak `5`, `2`, `9`:

```
3
10
4
18
```

## Hotovo, když

- `5, 2, 9` vypíše `3`, pak `10`, `4`, `18`.
- Počet `0` vypíše jen `0` (žádná čísla ke zdvojnásobení).
