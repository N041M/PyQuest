find ti řekne, kde je „=“. Pak udělej řez od pozice hned za ním.

---

i = s.find("=") dá pozici; s[i+1:] je vše za ním.

---

s = input()
i = s.find("=")
print(s[i+1:])
