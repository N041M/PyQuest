Nejprve rozhodni kladné vs. ne. Jen pokud je kladné, ptáš se na malé vs. velké.

---

Vnější: `if n > 0:` ... `else: print("non-positive")`. Uvnitř if další if/else
porovnávající n se 100.

---

n = int(input())
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
