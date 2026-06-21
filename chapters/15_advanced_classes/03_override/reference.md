**Overriding** is defining, in a subclass, a method the parent already has. For
the subclass's instances, Python finds the subclass's version first (it's earlier
in the MRO), so the child's behaviour replaces the parent's.

- This is **polymorphism**: one call site, `x.speak()`, runs the right code for
  whatever type `x` actually is — `Cat` says "Meow", a generic `Animal` says
  "...". Calling code needn't know the exact type.
- The subclass still **inherits** everything it does *not* override (here
  `__init__`).
- An override can reuse the parent's version with `super().method()` — extend
  rather than fully replace.

```python
class Animal:
    def speak(self): return "..."
class Cat(Animal):
    def speak(self): return "Meow"

for a in [Animal(), Cat()]:
    print(a.speak())     # '...' then 'Meow' -- same call, different result
```
