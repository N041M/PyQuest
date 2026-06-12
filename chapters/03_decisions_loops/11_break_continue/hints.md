Inside the loop, check for "x" first (break), then "o" (continue), then print.

---

`for ch in word:` -> `if ch == "x": break`, then `if ch == "o": continue`,
then `print(ch)`.

---

word = input()
for ch in word:
    if ch == "x":
        break
    if ch == "o":
        continue
    print(ch)
