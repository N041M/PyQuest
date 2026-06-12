find tells you where the "=" is. Then slice from just after it.

---

i = s.find("=") gives the position; s[i+1:] is everything after it.

---

s = input()
i = s.find("=")
print(s[i+1:])
