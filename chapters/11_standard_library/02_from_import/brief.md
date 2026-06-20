# 11.2 -- from import: pull out one name

## Concept

`import math` brings in the *whole* module and you reach into it with
`math.something`. Often you want just one tool, used by its plain name. The
**`from ... import ...`** form does that:

```python
from math import gcd

gcd(12, 18)      # 6  -- called directly, no math. prefix
```

- `from math import gcd` binds the single name `gcd` into your file.
- You then call it as `gcd(...)`, not `math.gcd(...)`.
- You can pull several at once: `from math import gcd, sqrt, pi`.

`gcd(a, b)` is the **greatest common divisor** -- the largest integer that
divides both. It's exactly what you need to reduce a fraction to lowest terms:
divide the top and bottom by their gcd.

## Example

```python
from math import gcd

def both_divisible_by(a, b):
    return gcd(a, b)
```

## Your task

Using **`from math import gcd`**, define `simplify(num, den)` that returns the
fraction `num/den` reduced to lowest terms, as a tuple `(top, bottom)`: divide
both `num` and `den` by their `gcd`.

## Done when

- `simplify(6, 8)` returns `(3, 4)`, `simplify(10, 5)` returns `(2, 1)`.
- `simplify(7, 7)` returns `(1, 1)`.
- The gcd comes from `math`, imported with `from math import gcd`.
