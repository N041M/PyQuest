# PyQuest translations -- language 'cs' -- chapter 06_functions -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"6.1 brief": r"""# 6.1 -- def: tvoje první funkce

## Koncept

**Funkce** je pojmenovaný, znovupoužitelný kus kódu. Funkce jsi *volal* celou dobu
-- `print()`, `len()`, `sorted()`. Teď si můžeš **definovat** vlastní:

```python
def double(x):
    return x * 2
```

- `def` zahajuje definici; `double` je jméno, které si zvolíš.
- `x` je **parametr**: proměnná, která přijme libovolnou hodnotu, jíž jí volající
  předá.
- `return` předá hodnotu **zpět volajícímu**. Volání `double(3)` je pak výraz s
  hodnotou `6`:

```python
result = double(3)     # result is 6
print(double(10))      # 20
```

**Tato kapitola kontroluje tvůj kód jinak.** Dosud se tvůj soubor *spouštěl* a
vypisoval. Odsud checker tvůj soubor **naimportuje** a **volá tvé funkce přímo** a
předává jim spoustu různých argumentů -- takže není potřeba žádný `input()` ani
`print()`. Tvůj soubor jen definuje funkci.

## Příklad

```python
def double(x):
    return x * 2
```

Celý tento soubor je platná odpověď na úlohu: definuje `double` a `double(21)`
vrátí `42`.

## Tvůj úkol

Definuj funkci `double(x)`, která **vrátí** `x` zdvojnásobené.

## Hotovo, když

- `double(3)` vrátí `6`, `double(0)` vrátí `0`, `double(-5)` vrátí `-10`.
- Tvůj soubor jen definuje funkci -- žádný `input()`, žádný `print()`.
""",

"6.1 hints": r"""Tvar je:  def jméno(parametr):  pak odsazené tělo, které něco vrací.

---

`def double(x):` na prvním řádku; tělo je jeden řádek: return x krát 2.

---

def double(x):
    return x * 2
""",

"6.1 reference": r"""**Funkce** zabalí kus práce pod jméno, takže ji lze spustit na vyžádání,
kolikrát je potřeba. **`def`** ji uvádí: hlavička `def jméno():` a odsazené tělo.

- **Volání** — `jméno()` — spustí tělo. Definice funkce ji nespustí; udělá to
  volání.
- **`return hodnota`** předá výsledek zpět volajícímu a funkci okamžitě ukončí.
  Volání `jméno()` se pak *stane* touto hodnotou.
- Funkce bez `return` (nebo s holým `return`) vrátí `None`.

```python
def greet():
    return "hello"

greet()        # 'hello'  -- the call evaluates to the returned value
```
""",

"6.2 brief": r"""# 6.2 -- Dva parametry

## Koncept

Funkce může přijmout několik parametrů -- vyjmenuj je čárkami a hodnoty volajícího
dorazí **ve stejném pořadí**:

```python
def rect_area(width, height):
    return width * height

rect_area(3, 4)     # 12  (width=3, height=4)
```

Uvnitř těla jsou parametry obyčejné proměnné. Funguje na nich vše, co už znáš --
aritmetika, porovnání, f-řetězce, cykly.

Jemnost, kterou je dobré potkat brzy: parametry jsou **lokální** pro funkci. `width`
uvnitř `rect_area` existuje jen po dobu běhu volání; není vidět (ani se nesráží) s
ničím venku.

## Příklad

```python
def diff(a, b):
    return a - b

print(diff(10, 4))   # 6
print(diff(4, 10))   # -6  -- order matters
```

## Tvůj úkol

Definuj `rect_area(width, height)`, která vrátí obsah obdélníku (šířka krát výška).

## Hotovo, když

- `rect_area(3, 4)` vrátí `12`; `rect_area(4, 3)` také.
- Nulová strana vrátí `0`.
- Žádný `input()`, žádný `print()` -- checker hodnoty předá.
""",

"6.2 hints": r"""Dva parametry se vyjmenují čárkou:  def rect_area(width, height):

