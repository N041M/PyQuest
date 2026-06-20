**`import module as alias`** imports a module but binds it under a name of your
choosing. `import statistics as stats` makes the module available as `stats`;
`stats.mean` *is* `statistics.mean` — the alias changes only the local name, not
the module.

- Use it to **shorten** a long module name or to **avoid a clash** with one of
  your own names. The convention-driven aliases you'll meet (`import numpy as
  np`) are exactly this.
- The same `as` works on a single name from a from-import: `from statistics
  import mean as avg`.
- Only your file sees the alias; other modules keep their own names for it.

```python
import statistics as stats

stats.mean([1, 2, 3, 4])     # 2.5
stats.median([1, 5, 2])      # 2
```
