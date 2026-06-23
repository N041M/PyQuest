# PyQuest translations -- language 'cs' -- chapter 07_errors -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"7.1 brief": r"""# 7.1 -- try / except

## Koncept

Doteď jsi spoustu chyb *způsobil*. Čas jednu **ošetřit**.

Když Python narazí na něco nemožného -- jako `int("hello")` -- **vyvolá výjimku**:
normální tok se zastaví a, pokud se s tím nikdo nevypořádá, program spadne s
traceblackem. `try`/`except` je způsob, jak se s tím vypořádat:

```python
try:
    n = int(text)
    print("a number!")
except ValueError:
    print("not a number")
```

Jak to běží:

- Blok `try` běží normálně -- **dokud** nějaký řádek nevyvolá chybu.
- Pokud nic nevyvolá chybu, blok `except` se zcela přeskočí.
- Pokud `int(text)` vyvolá `ValueError` (jeho stížnost na nepřevoditelný text),
  zbytek bloku `try` se opustí a místo něj se spustí blok `except`. **Žádný pád.**

Program se *zotaví*: zvolil, co znamená selhání, místo aby se skácel.

## Příklad

Vstup `7` vypíše `14`. Vstup `seven` vypíše `not a number` -- stejný kód, žádný pád
v ani jednom případě.

## Tvůj úkol

Přečti jeden řádek. Pokud se převede na celé číslo, vypiš to číslo **zdvojnásobené**.
Pokud ne, vypiš přesně `not a number`. (Tohle je zase skriptová úloha: `input()` a
`print()` jsou zpět.)

## Hotovo, když

- `7` vypíše `14`; `-3` vypíše `-6`.
- `seven` a `12abc` vypíšou `not a number` -- a program skončí čistě, bez
  tracebacku.
- Použil jsi `try`/`except` -- checker vyžaduje skutečnou věc.
""",

"7.1 hints": r"""int("seven") vyvolá ValueError -- dej převod dovnitř bloku try.

---

try: převeď a vypiš dvojnásobek. except ValueError: vypiš zprávu.
Blok except se spustí jen tehdy, když převod selhal.

---

line = input()
try:
    n = int(line)
    print(n * 2)
except ValueError:
    print("not a number")
""",

"7.1 reference": r"""Příkaz **`try` / `except`** spustí rizikový kód a chybu zachytí, pokud selže,
místo aby nechal program spadnout. Blok `try` drží kód, který může **vyvolat
chybu**; blok `except` se spustí jen tehdy, když k tomu dojde.

- Pokud blok `try` uspěje, `except` se zcela přeskočí.
- Pokud nějaký příkaz v `try` vyvolá chybu, **zbytek `try` se opustí** a řízení
  skočí na odpovídající `except`; program pak pokračuje níže.
- Nezachycená chyba rozvine celý program s tracebackem — `except` je způsob, jak
  zasáhnout.

```python
try:
    n = int(text)        # may raise ValueError
except ValueError:
    n = 0                # recover instead of crashing
```
""",

"7.2 brief": r"""# 7.2 -- Zachyť SPRÁVNOU chybu

## Koncept

`except` může pojmenovat, kterou chybu ošetří -- a měl by. Chyby, které jsi
nečekal, jsou **informace**, a jejich spolknutí skrývá bugy.

```python
try:
    n = int(text)
except ValueError:        # exactly the error int() raises for bad TEXT
    n = None
```

Lákavá zkratka je holé `except:` (nebo `except Exception:`) -- „chyť všechno,
nemůže to spadnout!“ Ale *všechno* zahrnuje chyby, které znamenají, že **tvůj kód
je špatně používán**. `int([1, 2])` nevyvolá `ValueError` -- vyvolá `TypeError`
(„úplně špatný druh věci“), a ten by *měl* spadnout nahlas, aby se bug volajícího
našel, ne zalepil.

Pravidlo: **chytej přesně to, co čekáš; vše ostatní nech uniknout.**

## Příklad

```python
safe_int("42")      # 42
safe_int("nope")    # None         (ValueError, handled)
safe_int([1, 2])    # TypeError!   (NOT handled -- a misuse, let it crash)
```

## Tvůj úkol

Definuj `safe_int(text)`, která vrátí `int(text)`, nebo `None`, když text není
platné číslo. Chytej **jen** `ValueError` -- `TypeError` z neřetězce musí
uniknout.

## Hotovo, když

