An **`import`** statement loads a **module** — a file of ready-made code from the
standard library — and binds it to a name. `import math` makes the module object
available as `math`, and its contents are reached through it: `math.sqrt`,
`math.pi`, `math.floor`.

- The statement runs **once**, conventionally at the **top** of the file; the
  name then refers to the whole module for the rest of the program.
- **`module.name`** (attribute access) looks a function or constant up *on* the
  module, which keeps each module's names in their own namespace — `math.pi` and
  your own `pi` never collide.
- Importing a name that doesn't exist raises `ModuleNotFoundError`; the module's
  code runs the first time it is imported and is cached thereafter.
- The standard library ships with Python ("batteries included"), so these
  modules need no installation — just the import.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
math.floor(2.7)  # 2
```
