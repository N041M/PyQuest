# 8.6 -- Filtrování řádků do nového souboru

## Koncept

Spoj čtení a zápis a dostaneš každodenní datovou rutinu: projdi vstupní soubor řádek
po řádku, **rozhodni**, které řádky ponechat (`if`, 3.2), a zapiš jen ty do
výstupního souboru.

```python
with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if keep(line):
            f.write(line)
```

`f.readlines()` přečte celý soubor do seznamu řádků předem -- hodí se, když chceš
dočíst, než začneš zapisovat.

Řádek, který je prázdný nebo jen mezery, je „prázdný“: `line.strip()` pro něj vrátí
`""`, a prázdný řetězec je nepravdivý (3.1), takže `if line.strip():` je úhledný
test na „tento řádek má skutečný obsah“.

## Příklad

Z `lines.txt` ve tvaru:

```
keep me

and me
```

se prázdný prostřední řádek zahodí a zůstanou `keep me` a `and me`.

## Tvůj úkol

Přečti `lines.txt` a zapiš jen jeho **neprázdné** řádky do `kept.txt`, ve stejném
pořadí. Zahoď každý řádek, který je prázdný nebo jen bílé znaky.

## Hotovo, když

- `kept.txt` drží přesně neprázdné řádky z `lines.txt`, v pořadí.
- Soubor bez prázdných řádků se zkopíruje beze změny; soubor jen z prázdných řádků
  dá prázdný `kept.txt`.
- Použil jsi `with`, cyklus a `if`, abys rozhodl, co ponechat.
