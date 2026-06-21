**Inheritance** lets a class build on another. Writing `class Child(Parent):`
makes `Child` a **subclass**: it automatically has all of `Parent`'s methods, and
can add new ones or replace existing ones.

- The relationship is **"is-a"**: a `Dog(Animal)` *is an* `Animal`, so
  `isinstance(dog, Animal)` is `True` and a `Dog` works anywhere an `Animal` is
  expected.
- Shared behaviour lives **once** in the base class; subclasses inherit it rather
  than copying it, so a fix in the parent reaches every child.
- Python finds a method by walking the **MRO** (method resolution order): the
  instance's class first, then its bases. `object` is the implicit base of every
  class.

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
