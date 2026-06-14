# 9.1 -- A first class

## Concept

A **class** is a blueprint for an object that bundles related data together. So
far a dog's name and age would be two loose variables; a class ties them into
one thing you can pass around.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `class Dog:` names the blueprint.
- `__init__` is the **constructor** -- it runs when you build a new Dog, and its
  job is to set up the object's data.
- `self` is the object being built; `self.name = name` stores the value **on the
  object** so it's still there later.

You build one (an *instance*) by calling the class like a function, and you read
its data with a dot:

```python
d = Dog("Rex", 3)
print(d.name)   # Rex
print(d.age)    # 3
```

## Your task

Define a class `Dog` whose `__init__` takes a `name` and an `age` and stores
each on the object as `self.name` and `self.age`.

## Done when

- `Dog("Rex", 3)` makes an object whose `.name` is `"Rex"` and `.age` is `3`.
- It works for any name and age.
- You used a `class` with an `__init__` that stores both values on `self`.
