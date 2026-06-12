Write clean first and get it passing in your head: .strip() then .lower(),
chained.

---

same_word is one line: compare clean(a) with clean(b) using == and return the
result -- a comparison already IS True or False.

---

def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