---

Tělo je jeden řádek: return součin obou parametrů.

---

def rect_area(width, height):
    return width * height
""",

"6.2 reference": r"""**Parametr** je jméno v hlavičce funkce, které zastupuje hodnotu dodanou
volajícím. Hodnoty předané ve volání jsou **argumenty**, přiřazené parametrům
zleva doprava.

- `def f(a, b):` deklaruje dva parametry; `f(3, 4)` volá s `a = 3`, `b = 4`.
- Parametry jsou **lokální**: existují jen po dobu volání a nesrážejí se se jmény
  venku. Funkce pracuje s tím, co dostane, což ji činí znovupoužitelnou.
- Předání špatného počtu argumentů vyvolá `TypeError`.

```python
def add(a, b):
    return a + b

add(3, 4)      # 7
```
""",

"6.3 brief": r"""# 6.3 -- return, ne print

## Koncept

`print()` a `return` vypadají od oka při testování podobně, ale dělají úplně jinou
práci:

- `print(x)` `x` **zobrazí** na obrazovce -- a to je vše. Volající nedostane nic.
- `return x` **předá `x` zpět** volajícímu, který ho může uložit, porovnat nebo
  poslat dál.

Funkce, která místo vracení vypisuje, ve skutečnosti vrací `None` (hodnotu „žádná
hodnota“). Rozdíl uštkne ve chvíli, kdy někdo výsledek *použije*:

```python
def shout_wrong(word):
    print(word.upper() + "!")     # shows it... returns None

answer = shout_wrong("hi")        # HI! appears, but...
print(answer)                     # None  -- the caller got nothing
```

Pravidlo: **úkolem funkce je počítat a vracet.** Ať *volající* rozhodne, zda
vypsat.

## Příklad

```python
def shout(word):
    return word.upper() + "!"

print(shout("hi"))      # HI!  -- printed BY THE CALLER
loud = shout("ok")      # and it can be stored instead
```

## Tvůj úkol

Definuj `shout(word)`, která **vrátí** slovo VELKÝMI písmeny s `!` přilepeným na
konec. (`.upper()` je z 2.7.)

## Hotovo, když

- `shout("hi")` vrátí `"HI!"`; `shout("")` vrátí `"!"`.
- Hodnota se *vrací* -- verze, která jen vypisuje, selže, protože checker dostane
  `None`.
""",

"6.3 hints": r"""Pokud checker říká, že dostal None, tvá funkce místo vracení vypisovala.

---

Sestav řetězec pomocí .upper() a + "!", pak ho vrať -- nikde žádný print.

---

def shout(word):
    return word.upper() + "!"
""",

"6.3 reference": r"""**Vrácení** hodnoty a její **vypsání** jsou různé činy a jejich záměna je častá
chyba.

- **`return`** předá hodnotu zpět volajícímu kódu, který ji může uložit, počítat s
  ní nebo ji poslat dál. Hodnota putuje.
- **`print`** zapíše text na obrazovku a vrátí `None`. Hodnota se zobrazí, ale
  nezachytí — `x = print(5)` udělá z `x` `None`.
- Na funkci, která místo vracení vypisuje, nelze stavět. Dej přednost `return`
  výsledku a nech **volajícího** rozhodnout, zda ho vypsat.

```python
def double(n):
    return n * 2        # caller can use it
print(double(5) + 1)    # 11  -- works because double returned
```
""",

"6.4 brief": r"""# 6.4 -- Výchozí hodnoty

## Koncept

