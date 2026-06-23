Chceš znovu vydat každou položku `a`, pak každou položku `b`. `yield from` to
udělá přesně pro jeden iterovatelný objekt po druhém.

---

Dva řádky: `yield from a` pak `yield from b`. Každý z nich proudí celý ten seznam
do výstupu generátoru.

---

def chain(a, b):
    yield from a
    yield from b
