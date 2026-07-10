Tenta a divisão dentro do try -- não testes b primeiro.

---

`except ZeroDivisionError: return None` -- o return antecipado (6.5) dentro
do try trata do caminho feliz.

---

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
