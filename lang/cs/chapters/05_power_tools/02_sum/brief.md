# 5.2 -- sum()

## Koncept

V 3.12 jsi napsal **vzor akumulátoru** ručně:

```python
total = 0
for x in nums:
    total = total + x
```

Tento vzor je tak častý, že ho Python dodává jako vestavěnou funkci:

```python
total = sum(nums)
```

`sum(seznam_čísel)` sečte každou položku a vrátí součet. U prázdného seznamu vrátí
`0` -- přesně to, čím tvůj ručně psaný akumulátor začínal.

Tato kapitola je plná takových **mocných nástrojů**: vestavěných funkcí, které
nahrazují cyklus, jejž sis už jednou sám napsal. Zkratku si zasloužíš tím, že víš,
co nahrazuje.

## Příklad

```python
nums = [3, 1, 4]
print(sum(nums))    # 8
print(sum([]))      # 0
```

## Tvůj úkol

Přečti počet `n`, pak `n` celých čísel (jedno na řádek). Vypiš jejich součet pomocí
`sum()`.

Pro vstup `3`, pak `3`, `1`, `4`:

```
8
```

## Hotovo, když

- `3, 1, 4` vypíše `8`; záporná čísla také fungují.
- Počet `0` vypíše `0`.
- Použil jsi `sum()` -- tentokrát ne ručně psaný cyklus.
