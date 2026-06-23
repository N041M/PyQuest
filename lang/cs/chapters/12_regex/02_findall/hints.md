`import re`, pak `re.findall(pattern, text)` vrátí seznam každé shody. Chceš úseky
číslic.

---

Vzor `r"\d+"` odpovídá jedné nebo více číslicím v řadě, takže každá shoda je celé
číslo. `re.findall(r"\d+", text)` je celá odpověď.

---

import re


def all_numbers(text):
    return re.findall(r"\d+", text)
