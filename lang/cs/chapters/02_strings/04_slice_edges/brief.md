# 2.4 -- Řez prostředku

## Koncept

Řez se v pohodě kombinuje se zápornými indexy a řezy nikdy nespadnou -- pokud je
řez prázdný, prostě dostaneš prázdný řetězec `""`.

`s[1:-1]` znamená „od indexu 1 až po poslední znak (ten už ne)“ -- jinými slovy
zahodit první a poslední znak:

```python
s = "python"
print(s[1:-1])   # ytho
```

Pokud je řetězec příliš krátký na to, aby měl prostředek, řez je prostě prázdný:

```python
print("ab"[1:-1])   # (nothing -- an empty string)
print("a"[1:-1])    # (nothing)
```

Žádná chyba. Prázdný řez je normální, platný výsledek.

## Častý omyl

Jít s řezem „mimo rozsah“ **nespadne**, na rozdíl od indexování jednoho znaku.
`"hi"[5]` by byla chyba, ale `"hi"[1:5]` je v pořádku -- prostě se zastaví na
konci.

## Příklad

```python
s = "hello"
print(s[1:-1])   # ell
```

## Tvůj úkol

Přečti slovo a pak ho vypiš **bez prvního a posledního znaku**.

Pro vstup `hello` je výstup:

```
ell
```

## Hotovo, když

- Pro `hello` vypíše `ell`.
- Pro 1- nebo 2písmenné slovo vypíše prázdný řádek (žádný prostředek) a nespadne.
  Kontrola zkouší `ab` a `a`.
