# 10.6 -- yield from: předej celý proud dál

## Koncept

Když chceš, aby generátor znovu vydal **každou** položku jiného iterovatelného
objektu, mohl bys procházet a yieldovat každou:

```python
def both(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
```

Python má pro přesně tenhle vnitřní cyklus zkratku: **`yield from`**.

```python
def both(a, b):
    yield from a        # yield every item of a, one by one
    yield from b        # then every item of b
```

`yield from iterable` je „yieldni každou hodnotu, kterou tento iterovatelný objekt
vyprodukuje“. Obě verze výše se chovají stejně; `yield from` to jen řekne jedním
řádkem.

## Příklad

```python
def repeat_each(items):
    for x in items:
        yield from (x, x)      # yield x, then x again

list(repeat_each([1, 2]))      # [1, 1, 2, 2]
```

## Tvůj úkol

Definuj generátor `chain(a, b)`, který yielduje **všechny** položky `a`, pak
**všechny** položky `b`, v pořadí. Použij `yield from`. Kterýkoli seznam může být
prázdný.

## Hotovo, když

- `list(chain([1, 2], [3, 4]))` je `[1, 2, 3, 4]`.
- `list(chain([], [9]))` je `[9]`; `list(chain([], []))` je `[]`.
- Použiješ `yield from`, takže volání `chain` vrátí generátor.
