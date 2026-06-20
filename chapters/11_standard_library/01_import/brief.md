# 11.1 -- import: bring in a module

## Concept

Python ships a large **standard library**: ready-made tools grouped into
**modules**. You don't get them for free in every file -- you **import** the
module you need, then reach its contents through its name.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
```

- `import math` runs once at the top of the file and binds the name `math` to
  the whole module.
- After that, `math.sqrt` is the square-root function and `math.pi` the
  constant -- `module.name` reaches anything the module provides.

The point of importing is that someone has already written and tested these, so
you call `math.sqrt` instead of re-deriving a square root yourself.

## Example

```python
import math

def diagonal(side):
    return math.sqrt(2) * side
```

## Your task

Define `hypotenuse(a, b)` that returns the length of the hypotenuse of a
right triangle with legs `a` and `b` -- the square root of `a*a + b*b` --
using **`math.sqrt`** from the imported `math` module.

## Done when

- `hypotenuse(3, 4)` returns `5.0`, `hypotenuse(5, 12)` returns `13.0`.
- `hypotenuse(0, 0)` returns `0.0`.
- The square root comes from `math.sqrt`, via `import math`.
