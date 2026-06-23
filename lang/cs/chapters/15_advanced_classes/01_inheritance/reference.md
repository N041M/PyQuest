**Dědičnost** umožní třídě stavět na druhé. Zápis `class Child(Parent):` udělá z
`Child` **podtřídu**: automaticky má všechny metody `Parent` a může přidat nové nebo
nahradit stávající.

- Vztah je **„je-“** (is-a): `Dog(Animal)` *je* `Animal`, takže
  `isinstance(dog, Animal)` je `True` a `Dog` funguje všude, kde se očekává
  `Animal`.
- Sdílené chování žije **jednou** v základní třídě; podtřídy ho dědí, místo aby ho
  kopírovaly, takže oprava v rodiči dosáhne na každého potomka.
- Python najde metodu procházením **MRO** (method resolution order, pořadí
  rozlišení metod): nejprve třída instance, pak její základy. `object` je implicitní
  základ každé třídy.

```python
class Animal:
    def __init__(self, name): self.name = name
    def describe(self): return self.name + " the animal"

class Dog(Animal):
    def speak(self): return "Woof"

d = Dog("Rex")
d.describe()              # 'Rex the animal'  -- inherited
isinstance(d, Animal)    # True
```
