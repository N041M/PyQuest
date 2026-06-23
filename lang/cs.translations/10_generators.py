# PyQuest translations -- language 'cs' -- chapter 10_generators -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"10.1 brief": r"""# 10.1 -- yield: funkce, která se pozastaví

## Koncept

Normální funkce `return`ne **jednou** a je hotová. **Generátor** je funkce, která
místo toho používá `yield`: každý `yield` vrátí **jednu** hodnotu a funkci přesně
tam **pozastaví**. Požádej o další hodnotu a funkce se **obnoví** tam, kde se
zastavila.

```python
def two_words():
    yield "hello"
    yield "world"
```

Jeho zavolání tělo **nespustí**. Podá ti **generátor** -- objekt, ze kterého taháš
hodnoty po jedné, obvykle cyklem `for`:

```python
for w in two_words():
    print(w)        # hello, then world
```

Odměna: generátor vytváří posloupnost **bez stavění celého seznamu v paměti**.
Pocítíš to v 10.3.

## Příklad

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1
```

`list(count_up(3))` je `[1, 2, 3]` -- každý průchod cyklu vyzve jedno číslo, pak se
pozastaví, dokud není požádán o další.

## Tvůj úkol

Definuj generátor `count_down(n)`, který **yielduje** celá čísla od `n` dolů k `1`,
v tomto pořadí. Je-li `n` `0` (nebo méně), nevyzve nic.

## Hotovo, když

- `list(count_down(5))` je `[5, 4, 3, 2, 1]`.
- `list(count_down(1))` je `[1]`; `list(count_down(0))` je `[]`.
- Použiješ `yield` -- takže volání `count_down` vrátí generátor, ne seznam.
""",

"10.1 hints": r"""Generátor vypadá jako normální funkce, ale řekne `yield` tam, kde by normální
sestavila výsledek. Každý `yield` vyprodukuje jedno číslo.

---

Počítej cyklem od `n` dolů a `yield`ni každou hodnotu. Cyklus `while`: začni `i`
na `n`, `yield i`, pak `i = i - 1`, dokud `i >= 1`. (Funguje i
`for i in range(n, 0, -1):`.)

---

def count_down(n):
    i = n
    while i >= 1:
        yield i
        i = i - 1
""",

"10.1 reference": r"""Funkce obsahující **`yield`** je **generátorová funkce**. Její zavolání tělo
nespustí — vrátí **objekt generátoru**, který vytváří hodnoty po jedné, **pozastaví
se** u každého `yield` a obnoví se tam, kde přestal, když je požádán o další.

- Každý `yield hodnota` podá jednu hodnotu tomu, kdo iteruje, pak zmrazí stav
  funkce do dalšího požadavku.
- Generátor konzumuješ jeho procházením (`for x in gen:`) nebo pomocí `next(gen)`.
- Liší se to od `return`, který vrátí **jednu** hodnotu a funkci natrvalo ukončí.

```python
def two():
    yield 1
    yield 2

for n in two():
    print(n)            # 1, then 2
```
""",

"10.2 brief": r"""# 10.2 -- yield uvnitř cyklu

## Koncept

Skutečná síla `yield` se ukáže, když sedí **uvnitř cyklu**: jeden řádek `yield`
proběhne jednou na průchod a proudí celou transformovanou posloupnost -- hodnotu po
hodnotě, nikdy ne celý seznam najednou.

```python
def letters(word):
    for ch in word:
        yield ch.upper()
```

`list(letters("hi"))` je `["H", "I"]`. Cyklus prochází vstup; `yield` pokaždé vydá
jednu transformovanou položku a mezitím se pozastaví.

## Příklad

```python
def doubles(nums):
    for x in nums:
        yield x * 2
```

`list(doubles([1, 5, 9]))` je `[2, 10, 18]`.

## Tvůj úkol

Definuj generátor `squares(n)`, který **yielduje** druhé mocniny celých čísel od `0`
až po (ale ne včetně) `n`: `0, 1, 4, 9, ...`. Je-li `n` `0` (nebo méně), nevyzve
nic.

## Hotovo, když

- `list(squares(4))` je `[0, 1, 4, 9]`.
- `list(squares(1))` je `[0]`; `list(squares(0))` je `[]`.
- Použiješ `yield` uvnitř cyklu -- ne vrácený seznam nebo komprehenzi.
""",

"10.2 hints": r"""Projdi čísla `0, 1, ..., n-1` cyklem a `yield`ni každé umocněné.

---

`for i in range(n):` pak `yield i * i`. Cyklus ti dá každé číslo; yield vydá jeho
druhou mocninu a pozastaví se, dokud není požádán o další.

---

def squares(n):
    for i in range(n):
        yield i * i
""",

"10.2 reference": r"""Umístění **`yield` dovnitř cyklu** proudí celou posloupnost: generátor vydá jednu
transformovanou hodnotu na průchod, pozastaví se po každé a obnoví se na další
požadavek.

- `for x in source: yield f(x)` vyzve `f(x)` pro každou položku — generátorová
  podoba stavění seznamu komprehenzí, ale produkovaná líně.
- Nic se nespočítá, dokud něco generátor neprochází, a jen do té míry, do jaké se
  konzumuje.

```python
def squares(nums):
    for n in nums:
        yield n * n

