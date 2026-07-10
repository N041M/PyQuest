Um bloco `with open(name) as f:` dá-te o ficheiro como `f`. Dentro dele, pede
ao ficheiro tudo o que contém.

---

`f.read()` devolve o ficheiro inteiro como uma única cadeia de caracteres.
Guarda-a e depois imprime-a a seguir (ou dentro) do bloco.

---

with open("note.txt") as f:
    text = f.read()
print(text)
