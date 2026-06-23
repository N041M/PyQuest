# PyQuest translations -- language 'cs' -- chapter 14_functional -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"14.1 brief": r"""# 14.1 -- lambda: funkce ve výrazu

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
""",

"14.1 hints": r"""lambda je `lambda args: expression`. Chceš takovou, která bere `x` a vrací `x * n`.

---

`multiplier` tu lambdu vrátí. lambda uzavře `n`, takže každé volání `multiplier`
vytvoří funkci svázanou s vlastním `n`.

---

def multiplier(n):
    return lambda x: x * n
""",

"14.1 reference": r"""**`lambda`** je anonymní funkce psaná jako jediný výraz: `lambda args: expression`.
Hodnota výrazu se vrátí automaticky — není tu žádné `return` a tělo musí být
**jeden** výraz.

- lambda je prvotřídní **hodnota**: přiřaď ji, vrať ji nebo ji předej jako argument.
  `f = lambda x: x * 2` je hodně podobné `def f(x): return x * 2`, jen inline a bez
  jména.
- Definovaná uvnitř jiné funkce lambda **uzavře** proměnné toho rozsahu —
  `lambda x: x * n` zachytí `n` odtud, kde byla vytvořena, takže každé
  `multiplier(n)` dá funkci svázanou s vlastním `n`.
- Lambdy jsou pro *malé* inline funkce, hlavně jako `key=` pro `sorted` nebo funkce
  pro `map`/`filter` (zbytek této kapitoly). Na cokoli s více příkazy použij
  pojmenovaný `def`.

```python
double = lambda x: x * 2
double(5)                  # 10

def multiplier(n):
    return lambda x: x * n
multiplier(3)(4)           # 12
```
""",

"14.2 brief": r"""# 14.2 -- map: aplikuj na každou položku

## Koncept

**`map(func, iterable)`** spustí `func` na **každé** položce a vydá výsledky. Je to
vzor „aplikuj na každou“ jako funkce vyššího řádu -- funkce, která bere jinou funkci:

```python
list(map(str.upper, ["a", "b"]))     # ['A', 'B']
list(map(lambda x: x * x, [1, 2, 3])) # [1, 4, 9]
```

- `map` vrátí **líný iterátor**, takže ho obal do `list(...)`, abys dostal seznam.
- Funkce může být `lambda`, `def` nebo vestavěná jako `str.upper` nebo `int`.

(Seznamová komprehenze `[f(x) for x in items]` dělá totéž a často se čte
přirozeněji; tato úloha je o naučení se samotného `map`, nástroje, který potkáš v
hromadě kódu.)

## Příklad

```python
def lengths(words):
    return list(map(len, words))
```

## Tvůj úkol

Pomocí **`map`** definuj `squares(nums)`, která vrátí seznam každého čísla v `nums`
umocněného.

## Hotovo, když

- `squares([1, 2, 3])` vrátí `[1, 4, 9]`.
- `squares([])` vrátí `[]`.
- Mapování dělá `map`, ne komprehenze nebo ruční cyklus.
""",

"14.2 hints": r"""`map(func, nums)` aplikuje `func` na každé číslo. Tvá `func` umocní svůj vstup:
`lambda x: x * x`.

---

`map` je líný, takže ho obal: `list(map(lambda x: x * x, nums))`.

---

def squares(nums):
    return list(map(lambda x: x * x, nums))
""",

"14.2 reference": r"""**`map(func, iterable)`** aplikuje `func` na každou položku a vydá výsledky — vzor
„transformuj každou položku“ jako funkce vyššího řádu (taková, která bere jinou
funkci jako argument).

- Vrátí **líný iterátor**, který počítá každý výsledek na vyžádání; obal ho do
  `list(...)` (nebo `tuple`, nebo napájej `for`), abys ho zkonzumoval.
- `func` může být `lambda`, pojmenovaný `def` nebo libovolný volatelný objekt —
  vestavěná jako `len`, `str.upper` nebo `int` je běžná.
- S několika iterovatelnými objekty `map(func, a, b)` volá `func(a_i, b_i)` v
  zákrytu a zastaví se u nejkratšího.
- Seznamová komprehenze `[func(x) for x in items]` vyjadřuje totéž a je často
  jasnější; `map` je funkcionálně stylový ekvivalent, který uvidíš všude.