Parametr může nést **výchozí hodnotu**: hodnotu použitou, když ji volající vynechá.
Napíšeš ji s `=` na řádku `def`:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")              # "Hello, Ada!"   -- default used
greet("Ada", "Hi")        # "Hi, Ada!"      -- default overridden
```

Tohle už jsi *používal*: `print(..., sep=" ")` z 1.3 -- `sep` má výchozí hodnotu
jednu mezeru, kterou jsi přepsal `sep=", "`. Teď můžeš stejnou flexibilitu vestavět
do vlastních funkcí.

Pravidla: parametry s výchozí hodnotou jdou **za** těmi bez ní a výchozí hodnota se
použije *jen* tehdy, když volající ten argument vynechá.

## Příklad

```python
def repeat(word, times=2):
    return word * times

repeat("ha")        # "haha"
repeat("ha", 3)     # "hahaha"
```

## Tvůj úkol

Definuj `greet(name, greeting="Hello")`, která vrátí `"<greeting>, <name>!"` --
přesně: pozdrav, čárka a mezera, jméno, vykřičník.

## Hotovo, když

- `greet("Ada")` vrátí `"Hello, Ada!"` (výchozí hodnota v akci).
- `greet("Ada", "Hi")` vrátí `"Hi, Ada!"`.
- Bez výchozí hodnoty by jednoargumentové volání spadlo -- checker dělá oba druhy
  volání.
""",

"6.4 hints": r"""Výchozí hodnota jde do řádku def:  def greet(name, greeting="Hello"):

---

Sestav výsledek f-řetězcem: pozdrav, pak ", ", pak jméno, pak "!".

---

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
""",

"6.4 reference": r"""**Výchozí hodnota** v hlavičce dělá parametr volitelným: vynechá-li volající ten
argument, použije se výchozí hodnota.

- `def greet(name, greeting="hi"):` lze volat `greet("Ada")` (použije `"hi"`) nebo
  `greet("Ada", "hello")` (přepíše ji).
- Parametry **s** výchozí hodnotou musí jít **za** těmi bez ní.
- U měnitelných typů používej *novou* výchozí hodnotu při každém volání — napiš
  `def f(items=None):` a pak `if items is None: items = []`, nikdy
  `def f(items=[]):` (jeden sdílený seznam přetrvá mezi voláními).

```python
def power(base, exp=2):
    return base ** exp

power(5)       # 25  -- exp defaults to 2
power(5, 3)    # 125
```
""",

"6.5 brief": r"""# 6.5 -- return ukončí funkci

## Koncept

`return` nejen předá hodnotu -- také **funkci na místě zastaví**. Nic za provedeným
`return` se neprovede. Díky tomu se větvící funkce čtou přehledně: vyřeš každý
případ a odejdi.

```python
def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
```

Všimni si, že tu není žádné `else` -- není potřeba. Pokud vystřelil první `return`,
funkce už skončila; dosáhnout posledního řádku *znamená*, že `n` bylo kladné. Tomuto
stylu se říká **časný return** (early return).

Funkce s několika příkazy `return` stále vrací přesně **jednu** hodnotu na volání:
ten `return`, který se provede první.

## Příklad

```python
sign(-3)    # "negative"
sign(0)     # "zero"
sign(42)    # "positive"
```

## Tvůj úkol

Definuj `sign(n)`, která pro celé číslo `n` vrátí `"negative"`, `"zero"`, nebo
`"positive"`.

## Hotovo, když

- `sign(-3)`, `sign(0)`, `sign(42)` vrátí tři výše uvedená slova.
- Hraniční případy `-1` a `1` jsou také správně.
""",

"6.5 hints": r"""Každý případ je if s vlastním return. Jakmile return proběhne, funkce je u konce.

---

Nejprve zkontroluj `n < 0`, pak `n == 0`; pokud ani jeden nevrátil, musí být n
kladné -- prostě vrať "positive" bez podmínky.

---

def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
""",

"6.5 reference": r"""`return` se může objevit **kdekoli** ve funkci a jeho dosažení volání ihned ukončí
— pozdější řádky se neprovedou. **Časný return** toho využívá k ošetření případu a
okamžitému odchodu.

- Zplošťuje kód: ošetři speciální nebo neplatný případ na začátku stráží
  (`if bad: return ...`), pak napiš hlavní cestu bez jejího vnoření do `else`.
- Vítězí první dosažený `return`; nic za ním se v tom volání neprovede.

```python
def reciprocal(n):
    if n == 0:
        return None     # bail out early on the bad case
    return 1 / n        # main path, not indented under an else
