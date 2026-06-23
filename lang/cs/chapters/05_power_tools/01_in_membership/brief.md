# 5.1 -- in: testování příslušnosti

## Koncept

S `in` ses setkal u množin (4.11). Ve skutečnosti funguje skoro na všem:

```python
"e" in "hello"        # True   (substring of a string)
3 in [1, 2, 3]        # True   (item of a list)
"sam" in {"sam": 20}  # True   (KEY of a dict)
```

`x in s` je výraz, který dá **boolean** (`True`/`False`), takže ho zasadíš rovnou
do `if`:

```python
if "@" in address:
    print("looks like an email")
```

Existuje i opak, `not in`:

```python
if "x" not in word:
    print("no x here")
```

Srovnej to s kapitolou 2, kde jsi použil `s.find()` a kontroloval `-1`. `in` říká
totéž prostou řečí -- dej mu přednost, kdykoli potřebuješ jen *zda* tam něco je, ne
*kde*.

## Příklad

```python
word = "banana"
print("n" in word)     # True
print("z" in word)     # False
```

## Tvůj úkol

Přečti slovo, pak jediné písmeno. Vypiš `yes`, pokud se písmeno ve slově vyskytuje,
a `no`, pokud ne.

Pro vstup `banana`, pak `n`:

```
yes
```

## Hotovo, když

- Písmeno, které se vyskytuje, vypíše `yes`; to, které ne, vypíše `no`.
- Funguje i pro jednopísmenné slovo.
- Použil jsi operátor `in` (ne `.find()` ani `.count()`).
