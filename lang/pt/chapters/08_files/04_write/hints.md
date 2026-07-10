Dois passos: primeiro lê in.txt para uma cadeia de caracteres, depois abre
out.txt em modo `"w"` e escreve a cadeia em maiúsculas.

---

`open("out.txt", "w")` é a parte da escrita; `text.upper()` faz a conversão
para maiúsculas. `.write()` escreve a cadeia tal como está.

---

with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
