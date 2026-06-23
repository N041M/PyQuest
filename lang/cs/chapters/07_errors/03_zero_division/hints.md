Zkus dělení uvnitř try -- netestuj b napřed.

---

`except ZeroDivisionError: return None` -- časný return (6.5) uvnitř try ošetří
šťastnou cestu.

---

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
