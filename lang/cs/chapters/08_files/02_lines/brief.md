# 8.2 -- Soubor řádek po řádku

## Koncept

`f.read()` ti dá vše najednou. Častěji chceš soubor **po jednom řádku** -- a objekt
souboru je *iterovatelný*, takže cyklus `for` jeho řádky projde za tebe:

```python
with open("tasks.txt") as f:
    for line in f:
        ...
```

Jeden háček: každý `line` stále nese zalomení řádku, které ho ukončilo -- `"wash\n"`,
ne `"wash"`. Ořízni ho pomocí `line.strip()` (3.7), než text použiješ, jinak ti
výstup naroste o prázdné řádky.

## Příklad

Pro `tasks.txt` ve tvaru:

```
wash
cook
sleep
```

dá očíslování každého řádku:

```
1. wash
2. cook
3. sleep
```

`enumerate` (5.5) se přirozeně hodí -- začni od `1`:

```python
for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")
```

## Tvůj úkol

Přečti `tasks.txt` a vypiš každý řádek **číslovaný od 1**, ve tvaru `1. wash`. Zahoď
koncové zalomení řádku, aby nevznikly zbloudilé prázdné řádky.

## Hotovo, když

- Každý řádek se vypíše jako `<číslo>. <text>`, počínaje od 1.
- Funguje to pro soubor libovolné délky.
- Soubor jsi otevřel pomocí `with` a procházel ho pomocí `for`.
