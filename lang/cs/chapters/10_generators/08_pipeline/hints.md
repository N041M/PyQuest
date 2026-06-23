Každá fáze je svůj vlastní malý generátor. `numbers` prochází `range(n)` a
yielduje; `keep_even` prochází `stream` a yielduje jen sudá; `labelled` prochází
`stream` a yielduje naformátovaný řetězec. Žádný z nich nestaví seznam.

---

`keep_even` a `labelled` berou `stream` a `for x in stream:` -- ten cyklus funguje,
ať je `stream` seznam nebo jiný generátor, což je to, co ti umožní je vnořovat.
Použij f-řetězec na štítek: `yield f"#{x}"`.

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
