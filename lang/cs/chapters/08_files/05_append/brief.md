# 8.5 -- Připojuj, nepřepisuj

## Koncept

Režim `"w"` je nemilosrdný: před zápisem soubor **vyprázdní**. To je špatně, když
chceš do souboru *přidávat* -- třeba log, který stále rozšiřuješ. Na to existuje
režim `"a"` (pro *append*, připojení):

```python
with open("log.txt", "a") as f:
    f.write("another line\n")
```

`"a"` nechá vše, co už v souboru je, nedotčené a tvůj nový text zapíše **za** něj (a
pokud soubor ještě neexistuje, `"a"` ho prostě vytvoří). Stejné `.write()`, stejná
potřeba přidat vlastní `"\n"` -- mění se jen písmeno režimu, a to jedno písmeno je
celý rozdíl mezi „přidat k“ a „smazat a nahradit“. Celý smysl `"a"` je, že soubor
*nečteš* nejdřív -- prostě zapisuješ na konec.

## Příklad

Pokud `log.txt` už obsahuje:

```
woke up
ate
```

pak připojení řádku `ran` ho nechá držet `woke up`, `ate`, `ran` -- všechny tři, v
pořadí.

## Tvůj úkol

Soubor `log.txt` už existuje. Přečti jeden řádek textu ze vstupu (`input()`) a
**připoj** ho do `log.txt` jako nový řádek, přičemž zachovej vše, co tam už je.

## Hotovo, když

- Původní obsah `log.txt` je stále přítomen, v pořadí.
- Nový záznam je přidán jako vlastní řádek na konci.
- Použití `"w"` by smazalo staré řádky -- takže musíš použít `"a"`.
