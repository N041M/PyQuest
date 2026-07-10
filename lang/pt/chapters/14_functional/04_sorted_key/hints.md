`sorted(words, key=...)` ordena pelo que quer que a função `key` devolva.
Queres ordenar pelo último caráter de cada palavra.

---

O último caráter de `w` é `w[-1]`, por isso a chave é `lambda w: w[-1]`:
`sorted(words, key=lambda w: w[-1])`.

---

def by_last(words):
    return sorted(words, key=lambda w: w[-1])
