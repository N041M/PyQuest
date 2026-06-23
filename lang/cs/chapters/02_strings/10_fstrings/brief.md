# 2.10 -- f-řetězce

## Koncept

**f-řetězec** ti umožní vložit hodnoty přímo do textu. Dej `f` před úvodní uvozovku
a pak napiš `{...}` všude, kam má přijít hodnota:

```python
name = "Sam"
print(f"Hello, {name}!")     # Hello, Sam!
```

Do `{}` můžeš vložit libovolný výraz, ne jen prostou proměnnou -- vyhodnotí se a
jeho výsledek se vloží do textu:

```python
word = "cat"
print(f"{word} has {len(word)} letters")    # cat has 3 letters
print(f"{word} reversed is {word[::-1]}")   # cat reversed is tac
```

f-řetězce jsou nejpřehlednější způsob, jak sestavit text z hodnot -- mnohem
úhlednější než spojování kousků pomocí `+`.

## Příklad

```python
s = "python"
print(f"{s} reversed is {s[::-1]}")   # python reversed is nohtyp
```

## Tvůj úkol

Přečti slovo a pak pomocí f-řetězce vypiš přesně tuto větu:

```
WORD reversed is REVERSED
```

kde `WORD` je vstup a `REVERSED` je pozpátku. Pro vstup `hello`:

```
hello reversed is olleh
```

## Hotovo, když

- Pro `hello` vypíše `hello reversed is olleh`.
- Funguje pro libovolné slovo, včetně jednoho písmene. Kontrola jich zkouší
  několik.
