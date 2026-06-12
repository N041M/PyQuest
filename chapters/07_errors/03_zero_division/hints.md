Attempt the division inside try -- don't test b first.

---

`except ZeroDivisionError: return None` -- the early return (6.5) inside try
handles the happy path.

---

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
