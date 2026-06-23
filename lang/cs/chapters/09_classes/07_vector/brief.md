# 9.7 -- Objekty spolupracující

## Koncept

Metoda může brát **jiný objekt** jako argument a postavit **nový** objekt jako svůj
výsledek. Takto se objekty kombinují, aniž by ztratily svou vlastní identitu.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

`add` sáhne do `other` (jiného Vectoru) pro jeho data a **vrátí úplně nový
`Vector`** -- nemění `self` ani `other`:

```python
a = Vector(1, 2)
b = Vector(3, 4)
c = a.add(b)      # Vector(4, 6)
a.x               # still 1 -- a is untouched
```

Stavět `Vector(...)` *uvnitř* vlastní metody Vectoru je normální: třída může použít
sama sebe.

## Tvůj úkol

Definuj třídu `Vector` ukládající `x` a `y`, s metodou `add(other)`, která vrátí
**nový** `Vector`, jehož souřadnice jsou souřadnice obou vektorů sečtené dohromady.
Originály musí zůstat beze změny.

## Hotovo, když

- `Vector(1, 2).add(Vector(3, 4))` je Vector s `.x == 4` a `.y == 6`.
- Oba vstupní vektory jsou poté beze změny.
- `add` vrací nový objekt `Vector` (ne n-tici), postavený uvnitř metody.
