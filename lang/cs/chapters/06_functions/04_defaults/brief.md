# 6.4 -- Výchozí hodnoty

## Koncept

Parametr může nést **výchozí hodnotu**: hodnotu použitou, když ji volající vynechá.
Napíšeš ji s `=` na řádku `def`:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")              # "Hello, Ada!"   -- default used
greet("Ada", "Hi")        # "Hi, Ada!"      -- default overridden
```

Tohle už jsi *používal*: `print(..., sep=" ")` z 1.3 -- `sep` má výchozí hodnotu
jednu mezeru, kterou jsi přepsal `sep=", "`. Teď můžeš stejnou flexibilitu vestavět
do vlastních funkcí.

Pravidla: parametry s výchozí hodnotou jdou **za** těmi bez ní a výchozí hodnota se
použije *jen* tehdy, když volající ten argument vynechá.

## Příklad

```python
def repeat(word, times=2):
    return word * times

repeat("ha")        # "haha"
repeat("ha", 3)     # "hahaha"
```

## Tvůj úkol

Definuj `greet(name, greeting="Hello")`, která vrátí `"<greeting>, <name>!"` --
přesně: pozdrav, čárka a mezera, jméno, vykřičník.

## Hotovo, když

- `greet("Ada")` vrátí `"Hello, Ada!"` (výchozí hodnota v akci).
- `greet("Ada", "Hi")` vrátí `"Hi, Ada!"`.
- Bez výchozí hodnoty by jednoargumentové volání spadlo -- checker dělá oba druhy
  volání.
