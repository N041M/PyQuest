**`@classmethod`** je svázaná s **třídou**, ne s instancí: jejím prvním parametrem
je **`cls`** (samotná třída) místo `self`. Protože má třídu, může stavět instance —
klasické použití je **alternativní konstruktor**.

- Voláš ji na třídě: `Point.from_tuple((3, 4))`. Python předá `Point` jako `cls`.
- Stavění pomocí `cls(...)` místo doslovného jména třídy znamená, že **podtřída**,
  která volá zděděnou classmethodu, dostane instanci *sebe sama*.
- Kontrast s **`@staticmethod`**, která nebere ani `self`, ani `cls` — jen prostou
  funkci ve jmenném prostoru třídy, používanou, když metoda nepotřebuje přístup k
  instanci ani třídě.

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    @classmethod
    def from_tuple(cls, pair): return cls(pair[0], pair[1])

Point.from_tuple((3, 4)).x     # 3
```
