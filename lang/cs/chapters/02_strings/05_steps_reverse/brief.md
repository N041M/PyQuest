# 2.5 -- Kroky a obracení

## Koncept

Řez může mít třetí číslo, **krok**: `s[start:stop:step]`. Krok říká, o kolik pozic
se pokaždé posunout. Krok `2` vezme každý druhý znak:

```python
s = "abcdef"
print(s[::2])   # ace   (every 2nd character)
```

**Záporný** krok jde pozpátku. Zkratka `s[::-1]` -- prázdný start, prázdný stop,
krok `-1` -- obrátí celý řetězec:

```python
s = "python"
print(s[::-1])   # nohtyp
```

`s[::-1]` je standardní pythonovský způsob, jak obrátit řetězec.

## Příklad

```python
print("hello"[::-1])   # olleh
```

## Tvůj úkol

Přečti slovo a pak ho vypiš **obrácené**.

Pro vstup `hello` je výstup:

```
olleh
```

## Hotovo, když

- Pro `hello` vypíše `olleh`.
- Pro jediné písmeno nebo slovo, které se čte stejně pozpátku (jako `level`),
  vypíše slovo beze změny. Kontrola zkouší obojí.
