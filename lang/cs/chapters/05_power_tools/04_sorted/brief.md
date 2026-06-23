# 5.4 -- sorted()

## Koncept

`sorted(nums)` vrátí **nový seznam** se stejnými položkami v pořadí, nejmenší
první:

```python
nums = [3, 1, 2]
print(sorted(nums))    # [1, 2, 3]
print(nums)            # [3, 1, 2]  -- the original is untouched
```

Dvě věci, které je dobré vědět:

- Vrací *kopii*; původní seznam si ponechá své pořadí. (Existuje i `nums.sort()`,
  metoda, která seznam přeuspořádá **na místě** -- hodí se později, ale `sorted()`
  je bezpečnější výchozí volba, protože se nic nemění za tvými zády.)
- Největší první je na jedno klíčové slovo: `sorted(nums, reverse=True)`.

Duplicity se zachovají -- řazení přeuspořádá, nikdy neodebírá.

## Příklad

```python
for x in sorted([3, 1, 2]):
    print(x)
# 1
# 2
# 3
```

## Tvůj úkol

Přečti počet `n`, pak `n` celých čísel. Vypiš je od nejmenšího po největší, jedno
na řádek.

Pro vstup `4`, pak `3`, `1`, `3`, `2`:

```
1
2
3
3
```

## Hotovo, když

- `3, 1, 3, 2` vypíše `1, 2, 3, 3` -- duplicitní `3` se objeví dvakrát.
- Počet `0` nevypíše nic.
- Použil jsi `sorted()`.
