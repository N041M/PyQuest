A generator looks like a normal function, but it says `yield` where a normal
one would build a result. Each `yield` produces one number.

---

Count with a loop from `n` downwards and `yield` each value. A `while` loop:
start `i` at `n`, `yield i`, then `i = i - 1`, while `i >= 1`. (A
`for i in range(n, 0, -1):` works too.)

---

def count_down(n):
    i = n
    while i >= 1:
        yield i
        i = i - 1
