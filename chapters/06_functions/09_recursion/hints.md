Answer the smallest case first: if n is 0, return 1 -- no call needed.

---

For everything else, trust the function you are writing:
return n * fact(n - 1). The early return (6.5) keeps the base case clean.

---

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
