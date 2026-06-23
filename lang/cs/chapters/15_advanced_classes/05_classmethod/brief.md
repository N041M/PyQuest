# 15.5 -- @classmethod: alternativní konstruktor

## Koncept

Normální metoda bere `self` (instanci). **`@classmethod`** bere **`cls`** (samotnou
třídu), takže může postavit a vrátit **novou instanci** -- šikovný způsob, jak
nabídnout alternativní, pojmenovaný konstruktor:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

p = Point.from_tuple((3, 4))     # called on the class, not an instance
p.x, p.y                          # (3, 4)
```

- `@classmethod` udělá z `cls` první parametr -- třídu, na které je metoda volána
  (zde `Point`).
- `cls(...)` je totéž co `Point(...)`, ale použití `cls` znamená, že podtřídy
  dostanou instanci *svého* typu zadarmo.
- Voláš ji na **třídě**: `Point.from_tuple(...)`.

## Tvůj úkol

Definuj `Point` s `__init__(self, x, y)` a **classmethodou** `from_tuple(cls, pair)`,
která sestaví `Point` z n-tice `(x, y)`.

## Hotovo, když

- `Point.from_tuple((3, 4)).x` je `3` a `.y` je `4`.
- `from_tuple` je `@classmethod` beroucí `cls` a staví bod pomocí `cls(...)`.
