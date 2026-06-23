# PyQuest translations -- language 'cs' -- chapter 11_standard_library -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"11.1 brief": r"""# 11.1 -- import: přines modul

## Koncept

Python dodává rozsáhlou **standardní knihovnu**: hotové nástroje seskupené do
**modulů**. Nedostaneš je zadarmo v každém souboru -- modul, který potřebuješ,
**naimportuješ**, pak sáhneš na jeho obsah skrz jeho jméno.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
```

- `import math` proběhne jednou nahoře v souboru a naváže jméno `math` na celý
  modul.
- Poté `math.sqrt` je funkce odmocniny a `math.pi` konstanta -- `modul.jméno` sáhne
  na cokoli, co modul poskytuje.

Smysl importování je, že tohle už někdo napsal a otestoval, takže zavoláš
`math.sqrt` místo toho, abys znovu odvozoval odmocninu sám.

## Příklad

```python
import math

def diagonal(side):
    return math.sqrt(2) * side
```

## Tvůj úkol

Definuj `hypotenuse(a, b)`, která vrátí délku přepony pravoúhlého trojúhelníku s
odvěsnami `a` a `b` -- odmocninu z `a*a + b*b` -- pomocí **`math.sqrt`** z
naimportovaného modulu `math`.

## Hotovo, když

- `hypotenuse(3, 4)` vrátí `5.0`, `hypotenuse(5, 12)` vrátí `13.0`.
- `hypotenuse(0, 0)` vrátí `0.0`.
- Odmocnina pochází z `math.sqrt`, přes `import math`.
""",

"11.1 hints": r"""Úplně první řádek souboru zpřístupní modul: `import math`. Poté můžeš použít
cokoli, co poskytuje, jako `math.něco`.

---

`math.sqrt(x)` vrátí odmocninu z `x`. Chceš odmocninu z `a*a + b*b`. Dej `import
math` nahoru, pak napiš funkci.

---

import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)
""",

"11.1 reference": r"""Příkaz **`import`** načte **modul** — soubor hotového kódu ze standardní knihovny —
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
""",

"11.2 brief": r"""# 11.2 -- from import: vytáhni jedno jméno

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
""",

"11.2 hints": r"""Začni soubor s `from math import gcd`. Teď je `gcd` funkce, kterou můžeš volat
přímo, bez `math.` před ní.

---

Najdi `g = gcd(num, den)`, pak vrať n-tici `(num // g, den // g)`. Použij `//`
(celočíselné dělení), aby výsledek zůstal celými čísly.

---

from math import gcd


def simplify(num, den):
    g = gcd(num, den)
    return (num // g, den // g)
""",

"11.2 reference": r"""Tvar **`from modul import jméno`** naváže konkrétní jméno z modulu *přímo* do tvého
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
""",

"11.3 brief": r"""# 11.3 -- import as: přejmenuj při vstupu

## Koncept

Někdy je jméno modulu dlouhé, nebo se sráží s jedním z tvých. **`import ... as
...`** přinese modul pod jménem, které si **ty** zvolíš:

```python
import statistics as stats

stats.mean([1, 2, 3, 4])    # 2.5
```

- `import statistics as stats` naváže modul na `stats`; `stats.mean` je přesně
  `statistics.mean`.
- Alias je jen lokální přezdívka -- modul je beze změny a nové jméno vidí jen tvůj
  soubor.
- Proto všude uvidíš zaběhlé aliasy (`import numpy as np`); tady zkracujeme
  `statistics`.

Modul **`statistics`** za tebe dělá běžné průměry. `stats.mean(nums)` je
aritmetický průměr -- součet dělený počtem -- aniž bys psal `sum(nums) / len(nums)`.

## Příklad

```python
import statistics as stats

def midpoint(nums):
    return stats.median(nums)
```

## Tvůj úkol

Pomocí **`import statistics as stats`** definuj `average(nums)`, která vrátí průměr
seznamu `nums`, spočítaný pomocí `stats.mean`.

## Hotovo, když

- `average([2, 4, 6])` vrátí `4`, `average([1, 2])` vrátí `1.5`.
- `average([5])` vrátí `5`.
- Průměr pochází z `statistics.mean`, naimportované jako `stats`.
""",

"11.3 hints": r"""Začni s `import statistics as stats`. Od té chvíle je `stats` tvoje jméno pro
modul.

---

`stats.mean(nums)` vrátí průměr seznamu. Celá tvá funkce může být jeden řádek,
který ho vrátí.

---

import statistics as stats


def average(nums):
    return stats.mean(nums)
""",

"11.3 reference": r"""**`import modul as alias`** naimportuje modul, ale naváže ho pod jménem dle tvé
volby. `import statistics as stats` zpřístupní modul jako `stats`; `stats.mean` *je*
`statistics.mean` — alias mění jen lokální jméno, ne modul.

- Použij ho ke **zkrácení** dlouhého jména modulu nebo k **vyhnutí se srážce** s
  jedním z tvých vlastních jmen. Konvencí dané aliasy, které potkáš (`import numpy
  as np`), jsou přesně tohle.
- Stejné `as` funguje na jediném jméně z from-importu: `from statistics import mean
  as avg`.
- Alias vidí jen tvůj soubor; ostatní moduly si pro něj drží vlastní jména.

```python
import statistics as stats

stats.mean([1, 2, 3, 4])     # 2.5
stats.median([1, 5, 2])      # 2
```
""",

"11.4 brief": r"""# 11.4 -- random: reprodukovatelná náhoda

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
""",

"11.4 hints": r"""Potřebuješ tři kroky: zkopíruj seznam, semínkuj generátor, zamíchej kopii.
`out = list(items)` udělá kopii, aby byl originál v bezpečí.

---

`random.seed(seed)` zafixuje výchozí bod; `random.shuffle(out)` přeuspořádá `out`
na místě (vrací None, takže nepiš `return random.shuffle(...)`). Poté vrať `out`.

---

import random


def shuffled(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out
""",

"11.4 reference": r"""Modul **`random`** generuje pseudonáhodné hodnoty z vnitřního stavu:
`random.randint(a, b)` (celé číslo v `[a, b]`), `random.choice(seq)` (náhodná
položka), `random.shuffle(lst)` (přeuspořádá seznam **na místě**), `random.random()`
(float v `[0, 1)`).

- Čísla jsou deterministické funkce stavu, takže **`random.seed(n)`** je dělá
  **opakovatelnými**: po stejném semínku stejná volání dají stejné výsledky při
  každém spuštění a na každém stroji. Semínkuj jednou, před losy, které chceš
  reprodukovat.
- `random.shuffle` mutuje svůj argument a vrací `None` — zamíchej **kopii**
  (`out = list(items)`), abys zachoval originál, a nikdy nepiš
  `return random.shuffle(...)`.
- Výchozí (nesemínkovaný) generátor je semínkován z OS, takže bez semínka se každé
  spuštění liší. `random` **není** pro kryptografii — pro tokeny a hesla použij
  modul `secrets`.

```python
import random

random.seed(42)
random.randint(1, 6)     # same value every run for seed 42
deck = [1, 2, 3, 4]
random.shuffle(deck)     # deck reordered in place
```
""",

"11.5 brief": r"""# 11.5 -- Counter: sčítání v jednom kroku

## Koncept

Zpět v kapitole 5 jsi sčítal ručně: `counts[k] = counts.get(k, 0) + 1`. Modul
**`collections`** dodává tento vzor, napsaný a otestovaný, jako **`Counter`**:

```python
from collections import Counter

Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
```

- `Counter(items)` projde libovolný iterovatelný objekt a vrátí počet každé odlišné
  položky.
- `Counter` **je** slovník (je to podtřída), takže `counts[x]` i
  `for k, v in counts.items()` fungují přesně, jak bys čekal -- a porovnává se jako
  rovný prostému slovníku se stejnými počty.
- Zvládá dokonce chybějící klíč: `counts["zzz"]` je `0`, ne `KeyError`.

To je slib standardní knihovny: cyklus, který bys napsal, už je nástroj.

## Příklad

```python
from collections import Counter

def letter_counts(word):
    return Counter(word)
```

## Tvůj úkol

Pomocí **`Counter`** z `collections` definuj `tally(items)`, která vrátí počet, kolikrát se každá položka objeví v seznamu `items`.

## Hotovo, když

- `tally(["a", "b", "a"])` se rovná `{"a": 2, "b": 1}`.
- `tally([])` se rovná `{}`.
- Počítání dělá `Counter`, ne ručně psaný cyklus.
""",

"11.5 hints": r"""`from collections import Counter` nahoře. `Counter` udělá celé sčítání, když mu
předáš seznam.

---

`Counter(items)` už vrací počty a Counter se porovnává jako rovný prostému slovníku
stejných počtů -- takže ho můžeš vrátit přímo.

---

from collections import Counter


def tally(items):
    return Counter(items)
""",

"11.5 reference": r"""**`Counter`** (z modulu **`collections`**) je podtřída `dict`, která sečte
iterovatelný objekt jedním voláním: `Counter(items)` vrátí mapování každé odlišné
položky na to, kolikrát se objeví — cyklus `counts.get(k, 0) + 1`, už napsaný.

- Jelikož je to slovník, podporuje vše, co slovník (`c[key]`, `c.items()`,
  `key in c`), a porovnává se jako **rovný** prostému slovníku se stejnými počty.
- **Chybějící** klíč se čte jako `0`, místo aby vyvolal `KeyError`, což sčítání
  vyhovuje.
- **`c.most_common(n)`** vrátí `n` dvojic `(položka, počet)` s nejvyšším počtem, už
  seřazených — krok zprávy zadarmo. Countery se také sčítají a odčítají (`c1 + c2`),
  aby zkombinovaly součty.

```python
from collections import Counter

c = Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
c["a"]                    # 3
c["z"]                    # 0  -- no KeyError
c.most_common(1)          # [('a', 3)]
```
""",

"11.6 brief": r"""# 11.6 -- defaultdict: výchozí hodnota pro chybějící klíče

## Koncept

Abys seskupil položky v prostém slovníku, musíš nejdřív zkontrolovat, zda klíč
existuje:

```python
if length not in groups:
    groups[length] = []
groups[length].append(word)
```

**`defaultdict`** tento obřad odstraní. Dáš mu **továrnu** (factory) -- funkci, která
vytvoří výchozí hodnotu -- a on tu továrnu zavolá automaticky, když se poprvé dotkneš
chybějícího klíče:

```python
from collections import defaultdict

groups = defaultdict(list)     # missing key -> a fresh []
groups[5].append("hello")      # no setup needed
```

- `defaultdict(list)` vytvoří prázdný seznam pro každý nový klíč, takže `.append`
  prostě funguje.
- `defaultdict(int)` vytvoří `0` pro každý nový klíč -- sčítání bez `.get`.
- Jinak je to skutečný slovník; převeď pomocí `dict(groups)`, pokud chceš prostý.

## Příklad

```python
from collections import defaultdict

def by_first_letter(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return dict(groups)
```

## Tvůj úkol

Pomocí **`defaultdict`** z `collections` definuj `group_by_length(words)`, která
vrátí slovník mapující každou **délku** slova na seznam slov té délky, v jejich
původním pořadí.

## Hotovo, když

- `group_by_length(["hi", "ok", "bye"])` se rovná `{2: ["hi", "ok"], 3: ["bye"]}`.
- `group_by_length([])` se rovná `{}`.
- Seskupování používá `defaultdict(list)`, ne ruční kontrolu „if key in dict“.
""",

"11.6 hints": r"""`from collections import defaultdict`, pak `groups = defaultdict(list)`. `list` je
továrna: každý nový klíč začne jako prázdný seznam.

---

Procházej slova; pro každé `groups[len(w)].append(w)`. Klíč je délka, hodnota je
rostoucí seznam. Na konci vrať `dict(groups)`.

---

from collections import defaultdict


def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)
""",

"11.6 reference": r"""**`defaultdict`** (z **`collections`**) je `dict`, který automaticky dodá výchozí
hodnotu pro chybějící klíč. Předáš mu **továrnu** — bezargumentový volatelný objekt,
který sestaví výchozí hodnotu — a když poprvé přečteš nebo se dotkneš nepřítomného
klíče, zavolá továrnu, výsledek uloží a použije.

- `defaultdict(list)` vytvoří čerstvý `[]` pro každý nový klíč, takže
  `d[k].append(x)` funguje bez nastavení „if key not in d“ — idiom seskupování.
- `defaultdict(int)` vytvoří `0` pro každý nový klíč, takže `d[k] += 1` sčítá.
- Továrnu spustí jen **vyhledání** chybějícího klíče; jinak je to obyčejný slovník.
  `dict(d)` převede na prostý slovník a *skutečně* chybějící klíč se stále čte jako
  výchozí, místo aby vyvolal chybu.

```python
from collections import defaultdict

groups = defaultdict(list)
groups[5].append("hello")    # key 5 auto-starts as []
groups                       # defaultdict(<class 'list'>, {5: ['hello']})
```
""",

"11.7 brief": r"""# 11.7 -- json: data jako text

## Koncept

Abys uložil data do souboru nebo je poslal přes síť, potřebuješ je jako **text**.
**JSON** je téměř univerzální textový formát pro strukturovaná data a modul **`json`**
převádí oběma směry:

```python
import json

json.dumps({"name": "Ada", "score": 90})   # '{"name": "Ada", "score": 90}'
json.loads('{"ok": true}')                  # {'ok': True}
```

- `json.dumps(obj)` -- „dump string“ -- promění pythonovský dict/list/číslo/str na
  JSON **řetězec**.
- `json.loads(text)` -- „load string“ -- rozparsuje JSON řetězec zpět na pythonovské
  hodnoty.
- Oba jsou inverzní: `json.loads(json.dumps(x))` vrátí `x`.

Všimni si, že JSON se píše mírně jinak než Python (`true`/`false`/`null`), což je
přesně důvod, proč to necháš na modulu, místo abys formátoval ručně.

## Příklad

```python
import json

def parse(text):
    return json.loads(text)
```

## Tvůj úkol

Pomocí **`json.dumps`** definuj `to_json(record)`, která vrátí JSON řetězec pro
slovník `record`.

## Hotovo, když

- `to_json({"a": 1, "b": 2})` vrátí `'{"a": 1, "b": 2}'`.
- `to_json({})` vrátí `'{}'`.
- Řetězec produkuje `json.dumps`, ne ruční stavění.
""",

"11.7 hints": r"""`import json` nahoře. Funkce, kterou chceš, je `json.dumps`, která bere pythonovský
objekt a vrací jeho JSON text.

---

`json.dumps(record)` udělá celou práci. Tělo funkce je jeden řádek, který ho vrátí.

---

import json


def to_json(record):
    return json.dumps(record)
""",

"11.7 reference": r"""**JSON** (JavaScript Object Notation) je standardní **textový** formát pro
strukturovaná data a modul **`json`** převádí pythonovské hodnoty do něj a z něj.

- **`json.dumps(obj)`** („dump string“) serializuje pythonovský `dict`, `list`,
  `str`, číslo, `bool` nebo `None` do JSON řetězce. Klíče se stanou řetězci a
  pythonovské `True`/`False`/`None` se zapíšou jako JSON `true`/`false`/`null`.
- **`json.loads(text)`** („load string“) rozparsuje JSON řetězec zpět na pythonovské
  hodnoty. Oba jsou inverzní: `json.loads(json.dumps(x)) == x`.
- `dumps` bere možnosti — `indent=2` hezky odsadí, `sort_keys=True` seřadí klíče.
  Souborově orientované `json.dump(obj, f)` / `json.load(f)` zapisují a čtou objekt
  souboru přímo.
- Serializují se jen typy kompatibilní s JSON; `set` nebo vlastní objekt vyvolají
  `TypeError`, pokud `dumps` neřekneš, jak ho převést.

```python
import json

json.dumps({"name": "Ada", "ok": True})   # '{"name": "Ada", "ok": true}'
json.loads('[1, 2, 3]')                    # [1, 2, 3]
```
""",

"11.8 brief": r"""# 11.8 -- Závěrečná: statistický souhrn z JSON

## Koncept

Skutečnou lekcí této kapitoly je, že každodenní práce je **skládání knihovních
nástrojů**: nech jeden modul přečíst data, druhý je zpracovat a vrátit výsledek. Tady
zkombinuješ dva z modulů, které jsi právě potkal.

Vstup je **JSON řetězec** držící seznam čísel, např. `"[4, 8, 15, 16]"`. Ty:

1. ho rozparsuješ pomocí **`json.loads`** na pythonovský seznam,
2. ho shrneš pomocí **`statistics`** a vestavěných `max` / `min`,
3. vrátíš prostý slovník výsledků.

```python
import json
import statistics

data = json.loads("[4, 8, 15, 16]")     # [4, 8, 15, 16]
statistics.mean(data)                    # 10.75
```

## Tvůj úkol

Definuj `summary(numbers_json)`, která bere JSON řetězec seznamu čísel a vrátí
slovník s těmito klíči:

- `"count"` -- kolik čísel (`len`),
- `"mean"` -- jejich průměr (`statistics.mean`),
- `"max"` -- největší (`max`),
- `"min"` -- nejmenší (`min`).

Vstup rozparsuj pomocí `json.loads`. Předpokládej alespoň jedno číslo.

## Hotovo, když

- `summary("[2, 4, 6]")` se rovná
  `{"count": 3, "mean": 4, "max": 6, "min": 2}`.
- `summary("[5]")` se rovná `{"count": 1, "mean": 5, "max": 5, "min": 5}`.
- Vstup je rozparsován pomocí `json.loads`, ne ručně.
""",

"11.8 hints": r"""Dva importy nahoře: `import json` a `import statistics`. Nejprve proměň text na
seznam pomocí `json.loads(numbers_json)`.

---

Jakmile máš seznam `nums`, sestav slovník: `len(nums)` na count,
`statistics.mean(nums)` na mean a vestavěné `max(nums)` / `min(nums)`.

---

import json
import statistics


def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {
        "count": len(nums),
        "mean": statistics.mean(nums),
        "max": max(nums),
        "min": min(nums),
    }
""",

"11.8 reference": r"""Závěrečná úloha je skutečným smyslem kapitoly: **skládání modulů standardní
knihovny** do malého potrubí, místo psaní každého kroku od nuly.

- **Čti** pomocí `json` — `json.loads(text)` promění JSON vstup na pythonovské
  hodnoty (zde seznam čísel).
- **Shrň** pomocí `statistics` a vestavěných funkcí — `statistics.mean(nums)` na
  průměr, `max(nums)` / `min(nums)` na extrémy, `len(nums)` na počet.
- **Vrať** prostý `dict`, takže volající dostane obyčejné pythonovské hodnoty k
  použití.

Každá fáze je modul, který někdo jiný napsal a otestoval; tvým úkolem je propojit
je. To je to, čím většina skutečných programů je — lepidlo mezi dobře udělanými
knihovnami.

```python
import json
import statistics

def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {"count": len(nums), "mean": statistics.mean(nums),
            "max": max(nums), "min": min(nums)}

summary("[2, 4, 6]")   # {'count': 3, 'mean': 4, 'max': 6, 'min': 2}
```
""",
}
