# 14.1 -- lambda: funkce ve výrazu

## Koncept

**`lambda`** je drobná funkce psaná inline, bez jména a bez `def`:

```python
double = lambda x: x * 2
double(5)      # 10
```

- `lambda args: expression` -- hodnota výrazu se vrátí automaticky (žádné `return`
  a povolen je jen jeden výraz).
- lambda je **hodnota**, takže ji můžeš uložit, **vrátit** z jiné funkce nebo předat
  jako argument (kde si opravdu vydělá na živobytí -- zbytek této kapitoly).

Protože je lambda definovaná uvnitř jiné funkce, může **uzavřít** (close over)
proměnné té funkce. `lambda x: x * n` si pamatuje `n` odtud, kde byla vytvořena.

(Na cokoli delšího než jeden výraz použij normální `def` -- lambdy jsou pro malé
inline funkce.)

## Příklad

```python
def adder(n):
    return lambda x: x + n     # remembers n
```

## Tvůj úkol

Definuj `multiplier(n)`, která **vrátí lambdu**, jež násobí svůj argument číslem
`n`. Takže `multiplier(3)` vrátí funkci a zavolání té funkce se `4` dá `12`.

## Hotovo, když

- `multiplier(3)(4)` je `12`; `multiplier(10)(5)` je `50`.
- `multiplier(0)(7)` je `0`.
- Vrácená funkce je `lambda`, ne vnořený `def`.
