**f-řetězec** (formátovaný řetězcový literál) je řetězec s předponou `f`, v němž
`{ }` obsahuje pythonovský **výraz**; výraz se vyhodnotí a jeho hodnota se vloží,
převedená na text.

- Do složených závorek se vejde libovolný výraz: `f"{name}"`, `f"{a + b}"`,
  `f"{nums[0]}"`.
- Doslovnou složenou závorku napíšeš jejím zdvojením: `f"{{literal}}"` zobrazí
  `{literal}`.
- Formátovací předpis za dvojtečkou řídí zobrazení, např. `f"{price:.2f}"`
  zobrazí dvě desetinná místa a `f"{n:>5}"` zarovná vpravo do pole širokého 5.

f-řetězce jsou nejpřehlednější způsob, jak sestavit text z hodnot, a nahrazují
řetězce `+` a `str()`.

```python
name, n = "Ada", 3
f"{name} solved {n} puzzles"   # 'Ada solved 3 puzzles'
f"{1/3:.2f}"                    # '0.33'
```
