Each stage is its own little generator. `numbers` loops over `range(n)` and
yields; `keep_even` loops over `stream` and yields only the evens; `labelled`
loops over `stream` and yields a formatted string. None of them build a list.

---

`keep_even` and `labelled` take a `stream` and `for x in stream:` -- that loop
works whether `stream` is a list or another generator, which is what lets you
nest them. Use an f-string for the label: `yield f"#{x}"`.

---

def numbers(n):
    for i in range(n):
        yield i


def keep_even(stream):
    for x in stream:
        if x % 2 == 0:
            yield x


def labelled(stream):
    for x in stream:
        yield f"#{x}"
