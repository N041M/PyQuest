# 15.2 -- super(): extend the parent

## Concept

A subclass often needs everything the parent's `__init__` does **plus** a bit
more. **`super()`** gives you the parent, so you call its method and then add to
it -- rather than copying the parent's code:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # run Animal's __init__ (sets self.name)
        self.breed = breed         # then add Dog's own attribute
```

- `super().__init__(name)` calls the **parent's** `__init__` on this instance, so
  `self.name` gets set by `Animal`.
- After that, the child adds what's special to it (`self.breed`).
- This keeps the parent's set-up in one place; if `Animal.__init__` changes, `Dog`
  picks it up automatically.

## Your task

Define `Animal` with `__init__(self, name)` storing `self.name`. Then define
`Dog(Animal)` whose `__init__(self, name, breed)` calls **`super().__init__(name)`**
and then stores `self.breed`.

## Done when

- `Dog("Rex", "Lab").name` is `"Rex"` (set via `super().__init__`).
- `Dog("Rex", "Lab").breed` is `"Lab"`.
- A `Dog` is an `Animal`, and the name is set by the parent, not re-assigned by
  hand.
