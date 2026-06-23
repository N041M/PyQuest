# 11.4 -- random: reprodukovatelná náhoda

## Koncept

Modul **`random`** produkuje pseudonáhodné hodnoty: `random.randint(1, 6)` hodí
kostkou, `random.shuffle(lst)` přeuspořádá seznam na místě. Jsou *pseudo*náhodné --
počítané z vnitřního stavu -- což znamená, že je můžeš udělat **opakovatelnými** tím,
že ten stav zafixuješ **semínkem** (seed):

```python
import random

random.seed(42)
random.shuffle(deck)     # always the same order for seed 42
```

- `random.seed(n)` nastaví výchozí bod. Po stejném semínku stejná volání vyprodukují
  stejné výsledky, při každém spuštění, na každém stroji.
- `random.shuffle(lst)` zamíchá **na místě** (vrací `None`), takže zamíchej kopii,
  pokud potřebuješ zachovat originál.

Semínkování je způsob, jak hra přehraje úroveň nebo jak test zkontroluje „náhodný“
kód.

## Příklad

```python
import random

def pick(options, seed):
    random.seed(seed)
    return random.choice(options)
```

## Tvůj úkol

Definuj `shuffled(items, seed)`, která vrátí **nový** seznam s položkami `items`
zamíchanými, opakovatelný díky semínkování `seed` **před** mícháním. Neměň původní
`items`.

## Hotovo, když

- `shuffled(items, seed)` dá pokaždé stejný výsledek pro stejné `items` a `seed`.
- Předaný původní seznam zůstane beze změny (zamíchej kopii).
- `shuffled([], 1)` vrátí `[]`.
