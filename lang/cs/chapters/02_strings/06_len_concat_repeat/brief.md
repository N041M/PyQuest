# 2.6 -- Délka, spojování, opakování

## Koncept

Tři každodenní nástroje pro řetězce:

- `len(s)` dá **počet znaků** v `s` (číslo):
  ```python
  len("cat")    # 3
  ```
- `+` spojí dva řetězce (potkal jsi to v kapitole 1):
  ```python
  "cat" + "!"   # "cat!"
  ```
- `*` s číslem řetězec **opakuje**:
  ```python
  "ab" * 3      # "ababab"
  "-" * 5       # "-----"
  ```

`len` vrací číslo, takže s ním můžeš počítat. `+` a `*` staví nové řetězce.

## Příklad

```python
s = "hi"
print(len(s))    # 2
print(s + "!")   # hi!
print(s * 3)     # hihihi
```

## Tvůj úkol

Přečti slovo a vypiš tři řádky:

1. počet znaků ve slově
2. slovo s vykřičníkem přidaným na konec
3. slovo zopakované třikrát

Pro vstup `hi` je výstup:

```
2
hi!
hihihi
```

## Hotovo, když

- Pro `hi` jsou tři řádky `2`, `hi!`, `hihihi`.
- Funguje to i pro prázdný vstup: `0`, `!` a prázdný řádek. Kontrola to zkouší.
