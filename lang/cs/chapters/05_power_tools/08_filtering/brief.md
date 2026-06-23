# 5.8 -- Filtrování komprehenzemi

## Koncept

Komprehenze může také **vybírat**, které položky ponechat. Přidej `if` na konec:

```python
evens = [x for x in nums if x % 2 == 0]
```

Čti to: *„každé `x` z `nums` -- ale jen pokud `x % 2 == 0`“*. Položky, které testem
neprojdou, se prostě vynechají.

Obě části jsou nezávislé a volně se kombinují:

```python
[x * 2 for x in nums]                 # transform every item   (5.7)
[x for x in nums if x > 0]            # keep some, unchanged   (this puzzle)
[x * 2 for x in nums if x > 0]        # keep some AND transform
```

Připomenutí z 1.9: `x % 2` je zbytek po dělení 2, takže je `0` právě pro sudá čísla
-- a to zahrnuje i `0` samotnou a záporná jako `-4`.

## Příklad

```python
nums = [1, 2, 3, 4]
print([x for x in nums if x % 2 == 0])    # [2, 4]
```

## Tvůj úkol

Přečti počet `n`, pak `n` celých čísel. Ponech jen ta **sudá** (v původním pořadí)
a vypiš je, jedno na řádek.

Pro vstup `5`, pak `1`, `2`, `3`, `4`, `-6`:

```
2
4
-6
```

## Hotovo, když

- `1, 2, 3, 4, -6` vypíše `2, 4, -6` -- záporná čísla a nula se počítají jako sudá.
- Pokud žádné číslo není sudé, nic se nevypíše.
- Použil jsi komprehenzi s klauzulí `if`.
