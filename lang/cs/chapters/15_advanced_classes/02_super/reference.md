**`super()`** vrátí proxy na **rodičovskou třídu**, takže podtřída může zavolat
rodičovu metodu a stavět na ní, místo aby duplikovala jeho kód. Obvyklý případ je
`__init__`:

- `super().__init__(args)` spustí rodičův inicializátor na této instanci a nastaví
  vše, co rodič vlastní; potomek pak přidá své vlastní atributy.
- Drží rodičovu logiku na **jednom místě** — změň `Animal.__init__` a každá podtřída,
  která volá `super().__init__`, změnu zdědí.
- `super()` funguje pro libovolnou metodu, nejen `__init__`: přepisující metoda může
  zavolat `super().method()`, aby znovu použila rodičovu verzi a rozšířila ji.
- Bez `super().__init__` se rodičův inicializátor **nespustí**, takže atributy, které
  by nastavil, chybí.

```python
class Animal:
    def __init__(self, name): self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Animal sets self.name
        self.breed = breed         # Dog adds self.breed

Dog("Rex", "Lab").name             # 'Rex'
```
