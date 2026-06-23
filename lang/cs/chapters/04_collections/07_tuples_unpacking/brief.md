# 4.7 -- N-tice a rozbalování

## Koncept

**N-tice** (tuple) je jako seznam, ale **neměnná** -- jakmile je vytvořena, nelze
ji změnit. Zapíšeš ji závorkami (nebo jen čárkami):

```python
point = (3, 7)
print(point[0])    # 3
```

**Rozbalování** (unpacking) přiřadí několik proměnných najednou z n-tice (nebo
seznamu):

```python
x, y = point       # x = 3, y = 7
```

Jména vlevo odpovídají položkám vpravo, v pořadí. Pěkný trik, který to umožňuje, je
**prohození** dvou proměnných bez pomocné:

```python
a, b = 1, 2
a, b = b, a        # now a = 2, b = 1
```

Pravá strana `b, a` sestaví n-tici, která se pak rozbalí do `a, b`.

## Příklad

```python
a, b = 10, 20
a, b = b, a
print(a)    # 20
print(b)    # 10
```

## Tvůj úkol

Přečti dvě celá čísla (každé na vlastním řádku). **Prohoď** je pomocí rozbalování
n-tice, pak vypiš první, pak druhé.

Pro vstup `3` a pak `7`:

```
7
3
```

## Hotovo, když

- `3, 7` vypíše `7` pak `3`.
- Funguje pro libovolná dvě čísla (včetně dvou stejných).
