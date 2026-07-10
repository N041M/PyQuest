O valor por omissão vai na linha do def:  def greet(name, greeting="Hello"):

---

Constrói o resultado com uma f-string: o cumprimento, depois ", ", depois o nome,
depois "!".

---

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
