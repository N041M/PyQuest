Each case is an if with its own return. Once a return runs, the function is
over.

---

Check `n < 0` first, then `n == 0`; if neither returned, n must be positive --
just return "positive" with no condition.

---

def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
