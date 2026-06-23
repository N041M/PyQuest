Nejprve zodpověz nejmenší případ: pokud je n 0, vrať 1 -- žádné volání není
potřeba.

---

Pro vše ostatní důvěřuj funkci, kterou píšeš:
return n * fact(n - 1). Časný return (6.5) udrží základní případ čistý.

---

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
