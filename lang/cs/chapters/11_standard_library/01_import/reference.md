Příkaz **`import`** načte **modul** — soubor hotového kódu ze standardní knihovny —
a naváže ho na jméno. `import math` zpřístupní objekt modulu jako `math` a na jeho
obsah se sáhne skrz něj: `math.sqrt`, `math.pi`, `math.floor`.

- Příkaz proběhne **jednou**, obvykle **nahoře** v souboru; jméno pak odkazuje na
  celý modul po zbytek programu.
- **`modul.jméno`** (přístup k atributu) vyhledá funkci nebo konstantu *na* modulu,
  což drží jména každého modulu v jeho vlastním jmenném prostoru — `math.pi` a tvoje
  vlastní `pi` se nikdy nesrazí.
- Import jména, které neexistuje, vyvolá `ModuleNotFoundError`; kód modulu proběhne
  při prvním importu a poté se zacachuje.
- Standardní knihovna se dodává s Pythonem („baterie v ceně“), takže tyto moduly
  nepotřebují instalaci — jen import.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
math.floor(2.7)  # 2
```
