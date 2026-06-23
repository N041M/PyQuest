`sep` a `end` jsou pouze klíčové argumenty (keyword-only), které řídí mezerování
kolem výstupu `print`.

- **`sep`** je řetězec vkládaný mezi každou dvojici sousedních hodnot. Výchozí je
  `" "`. Nikdy se neobjeví před první hodnotou ani za poslední, takže *N* hodnot
  vytvoří *N − 1* oddělovačů.
- **`end`** je řetězec zapsaný jednou za poslední hodnotou. Výchozí je `"\n"`,
  proto každý `print` ukončí svůj řádek. Nastav `end=""`, aby kurzor zůstal na
  stejném řádku a další `print` na něj navázal.

```python
print("2024", "01", "15", sep="-")   # 2024-01-15
print("loading", end="")
print("...")                          # loading... (one line)
```
