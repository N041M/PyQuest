# 2.1 -- Indexování

## Koncept

Řetězec je posloupnost znaků a každý znak má **pozici** (zvanou *index*). Počítá
se od **0**, ne od 1. Takže v řetězci `"cat"`:

```
znak:    c  a  t
index:   0  1  2
```

Jeden znak přečteš pomocí hranatých závorek: `s[index]`.

```python
word = "cat"
print(word[0])   # c
print(word[1])   # a
```

`word[0]` je první znak, protože indexování začíná od nuly. To zpočátku zaskočí
skoro každého: „první“ znak je na indexu 0.

## Příklad

```python
s = "python"
print(s[0])   # p
```

## Tvůj úkol

Přečti slovo pomocí `input()` a pak vypiš pouze jeho **první** znak.

Pro vstup `hello` je výstup:

```
h
```

## Hotovo, když

- Pro `hello` vypíše `h`.
- Funguje pro libovolné slovo, včetně jednopísmenného (kontrola jich zkouší
  několik).
