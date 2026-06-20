The **`random`** module generates pseudo-random values from an internal state:
`random.randint(a, b)` (an integer in `[a, b]`), `random.choice(seq)` (a random
item), `random.shuffle(lst)` (reorder a list **in place**), `random.random()` (a
float in `[0, 1)`).

- The numbers are deterministic functions of the state, so **`random.seed(n)`**
  makes them **repeatable**: after the same seed, the same calls yield the same
  results on every run and machine. Seed once, before the draws you want to
  reproduce.
- `random.shuffle` mutates its argument and returns `None` — shuffle a **copy**
  (`out = list(items)`) to keep the original, and never `return
  random.shuffle(...)`.
- The default (unseeded) generator is seeded from the OS, so without a seed each
  run differs. `random` is **not** for cryptography — use the `secrets` module
  for tokens and passwords.

```python
import random

random.seed(42)
random.randint(1, 6)     # same value every run for seed 42
deck = [1, 2, 3, 4]
random.shuffle(deck)     # deck reordered in place
```