```python
list(map(len, ["hi", "there"]))        # [2, 5]
list(map(lambda x: x * x, [1, 2, 3]))  # [1, 4, 9]
list(map(int, ["1", "2", "3"]))        # [1, 2, 3]
```
""",

"14.3 brief": r"""# 14.3 -- filter: ponech, co projde

## Koncept

Kde `map` transformuje každou položku, **`filter`** ponechá jen **některé** z nich.
Dáš mu **predikát** -- funkci, která vrací pravda nebo nepravda -- a on ponechá
každou položku, na kterou predikát řekne ano:

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))     # [2, 4]
```

- `filter(pred, iterable)` vydá každou položku, pro kterou je `pred(item)` pravdivý,
  a zbytek zahodí, v pořadí.
- Stejně jako `map` vrátí **líný iterátor**, takže ho obal do `list(...)`.

(Komprehenze `[x for x in items if pred(x)]` dělá totéž; tato úloha je o samotném
`filter`.)

## Příklad

```python
def nonempty(strings):
    return list(filter(lambda s: s != "", strings))
```

## Tvůj úkol

Pomocí **`filter`** definuj `evens(nums)`, která vrátí seznam jen sudých čísel v
`nums`.

## Hotovo, když

- `evens([1, 2, 3, 4])` vrátí `[2, 4]`.
- `evens([1, 3, 5])` vrátí `[]`.
- Výběr dělá `filter`, ne komprehenze nebo ruční cyklus.
""",

"14.3 hints": r"""`filter(pred, nums)` ponechá každé číslo, kde je `pred` pravda. Tvůj predikát
testuje sudost: `lambda x: x % 2 == 0`.

---

Obal ho do `list(...)`: `list(filter(lambda x: x % 2 == 0, nums))`.

---

def evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
""",

"14.3 reference": r"""**`filter(pred, iterable)`** ponechá položky, pro které je **predikát** `pred`
(funkce vracející pravda nebo nepravda) pravdivý, a zbytek zahodí — protějšek
„ponech, pokud“ k „transformuj každou“ od `map`.

- Vrátí **líný iterátor** v původním pořadí; obal ho do `list(...)`, abys posbíral.
- `pred` je libovolný volatelný objekt vracející pravdivou/nepravdivou hodnotu —
  `lambda`, `def` nebo vestavěná. Předání **`None`** jako predikátu
  (`filter(None, items)`) ponechá položky, které jsou samy pravdivé, a zahodí `0`,
  `""`, `None` atd.
- Komprehenze `[x for x in items if pred(x)]` je ekvivalent a často se čte lépe;
  `filter` je funkcionální tvar.

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))   # [2, 4]
list(filter(None, [0, 1, "", "a", None]))        # [1, 'a']
list(filter(str.isalpha, "a1b2"))                # ['a', 'b']
```
""",

"14.4 brief": r"""# 14.4 -- sorted(key=lambda): řazení podle odvozené hodnoty

## Koncept

`sorted` (kapitola 5) řadí položky podle jejich přirozeného pořadí. Jeho argument
**`key=`** mění, *podle čeho* řadí: funkce mapující každou položku na hodnotu k
porovnání. Inline **lambda** je obvyklý způsob, jak to napsat:

```python
words = ["pear", "fig", "apple"]
sorted(words, key=len)                  # ['fig', 'pear', 'apple']
sorted(words, key=lambda w: w[-1])      # by last letter
```

- `key` se zavolá jednou na položku; `sorted` pak položky seřadí podle těchto hodnot
  klíče.
- lambda ti umožní řadit podle čehokoli **odvozeného** z položky -- její délky, pole,
  spočítaného skóre -- aniž bys měnil samotné položky.
- `sorted` je **stabilní**: položky se stejnými klíči si ponechají původní pořadí.

## Příklad

```python
def by_size(nums):
    return sorted(nums, key=lambda n: abs(n))   # by distance from zero
```

## Tvůj úkol

Pomocí **`sorted`** s **`key=lambda`** definuj `by_last(words)`, která vrátí slova
seřazená podle jejich **posledního znaku**.

## Hotovo, když

- `by_last(["pear", "fig", "kiwi"])` vrátí `["fig", "kiwi", "pear"]`
  (poslední písmena g, i, r jsou v pořadí).
