# 14.4 -- sorted(key=lambda): řazení podle odvozené hodnoty

## Koncept

`sorted` (kapitola 5) řadí položky podle jejich přirozeného pořadí. Jeho argument
**`key=`** mění, *podle čeho* řadí: funkce mapující každou položku na hodnotu k
porovnání. Inline **lambda** je obvyklý způsob, jak to napsat:

```python
words = ["pear", "fig", "apple"]
sorted(words, key=len)                  # ['fig', 'pear', 'apple']
sorted(words, key=lambda w: w[-1])      # by last letter
```

- `key` se zavolá jednou na položku; `sorted` pak položky seřadí podle těchto hodnot
  klíče.
- lambda ti umožní řadit podle čehokoli **odvozeného** z položky -- její délky, pole,
  spočítaného skóre -- aniž bys měnil samotné položky.
- `sorted` je **stabilní**: položky se stejnými klíči si ponechají původní pořadí.

## Příklad

```python
def by_size(nums):
    return sorted(nums, key=lambda n: abs(n))   # by distance from zero
```

## Tvůj úkol

Pomocí **`sorted`** s **`key=lambda`** definuj `by_last(words)`, která vrátí slova
seřazená podle jejich **posledního znaku**.

## Hotovo, když

- `by_last(["pear", "fig", "kiwi"])` vrátí `["fig", "kiwi", "pear"]`
  (poslední písmena g, i, r jsou v pořadí).
- `by_last([])` vrátí `[]`.
- Pořadí pochází z `sorted(..., key=lambda ...)`, ne z ručního řazení.
