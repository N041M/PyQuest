Queres reemitir cada item de `a`, depois cada item de `b`. `yield from` faz
exatamente isso para um iterável de cada vez.

---

Duas linhas: `yield from a` depois `yield from b`. Cada uma transmite essa
lista inteira para a saída do gerador.

---

def chain(a, b):
    yield from a
    yield from b
