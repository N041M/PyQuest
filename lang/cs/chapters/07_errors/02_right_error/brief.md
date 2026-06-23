# 7.2 -- Zachyť SPRÁVNOU chybu

## Koncept

`except` může pojmenovat, kterou chybu ošetří -- a měl by. Chyby, které jsi
nečekal, jsou **informace**, a jejich spolknutí skrývá bugy.

```python
try:
    n = int(text)
except ValueError:        # exactly the error int() raises for bad TEXT
    n = None
```

Lákavá zkratka je holé `except:` (nebo `except Exception:`) -- „chyť všechno,
nemůže to spadnout!“ Ale *všechno* zahrnuje chyby, které znamenají, že **tvůj kód
je špatně používán**. `int([1, 2])` nevyvolá `ValueError` -- vyvolá `TypeError`
(„úplně špatný druh věci“), a ten by *měl* spadnout nahlas, aby se bug volajícího
našel, ne zalepil.

Pravidlo: **chytej přesně to, co čekáš; vše ostatní nech uniknout.**

## Příklad

```python
safe_int("42")      # 42
safe_int("nope")    # None         (ValueError, handled)
safe_int([1, 2])    # TypeError!   (NOT handled -- a misuse, let it crash)
```

## Tvůj úkol

Definuj `safe_int(text)`, která vrátí `int(text)`, nebo `None`, když text není
platné číslo. Chytej **jen** `ValueError` -- `TypeError` z neřetězce musí
uniknout.

## Hotovo, když

- `safe_int("42")` je `42`; `safe_int("-7")` je `-7`.
- `safe_int("nope")` a `safe_int("")` jsou `None`.
- `safe_int([1, 2])` vyvolá `TypeError` -- checker ji schválně volá se seznamem,
  takže chytání příliš mnoha selže.
