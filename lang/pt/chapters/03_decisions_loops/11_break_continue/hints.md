Dentro do ciclo, verifica primeiro "x" (break), depois "o" (continue), depois imprime.

---

`for ch in word:` -> `if ch == "x": break`, depois `if ch == "o": continue`,
depois `print(ch)`.

---

word = input()
for ch in word:
    if ch == "x":
        break
    if ch == "o":
        continue
    print(ch)