```
""",

"6.6 brief": r"""# 6.6 -- Vrácení dvou hodnot

## Koncept

`return` může předat **několik hodnot najednou** -- odděl je čárkou a Python je
zabalí do **n-tice** (4.7):

```python
def min_max(nums):
    return min(nums), max(nums)
```

Volající si může n-tici ponechat, nebo ji rozbalit rovnou do proměnných -- stejné
rozbalování, jaké jsi použil u `a, b = b, a`:

```python
pair = min_max([3, 1, 4])     # (1, 4)  -- one tuple
lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4  -- unpacked
```

Takto pythonovské funkce vracejí „dvě odpovědi“ -- není v tom žádný zvláštní trik,
jen n-tice a rozbalování.

## Příklad

```python
def split_name(full):
    parts = full.split()
    return parts[0], parts[-1]

first, last = split_name("Ada King Lovelace")
# first = "Ada", last = "Lovelace"
```

## Tvůj úkol

Definuj `min_max(nums)`, která vrátí nejmenší a největší položku neprázdného
seznamu, **v tomto pořadí**, jako n-tici. (`min()`/`max()` jsou z 5.3.)

## Hotovo, když

- `min_max([3, 1, 4])` vrátí `(1, 4)` -- n-tici, nejmenší první.
- `min_max([7])` vrátí `(7, 7)`.
- Záporná čísla fungují.
""",

"6.6 hints": r"""Dvě hodnoty za jedním return, oddělené čárkou, se vrátí jako n-tice.

---

Obě poloviny už máš z 5.3: `return min(nums), max(nums)`.

---

def min_max(nums):
    return min(nums), max(nums)
""",

"6.6 reference": r"""Funkce vrací **jeden** objekt, ale tím objektem může být **n-tice**, takže
`return a, b` předá několik hodnot najednou (Python je zabalí do n-tice). Volající
je **rozbalí** odpovídajícími jmény.

- `return lo, hi` vrátí n-tici `(lo, hi)`; `low, high = bounds(xs)` ji rozbalí do
  dvou jmen.
- Při rozbalování se počty musí shodovat. Chceš-li, zachyť celou n-tici jedním
  jménem: `result = bounds(xs)` a pak `result[0]`, `result[1]`.

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4
```
""",

"6.7 brief": r"""# 6.7 -- Stavění na vestavěných funkcích

## Koncept

Funkce zazáří, když zabalí malý *recept* za dobré jméno. Recept na průměr:

> součet, vydělený počtem

Vlastníš každou přísadu: `sum()` (5.2), `len()` (2.6) a `/` (1.9). Pamatuj z 1.9,
že `/` **vždy vrací float** -- `4 / 2` je `2.0`, ne `2`. To je tady správně: průměr
je přirozeně desetinné číslo.

```python
def average(nums):
    return sum(nums) / len(nums)
```

Jedna funkce, jeden řádek, okamžitě znovupoužitelné -- a jméno říká, co ten řádek
znamená.

## Příklad

```python
average([1, 2])        # 1.5
average([10, 20, 30])  # 20.0
```

## Tvůj úkol

Definuj `average(nums)`, která vrátí průměr neprázdného seznamu čísel.

## Hotovo, když

- `average([1, 2])` vrátí `1.5`; `average([10, 20, 30])` vrátí `20.0`.
- Výsledek je **float**, i když je dělení přesné (použij `/`, ne `//`).
- Jednopoložkový seznam vrátí tu položku (jako float).
""",

"6.7 hints": r"""Průměr je součet dělený počtem -- a pro každou polovinu máš vestavěnou funkci.

