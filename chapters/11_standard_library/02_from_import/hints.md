Start the file with `from math import gcd`. Now `gcd` is a function you can call
directly, no `math.` in front of it.

---

Find `g = gcd(num, den)`, then return the tuple `(num // g, den // g)`. Use `//`
(integer division) so the result stays whole numbers.

---

from math import gcd


def simplify(num, den):
    g = gcd(num, den)
    return (num // g, den // g)
