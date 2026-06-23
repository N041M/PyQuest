# 2.8 -- Nahrazování a počítání

## Koncept

Další dvě metody řetězců:

- `s.replace(old, new)` vrátí kopii `s`, kde je **každý** výskyt `old` nahrazen
  `new`:
  ```python
  "banana".replace("a", "o")   # "bonono"
  ```
- `s.count(sub)` vrátí, **kolikrát** se `sub` vyskytuje (číslo):
  ```python
  "banana".count("a")          # 3
  ```

Pokud `old` chybí, `replace` vrátí řetězec beze změny; pokud `sub` chybí, `count`
vrátí `0`.

## Příklad

```python
s = "foo bar"
print(s.replace("o", "0"))   # f00 bar
print(s.count("o"))          # 2
```

## Tvůj úkol

Přečti řádek a vypiš dva řádky:

1. řádek, kde je každé písmeno `o` nahrazeno nulou `0`
2. kolik `o` bylo v **původním** řádku

Pro vstup `foobar` je výstup:

```
f00bar
2
```

## Hotovo, když

- Pro `foobar` jsou řádky `f00bar` a `2`.
- Pro řádek bez `o` vypíše řádek beze změny a `0`. Kontrola to zkouší.
