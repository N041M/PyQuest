# 6.6 -- Vrácení dvou hodnot

## Koncept

`return` může předat **několik hodnot najednou** -- odděl je čárkou a Python je
zabalí do **n-tice** (4.7):

```python
def min_max(nums):
    return min(nums), max(nums)
```

Volající si může n-tici ponechat, nebo ji rozbalit rovnou do proměnných -- stejné
rozbalování, jaké jsi použil u `a, b = b, a`:

```python
pair = min_max([3, 1, 4])     # (1, 4)  -- one tuple
lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4  -- unpacked
```

Takto pythonovské funkce vracejí „dvě odpovědi“ -- není v tom žádný zvláštní trik,
jen n-tice a rozbalování.

## Příklad

```python
def split_name(full):
    parts = full.split()
    return parts[0], parts[-1]

first, last = split_name("Ada King Lovelace")
# first = "Ada", last = "Lovelace"
```

## Tvůj úkol

Definuj `min_max(nums)`, která vrátí nejmenší a největší položku neprázdného
seznamu, **v tomto pořadí**, jako n-tici. (`min()`/`max()` jsou z 5.3.)

## Hotovo, když

- `min_max([3, 1, 4])` vrátí `(1, 4)` -- n-tici, nejmenší první.
- `min_max([7])` vrátí `(7, 7)`.
- Záporná čísla fungují.
