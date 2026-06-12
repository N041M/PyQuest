An f-string starts with f" and inserts values inside { }.

---

You can put an expression in the braces: f"{w} reversed is {w[::-1]}".

---

w = input()
print(f"{w} reversed is {w[::-1]}")