list(squares([1, 2, 3]))    # [1, 4, 9]
```
""",

"10.3 brief": r"""# 10.3 -- generátory jsou líné

## Koncept

Tohle je superschopnost. Generátor odvede práci jen tehdy, **když požádáš o další
hodnotu**. Nikdy nestaví celou posloupnost předem -- takže generátor může být
**nekonečný** a přesto téměř nic nestát, dokud z něj netaháš.

```python
def naturals():
    i = 0
    while True:        # never stops on its own...
        yield i
        i = i + 1
```

`while True` v normální funkci by zamrzlo navždy. V generátoru je v pořádku: každý
`yield` cyklus **pozastaví**, dokud volající nechce ještě jeden. Vezmeš si jen tolik,
kolik potřebuješ:

```python
from itertools import islice
list(islice(naturals(), 4))     # [0, 1, 2, 3] -- then it just stops asking
```

`islice(gen, k)` vytáhne z generátoru prvních `k` položek a víc ne. Generátor
vyprodukuje přesně tyto čtyři, pak sedí pozastavený.

## Příklad

`naturals()` výše yielduje `0, 1, 2, 3, ...` bez konce. Vytažení 3 položek dá
`[0, 1, 2]`; vytažení 10 dá `[0, 1, ..., 9]`. Tentýž nekonečný generátor, požádaný o
různá množství.

## Tvůj úkol

Definuj **nekonečný** generátor `naturals()`, který yielduje celá čísla začínající
od `0`: `0, 1, 2, 3, ...` navždy. Nikdy se nesmí zastavit sám od sebe; checker z něj
vždy vytáhne jen hrstku hodnot.

## Hotovo, když

- Prvních 5 hodnot `naturals()` je `[0, 1, 2, 3, 4]`.
- Je nekonečný -- vytažení dalších hodnot prostě dá další čísla; nikdy nedojde.
- Použiješ `yield`, takže volání `naturals()` vrátí generátor.
""",

"10.3 hints": r"""Potřebuješ cyklus, který nikdy neskončí, yieldující počítadlo, které se pokaždé
zvýší o jedna. `yield` je to, co mu brání zamrznout.

---

Začni `i` na `0`. Pak `while True:` -- `yield i`, pak `i = i + 1`. Cyklus „nikdy
neskončí“, ale každý yield ho pozastaví, dokud se nechce další hodnota.

---

def naturals():
    i = 0
    while True:
        yield i
        i = i + 1
""",

"10.3 reference": r"""Generátory jsou **líné**: každá hodnota se spočítá až na vyžádání, takže generátor
může popisovat **nekonečnou** posloupnost a přesto být užitečný — prostě si vezmeš
hodnoty, které potřebuješ.

- Nekonečné `while True: yield n; n += 1` samo o sobě nikdy neskončí, ale
  konzument může zastavit dříve (`break`, nebo několik volání `next`).
- Línost znamená, že generátor pro posloupnost drží v podstatě **žádnou paměť** —
  drží jen svůj aktuální stav, ne každou hodnotu — na rozdíl od seznamu, který je
  všechny zhmotní.

```python
def naturals():
    n = 0
    while True:
        yield n             # endless, but only as far as asked
        n += 1

g = naturals(); next(g), next(g)   # (0, 1)
```
""",

"10.4 brief": r"""# 10.4 -- generátor si pamatuje

## Koncept

Protože se generátor **pozastaví** místo dokončení, jeho lokální proměnné zůstávají
naživu mezi `yield`y. Hodnota, kterou buduješ, přežije každou pauzu -- generátor
naváže přesně tam, kde přestal, i s akumulátorem.

```python
def tally(words):
    seen = 0
    for w in words:
        seen = seen + 1
        yield seen          # 1, then 2, then 3, ... -- `seen` is remembered
