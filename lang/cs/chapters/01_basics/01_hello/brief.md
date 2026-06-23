# 1.1 -- Hello, output

## Koncept

**Program** je seznam instrukcí, které počítač provádí shora dolů. Nejzákladnější
instrukcí je **vypsat** (print) -- zobrazit řádek textu na obrazovce. V Pythonu to
uděláš pomocí `print(...)`. Vypíše se cokoli, co vložíš dovnitř závorek do
uvozovek.

`print` je **funkce**: vestavěná akce, kterou spustíš tím, že napíšeš její jméno
následované závorkami. To, co je v uvozovkách, je **text** (Python textu říká
*řetězec* -- řetězec znaků).

## Příklad

```python
print("Good morning")
```

Když se to spustí, na obrazovce se objeví:

```
Good morning
```

Uvozovky vyznačují, kde text začíná a končí; samy se nevypisují. Python navíc na
konci automaticky přidá zalomení řádku, takže další print začne na novém řádku.

## Tvůj úkol

Zařiď, aby program vypsal přesně tento řádek:

```
Hello, output
```

Otevři pracovní soubor kapitoly `work.py`, napiš jeden `print(...)`, který vytvoří
tento řádek, **ulož soubor** a pak spusť `check`.

## Hotovo, když

- Spuštění `check` ukáže CHECK PASSED.
- Výstup zní `Hello, output` -- stejná slova, stejná čárka. (Kontrola ignoruje
  velikost písmen, ale přesné dodržení zadání je dobrý zvyk.)
