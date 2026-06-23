# 6.2 -- Dva parametry

## Koncept

Funkce může přijmout několik parametrů -- vyjmenuj je čárkami a hodnoty volajícího
dorazí **ve stejném pořadí**:

```python
def rect_area(width, height):
    return width * height

rect_area(3, 4)     # 12  (width=3, height=4)
```

Uvnitř těla jsou parametry obyčejné proměnné. Funguje na nich vše, co už znáš --
aritmetika, porovnání, f-řetězce, cykly.

Jemnost, kterou je dobré potkat brzy: parametry jsou **lokální** pro funkci. `width`
uvnitř `rect_area` existuje jen po dobu běhu volání; není vidět (ani se nesráží) s
ničím venku.

## Příklad

```python
def diff(a, b):
    return a - b

print(diff(10, 4))   # 6
print(diff(4, 10))   # -6  -- order matters
```

## Tvůj úkol

Definuj `rect_area(width, height)`, která vrátí obsah obdélníku (šířka krát výška).

## Hotovo, když

- `rect_area(3, 4)` vrátí `12`; `rect_area(4, 3)` také.
- Nulová strana vrátí `0`.
- Žádný `input()`, žádný `print()` -- checker hodnoty předá.
