Walk the numbers `0, 1, ..., n-1` with a loop, and `yield` each one squared.

---

`for i in range(n):` then `yield i * i`. The loop gives you each number; the
yield emits its square and pauses until the next is asked for.

---

def squares(n):
    for i in range(n):
        yield i * i
