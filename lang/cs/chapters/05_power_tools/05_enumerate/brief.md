# 5.5 -- enumerate()

## Koncept

Někdy cyklus potřebuje **položku** i její **pozici**. Mohl bys sledovat počítadlo
ručně, ale Python má přesně na tohle vestavěnou funkci:

```python
words = ["tea", "milk"]
for i, w in enumerate(words):
    print(i, w)
# 0 tea
# 1 milk
```

Při každém průchodu ti `enumerate` podá dvojici `(pozice, položka)`, kterou
rozbalíš do dvou proměnných (4.7) -- stejný trik jako `for k, v in d.items()`.

Počítat od `0` je zřídka to, co chceš člověku *ukázat*. Druhý argument nastaví
počáteční číslo:

```python
for i, w in enumerate(words, 1):
    print(i, w)
# 1 tea
# 2 milk
```

## Příklad

```python
for i, ch in enumerate("hi", 1):
    print(f"{i}. {ch}")
# 1. h
# 2. i
```

## Tvůj úkol

Přečti počet `n`, pak `n` slov. Vypiš je jako číslovaný seznam začínající od 1, ve
formátu `1. word` (tečka a mezera za číslem).

Pro vstup `3`, pak `tea`, `milk`, `sugar`:

```
1. tea
2. milk
3. sugar
```

## Hotovo, když

- Tři slova se vypíšou jako `1. ...`, `2. ...`, `3. ...`.
- Počet `0` nevypíše nic.
- Použil jsi `enumerate()` -- žádné ručně držené počítadlo.
