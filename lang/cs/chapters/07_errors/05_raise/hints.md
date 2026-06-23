Nejprve stráž, pak return: je-li věk záporný, vyvolej chybu; jinak je v pořádku
tak, jak je.

---

Stráž jsou dva řádky:  if age < 0:  pak
raise ValueError("age cannot be negative").

---

def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
