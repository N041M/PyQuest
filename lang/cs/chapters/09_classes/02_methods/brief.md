# 9.2 -- Metody: chování nad daty

## Koncept

Objekty nejen drží data -- mají **metody**, funkce, které žijí na objektu a pracují
s jeho vlastními daty skrze `self`.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

`area` je metoda: bere `self` (objekt, na kterém je volána) a používá `self.side`.
Voláš ji tečkou a závorkami -- `self` předávat netřeba, Python ho doplní:

```python
s = Square(5)
print(s.area())   # 25
```

Smysl metody je, že chování putuje *spolu* s daty: každý Square už ví, jak spočítat
svůj vlastní obsah.

## Tvůj úkol

Definuj třídu `Square`, jejíž `__init__` uloží `side`, a přidej metodu `area()`,
která vrátí obsah čtverce (`side * side`).

## Hotovo, když

- `Square(5).area()` vrátí `25`.
- Funguje pro libovolnou délku strany, včetně `0`.
- `area` je metoda na třídě a počítá z `self.side`.
