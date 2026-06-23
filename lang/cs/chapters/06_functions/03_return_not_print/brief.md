# 6.3 -- return, ne print

## Koncept

`print()` a `return` vypadají od oka při testování podobně, ale dělají úplně jinou
práci:

- `print(x)` `x` **zobrazí** na obrazovce -- a to je vše. Volající nedostane nic.
- `return x` **předá `x` zpět** volajícímu, který ho může uložit, porovnat nebo
  poslat dál.

Funkce, která místo vracení vypisuje, ve skutečnosti vrací `None` (hodnotu „žádná
hodnota“). Rozdíl uštkne ve chvíli, kdy někdo výsledek *použije*:

```python
def shout_wrong(word):
    print(word.upper() + "!")     # shows it... returns None

answer = shout_wrong("hi")        # HI! appears, but...
print(answer)                     # None  -- the caller got nothing
```

Pravidlo: **úkolem funkce je počítat a vracet.** Ať *volající* rozhodne, zda
vypsat.

## Příklad

```python
def shout(word):
    return word.upper() + "!"

print(shout("hi"))      # HI!  -- printed BY THE CALLER
loud = shout("ok")      # and it can be stored instead
```

## Tvůj úkol

Definuj `shout(word)`, která **vrátí** slovo VELKÝMI písmeny s `!` přilepeným na
konec. (`.upper()` je z 2.7.)

## Hotovo, když

- `shout("hi")` vrátí `"HI!"`; `shout("")` vrátí `"!"`.
- Hodnota se *vrací* -- verze, která jen vypisuje, selže, protože checker dostane
  `None`.
