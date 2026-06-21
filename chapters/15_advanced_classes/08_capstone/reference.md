The capstone blends the chapter into one hierarchy, the way real classes are
built:

- **Inheritance** — `Rectangle(Shape)` *is a* `Shape`, so it gets `describe` for
  free and `isinstance(r, Shape)` is true.
- **`super()`** — `Rectangle.__init__` calls `super().__init__("rectangle")` to let
  the base set `self.name`, then adds its own width and height.
- **`@property`** — `area` is computed from width and height on each access, so it
  stays correct when a side changes.
- **Polymorphism** — `Shape.describe` reads `self.area`, which only `Rectangle`
  defines; the base method works through the subclass's property.
- **Dunders** — `__eq__` and `__lt__` (both by area) make rectangles compare and
  sort like built-in values, so `==` and `sorted` just work.

Together these turn a plain object into one that behaves like a first-class
value: it has an identity in a hierarchy, derived data, and meaningful equality
and ordering — the payoff of the whole chapter.

```python
r = Rectangle(3, 4)
r.describe()                              # 'rectangle with area 12'
Rectangle(2, 6) == Rectangle(3, 4)        # True  -- equal areas
sorted([Rectangle(3, 4), Rectangle(1, 1)])   # by area: 1, then 12
```
