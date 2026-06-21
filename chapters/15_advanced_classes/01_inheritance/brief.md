# 15.1 -- Inheritance: build on a base class

## Concept

Chapter 9 built single classes. **Inheritance** lets one class build on another:
a **subclass** automatically gets the **base class's** methods, then adds or
changes its own.

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

- `class Dog(Animal):` makes `Dog` a subclass of `Animal`. A `Dog` instance can
  call `describe()` -- inherited from `Animal` -- *and* `speak()`, its own.
- The relationship is "**is-a**": a `Dog` **is an** `Animal`, so
  `isinstance(dog, Animal)` is `True`.
- Shared behaviour lives once in the base; subclasses don't repeat it.

## Your task

Define a base class `Animal` with an `__init__(self, name)` and a
`describe(self)` returning `"<name> the animal"`. Then define `Dog(Animal)` that
**inherits** from it and adds `speak(self)` returning `"Woof"`.

## Done when

- `Dog("Rex").describe()` returns `"Rex the animal"` (inherited).
- `Dog("Rex").speak()` returns `"Woof"`.
- A `Dog` **is an** `Animal`: it inherits rather than copying `describe`.
