# 9.4 -- Více dat, více metod

## Koncept

Třída může držet několik kusů dat a nabízet nad nimi několik metod. V syntaxi nic
nového -- jen víc téhož:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

Obě metody čtou stejná uložená data skrze `self`; každý Rectangle o sobě zodpoví
kteroukoli otázku:

```python
r = Rectangle(3, 4)
r.area()        # 12
r.perimeter()   # 14
```

## Tvůj úkol

Definuj třídu `Rectangle`, jejíž `__init__` uloží `width` a `height`, se dvěma
metodami: `area()` vrací `width * height` a `perimeter()` vrací
`2 * (width + height)`.

## Hotovo, když

- `Rectangle(3, 4).area()` je `12` a `.perimeter()` je `14`.
- Obojí funguje pro libovolnou šířku a výšku.
- Obojí jsou metody na třídě, počítající z `self`.
