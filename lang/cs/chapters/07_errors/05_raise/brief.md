# 7.5 -- raise: chyby jsou taky tvoje

## Koncept

Dosud jsi *chytal* chyby, které vyvolal Python. Můžeš také **vyvolat vlastní** -- a
dobré funkce to dělají, ve chvíli, kdy dostanou něco nesmyslného:

```python
def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

`raise` chybu vytvoří a hned ji vyhodí: funkce se zastaví a volající dostane stejné
zacházení, jaké mu dá `int("nope")` -- chytatelné pomocí `try`, hlasité, když se
ignoruje.

Proč vyvolat chybu místo vrácení něčeho jako `None` nebo `-1`? Protože špatná
hodnota putuje: uloží se, přičte, vypíše, a pád (pokud nějaký) nastane daleko od
skutečné chyby. Raise připne selhání k okamžiku a ke zprávě --
`ValueError("age cannot be negative")` říká přesně, co se pokazilo a kde. Smetí
dovnitř, **chyba** ven -- nikdy smetí ven.

## Příklad

```python
checked_age(30)     # 30
checked_age(0)      # 0    -- zero is a fine age
checked_age(-1)     # ValueError: age cannot be negative
```

## Tvůj úkol

Definuj `checked_age(age)`, která vrátí věk beze změny -- ale vyvolá `ValueError`,
když je záporný. Dej mu zprávu říkající, co je špatně.

## Hotovo, když

- `checked_age(30)` vrátí `30`; `checked_age(0)` vrátí `0`.
- `checked_age(-1)` vyvolá `ValueError`.
- Použil jsi `raise` -- checker hledá samotný příkaz.
