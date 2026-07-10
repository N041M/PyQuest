return int(text) dentro do try; o except devolve None em vez disso.

---

Nomeia o erro: `except ValueError:` -- não nomear nada (ou Exception) também
apanha o TypeError que o verificador envia, e esse tem de escapar.

---

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
