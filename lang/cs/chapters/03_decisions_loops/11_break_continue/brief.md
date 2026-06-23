# 3.11 -- break a continue

## Koncept

Dvě klíčová slova mění tok cyklu:

- **`break`** zastaví cyklus **okamžitě** -- žádné další průchody.
- **`continue`** přeskočí **zbytek aktuálního průchodu** a skočí na další.

```python
for ch in "a,b,c":
    if ch == ",":
        continue        # skip commas
    print(ch)
# prints a, b, c (commas skipped)

for n in range(100):
    if n == 3:
        break           # stop the whole loop at 3
    print(n)
# prints 0, 1, 2
```

`continue` přeskočí jednu položku; `break` cyklus ukončí.

## Příklad

```python
for ch in "abxcd":
    if ch == "x":
        break
    print(ch)
# prints a, b   (stops at x)
```

## Tvůj úkol

Přečti slovo a procházej jeho znaky:

- písmeno `o` **přeskoč** (použij `continue` -- nevypisuj ho),
- u písmena `x` se úplně **zastav** (použij `break` -- od `x` dál nic nevypisuj),
- každý jiný znak vypiš na vlastním řádku.

Pro vstup `boxes` je výstup:

```
b
```

(`b`, pak se `o` přeskočí, pak `x` cyklus zastaví.)

## Hotovo, když

- `boxes` vypíše `b`; `good` vypíše `g` a pak `d` (`o` přeskočeny); `abc` vypíše
  `a`, `b`, `c`.
