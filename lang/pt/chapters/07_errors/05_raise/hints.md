Protege primeiro, devolve depois: se a idade for negativa, levanta a
exceção; caso contrário está bem como está.

---

A proteção são duas linhas: if age < 0: e depois
raise ValueError("age cannot be negative").

---

def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
