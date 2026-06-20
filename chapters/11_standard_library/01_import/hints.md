The very first line of the file makes the module available: `import math`. After
that you can use anything it provides as `math.something`.

---

`math.sqrt(x)` returns the square root of `x`. You want the square root of
`a*a + b*b`. Put the `import math` at the top, then write the function.

---

import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)
