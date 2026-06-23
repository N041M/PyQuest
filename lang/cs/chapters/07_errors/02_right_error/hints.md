return int(text) uvnitř try; except místo toho vrátí None.

---

Pojmenuj chybu: `except ValueError:` -- nepojmenovat nic (nebo Exception) chytí i
TypeError, který checker posílá, a ten musí uniknout.

---

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
