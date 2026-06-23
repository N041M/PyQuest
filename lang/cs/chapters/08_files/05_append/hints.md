Přečti záznam pomocí `input()`, pak otevři soubor v režimu, který *zachová* to, co
už tam je.

---

Režim `"a"` připojuje místo mazání. Nezapomeň na `"\n"`, aby nový záznam seděl na
vlastním řádku.

---

entry = input()
with open("log.txt", "a") as f:
    f.write(entry + "\n")
