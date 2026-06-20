**`elif`** ("else if") adds more branches between `if` and `else`. Python checks
each condition **in order** and runs the block of the **first** one that is true,
then skips the rest. An optional final `else` handles "none matched".

- Only one branch ever runs — the first true one. Later conditions aren't even
  evaluated.
- Because the first match wins, order matters: put the more specific or
  higher-priority tests first.
- An `elif` chain is flatter and clearer than nesting an `if` inside each
  `else`.

```python
if score >= 90:
    grade = "A"
elif score >= 80:       # only checked if the first was False
    grade = "B"
else:
    grade = "C"
```
