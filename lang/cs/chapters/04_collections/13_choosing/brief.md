# 4.13 -- Volba správné kolekce

## Koncept

Teď máš čtyři kolekce. Volba té správné dělá problém snadným:

- **list** -- uspořádané položky, duplicity povoleny (`[1, 2, 2]`). Použij pro
  posloupnosti.
- **tuple** -- jako seznam, ale pevná/neměnná. Použij pro pevné skupiny.
- **set** -- neuspořádané, **jedinečné** položky. Použij pro „odlišné“ a rychlou
  příslušnost.
- **dict** -- vyhledávání klíč -> hodnota. Použij pro „dané X, najdi jeho Y“.

Tato úloha jich pár kombinuje:

- `len(nums)` -- kolik položek (**seznam** zachová každou hodnotu, včetně
  opakování).
- `len(set(nums))` -- kolik **odlišných** hodnot (**množina** zahodí duplicity).
- **součet** -- cyklus s akumulátorem (nebo `sum(nums)`).

## Příklad

```python
nums = [1, 2, 2, 3]
print(len(nums))        # 4
print(len(set(nums)))   # 3
```

## Tvůj úkol

Přečti počet `n`, pak `n` čísel. Vypiš tři řádky:

1. kolik čísel je,
2. kolik je **odlišných** čísel,
3. jejich **součet**.

Pro vstup `4`, pak `1`, `2`, `2`, `3`:

```
4
3
8
```

## Hotovo, když

- `1, 2, 2, 3` vypíše `4`, `3`, `8`.
- Počet `0` vypíše `0`, `0`, `0`.
