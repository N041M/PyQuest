# 11.2 -- from import: vytáhni jedno jméno

## Koncept

`import math` přinese *celý* modul a sáhneš do něj pomocí `math.něco`. Často chceš
jen jeden nástroj, používaný jeho prostým jménem. Tvar **`from ... import ...`** to
udělá:

```python
from math import gcd

gcd(12, 18)      # 6  -- called directly, no math. prefix
```

- `from math import gcd` naváže jediné jméno `gcd` do tvého souboru.
- Pak ho voláš jako `gcd(...)`, ne `math.gcd(...)`.
- Můžeš vytáhnout několik najednou: `from math import gcd, sqrt, pi`.

`gcd(a, b)` je **největší společný dělitel** -- největší celé číslo, které dělí obě.
Je to přesně to, co potřebuješ ke zkrácení zlomku na základní tvar: vyděl čitatele
a jmenovatele jejich gcd.

## Příklad

```python
from math import gcd

def both_divisible_by(a, b):
    return gcd(a, b)
```

## Tvůj úkol

Pomocí **`from math import gcd`** definuj `simplify(num, den)`, která vrátí zlomek
`num/den` zkrácený na základní tvar, jako n-tici `(top, bottom)`: vyděl `num` i
`den` jejich `gcd`.

## Hotovo, když

- `simplify(6, 8)` vrátí `(3, 4)`, `simplify(10, 5)` vrátí `(2, 1)`.
- `simplify(7, 7)` vrátí `(1, 1)`.
- gcd pochází z `math`, naimportované pomocí `from math import gcd`.
