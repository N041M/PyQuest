You need a loop that never ends, yielding a counter that goes up by one each
time. The `yield` is what stops it from hanging.

---

Start `i` at `0`. Then `while True:` -- `yield i`, then `i = i + 1`. The loop
"never ends", but each yield pauses it until the next value is wanted.

---

def naturals():
    i = 0
    while True:
        yield i
        i = i + 1