- `safe_int("42")` je `42`; `safe_int("-7")` je `-7`.
- `safe_int("nope")` a `safe_int("")` jsou `None`.
- `safe_int([1, 2])` vyvolá `TypeError` -- checker ji schválně volá se seznamem,
  takže chytání příliš mnoha selže.
""",

"7.2 hints": r"""return int(text) uvnitř try; except místo toho vrátí None.

---

Pojmenuj chybu: `except ValueError:` -- nepojmenovat nic (nebo Exception) chytí i
TypeError, který checker posílá, a ten musí uniknout.

---

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
""",

"7.2 reference": r"""`except` by měl pojmenovat **konkrétní** výjimku, kterou čekáš. Zachycení přesně
správného typu nechá nečekané chyby vyplout jako bugy, místo aby byly tiše
spolknuty.

- `except ValueError:` chytá jen tento typ; nesouvisející selhání (překlep ve
  jméně vyvolávající `NameError`) se stále šíří dál, což je to, co chceš.
- Holé `except:` (nebo `except Exception:`) chytá **všechno**, včetně bugů, které
  bys raději viděl — vyhni se mu, pokud opravdu nemyslíš „jakékoli selhání“.
- Přizpůsob typ operaci: `int()` vyvolá `ValueError`, indexování `IndexError`,
  vyhledání ve slovníku `KeyError`.

```python
try:
    value = data[key]
except KeyError:         # only a missing key, not other bugs
    value = None
```
""",

"7.3 brief": r"""# 7.3 -- ZeroDivisionError: žádej o odpuštění

## Koncept

Dělení nulou vyvolá `ZeroDivisionError`. Existují dva způsoby, jak napsat dělení,
které to přežije:

```python
# "look before you leap": test first
if b == 0:
    return None
return a / b

# "easier to ask forgiveness": just try it
try:
    return a / b
except ZeroDivisionError:
    return None
```

Oba se *tady* chovají stejně -- ale pythonovský styl silně preferuje ten druhý a
tato úloha ho vyžaduje. Proč:

- `try` pojmenuje skutečnou událost („dělení selhalo“) místo předpokladu, který s
  ní musíš držet v souladu.
- Předběžné kontroly se neškálují: skutečné operace mohou selhat tuctem způsobů
  (chybějící soubor, odepřené oprávnění, přerušené spojení...). Nemůžeš je všechny
  předem otestovat -- ale jediný `except` může zachytit samotné selhání.

Tomuto stylu se říká **EAFP**: *snazší žádat o odpuštění než o povolení* (easier to
ask forgiveness than permission).

## Příklad

```python
safe_div(10, 4)    # 2.5
safe_div(5, 0)     # None  -- handled, no crash
```

## Tvůj úkol

Definuj `safe_div(a, b)`, která vrátí `a / b`, nebo `None`, když je `b` nula --
pomocí `try`/`except`, ne `if`.

## Hotovo, když

- `safe_div(10, 4)` je `2.5`; `safe_div(5, 0)` je `None`.
- `safe_div(0, 5)` je `0.0` -- nula NAHOŘE je v pořádku.
- Zachytil jsi `ZeroDivisionError` -- if-test se lekci vyhne a selže.
""",

"7.3 hints": r"""Zkus dělení uvnitř try -- netestuj b napřed.

---

`except ZeroDivisionError: return None` -- časný return (6.5) uvnitř try ošetří
šťastnou cestu.

---

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
""",

"7.3 reference": r"""Dělení nulou vyvolá **`ZeroDivisionError`**. Jeho zachycení předvádí styl **EAFP**
— „snazší žádat o odpuštění než o povolení“: zkus operaci a ošetři selhání, místo
abys nejprve testoval každý špatný případ.

- `a / 0` i `a // 0` i `a % 0` vyvolají chybu. Obalení dělení do `try` ti umožní
  dodat náhradní hodnotu, když se dělitel ukáže být nula.
- EAFP se často čte čistěji než hlídací `if b != 0:` a vyhne se závodu mezi
  kontrolou a použitím.

```python
try:
    rate = hits / total
except ZeroDivisionError:
    rate = 0.0           # no data yet -- sensible fallback
```
""",

"7.4 brief": r"""# 7.4 -- IndexError a bezpečný přístup

## Koncept

Indexování za konec seznamu vyvolá `IndexError`:

```python
items = ["a", "b"]
items[5]      # IndexError!
```