- `by_last([])` vrátí `[]`.
- Pořadí pochází z `sorted(..., key=lambda ...)`, ne z ručního řazení.
""",

"14.4 hints": r"""`sorted(words, key=...)` řadí podle toho, co vrátí klíčová funkce. Chceš řadit podle
posledního znaku každého slova.

---

Poslední znak `w` je `w[-1]`, takže klíč je `lambda w: w[-1]`:
`sorted(words, key=lambda w: w[-1])`.

---

def by_last(words):
    return sorted(words, key=lambda w: w[-1])
""",

"14.4 reference": r"""Argument **`key=`** od `sorted` je funkce mapující každou položku na hodnotu, podle
níž se řadí, takže můžeš řadit podle něčeho **odvozeného** z položek, ne podle
samotných položek. Inline **`lambda`** je idiomatický způsob, jak ten klíč napsat.

- `key` se volá **jednou na položku**; `sorted` položky seřadí podle výsledných
  hodnot klíče, ale vrátí původní položky. `sorted(words, key=len)` řadí podle délky,
  `sorted(words, key=lambda w: w[-1])` podle posledního písmene.
- `sorted` je **stabilní**: položky se stejnými klíči si ponechají vstupní pořadí.
- Spoj `key=` s **`reverse=True`** k sestupnému řazení. Stejné `key=` funguje na
  `list.sort`, `min` a `max`.

```python
sorted(["pear", "fig", "apple"], key=len)            # ['fig', 'pear', 'apple']
sorted([-3, 1, -2], key=lambda n: abs(n))            # [1, -2, -3]
sorted(records, key=lambda r: r[1], reverse=True)    # by 2nd field, high first
```
""",

"14.5 brief": r"""# 14.5 -- any: je alespoň jedna pravda?

## Koncept

**`any(iterable)`** vrátí `True`, pokud je **alespoň jedna** položka pravdivá, jinak
`False`. Když ho napájíš generátorem testů, odpoví na „projde *nějaká* položka?“:

```python
any(n < 0 for n in [1, 2, -3])     # True
any(n < 0 for n in [1, 2, 3])      # False
```

- Nahradí cyklus s příznakem (`found = False; for ...: if ...: found = True`)
  jediným výrazem.
- Vyhodnocuje se **zkráceně**: zastaví se a vrátí `True` u první pravdivé položky.
- `any([])` je `False` (nic neprošlo).

Vzor je `any(<test> for <item> in <iterable>)` -- generátorový výraz booleanů
předaný `any`.

## Příklad

```python
def has_blank(strings):
    return any(s == "" for s in strings)
```

## Tvůj úkol

Pomocí **`any`** definuj `has_negative(nums)`, která vrátí `True`, pokud `nums`
obsahuje alespoň jedno záporné číslo.

## Hotovo, když

- `has_negative([1, 2, -3])` je `True`; `has_negative([1, 2, 3])` je `False`.
- `has_negative([])` je `False`.
- Odpověď pochází z `any(...)`, ne z ručně psaného cyklu s příznakem.
""",

"14.5 hints": r"""`any(...)` bere posloupnost hodnot pravda/nepravda a vrátí True, pokud je nějaká
pravda. Tu posloupnost sestav generátorovým výrazem.

---

`any(n < 0 for n in nums)` -- pro každé číslo je test `n < 0` True nebo False a
`any` nahlásí, zda byla alespoň jedna True.

---

def has_negative(nums):
    return any(n < 0 for n in nums)
""",

"14.5 reference": r"""**`any(iterable)`** vrátí `True`, jakmile je **jedna** položka pravdivá, jinak
`False`. Když dostane generátor testů, odpoví na „projde nějaká položka?“ jediným
výrazem a nahradí cyklus, který nastavuje příznak.

- Vyhodnocuje se **zkráceně**: vyhodnocování se zastaví u první pravdivé položky,
  takže je efektivní a funguje na nekonečných/líných iterovatelných objektech.
- `any([])` je `False` — není tu nic, co by bylo pravda.
- Idiom je `any(<test> for <item> in <iterable>)`: generátorový výraz booleanů.
  (Jeho partner `all` je 14.6.)

```python
any(n < 0 for n in [1, 2, -3])    # True
any(c.isdigit() for c in "abc")   # False
any([])                           # False
```
""",

"14.6 brief": r"""# 14.6 -- all: jsou pravdivé úplně všechny?

