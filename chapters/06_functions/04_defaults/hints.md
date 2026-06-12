The default goes in the def line:  def greet(name, greeting="Hello"):

---

Build the result with an f-string: the greeting, then ", ", then the name,
then "!".

---

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