„Bezpečné získání“ vrátí náhradní hodnotu místo pádu -- a je to další místo, kde
*zkoušení* poráží *předběžné testování*. Pamatuj, že záporné indexy jsou **platné**
(2.2): `items[-1]` je poslední položka, `items[-2]` ta před ní. Ručně psaná
kontrola mezí musí trefit `0 <= i`... ne počkat, `-len <= i < len`... přesně
správně, ve dvou směrech. Nebo to prostě zkusíš:

```python
try:
    return items[i]
except IndexError:
    return default
```

`except` je správný *z definice* -- vystřelí přesně tehdy, když sám Python řekne,
že je index špatný, záporné včetně.

## Příklad

```python
item_or(["a", "b"], 0, "?")     # "a"
item_or(["a", "b"], -1, "?")    # "b"   -- valid negative index
item_or(["a", "b"], 5, "?")     # "?"   -- out of range, fallback
```

## Tvůj úkol

Definuj `item_or(items, i, default)`, která vrátí `items[i]`, nebo `default`, když
je `i` mimo rozsah -- pomocí `try`/`except IndexError`.

## Hotovo, když

- `item_or(["a", "b"], 1, "?")` je `"b"`; index `5` dá `"?"`.
- `item_or(["a", "b"], -1, "?")` je `"b"` -- záporné, které se vejdou, jsou platné.
- `item_or([], 0, "?")` je `"?"` -- prázdný seznam nemá platný index.
- Použil jsi `try`/`except` -- aritmetika mezí se lekci vyhne a selže.
""",

"7.4 hints": r"""Prostě to zaindexuj uvnitř try -- Python už přesně ví, které indexy jsou špatné.

---

`except IndexError: return default` -- tím zvládneš záporné zadarmo, což ručně
psaná kontrola mezí obvykle ne.

---

def item_or(items, i, default):
    try:
        return items[i]
    except IndexError:
        return default
""",

"7.4 reference": r"""Indexování za konec seznamu (nebo řetězce) vyvolá **`IndexError`**. Jeho zachycení
promění rizikové vyhledání v **bezpečný přístup**, který vrátí náhradní hodnotu,
když pozice neexistuje.

- `lst[i]` vyvolá chybu, je-li `i >= len(lst)` (nebo `i < -len(lst)`); `except`
  místo pádu dodá výchozí hodnotu.
- Tohle je EAFP protějšek kontroly `if i < len(lst):` napřed — užitečné, když je
  případ mimo rozsah normální, ne bug.

```python
def get(lst, i, default=None):
    try:
        return lst[i]
    except IndexError:
        return default   # position absent -> fallback
```
""",

"7.5 brief": r"""# 7.5 -- raise: chyby jsou taky tvoje

## Koncept

Dosud jsi *chytal* chyby, které vyvolal Python. Můžeš také **vyvolat vlastní** -- a
dobré funkce to dělají, ve chvíli, kdy dostanou něco nesmyslného:

