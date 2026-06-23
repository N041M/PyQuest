# 7.3 -- ZeroDivisionError: žádej o odpuštění

## Koncept

Dělení nulou vyvolá `ZeroDivisionError`. Existují dva způsoby, jak napsat dělení,
které to přežije:

```python
# "look before you leap": test first
if b == 0:
    return None
return a / b

# "easier to ask forgiveness": just try it
try:
    return a / b
except ZeroDivisionError:
    return None
```

Oba se *tady* chovají stejně -- ale pythonovský styl silně preferuje ten druhý a
tato úloha ho vyžaduje. Proč:

- `try` pojmenuje skutečnou událost („dělení selhalo“) místo předpokladu, který s
  ní musíš držet v souladu.
- Předběžné kontroly se neškálují: skutečné operace mohou selhat tuctem způsobů
  (chybějící soubor, odepřené oprávnění, přerušené spojení...). Nemůžeš je všechny
  předem otestovat -- ale jediný `except` může zachytit samotné selhání.

Tomuto stylu se říká **EAFP**: *snazší žádat o odpuštění než o povolení* (easier to
ask forgiveness than permission).

## Příklad

```python
safe_div(10, 4)    # 2.5
safe_div(5, 0)     # None  -- handled, no crash
```

## Tvůj úkol

Definuj `safe_div(a, b)`, která vrátí `a / b`, nebo `None`, když je `b` nula --
pomocí `try`/`except`, ne `if`.

## Hotovo, když

- `safe_div(10, 4)` je `2.5`; `safe_div(5, 0)` je `None`.
- `safe_div(0, 5)` je `0.0` -- nula NAHOŘE je v pořádku.
- Zachytil jsi `ZeroDivisionError` -- if-test se lekci vyhne a selže.