```

`list(tally(["a", "b", "c"]))` je `[1, 2, 3]`. Počítadlo `seen` se při každém
průchodu neresetuje; drží si svou hodnotu napříč yieldy.

## Příklad

```python
def running_max(nums):
    best = None
    for n in nums:
        if best is None or n > best:
            best = n
        yield best
```

`list(running_max([3, 1, 5]))` je `[3, 3, 5]` -- každá položka je největší viděná
**dosud**.

## Tvůj úkol

Definuj generátor `running_total(nums)`, který yielduje **průběžný součet** `nums`:
každá hodnota je součet všech čísel až po aktuální včetně. Prázdný seznam nevyzve
nic.

## Hotovo, když

- `list(running_total([3, 1, 2]))` je `[3, 4, 6]`.
- `list(running_total([5]))` je `[5]`; `list(running_total([]))` je `[]`.
- Použiješ `yield` a proměnnou, která nese součet napříč yieldy.
""",

"10.4 hints": r"""Drž proměnnou `total` mimo cyklus, uvnitř cyklu k ní přičítej každé číslo a po
každém přičtení `yield`ni total.

---

`total = 0` před cyklem. Pak `for n in nums:` -- `total = total + n`,
pak `yield total`. Total se pamatuje napříč yieldy, takže pořád roste.

---

def running_total(nums):
    total = 0
    for n in nums:
        total = total + n
        yield total
""",

"10.4 reference": r"""Generátor si **pamatuje** své lokální proměnné napříč `yield`y: běh zmrzne u
`yield` a každá lokální proměnná si drží svou hodnotu do dalšího požadavku, který
funkci obnoví. Díky tomu může generátor **nést stav**, jak proudí.

- Proměnná aktualizovaná v cyklu (průběžný součet, předchozí hodnota) přetrvává
  mezi yieldy bez jakéhokoli objektu nebo globální proměnné.
- To je to, co dělá generátor přirozeným **průběžným akumulátorem** — třeba
  průběžným součtem, který v každém kroku vydá dosavadní součet.

```python
def running_sum(nums):
    total = 0
    for n in nums:
        total += n          # total survives across yields
        yield total

list(running_sum([1, 2, 3]))    # [1, 3, 6]
```
""",

"10.5 brief": r"""# 10.5 -- filtruj během yieldování

## Koncept

Generátor nemusí yieldovat při každém průchodu. Dej `yield` za `if` a stream
**filtruješ**, jak teče -- přeskakuješ položky, které nechceš, a vydáváš jen ty,
které ano.

```python
def shouts(words):
    for w in words:
        if w.isupper():
            yield w          # only the all-caps words come out
```

`list(shouts(["hi", "STOP", "go", "NOW"]))` je `["STOP", "NOW"]`. Cyklus navštíví
každé slovo; `yield` proběhne jen tehdy, když je `if` pravdivý.

## Příklad

```python
def positives(nums):
    for n in nums:
        if n > 0:
            yield n
```

`list(positives([-1, 4, 0, 2]))` je `[4, 2]`.

## Tvůj úkol

Definuj generátor `evens(nums)`, který yielduje jen **sudá** čísla z `nums` a
zachová jejich původní pořadí. (Číslo je sudé, když `n % 2 == 0`.) Pokud žádné není
sudé, nevyzve nic.

## Hotovo, když

- `list(evens([1, 2, 3, 4]))` je `[2, 4]`.
- `list(evens([1, 3, 5]))` je `[]`; `list(evens([]))` je `[]`.
- Použiješ `yield` za `if` -- ne vrácený seznam nebo komprehenzi.
""",

"10.5 hints": r"""Procházej každé číslo, ale `yield`ni jen ta, která projdou testem sudosti.

---

`for n in nums:` pak `if n % 2 == 0:` a, odsazené pod if, `yield n`.
Lichá čísla prostě propadnou bez yieldnutí.

---

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
""",

"10.5 reference": r"""Umístění **`yield` za `if`** filtruje stream, jak teče: generátor vydá jen
položky, které projdou testem, a zbytek tiše přeskočí — líný protějšek klauzule
`if` v komprehenzi.

- `for x in source: if test(x): yield x` vyprodukuje filtrovaný stream, aniž by
  stavěl jakýkoli mezilehlý seznam.
- Protože je líný, čistě se skládá: filtrovací generátor může napájet další
  generátor, každý zpracovává jednu fázi.

```python
def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n         # only the evens make it out

