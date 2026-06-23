# 3.12 -- Vzor akumulátoru

## Koncept

Velmi častý vzor cyklu: drž v proměnné **průběžný součet**, začni na `0` a v každém
průchodu k němu přičítej. Proměnná výsledek „akumuluje“.

```python
total = 0
for n in [4, 2, 9]:
    total = total + n
print(total)        # 15
```

Klíčové kroky jsou: **začni na 0 před cyklem**, **přičítej uvnitř cyklu**, **použij
výsledek po cyklu**. Stejný tvar funguje pro počítání (začni na 0, pokaždé přičti
1) nebo stavění řetězce (začni na "", pokaždé přidej kousek).

Tato úloha kombinuje, co ses naučil: cyklus `for`, `range`, čtení vstupu a
akumulátor.

## Příklad

```python
total = 0
for _ in range(3):
    total = total + int(input())
print(total)
```

(`_` je normální jméno proměnné, často používané, když nepotřebuješ hodnotu
cyklu.)

## Tvůj úkol

Přečti celé číslo `n` (počet). Pak přečti dalších `n` celých čísel, jedno na řádek,
a vypiš jejich **součet**.

Pro vstup `3`, pak `10`, `20`, `5` je výstup:

```
35
```

## Hotovo, když

- Počet `3` s `10, 20, 5` vypíše `35`.
- Počet `0` nečte žádná další čísla a vypíše `0`.
- Čísla mohou být záporná.
