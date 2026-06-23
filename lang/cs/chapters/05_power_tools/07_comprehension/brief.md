# 5.7 -- Seznamové komprehenze

## Koncept

Velmi častý tvar cyklu je *„sestav nový seznam tím, že s každou položkou něco
uděláš“*:

```python
doubled = []
for x in nums:
    doubled.append(x * 2)
```

Python má přesně pro to jednořádkový tvar, zvaný **seznamová komprehenze**:

```python
doubled = [x * 2 for x in nums]
```

Čti to zevnitř ven: *„pro každé `x` v `nums` dej `x * 2` do nového seznamu“*.
Hranaté závorky říkají „stavím seznam“; výraz před `for` je to, čím se každá
položka stane.

Funguje s čímkoli, co můžeš procházet -- včetně `range`. Čtení `n` čísel (které jsi
teď udělal už tucetkrát) se smrskne na:

```python
nums = [int(input()) for _ in range(n)]
```

## Příklad

```python
nums = [1, 2, 3]
squares = [x * x for x in nums]
print(squares)    # [1, 4, 9]
```

## Tvůj úkol

Přečti počet `n`, pak `n` celých čísel. Sestav nový seznam, kde je každé číslo
**zdvojnásobené**, pak vypiš jeho položky, jednu na řádek.

Pro vstup `3`, pak `4`, `-1`, `0`:

```
8
-2
0
```

## Hotovo, když

- `4, -1, 0` vypíše `8, -2, 0` -- každé zdvojnásobeno, pořadí zachováno.
- Počet `0` nevypíše nic.
- K sestavení seznamu jsi použil seznamovou komprehenzi.
