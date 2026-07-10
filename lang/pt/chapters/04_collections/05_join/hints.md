Reúne as palavras numa lista, e depois junta-as. O join é chamado sobre o separador.

---

Constrói a lista, depois `print("-".join(words))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print("-".join(words))
