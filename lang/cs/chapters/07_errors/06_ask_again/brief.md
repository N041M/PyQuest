# 7.6 -- Zeptej se znovu: opakovací cyklus

## Koncept

Klasické použití `try`/`except` ve skutečném programu: **ptej se, dokud vstup
nedává smysl.** Spoj cyklus `while True` (3.7), `break` (3.11) a `except` ze 7.1:

```python
while True:
    try:
        n = int(input())
        break              # got a good one -- leave the loop
    except ValueError:
        pass               # bad line -- silently go around again
```

Tvar k zvnitřnění:

- **šťastná cesta** končí `break`;
- **except** pohltí selhání a nechá cyklus zkusit znovu;
- po cyklu je `n` zaručeně platné -- kód níže mu může důvěřovat.

(`pass` je pythonovský příkaz „nedělej nic“ -- blok except musí obsahovat *něco*.)

## Příklad

Pro vstupní řádky `cat`, `dog`, `21` program první dva ignoruje a vypíše `42`.

## Tvůj úkol

Čti řádky, dokud se jeden nepřevede na celé číslo, pak vypiš to číslo
**zdvojnásobené**. Špatné řádky nevyprodukují žádný výstup.

## Hotovo, když

- `21` jako první řádek vypíše `42`.
- `cat`, `dog`, `21` také vypíše jen `42` -- smetí se tiše zkusí znovu.
- Záporná čísla fungují.
- Použil jsi cyklus a `try`/`except`.
