Nejprve přečti všechny řádky, pak otevři výstupní soubor v režimu `"w"` a procházej,
přičemž zapisuj jen ty, které chceš ponechat.

---

`if line.strip():` je pravda jen tehdy, když má řádek skutečný obsah. Zapiš původní
`line` (už končí na `\n`), ne oříznutou kopii.

---

with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)