## Koncept

**`all(iterable)`** je partner `any`: vrátí `True` jen tehdy, když je **každá**
položka pravdivá. Odpoví na „projdou *všechny*?“:

```python
all(n > 0 for n in [1, 2, 3])      # True
all(n > 0 for n in [1, -2, 3])     # False
```

- Vyhodnocuje se **zkráceně** opačně: zastaví se a vrátí `False` u první položky,
  která selže.
- `all([])` je `True` -- prázdně (vacuously), protože žádná položka neselhala.
  (Častý překvap: „všechny z ničeho“ je pravda.)

Stejný tvar jako `any`: `all(<test> for <item> in <iterable>)`.

## Příklad

```python
def all_words(strings):
    return all(s.isalpha() for s in strings)
```

## Tvůj úkol

Pomocí **`all`** definuj `all_positive(nums)`, která vrátí `True`, pokud je **každé**
číslo v `nums` větší než nula.

## Hotovo, když

- `all_positive([1, 2, 3])` je `True`; `all_positive([1, -2, 3])` je `False`.
- `all_positive([])` je `True` (nic neselže).
- Odpověď pochází z `all(...)`, ne z ručně psaného cyklu s příznakem.
""",

"14.6 hints": r"""`all(...)` vrátí True jen tehdy, když je každá hodnota v posloupnosti pravda.
Posloupnost testů sestav generátorovým výrazem.

---

`all(n > 0 for n in nums)` -- každé `n > 0` je True nebo False a `all` je True jen
tehdy, když žádná nebyla False.

---

def all_positive(nums):
    return all(n > 0 for n in nums)
""",

"14.6 reference": r"""**`all(iterable)`** vrátí `True` jen tehdy, když je **každá** položka pravdivá —
partner k `any`. Odpoví na „projdou všechny?“ jedním výrazem.

- Vyhodnocuje se **zkráceně** u první nepravdivé položky a okamžitě vrátí `False`.
- `all([])` je `True` — *prázdně* (vacuously), protože žádná položka neselhala. Toto
  pravidlo „všechny z ničeho je pravda“ je častý překvap; ošetři prázdný případ,
  pokud na něm záleží.
- Stejný tvar jako `any`: `all(<test> for <item> in <iterable>)`. Dohromady
  vyjadřují univerzální („pro všechny“) a existenční („existuje“) otázku nad
  posloupností.

```python
all(n > 0 for n in [1, 2, 3])     # True
all(n > 0 for n in [1, -2, 3])    # False
all([])                           # True  -- vacuously
```
""",

"14.7 brief": r"""# 14.7 -- reduce: slož posloupnost do jedné hodnoty

## Koncept

**`reduce`** (z `functools`) **složí** (fold) celou posloupnost do jediné hodnoty
tím, že kumulativně aplikuje dvouargumentovou funkci, zleva doprava:

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])     # 10  ((((1+2)+3)+4))
reduce(lambda a, b: a * b, [1, 2, 3, 4])     # 24
```

- `reduce(func, items)` spočítá `func(func(func(i0, i1), i2), i3)...` -- každý krok
  zkombinuje průběžný výsledek s další položkou.
- Třetí argument je **počáteční** hodnota: `reduce(func, items, start)` začne skládat
  od `start`, což také definuje odpověď pro **prázdnou** posloupnost.
- Je to akumulátorový cyklus (kapitola 3) jako funkce vyššího řádu. (`sum` je
  speciální případ pro `+`; `reduce` ti umožní skládat s *libovolným* kombinátorem.)

## Příklad

```python
from functools import reduce

def total(nums):
    return reduce(lambda a, b: a + b, nums, 0)
