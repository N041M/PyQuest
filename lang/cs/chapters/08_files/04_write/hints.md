Dva kroky: nejprve načti in.txt do řetězce, pak otevři out.txt v režimu `"w"` a
zapiš řetězec velkými písmeny.

---

`open("out.txt", "w")` je polovina pro zápis; `text.upper()` udělá velká písmena.
`.write()` zapíše řetězec tak, jak je.

---

with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
