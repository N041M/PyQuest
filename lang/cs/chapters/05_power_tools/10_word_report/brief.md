# 5.10 -- Závěrečná: zpráva o slovech

## Koncept

Tentokrát nic nového -- tato úloha spojuje celou kapitolu (a kapitolu 4) do jednoho
malého, skutečného programu: **zprávy o četnosti slov**, srdce každé funkce
„nejčastější slova“, jakou jsi kdy viděl.

Díly, které všechny máš:

- `.split()` -- řádek na slova (4.4)
- sčítací vzor -- spočítej každé slovo (5.9)
- `sorted()` -- seřaď zprávu (5.4). Jedno nové pohodlí: procházení slovníku
  navštěvuje jeho **klíče**, takže `sorted(counts)` jsou prostě klíče v abecedním
  pořadí.
- vypsání slova a jeho počtu na jeden řádek (1.2)

## Příklad

Pro řádek `b a b`:

```python
counts = {"b": 2, "a": 1}
for w in sorted(counts):
    print(w, counts[w])
# a 1
# b 2
```

## Tvůj úkol

Přečti jeden řádek slov. Vypiš jeden řádek na každé **odlišné** slovo -- slovo,
mezeru a kolikrát se objevilo -- v **abecedním** pořadí.

Pro vstup `tea milk tea`:

```
milk 1
tea 2
```

## Hotovo, když

- `tea milk tea` vypíše `milk 1` pak `tea 2` -- odlišná slova, abecedně.
- Jediné opakované slovo vypíše jeden řádek s jeho úplným počtem.
- Prázdný řádek nevypíše nic.
- Použil jsi sčítací slovník a `sorted()`.
