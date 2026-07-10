Escreve primeiro clean e imagina-a a passar: .strip() depois .lower(),
encadeados.

---

same_word é uma linha: compara clean(a) com clean(b) usando == e devolve o
resultado -- uma comparação já É True ou False.

---

def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