```

## Tvůj úkol

Pomocí **`reduce`** z `functools` definuj `product(nums)`, která vrátí součin všech
čísel (s počátkem `1`, takže prázdný seznam dá `1`).

## Hotovo, když

- `product([1, 2, 3, 4])` vrátí `24`; `product([5])` vrátí `5`.
- `product([])` vrátí `1`.
- Skládání používá `reduce`, ne ruční akumulátorový cyklus.
""",

"14.7 hints": r"""`from functools import reduce`. Bere dvouargumentový kombinátor, položky a
počáteční hodnotu.

---

Kombinátor násobí průběžný výsledek dalším číslem:
`reduce(lambda a, b: a * b, nums, 1)`. Počátek `1` zařídí, že prázdný seznam dá 1.

---

from functools import reduce


def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)
""",

"14.7 reference": r"""**`functools.reduce(func, iterable[, start])`** **složí** (fold) posloupnost do
jediné hodnoty tím, že kumulativně aplikuje dvouargumentovou `func`, zleva doprava:
`func(func(func(i0, i1), i2), i3)...`. Každý krok zkombinuje průběžný výsledek s
další položkou.

- **Počáteční** hodnota (`reduce(func, items, start)`) skládání nasadí a definuje
  výsledek pro **prázdnou** posloupnost; bez ní redukce prázdného iterovatelného
  objektu vyvolá `TypeError`.
- Zobecňuje akumulátorový cyklus na *libovolný* kombinátor: `+` dá součet, `*`
  součin, `max` největší. Vyhrazený `sum` je speciální případ `+` a `math.prod` ten
  pro `*` — ale `reduce` skládá s jakoukoli funkcí, kterou dodáš.
- `reduce` žije v `functools` (není vestavěný), takže se musí naimportovat.

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])      # 10
reduce(lambda a, b: a * b, [1, 2, 3, 4], 1)   # 24
reduce(lambda a, b: a if a > b else b, [3, 9, 2])   # 9  (max)
```
""",

"14.8 brief": r"""# 14.8 -- Závěrečná: seřazený užší výběr

## Koncept

Nástroje kapitoly se zřetězí do **potrubí** (pipeline). Daný seznam záznamů
`(name, score)` sestav užší výběr:

1. **`filter`** na záznamy, které splní práh,
2. **`sorted`** s `key=lambda` (a `reverse=True`), abys je seřadil od nejvyššího po
   nejnižší,
3. **`map`** ven jen jména.

```python
records = [("Ada", 90), ("Linus", 70), ("Grace", 95)]
qualified = filter(lambda r: r[1] >= 80, records)
ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
list(map(lambda r: r[0], ranked))     # ['Grace', 'Ada']
```

Každý záznam je n-tice, takže `r[0]` je jméno a `r[1]` skóre.

## Tvůj úkol

Definuj `passing(records, threshold)`, která bere seznam n-tic `(name, score)` a
vrátí **jména** těch se `score >= threshold`, seřazená podle skóre **od nejvyššího**,
sestavená pomocí `filter`, `sorted(key=lambda ...)` a `map`.

## Hotovo, když

- `passing([("Ada", 90), ("Linus", 70), ("Grace", 95)], 80)` vrátí
  `["Grace", "Ada"]`.
- `passing([], 50)` vrátí `[]`; práh nad každým skóre vrátí `[]`.
- Výsledek je sestaven filtrováním, řazením podle lambda klíče a mapováním -- potrubí
  nástrojů kapitoly.
""",

"14.8 hints": r"""Tři kroky. Nejprve `filter(lambda r: r[1] >= threshold, records)` ponechá záznamy,
které kvalifikují (r[1] je skóre).

---

Pak `sorted(qualified, key=lambda r: r[1], reverse=True)` je seřadí od nejvyššího po
nejnižší a `map(lambda r: r[0], ...)` vytáhne jména. Obal map do `list`.

---

def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
""",

"14.8 reference": r"""Závěrečná úloha zřetězí funkce vyššího řádu kapitoly do **datového potrubí** —
podoby velké části skutečného zpracování:

1. **`filter(lambda r: r[1] >= threshold, records)`** zúží na záznamy, které
   kvalifikují;
2. **`sorted(..., key=lambda r: r[1], reverse=True)`** je seřadí podle skóre, od
   nejvyššího po nejnižší (stabilně, takže stejná skóre si ponechají pořadí);
3. **`map(lambda r: r[0], ...)`** vyprojektuje jen pole, které chceš — jméno.

Každá fáze bere funkci a iterovatelný objekt a vydá další iterovatelný objekt,
takže se přímo skládají: filtr napájí řazení, řazení napájí mapování. Stejné potrubí
by se dalo napsat komprehenzemi; vyjádřit ho jako `filter`/`sorted`/`map` je
funkcionální styl a vidět úlohu *jako* potrubí transformací je dovednost, ke které
kapitola směřuje.

```python
def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
```
""",
}