---

`sum(nums)` přes `len(nums)`, pomocí `/` (float dělení z 1.9).

---

def average(nums):
    return sum(nums) / len(nums)
""",

"6.7 reference": r"""Funkce **skládají vestavěné funkce** do pojmenované, znovupoužitelné operace.
Funkce `average` je modelem: obalí `sum` a `len` za jedno jasné jméno.

- `return sum(nums) / len(nums)` spočítá průměr — ale `len(nums)` je pro prázdný
  seznam `0`, což vyvolá `ZeroDivisionError`, takže to ošetři časným returnem.
- Pojmenování operace (`average(scores)`) dělá volající kód čitelným jako záměr a
  oprava nebo vylepšení logiky se děje na jednom místě.

```python
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

average([2, 4, 9])    # 5.0
```
""",

"6.8 brief": r"""# 6.8 -- Funkce volající funkce

## Koncept

Tvé funkce mohou volat **jedna druhou**. To je opravdový tahák: vyřeš malý problém
jednou, pojmenuj ho a postav na něm další funkci.

```python
def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
```

`same_word` neopakuje recept ořež-a-zmenši -- *deleguje* na `clean`. Pokud `clean`
někdy vylepšíš (řekněme, že bude odstraňovat i interpunkci), každá funkce na něm
postavená se vylepší zadarmo. Opakování receptu na obou místech je způsob, jak se
rodí chyby: opravíš jednu kopii, na druhou zapomeneš.

Všimni si, že `same_word` vrací výsledek porovnání -- **boolean** (`True`/`False`),
jako v 3.1. Žádné `if` není potřeba: `clean(a) == clean(b)` už *je* odpovědí.

## Příklad

```python
clean("  Tea ")              # "tea"
same_word("  Tea ", "tea")   # True
same_word("tea", "milk")     # False
```

## Tvůj úkol

Definuj **obě** funkce:

- `clean(text)` -- vrátí text s oříznutými okolními mezerami a malými písmeny (2.7).
- `same_word(a, b)` -- vrátí `True` právě tehdy, když jsou oba texty po vyčištění
  stejné. Musí **volat `clean`**, ne recept opakovat.

## Hotovo, když

- `clean("  Tea ")` vrátí `"tea"`.
- `same_word("  Tea ", "tea")` je `True`; `same_word("tea", "milk")` je `False`.
- `same_word` volá `clean` -- checker hledá tu delegaci.
""",

"6.8 hints": r"""Nejprve napiš clean a v hlavě si ho odlaď: .strip() pak .lower(), zřetězené.

---

same_word je jeden řádek: porovnej clean(a) s clean(b) pomocí == a vrať výsledek
-- porovnání už SAMO je True nebo False.

---

def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
""",

"6.8 reference": r"""Funkce **volají jiné funkce**, takže větší úloha se staví z malých, ověřených
dílů. Výsledek jedné se stává argumentem nebo stavebním kamenem další.

- Pomocná funkce dělá jednu věc dobře; funkce vyšší úrovně volá několik pomocných
  a kombinuje jejich výsledky. To je jádro strukturování programu.
- `f(g(x))` předá výsledek `g` rovnou do `f`. Každá funkce zůstává jednoduchá a
  nezávisle ověřitelná.

```python
def clean(s):  return s.strip().lower()
def is_yes(s): return clean(s) == "yes"

is_yes("  YES ")   # True  -- is_yes builds on clean
```
""",

"6.9 brief": r"""# 6.9 -- Rekurze: funkce volající sebe sama

## Koncept

Funkce může volat **sebe sama**. Tomu se říká **rekurze** a funguje vždy, když
problém obsahuje menší kopii téhož problému.

Faktoriál je klasika: `5!` znamená `5 * 4 * 3 * 2 * 1`. Ale podívej se znovu:

