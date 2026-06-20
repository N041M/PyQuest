# 11.4 -- random: reproducible chance

## Concept

The **`random`** module produces pseudo-random values: `random.randint(1, 6)`
rolls a die, `random.shuffle(lst)` reorders a list in place. They're *pseudo*-
random -- computed from an internal state -- which means you can make them
**repeatable** by fixing that state with a **seed**:

```python
import random

random.seed(42)
random.shuffle(deck)     # always the same order for seed 42
```

- `random.seed(n)` sets the starting point. After the same seed, the same calls
  produce the same results, every run, every machine.
- `random.shuffle(lst)` shuffles **in place** (it returns `None`), so shuffle a
  copy if you need to keep the original.

Seeding is how a game replays a level, or a test checks "random" code.

## Example

```python
import random

def pick(options, seed):
    random.seed(seed)
    return random.choice(options)
```

## Your task

Define `shuffled(items, seed)` that returns a **new** list with the items of
`items` shuffled, made repeatable by seeding with `seed` **before** shuffling.
Don't change the original `items`.

## Done when

- `shuffled(items, seed)` gives the same result every time for the same
  `items` and `seed`.
- The original list passed in is left unchanged (shuffle a copy).
- `shuffled([], 1)` returns `[]`.
