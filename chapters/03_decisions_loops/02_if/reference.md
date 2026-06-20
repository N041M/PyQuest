An **`if`** statement runs an indented block **only when** its condition is true.
The condition is evaluated to a boolean; if true, the block runs; if false, it is
skipped and the program continues below.

- The block is defined by **indentation** (conventionally 4 spaces). Every line
  indented under the `if` belongs to it; the first line back at the outer level
  ends it.
- The condition need not be a literal `True`/`False` — any value is tested for
  **truthiness**: `0`, `0.0`, `""`, and empty collections are falsy; everything
  else is truthy.

```python
if temperature > 30:
    print("hot")        # runs only when the test is True
print("done")           # always runs -- not indented under the if
```
