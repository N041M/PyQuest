# 15.4 -- @property: počítaný atribut

## Koncept

Někdy je hodnota **odvozená** z jiných -- obsah obdélníku z jeho šířky a výšky. Mohl
bys ji uložit, ale pak zastará, když se změní šířka. **`@property`** ji spočítá při
každém přístupu, a přitom se stále čte jako prostý atribut:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12   -- no parentheses, but the method runs
r.width = 5
r.area        # 20   -- recomputed from the new width
```

- `@property` nad metodou udělá z `obj.area` (bez `()`) volání té metody a vrácení
  jejího výsledku.
- Protože běží pokaždé, hodnota je vždy aktuální -- na rozdíl od hodnoty uložené
  jednou v `__init__`.

## Tvůj úkol

Definuj `Rectangle` s `__init__(self, width, height)` a **property** **`area`**,
která vrátí `width * height`.

## Hotovo, když

- `Rectangle(3, 4).area` je `12` (přístup bez závorek).
- Po `r = Rectangle(3, 4); r.width = 5` je `r.area` `20` -- přepočítáno, ne uloženo.
