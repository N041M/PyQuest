A lambda is `lambda args: expression`. You want one that takes an `x` and gives
back `x * n`.

---

`multiplier` returns that lambda. The lambda closes over `n`, so each call to
`multiplier` makes a function tied to its own `n`.

---

def multiplier(n):
    return lambda x: x * n
