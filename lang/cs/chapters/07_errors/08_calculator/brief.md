# 7.8 -- Závěrečná: odolná kalkulačka

## Koncept

Jeden `try` může mít **několik** bloků `except` -- jeden na každý druh selhání,
každý si volí vlastní zotavení:

```python
try:
    ...
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
```

Kterákoli chyba se vyvolá, vybere svůj odpovídající blok; ostatní se přeskočí. Tato
závěrečná úloha zapojí celou kapitolu do klasického cvičení: kalkulačky, kterou
**nelze shodit** jejím vstupem. Potřebuje také `split` (4.4), indexování (2.1),
`elif` (3.4) a `/` (1.9).

## Příklad

```
input "8 + 5"   ->  13
input "9 / 2"   ->  4.5
input "9 / 0"   ->  cannot divide
input "two * 3" ->  bad number
input "8 ? 5"   ->  unknown op
```

## Tvůj úkol

Přečti jeden řádek tvaru `<číslo> <op> <číslo>` (tři části oddělené mezerami). Pro
operace `+`, `-`, `*` vypiš celočíselný výsledek; pro `/` vypiš výsledek typu float.
Ošetři každé selhání:

- část, která není celé číslo -> vypiš `bad number`
- dělení nulou -> vypiš `cannot divide`
- jakýkoli jiný symbol operace -> vypiš `unknown op`

## Hotovo, když

- `8 + 5` -> `13`, `9 / 2` -> `4.5`, `3 * -2` -> `-6`.
- `9 / 0` -> `cannot divide`; `two * 3` -> `bad number`; `8 ? 5` -> `unknown op`.
- Žádný vstup ji neshodí: každé selhání vypíše svou vlastní zprávu přes bloky
  `except` (a `else`/`elif` pro neznámou operaci).
