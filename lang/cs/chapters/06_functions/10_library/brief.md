# 6.10 -- Závěrečná: malá knihovna

## Koncept

Nic nového -- tato závěrečná úloha je kapitola v miniatuře: několik funkcí, každá s
jedním jasným úkolem, ty pozdější **delegují** na ty dřívější (6.8). Soubor
souvisejících funkcí jako tento je semenem každé skutečné *knihovny*, jakou kdy
naimportuješ.

Díly: `for ch in word` (3.10), `in` (5.1), nápad se sčítáním (5.9), f-řetězce
(2.10) a časné returny (6.5).

## Příklad

```python
count_vowels("tea")        # 2   ("e" and "a")
count_vowels("xyz")        # 0
describe("tea")            # "tea has 2 vowels"
describe("xyz")            # "xyz has no vowels"
```

## Tvůj úkol

Definuj **obě** funkce:

- `count_vowels(word)` -- vrátí, kolik znaků slova `word` je samohlásek (`a`, `e`,
  `i`, `o`, `u`; slova jsou malými písmeny).
- `describe(word)` -- vrátí řetězec `"<word> has <n> vowels"`, kromě případu, kdy
  je počet nula: pak je to `"<word> has no vowels"`. Musí **volat `count_vowels`**.

## Hotovo, když

- `count_vowels("tea")` je `2`; `count_vowels("xyz")` je `0`.
- `describe("tea")` je `"tea has 2 vowels"`; `describe("xyz")` je
  `"xyz has no vowels"`.
- `describe` deleguje na `count_vowels` -- checker hledá to volání.
