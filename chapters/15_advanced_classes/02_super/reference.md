**`super()`** returns a proxy to the **parent class**, so a subclass can call the
parent's method and build on it instead of duplicating its code. The usual case
is `__init__`:

- `super().__init__(args)` runs the parent's initialiser on this instance,
  setting up whatever the parent owns; the child then adds its own attributes.
- It keeps the parent's logic in **one place** — change `Animal.__init__` and
  every subclass that calls `super().__init__` inherits the change.
- `super()` works for any method, not just `__init__`: an overriding method can
  call `super().method()` to reuse the parent's version and extend it.
- With no `super().__init__`, the parent's initialiser does **not** run, so the
  attributes it would set are missing.

```python
class Animal:
    def __init__(self, name): self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Animal sets self.name
        self.breed = breed         # Dog adds self.breed

Dog("Rex", "Lab").name             # 'Rex'
```
