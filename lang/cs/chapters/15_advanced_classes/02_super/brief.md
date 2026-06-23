# 15.2 -- super(): rozšiř rodiče

## Koncept

Podtřída často potřebuje vše, co dělá rodičův `__init__`, **plus** trochu navíc.
**`super()`** ti dá rodiče, takže zavoláš jeho metodu a pak k ní přidáš -- místo
kopírování rodičova kódu:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # run Animal's __init__ (sets self.name)
        self.breed = breed         # then add Dog's own attribute
```

- `super().__init__(name)` zavolá **rodičův** `__init__` na této instanci, takže
  `self.name` nastaví `Animal`.
- Poté potomek přidá to, co je pro něj zvláštní (`self.breed`).
- Tím se rodičovo nastavení drží na jednom místě; pokud se `Animal.__init__` změní,
  `Dog` to převezme automaticky.

## Tvůj úkol

Definuj `Animal` s `__init__(self, name)` ukládajícím `self.name`. Pak definuj
`Dog(Animal)`, jehož `__init__(self, name, breed)` zavolá **`super().__init__(name)`**
a pak uloží `self.breed`.

## Hotovo, když

- `Dog("Rex", "Lab").name` je `"Rex"` (nastaveno přes `super().__init__`).
- `Dog("Rex", "Lab").breed` je `"Lab"`.
- `Dog` je `Animal` a jméno nastaví rodič, ne ruční přiřazení.
