# 1.10 -- Dotaz na uživatele

## Koncept

`input()` pozastaví program, nechá člověka napsat řádek a **vrátí to, co napsal,
jako text** (řetězec). Obvykle to uložíš do proměnné:

```python
name = input()
print("Hi, " + name)
```

Když člověk napíše `Sam`, program vypíše `Hi, Sam`.

`input()` vždy vrátí **řetězec**, i když člověk napíše číslice. (To budeš řešit v
další úloze.)

Napsaný text můžeš spojit s jiným textem pomocí `+`, přesně jako v úloze 1.7:

```python
city = input()
print("You live in " + city)
```

> Poznámka: když spustíš `check`, kontrola za tebe vstup dodá automaticky -- nic
> nepíšeš ručně.

## Příklad

Zadaný vstup: `Berlin`

```python
city = input()
print("Welcome to " + city)
```

Výstup:

```
Welcome to Berlin
```

## Tvůj úkol

Přečti jeden řádek vstupu (jméno) a pozdrav ho. Pokud je vstup `World`, výstup musí
být přesně:

```
Hello, World
```

Tedy: přečti jméno pomocí `input()` a pak vypiš `Hello, ` spojené se jménem. Dej
pozor na čárku a jednu mezeru za ní.

## Hotovo, když

- Pro vstup `World` je výstup `Hello, World`.
- Pro libovolné jiné jméno pozdraví stejným způsobem (kontrola jich zkouší více).
