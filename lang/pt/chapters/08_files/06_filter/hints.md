Lê primeiro todas as linhas, depois abre o ficheiro de saída em modo `"w"` e
percorre-as, escrevendo apenas as que queres manter.

---

`if line.strip():` é verdadeiro apenas quando a linha tem conteúdo real.
Escreve a `line` original (já termina em `\n`), não uma cópia sem espaços.

---

with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)