```python
def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

`raise` chybu vytvoří a hned ji vyhodí: funkce se zastaví a volající dostane stejné
zacházení, jaké mu dá `int("nope")` -- chytatelné pomocí `try`, hlasité, když se
ignoruje.

Proč vyvolat chybu místo vrácení něčeho jako `None` nebo `-1`? Protože špatná
hodnota putuje: uloží se, přičte, vypíše, a pád (pokud nějaký) nastane daleko od
skutečné chyby. Raise připne selhání k okamžiku a ke zprávě --
`ValueError("age cannot be negative")` říká přesně, co se pokazilo a kde. Smetí
dovnitř, **chyba** ven -- nikdy smetí ven.

## Příklad

```python
checked_age(30)     # 30
checked_age(0)      # 0    -- zero is a fine age
checked_age(-1)     # ValueError: age cannot be negative
```

## Tvůj úkol

Definuj `checked_age(age)`, která vrátí věk beze změny -- ale vyvolá `ValueError`,
když je záporný. Dej mu zprávu říkající, co je špatně.

## Hotovo, když

- `checked_age(30)` vrátí `30`; `checked_age(0)` vrátí `0`.
- `checked_age(-1)` vyvolá `ValueError`.
- Použil jsi `raise` -- checker hledá samotný příkaz.
""",

"7.5 hints": r"""Nejprve stráž, pak return: je-li věk záporný, vyvolej chybu; jinak je v pořádku
tak, jak je.

---

Stráž jsou dva řádky:  if age < 0:  pak
raise ValueError("age cannot be negative").

---

def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
""",

"7.5 reference": r"""**`raise`** spustí výjimku **ty sám**, zastaví funkci a signalizuje, že je něco
špatně. Umožní tvému kódu odmítnout špatný vstup v bodě, kde je zjištěn, stejně
jako to dělají vestavěné funkce.

- `raise ValueError("amount must be positive")` sestaví výjimku se zprávou a vyhodí
  ji; běh se zastaví, pokud ji nezachytí nějaký `try` výše v řetězci volání.
- Zvol typ, který sedí: `ValueError` pro špatnou hodnotu, `TypeError` pro špatný
  typ. Zpráva vysvětlí, co se očekávalo.
- Vyvolání chyby na hranici (jak vstup přichází) udrží zbytek kódu schopným
  důvěřovat svým datům.

```python
def withdraw(amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    ...
```
""",

"7.6 brief": r"""# 7.6 -- Zeptej se znovu: opakovací cyklus

## Koncept

Klasické použití `try`/`except` ve skutečném programu: **ptej se, dokud vstup
nedává smysl.** Spoj cyklus `while True` (3.7), `break` (3.11) a `except` ze 7.1:

```python
while True:
    try:
        n = int(input())
        break              # got a good one -- leave the loop
    except ValueError:
        pass               # bad line -- silently go around again
```

Tvar k zvnitřnění:

- **šťastná cesta** končí `break`;
- **except** pohltí selhání a nechá cyklus zkusit znovu;
- po cyklu je `n` zaručeně platné -- kód níže mu může důvěřovat.

(`pass` je pythonovský příkaz „nedělej nic“ -- blok except musí obsahovat *něco*.)

## Příklad

Pro vstupní řádky `cat`, `dog`, `21` program první dva ignoruje a vypíše `42`.

## Tvůj úkol

Čti řádky, dokud se jeden nepřevede na celé číslo, pak vypiš to číslo
**zdvojnásobené**. Špatné řádky nevyprodukují žádný výstup.

## Hotovo, když

- `21` jako první řádek vypíše `42`.
- `cat`, `dog`, `21` také vypíše jen `42` -- smetí se tiše zkusí znovu.
- Záporná čísla fungují.
- Použil jsi cyklus a `try`/`except`.
""",

"7.6 hints": r"""while True kolem try: převeď-a-break; except prostě jde znovu dokola.

---

except ValueError: pass  -- `pass` znamená „nedělej nic“, což tady znamená
„zkus znovu“. Vypiš AŽ PO cyklu, kde je n zaručeně dobré.

---

while True:
    try:
        n = int(input())
        break
    except ValueError:
        pass
print(n * 2)
""",

"7.6 reference": r"""**Opakovací cyklus** se ptá, dokud nezíská platnou hodnotu. Spojuje `while True` s
`try` / `except`: uspěj a `break` ven; selhej a obtoč se, abys se zeptal znovu.

- `try` zkusí parsování/operaci; úspěšná cesta končí `break`, který opustí cyklus.
- `except` ošetří špatný vstup (často jen vypíše nápovědu a propadne dál), takže
  `while True` proběhne další kolo.
- `while True` bez jiného východu spoléhá na ten `break` — platný případ je jediná
  cesta ven.

```python
while True:
    try:
        n = int(input("number: "))
        break                 # valid -> leave the loop
    except ValueError:
        print("not a number, try again")
```
""",

"7.7 brief": r"""# 7.7 -- Čtení chyby: except ... as e

## Koncept

Výjimka není jen signál -- je to **objekt nesoucí zprávu**. Zachyť ji *do
proměnné* pomocí `as` a můžeš tu zprávu použít:

```python
try:
    n = int(text)
except ValueError as e:
    print(e)
```

Pro `text = "5x"` to vypíše Pythonovu vlastní diagnózu:

```
invalid literal for int() with base 10: '5x'
```

`e` je objekt chyby; jeho vypsání ukáže jeho zprávu. Takto skutečné programy logují,
co se opravdu pokazilo, místo vágního „něco selhalo“ -- rozdíl mezi hlášením bugu,
podle kterého můžeš jednat, a tím, podle kterého ne.

(Zprávu tu nepíšeš sám -- *předáváš* tu, kterou Python připojil, když chybu
vyvolal.)

## Příklad

Vstup `7` vypíše `7`. Vstup `5x` vypíše
`invalid literal for int() with base 10: '5x'`.

## Tvůj úkol

Přečti jeden řádek. Pokud se převede na celé číslo, vypiš to číslo. Pokud ne, chyť
`ValueError` **jako `e`** a vypiš samotné `e` -- Pythonovu zprávu, ne svou vlastní.

## Hotovo, když

- `7` vypíše `7`.
- `5x` vypíše přesnou zprávu `invalid literal ...: '5x'` -- s urážlivým textem v ní
  v uvozovkách.
- Zprávu jsi nenapsal ručně (musí sedět pro *jakýkoli* vstup, což trefí jen
  vypsání `e`).
""",

"7.7 hints": r"""`as e` jde rovnou do řádku except:  except ValueError as e:

---

Uvnitř bloku except prostě print(e) -- objekt se vypíše jako svá zpráva.

---

line = input()
try:
    print(int(line))
except ValueError as e:
    print(e)
""",

"7.7 reference": r"""**`except ValueError as e:`** naváže zachycený **objekt** výjimky na jméno, takže
ho můžeš prozkoumat — nejjednodušeji jeho vypsáním, abys ukázal, co se pokazilo.

- Objekt výjimky nese detail; `str(e)` (nebo `print(e)`) dá jeho zprávu.
  `type(e).__name__` dá jméno třídy chyby.
- Jméno `e` existuje jen uvnitř bloku `except`.
- Jeden handler může chytit celou rodinu pojmenováním základní třídy:
  `except Exception as e:` naváže kteroukoli z jejích podtříd (používej střídmě —
  široké chytání skrývá bugy).

```python
try:
    int("xyz")
except ValueError as e:
    print("bad input:", e)    # bad input: invalid literal for int()...
```
""",

"7.8 brief": r"""# 7.8 -- Závěrečná: odolná kalkulačka

## Koncept

Jeden `try` může mít **několik** bloků `except` -- jeden na každý druh selhání,
každý si volí vlastní zotavení:

```python
try:
    ...
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
```

Kterákoli chyba se vyvolá, vybere svůj odpovídající blok; ostatní se přeskočí. Tato
závěrečná úloha zapojí celou kapitolu do klasického cvičení: kalkulačky, kterou
**nelze shodit** jejím vstupem. Potřebuje také `split` (4.4), indexování (2.1),
`elif` (3.4) a `/` (1.9).

## Příklad

```
input "8 + 5"   ->  13
input "9 / 2"   ->  4.5
input "9 / 0"   ->  cannot divide
input "two * 3" ->  bad number
input "8 ? 5"   ->  unknown op
```

## Tvůj úkol

Přečti jeden řádek tvaru `<číslo> <op> <číslo>` (tři části oddělené mezerami). Pro
operace `+`, `-`, `*` vypiš celočíselný výsledek; pro `/` vypiš výsledek typu float.
Ošetři každé selhání:

- část, která není celé číslo -> vypiš `bad number`
- dělení nulou -> vypiš `cannot divide`
- jakýkoli jiný symbol operace -> vypiš `unknown op`

## Hotovo, když

- `8 + 5` -> `13`, `9 / 2` -> `4.5`, `3 * -2` -> `-6`.
- `9 / 0` -> `cannot divide`; `two * 3` -> `bad number`; `8 ? 5` -> `unknown op`.
- Žádný vstup ji neshodí: každé selhání vypíše svou vlastní zprávu přes bloky
  `except` (a `else`/`elif` pro neznámou operaci).
""",

"7.8 hints": r"""split() řádek na tři části; převeď parts[0] a parts[2] uvnitř try.

---

Naskládej dva excepty za jeden try: ValueError -> "bad number",
ZeroDivisionError -> "cannot divide". Řetěz operací je if/elif/else, s else
vypisujícím "unknown op".

---

parts = input().split()
try:
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("unknown op")
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
""",

"7.8 reference": r"""Po jediném `try` může následovat **několik klauzulí `except`**, každá ošetřuje jiné
selhání svou vlastní reakcí. Testují se shora dolů; spustí se **první**
odpovídající typ a zbytek se přeskočí.

- Tím se staví odolné zpracování vstupu: jeden `try` kolem práce, pak `except` na
  každou věc, která se může pokazit (`ValueError` pro špatné číslo,
  `ZeroDivisionError` pro `/0`), každý s vlastní zprávou.
- Řaď od konkrétního k obecnému, jsou-li typy příbuzné, protože vítězí první
  shoda.

```python
try:
    a, b = int(x), int(y)
    print(a / b)
except ValueError:
    print("please enter whole numbers")
except ZeroDivisionError:
    print("cannot divide by zero")
```
""",
}
