# 3.2 -- if

## Koncept

**Příkaz `if`** spustí blok kódu **jen když** je podmínka `True`:

```python
if condition:
    do_something()
    do_more()
```

Všimni si dvou věcí:

1. Řádek končí **dvojtečkou** `:`.
2. Řádky, které se mají spustit, když je podmínka pravdivá, jsou **odsazené**
   (použij 4 mezery). Podle odsazení Python pozná, které řádky patří k `if`. Když
   je podmínka `False`, odsazené řádky se přeskočí.

```python
age = 20
if age >= 18:
    print("adult")     # runs only when age >= 18
```

Kdyby `age` bylo `15`, nic by se nevypsalo.

## Častý omyl

Odsazení není v Pythonu dekorace -- definuje blok. Zapomenout odsadit (nebo míchat
mezery) je syntaktická chyba.

## Tvůj úkol

Přečti celé číslo. **Pokud je záporné**, vypiš `negative`. Pokud záporné není,
nevypisuj vůbec nic.

Pro vstup `-4` je výstup:

```
negative
```

Pro vstup `7` není žádný výstup.

## Hotovo, když

- Záporné číslo vypíše `negative`.
- Nula a kladná čísla nevypíšou nic (`0` není záporná).
