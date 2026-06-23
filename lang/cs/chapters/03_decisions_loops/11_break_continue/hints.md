Uvnitř cyklu nejprve zkontroluj "x" (break), pak "o" (continue), pak vypiš.

---

`for ch in word:` -> `if ch == "x": break`, pak `if ch == "o": continue`,
pak `print(ch)`.

---

word = input()
for ch in word:
    if ch == "x":
        break
    if ch == "o":
        continue
    print(ch)
