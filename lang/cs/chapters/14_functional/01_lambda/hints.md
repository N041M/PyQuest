lambda je `lambda args: expression`. Chceš takovou, která bere `x` a vrací `x * n`.

---

`multiplier` tu lambdu vrátí. lambda uzavře `n`, takže každé volání `multiplier`
vytvoří funkci svázanou s vlastním `n`.

---

def multiplier(n):
    return lambda x: x * n