list(evens(range(10)))      # [0, 2, 4, 6, 8]
```
""",

"10.6 brief": r"""# 10.6 -- yield from: předej celý proud dál

## Koncept

Když chceš, aby generátor znovu vydal **každou** položku jiného iterovatelného
objektu, mohl bys procházet a yieldovat každou:

```python
def both(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
```

Python má pro přesně tenhle vnitřní cyklus zkratku: **`yield from`**.

```python
def both(a, b):
    yield from a        # yield every item of a, one by one
    yield from b        # then every item of b
```

`yield from iterable` je „yieldni každou hodnotu, kterou tento iterovatelný objekt
vyprodukuje“. Obě verze výše se chovají stejně; `yield from` to jen řekne jedním
řádkem.

## Příklad

```python
def repeat_each(items):
    for x in items:
        yield from (x, x)      # yield x, then x again

list(repeat_each([1, 2]))      # [1, 1, 2, 2]
```

## Tvůj úkol

Definuj generátor `chain(a, b)`, který yielduje **všechny** položky `a`, pak
**všechny** položky `b`, v pořadí. Použij `yield from`. Kterýkoli seznam může být
prázdný.

## Hotovo, když

- `list(chain([1, 2], [3, 4]))` je `[1, 2, 3, 4]`.
- `list(chain([], [9]))` je `[9]`; `list(chain([], []))` je `[]`.
- Použiješ `yield from`, takže volání `chain` vrátí generátor.
""",

"10.6 hints": r"""Chceš znovu vydat každou položku `a`, pak každou položku `b`. `yield from` to
udělá přesně pro jeden iterovatelný objekt po druhém.

---

Dva řádky: `yield from a` pak `yield from b`. Každý z nich proudí celý ten seznam
do výstupu generátoru.

---

def chain(a, b):
    yield from a
    yield from b
""",

"10.6 reference": r"""**`yield from iterable`** znovu vydá **každou** položku, kterou iterovatelný objekt
vyprodukuje, jako bys napsal cyklus `yield`ů. Deleguje celý dílčí stream jedním
řádkem.

- `yield from sub` je ekvivalentní `for x in sub: yield x`, ale kratší a rychlejší
  — a funguje se seznamy, rozsahy, jinými generátory, libovolným iterovatelným
  objektem.
- Je to nástroj na **zploštění** nebo **zřetězení**: generátor může `yield from`
  několik zdrojů po sobě, aby spletl jejich streamy dohromady.

```python
def chain(a, b):
    yield from a
    yield from b            # splice two streams into one

list(chain([1, 2], [3, 4]))     # [1, 2, 3, 4]
```
""",

"10.7 brief": r"""# 10.7 -- zastav se brzy

## Koncept

Generátor skončí ve chvíli, kdy skončí jeho funkce -- a prosté `return` (bez
hodnoty) uvnitř generátoru znamená „zastav teď, žádné další položky“. Takže generátor
se může rozhodnout **skončit brzy**, dřív než dojde vstup.

```python
def before_blank(words):
    for w in words:
        if w == "":
            return          # stop the generator here
        yield w
```

`list(before_blank(["a", "b", "", "c"]))` je `["a", "b"]` -- jakmile se dosáhne
prázdného, `return` generátor ukončí a `"c"` se nikdy nevyprodukuje.

## Příklad

```python
def while_positive(nums):
    for n in nums:
        if n <= 0:
            return
        yield n

list(while_positive([3, 1, -1, 5]))    # [3, 1]
```

## Tvůj úkol

Definuj generátor `until_zero(nums)`, který yielduje každé číslo **dokud nedosáhne
`0`**, pak se zastaví. Samotná `0` ani nic po ní se **neyielduje**. Pokud žádná `0`
není, yielduje celý seznam.

## Hotovo, když

- `list(until_zero([1, 2, 0, 3]))` je `[1, 2]`.
- `list(until_zero([0, 9]))` je `[]`; `list(until_zero([1, 2, 3]))` je
  `[1, 2, 3]`.
- Použiješ `yield` a zastavíš se brzy, když narazíš na `0`.
""",

"10.7 hints": r"""Procházej čísla. Jakmile uvidíš `0`, zastav celý generátor; jinak číslo yieldni.

---

`for n in nums:` -- nejprve `if n == 0: return` (to ukončí generátor), pak
`yield n` pro vše před nulou.

---

def until_zero(nums):
    for n in nums:
        if n == 0:
            return
        yield n
""",

"10.7 reference": r"""Holé **`return`** uvnitř generátoru — nebo prostě dosažení konce funkce — ho
**zastaví**: iterace skončí a žádné další hodnoty nepřijdou. `return` v generátoru
nenese **žádnou hodnotu**; jen signalizuje „hotovo“.

- To umožní generátoru **zastavit se brzy** při splnění podmínky:
  `if x == sentinel: return` ukončí stream v tom bodě.
- Pro cyklus `for` je zastavený generátor prostě iterovatelný objekt, který došel —
  cyklus přirozeně skončí (interně generátor vyvolá `StopIteration`).

```python
def until_zero(nums):
    for n in nums:
        if n == 0:
            return          # stop the stream here
        yield n

list(until_zero([3, 1, 0, 9]))  # [3, 1]
```
""",

"10.8 brief": r"""# 10.8 -- Závěrečná: proudové potrubí

## Koncept

Nic nového -- tato závěrečná úloha je kapitola v miniatuře. Skutečný důvod, proč na
generátorech záleží, je, že se **skládají**: výstup jednoho generátoru je vstupem
druhého, takže data tečou skrz **potrubí** (pipeline), po jedné položce, aniž by se
mezitím kdy stavěl celý seznam.

Fáze potrubí je prostě generátor, který prochází `stream` (libovolný iterovatelný
objekt -- seznam, nebo *jiný generátor*) a průběžně yielduje:

```python
def only_long(stream):
    for word in stream:
        if len(word) >= 4:
            yield word
```

Postavíš zdroj, filtr a přeznačkovací fázi, pak je propojíš dohromady.

## Příklad

```python
numbers(4)                              # yields 0, 1, 2, 3
keep_even(numbers(4))                   # yields 0, 2
labelled(keep_even(numbers(4)))         # yields "#0", "#2"
```

## Tvůj úkol

Definuj **tři** generátory:

- `numbers(n)` -- yielduje `0, 1, ..., n-1` (zdroj). `n <= 0` nevyzve nic.
- `keep_even(stream)` -- yielduje jen sudá čísla ze `stream` (libovolný iterovatelný
  objekt).
- `labelled(stream)` -- yielduje řetězec `"#x"` pro každé `x` ve `stream` (např. `7`
  se stane `"#7"`).

Každý musí použít `yield`. `keep_even` a `labelled` musí fungovat na **libovolném**
streamu, včetně výstupu jiného generátoru, aby se skládaly.

## Hotovo, když

- `list(numbers(4))` je `[0, 1, 2, 3]`; `list(numbers(0))` je `[]`.
- `list(keep_even([1, 2, 3, 4]))` je `[2, 4]`.
- `list(labelled([0, 2]))` je `["#0", "#2"]`.
- `list(labelled(keep_even(numbers(6))))` je `["#0", "#2", "#4"]`.
- Všechny tři používají `yield` a filtrovací/přeznačkovací fáze přijímají libovolný
  iterovatelný objekt.
""",

"10.8 hints": r"""Každá fáze je svůj vlastní malý generátor. `numbers` prochází `range(n)` a
yielduje; `keep_even` prochází `stream` a yielduje jen sudá; `labelled` prochází
`stream` a yielduje naformátovaný řetězec. Žádný z nich nestaví seznam.

---

`keep_even` a `labelled` berou `stream` a `for x in stream:` -- ten cyklus funguje,
ať je `stream` seznam nebo jiný generátor, což je to, co ti umožní je vnořovat.
Použij f-řetězec na štítek: `yield f"#{x}"`.

---

def numbers(n):
    for i in range(n):
        yield i


def keep_even(stream):
    for x in stream:
        if x % 2 == 0:
            yield x


def labelled(stream):
    for x in stream:
        yield f"#{x}"
""",

"10.8 reference": r"""Závěrečná úloha skládá generátory do **proudového potrubí**: **zdrojový** generátor
napájí **filtrovací** generátor, který napájí **transformační** generátor. Každá
fáze je líná, takže hodnoty tečou po jedné a nic se nezhmotní celé.

- Protože každá fáze líně konzumuje předchozí, potrubí zpracovává obrovská nebo
  nekonečná data s nepatrnou pamětí — v každém okamžiku je v letu jedna položka.
- Fáze zůstávají malé a nezávislé: vyměň nebo přidej fázi, aniž by ses dotkl
  ostatních. To je generátorová obdoba skládání funkcí.

```python
def reader(nums):  yield from nums
def keep_pos(src): yield from (n for n in src if n > 0)
def doubled(src):  yield from (n * 2 for n in src)

list(doubled(keep_pos(reader([-1, 2, -3, 4]))))   # [4, 8]
```
""",
}
