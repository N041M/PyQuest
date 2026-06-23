# 14.3 -- filter: ponech, co projde

## Koncept

Kde `map` transformuje každou položku, **`filter`** ponechá jen **některé** z nich.
Dáš mu **predikát** -- funkci, která vrací pravda nebo nepravda -- a on ponechá
každou položku, na kterou predikát řekne ano:

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))     # [2, 4]
```

- `filter(pred, iterable)` vydá každou položku, pro kterou je `pred(item)` pravdivý,
  a zbytek zahodí, v pořadí.
- Stejně jako `map` vrátí **líný iterátor**, takže ho obal do `list(...)`.

(Komprehenze `[x for x in items if pred(x)]` dělá totéž; tato úloha je o samotném
`filter`.)

## Příklad

```python
def nonempty(strings):
    return list(filter(lambda s: s != "", strings))
```

## Tvůj úkol

Pomocí **`filter`** definuj `evens(nums)`, která vrátí seznam jen sudých čísel v
`nums`.

## Hotovo, když

- `evens([1, 2, 3, 4])` vrátí `[2, 4]`.
- `evens([1, 3, 5])` vrátí `[]`.
- Výběr dělá `filter`, ne komprehenze nebo ruční cyklus.
