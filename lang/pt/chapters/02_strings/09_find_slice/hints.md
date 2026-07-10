find diz-te onde está o "=". Depois fatia a partir de logo a seguir.

---

i = s.find("=") dá a posição; s[i+1:] é tudo o que vem depois dela.

---

s = input()
i = s.find("=")
print(s[i+1:])
