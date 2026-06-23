Tvar **`from modul import jméno`** naváže konkrétní jméno z modulu *přímo* do tvého
souboru, takže se volá bez předpony modulu. `from math import gcd` udělá z `gcd`
prosté jméno; píšeš `gcd(12, 18)`, ne `math.gcd(...)`.

- Několik jmen najednou: `from math import gcd, sqrt, pi`.
- Importuje jen to, co pojmenuješ — `math.floor` **není** dostupné, pokud
  neimportuješ i `floor`. (`import math` přinese vše, ale ponechá předponu; oba
  tvary vyměňují pohodlí za přehlednost jmenného prostoru.)
- Celý modul stále proběhne a zacachuje se; jen sis vybral, která jeho jména
  dopadnou do tvého jmenného prostoru. Protože jméno přijde holé, může **zastínit**
  jedno z tvých vlastních — `from math import e` by skrylo proměnnou jménem `e`.

```python
from math import gcd, sqrt

gcd(12, 18)    # 6
sqrt(16)       # 4.0
```
