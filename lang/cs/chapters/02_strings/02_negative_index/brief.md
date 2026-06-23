# 2.2 -- Záporné indexování

## Koncept

Můžeš také počítat od **konce** řetězce pomocí záporných indexů. `-1` je poslední
znak, `-2` předposlední a tak dále.

```
znak:        c   a   t
index:       0   1   2
od konce:   -3  -2  -1
```

```python
word = "cat"
print(word[-1])   # t
print(word[-2])   # a
```

To se hodí, když nechceš počítat délku: `s[-1]` je vždy poslední znak, ať je
řetězec jakkoli dlouhý.

## Příklad

```python
s = "python"
print(s[-1])   # n
```

## Tvůj úkol

Přečti slovo a pak vypiš jeho **poslední** znak.

Pro vstup `hello` je výstup:

```
o
```

## Hotovo, když

- Pro `hello` vypíše `o`.
- Funguje i pro jednopísmenné slovo (`-1` ukazuje na ten jeden znak).
