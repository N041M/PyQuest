# 2.3 -- Řezy (slicing)

## Koncept

**Řez** (slice) vezme rozsah znaků najednou: `s[start:stop]`. Zahrne znak na pozici
`start` a jde **až po `stop`, ale ten nezahrnuje**. Tomu se říká *polootevřený*:
koncový index není součástí.

```python
s = "python"
print(s[0:3])   # pyt   (indexes 0, 1, 2 -- not 3)
print(s[2:5])   # tho   (indexes 2, 3, 4)
```

Vynech `start` a začne od 0; vynech `stop` a poběží až do konce:

```python
print(s[:3])    # pyt   (same as s[0:3])
print(s[3:])    # hon   (from index 3 to the end)
```

Protože `stop` není zahrnut, `s[0:3]` ti dá přesně **3** znaky.

## Příklad

```python
s = "rainbow"
print(s[0:4])   # rain
```

## Tvůj úkol

Přečti slovo a pak vypiš jeho **první tři** znaky.

Pro vstup `hello` je výstup:

```
hel
```

## Hotovo, když

- Pro `hello` vypíše `hel`.
- Pro slovo kratší než tři písmena vypíše celé slovo -- řez za konec je bezpečný a
  nechybuje. Kontrola zkouší `hi`.
