**Přepsání** je definice metody, kterou rodič už má, v podtřídě. Pro instance
podtřídy najde Python verzi podtřídy první (je dřív v MRO), takže chování potomka
nahradí to rodičovo.

- To je **polymorfismus**: jedno místo volání, `x.speak()`, spustí správný kód pro
  jakýkoli typ, jímž `x` skutečně je — `Cat` řekne „Meow“, obecný `Animal` řekne
  „...“. Volající kód nemusí znát přesný typ.
- Podtřída stále **dědí** vše, co *nepřepíše* (zde `__init__`).
- Přepsání může znovu použít rodičovu verzi pomocí `super().method()` — rozšířit,
  místo úplně nahradit.

```python
class Animal:
    def speak(self): return "..."
class Cat(Animal):
    def speak(self): return "Meow"

for a in [Animal(), Cat()]:
    print(a.speak())     # '...' then 'Meow' -- same call, different result
```
