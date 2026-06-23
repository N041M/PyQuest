# 14.6 -- all: jsou pravdivé úplně všechny?

## Koncept

**`all(iterable)`** je partner `any`: vrátí `True` jen tehdy, když je **každá**
položka pravdivá. Odpoví na „projdou *všechny*?“:

```python
all(n > 0 for n in [1, 2, 3])      # True
all(n > 0 for n in [1, -2, 3])     # False
```

- Vyhodnocuje se **zkráceně** opačně: zastaví se a vrátí `False` u první položky,
  která selže.
- `all([])` je `True` -- prázdně (vacuously), protože žádná položka neselhala.
  (Častý překvap: „všechny z ničeho“ je pravda.)

Stejný tvar jako `any`: `all(<test> for <item> in <iterable>)`.

## Příklad

```python
def all_words(strings):
    return all(s.isalpha() for s in strings)
```

## Tvůj úkol

Pomocí **`all`** definuj `all_positive(nums)`, která vrátí `True`, pokud je **každé**
číslo v `nums` větší než nula.

## Hotovo, když

- `all_positive([1, 2, 3])` je `True`; `all_positive([1, -2, 3])` je `False`.
- `all_positive([])` je `True` (nic neselže).
- Odpověď pochází z `all(...)`, ne z ručně psaného cyklu s příznakem.
