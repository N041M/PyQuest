Lê a entrada com `input()`, depois abre o ficheiro num modo que *mantenha* o
que já lá está.

---

O modo `"a"` anexa em vez de apagar. Não te esqueças do `"\n"` para que a nova
entrada fique na sua própria linha.

---

entry = input()
with open("log.txt", "a") as f:
    f.write(entry + "\n")
