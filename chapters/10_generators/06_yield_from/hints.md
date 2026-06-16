You want to re-emit every item of `a`, then every item of `b`. `yield from`
does exactly that for one iterable at a time.

---

Two lines: `yield from a` then `yield from b`. Each one streams that whole list
into the generator's output.

---

def chain(a, b):
    yield from a
    yield from b
