# 14.5 -- any: je alespoň jedna pravda?

## Koncept

**`any(iterable)`** vrátí `True`, pokud je **alespoň jedna** položka pravdivá, jinak
`False`. Když ho napájíš generátorem testů, odpoví na „projde *nějaká* položka?“:

```python
any(n < 0 for n in [1, 2, -3])     # True
any(n < 0 for n in [1, 2, 3])      # False
```

- Nahradí cyklus s příznakem (`found = False; for ...: if ...: found = True`)
  jediným výrazem.
- Vyhodnocuje se **zkráceně**: zastaví se a vrátí `True` u první pravdivé položky.
- `any([])` je `False` (nic neprošlo).

Vzor je `any(<test> for <item> in <iterable>)` -- generátorový výraz booleanů
předaný `any`.

## Příklad

```python
def has_blank(strings):
    return any(s == "" for s in strings)
```

## Tvůj úkol

Pomocí **`any`** definuj `has_negative(nums)`, která vrátí `True`, pokud `nums`
obsahuje alespoň jedno záporné číslo.

## Hotovo, když

- `has_negative([1, 2, -3])` je `True`; `has_negative([1, 2, 3])` je `False`.
- `has_negative([])` je `False`.
- Odpověď pochází z `any(...)`, ne z ručně psaného cyklu s příznakem.
