Nejprve napiš clean a v hlavě si ho odlaď: .strip() pak .lower(), zřetězené.

---

same_word je jeden řádek: porovnej clean(a) s clean(b) pomocí == a vrať výsledek
-- porovnání už SAMO je True nebo False.

---

def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
