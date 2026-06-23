# 5.6 -- zip(): párování seznamů

## Koncept

Dva seznamy často patří k sobě položku po položce: jména a skóre, otázky a
odpovědi. `zip()` je prochází **v zákrytu** a podává ti jednu dvojici na průchod:

```python
names = ["amy", "ben"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
# amy 90
# ben 85
```

Stejně jako `enumerate` dá každý průchod dvojici, kterou rozbalíš do dvou
proměnných. Název odkazuje na zip: dvě řady zoubků spojené jeden k jednomu.

Pokud mají seznamy různou délku, `zip` se zastaví u toho **kratšího** -- položky
navíc v delším seznamu se prostě nikdy nenavštíví.

## Příklad

```python
for a, b in zip("ab", [1, 2]):
    print(a, b)
# a 1
# b 2
```

## Tvůj úkol

Přečti počet `n`, pak `n` jmen, pak `n` skóre (celá čísla). Vypiš jeden řádek na
dvojici: jméno, mezera, skóre.

Pro vstup `2`, pak `amy`, `ben`, pak `90`, `85`:

```
amy 90
ben 85
```

## Hotovo, když

- Dvě jména a dvě skóre se vypíšou jako dva řádky `jméno skóre`, v pořadí.
- Počet `0` nevypíše nic.
- Použil jsi `zip()` ke spárování obou seznamů.
