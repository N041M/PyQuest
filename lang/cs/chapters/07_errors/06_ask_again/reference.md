**Opakovací cyklus** se ptá, dokud nezíská platnou hodnotu. Spojuje `while True` s
`try` / `except`: uspěj a `break` ven; selhej a obtoč se, abys se zeptal znovu.

- `try` zkusí parsování/operaci; úspěšná cesta končí `break`, který opustí cyklus.
- `except` ošetří špatný vstup (často jen vypíše nápovědu a propadne dál), takže
  `while True` proběhne další kolo.
- `while True` bez jiného východu spoléhá na ten `break` — platný případ je jediná
  cesta ven.

```python
while True:
    try:
        n = int(input("number: "))
        break                 # valid -> leave the loop
    except ValueError:
        print("not a number, try again")
```
