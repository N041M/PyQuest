# 15.1 -- Dědičnost: stav na základní třídě

## Koncept

Kapitola 9 stavěla jednotlivé třídy. **Dědičnost** umožní jedné třídě stavět na
druhé: **podtřída** automaticky dostane metody **základní třídy**, pak přidá nebo
změní vlastní.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return self.name + " the animal"

class Dog(Animal):           # Dog IS an Animal
    def speak(self):
        return "Woof"
```

- `class Dog(Animal):` udělá z `Dog` podtřídu `Animal`. Instance `Dog` může zavolat
  `describe()` -- zděděné z `Animal` -- *i* `speak()`, svou vlastní.
- Vztah je „**je-**“ (is-a): `Dog` **je** `Animal`, takže `isinstance(dog, Animal)`
  je `True`.
- Sdílené chování žije jednou v základu; podtřídy ho neopakují.

## Tvůj úkol

Definuj základní třídu `Animal` s `__init__(self, name)` a `describe(self)`
vracejícím `"<name> the animal"`. Pak definuj `Dog(Animal)`, který z ní **dědí** a
přidá `speak(self)` vracející `"Woof"`.

## Hotovo, když

- `Dog("Rex").describe()` vrátí `"Rex the animal"` (zděděné).
- `Dog("Rex").speak()` vrátí `"Woof"`.
- `Dog` **je** `Animal`: dědí `describe`, místo aby ho kopíroval.
