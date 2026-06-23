`int` převede hodnotu na **celé číslo**. Nejčastěji se používá k převodu
**řetězce**, který vrací `input()`, na číslo, se kterým můžeš počítat.

- `int("42")` je `42`. Okolní mezery se ignorují (`int(" 42 ")` funguje); úvodní
  znaménko je povoleno (`int("-5")`).
- Text, který není celé číslo, vyvolá `ValueError` — `int("3.5")` i `int("ten")`
  selžou. Pro desetinná čísla použij `float("3.5")`.
- Zavolané na `float` `int` ořeže *směrem k nule* (`int(3.9)` je `3`, `int(-3.9)`
  je `-3`).

Protože `input()` vždy vrací text, čtení čísla je dvoukrokový idiom:

```python
n = int(input("How many? "))   # read text, then parse it to an int
print(n * 2)
```
