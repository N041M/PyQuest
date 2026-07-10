Uma palavra é uma ou mais letras seguidas. A classe de caracteres `[A-Za-z]`
corresponde a uma única letra; o quantificador `+` faz-a corresponder a uma
sequência.

---

`re.findall(r"[A-Za-z]+", text)` devolve todas as palavras, parando cada
correspondência no primeiro caractere que não seja letra. É a função inteira.

---

import re


def find_words(text):
    return re.findall(r"[A-Za-z]+", text)
