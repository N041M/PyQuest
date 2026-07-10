Basta indexar dentro de um try -- o Python já sabe exatamente quais os
índices que são maus.

---

`except IndexError: return default` -- isto acerta nos negativos de graça,
o que uma verificação de limites escrita à mão normalmente não consegue.

---

def item_or(items, i, default):
    try:
        return items[i]
    except IndexError:
        return default