> `5!` je prostě `5 * 4!` -- a `4!` je `4 * 3!` ...

Rekurzivní funkce přesně tohle vyjadřuje, plus **základní případ** -- nejmenší
vstup zodpovězený přímo, bez dalších volání:

```python
def fact(n):
    if n == 0:
        return 1            # base case: 0! is 1
    return n * fact(n - 1)  # the smaller copy of the same problem
```

`fact(3)` proběhne jako `3 * fact(2)` -> `3 * 2 * fact(1)` -> `3 * 2 * 1 * fact(0)`
-> `3 * 2 * 1 * 1` = `6`. Bez základního případu by se volání nikdy nezastavila --
rekurzivní verze nekonečného cyklu.

Faktoriál bys mohl spočítat cyklem `for` -- ale *lekce* je tady to volání sebe sama,
takže tato úloha ho vyžaduje.

## Příklad

```python
fact(0)    # 1
fact(3)    # 6
fact(5)    # 120
```

## Tvůj úkol

Definuj `fact(n)`, která vrátí `n!` **rekurzivně**: základní případ pro `0` a
`n * fact(n - 1)` pro zbytek. `n` nikdy není záporné.

## Hotovo, když

- `fact(0)` je `1`, `fact(1)` je `1`, `fact(5)` je `120`.
- `fact` volá sebe sama -- checker hledá volání sebe sama, takže verze s cyklem
  neprojde.
""",

"6.9 hints": r"""Nejprve zodpověz nejmenší případ: pokud je n 0, vrať 1 -- žádné volání není
potřeba.

---

Pro vše ostatní důvěřuj funkci, kterou píšeš:
return n * fact(n - 1). Časný return (6.5) udrží základní případ čistý.

---

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
""",

"6.9 reference": r"""**Rekurzivní** funkce volá **sebe sama**, aby vyřešila menší verzi téhož
problému. Dvě části jsou nezbytné:

- **základní případ**, který vrací přímo **bez** rekurze — to rekurzi zastaví;
- **rekurzivní případ**, který funkci zavolá na menším vstupu a staví na výsledku,
  přičemž se pokaždé posouvá k základnímu případu.

Vynech nebo nikdy nedosáhni základního případu a volání se vnořují, dokud Python
nevyvolá `RecursionError`. Mnoho rekurzí má jednodušší tvar cyklem; rekurze zazáří,
když je problém sám sobě podobný.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # smaller subproblem

factorial(4)   # 24
```
""",

"6.10 brief": r"""# 6.10 -- Závěrečná: malá knihovna

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
""",

"6.10 hints": r"""count_vowels je sčítání přes znaky: cyklus `for ch in word` a test `ch in
"aeiou"`.

---

describe zavolá count_vowels jednou, uloží číslo, pak časně vrátí znění "no
vowels", když je 0; jinak f-řetězec s počtem.

---

def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count = count + 1
    return count

def describe(word):
    n = count_vowels(word)
    if n == 0:
        return f"{word} has no vowels"
    return f"{word} has {n} vowels"
""",

"6.10 reference": r"""**Knihovna** zde znamená sadu souvisejících funkcí, které jsi napsal, každá
pojmenovaná podle svého úkolu, jež dohromady tvoří znovupoužitelnou sadu nástrojů —
odměnu kapitoly.

- Stav malé funkce, z nichž každá dělá jednu věc a `return` svůj výsledek; pak je
  funkce vyšší úrovně volají. Volající kód se čte jako sled záměrů.
- Držet logiku uvnitř pojmenovaných funkcí (místo kopírování inline) znamená, že
  oprava nebo vylepšení dopadne na jedno místo a každý volající z toho těží.

```python
def clean(s):    return s.strip().lower()
def words(s):    return clean(s).split()
def wordcount(s): return len(words(s))

wordcount("  The quick fox ")   # 3  -- each function builds on the last
```
""",
}
