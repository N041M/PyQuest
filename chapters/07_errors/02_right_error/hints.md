return int(text) inside the try; the except returns None instead.

---

Name the error: `except ValueError:` -- naming nothing (or Exception) also
catches the TypeError the checker sends, and that must escape.

---

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
