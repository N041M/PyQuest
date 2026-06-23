# 3.10 -- Procházení řetězce

## Koncept

Cyklus `for` nefunguje jen na rozsazích. **Řetězec je posloupnost znaků**, takže ho
můžeš procházet přímo -- jeden znak na průchod:

```python
for ch in "cat":
    print(ch)
# prints:
# c
# a
# t
```

Žádné indexování není potřeba: `ch` je postupně každý znak. (Takto můžeš procházet
mnoho druhů posloupností; řetězce jsou první.)

## Příklad

```python
word = "hi"
for ch in word:
    print(ch)
# prints h then i
```

## Tvůj úkol

Přečti slovo a vypiš každý jeho znak na vlastním řádku pomocí cyklu `for` přes
řetězec.

Pro vstup `cat` je výstup:

```
c
a
t
```

## Hotovo, když

- `cat` vypíše `c`, `a`, `t` na samostatných řádcích.
- Jediné písmeno vypíše to písmeno; prázdný vstup nevypíše nic.
