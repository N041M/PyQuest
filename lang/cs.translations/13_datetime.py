# PyQuest translations -- language 'cs' -- chapter 13_datetime -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"13.1 brief": r"""# 13.1 -- date: kalendářní den

## Koncept

Modul **`datetime`** modeluje skutečná kalendářní data a hodinové časy. Jeho typ
**`date`** drží jediný den -- rok, měsíc, den -- jako jeden objekt:

```python
from datetime import date

d = date(2026, 6, 20)
d.year      # 2026
d.isoformat()   # '2026-06-20'
```

- `date(year, month, day)` objekt sestaví a **validuje** ho: `date(2026, 13, 1)`
  vyvolá chybu, protože měsíc 13 neexistuje.
- `.isoformat()` ho vykreslí jako standardní řetězec `YYYY-MM-DD`, doplněný nulami.
- `date` je mnohem lepší než tři volná celá čísla: zná kalendář, takže se umí
  porovnat, odečíst a naformátovat.

## Příklad

```python
from datetime import date

def new_year(year):
    return date(year, 1, 1).isoformat()
```

## Tvůj úkol

Pomocí **`date`** z `datetime` definuj `iso(y, m, d)`, která datum sestaví a vrátí
jeho řetězec `YYYY-MM-DD` přes `.isoformat()`.

## Hotovo, když

- `iso(2026, 6, 20)` vrátí `"2026-06-20"`.
- `iso(1999, 1, 5)` vrátí `"1999-01-05"` (všimni si doplnění nulami).
- Řetězec pochází z `.isoformat()` objektu `date`, ne z ručního formátování.
""",

"13.1 hints": r"""`from datetime import date`, pak `date(y, m, d)` vytvoří objekt. Má metodu
`.isoformat()`, která vrátí řetězec YYYY-MM-DD.

---

Zřetěz je: `date(y, m, d).isoformat()`. Doplnění nulami se vyřeší za tebe.

---

from datetime import date


def iso(y, m, d):
    return date(y, m, d).isoformat()
""",

"13.1 reference": r"""Modul **`datetime`** poskytuje typy pro kalendářní data a hodinové časy. Jeho typ
**`date`** drží jeden den jako jeden objekt: `date(year, month, day)`.

- Konstruktor hodnoty **validuje** proti skutečnému kalendáři — `date(2026, 2, 30)`
  vyvolá `ValueError`, takže nemožné datum neproklouzne.
- Atributy `.year`, `.month`, `.day` přečtou části zpět; **`.isoformat()`** vykreslí
  standardní řetězec `YYYY-MM-DD`, vždy doplněný nulami.
- `date` zná kalendář, takže se umí porovnat (`<`, `==`), odečíst (13.5) a nahlásit
  svůj den v týdnu (13.3) — věci, které tři volná celá čísla nebo ručně sestavený
  řetězec neumějí. `date.today()` vrátí aktuální den.

```python
from datetime import date

d = date(2026, 6, 20)
d.month          # 6
d.isoformat()    # '2026-06-20'
date(2026, 1, 5).isoformat()   # '2026-01-05'  -- padded
```
""",

"13.2 brief": r"""# 13.2 -- fromisoformat: text na datum

## Koncept

Data obvykle dorazí jako **text** -- ze souboru, z formuláře, z API.
**`date.fromisoformat`** rozparsuje standardní řetězec `YYYY-MM-DD` na skutečný
objekt `date`, inverze k `.isoformat()`:

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
d.year      # 2026
d.month     # 6
d.day       # 20
```

- Vrátí `date`, takže pak můžeš číst `.year` / `.month` / `.day`, porovnat ho nebo s
  ním počítat -- vše, co datum umí.
- Očekává přesný tvar `YYYY-MM-DD`; chybně utvořený řetězec vyvolá `ValueError`.

Parsování na skutečné datum (místo abys řetězec sám řezal) znamená, že hodnota je
zvalidovaná a připravená pro kalendářní práci.

## Příklad

```python
from datetime import date

def month_of(text):
    return date.fromisoformat(text).month
```

## Tvůj úkol

Pomocí **`date.fromisoformat`** definuj `parts(text)`, která rozparsuje řetězec
`YYYY-MM-DD` a vrátí n-tici celých čísel `(year, month, day)` přečtenou z atributů
objektu data.

## Hotovo, když

- `parts("2026-06-20")` vrátí `(2026, 6, 20)`.
- `parts("1999-01-05")` vrátí `(1999, 1, 5)`.
- Hodnoty pocházejí z atributů rozparsovaného `date`, ne z `text.split("-")`.
""",

"13.2 hints": r"""`date.fromisoformat(text)` promění řetězec na objekt data. Ulož ho do proměnné.

---

Přečti `d.year`, `d.month`, `d.day` z toho objektu a vrať je jako n-tici.

---

from datetime import date


def parts(text):
    d = date.fromisoformat(text)
    return (d.year, d.month, d.day)
""",

"13.2 reference": r"""**`date.fromisoformat(text)`** rozparsuje standardní řetězec `YYYY-MM-DD` na objekt
`date` — inverze k `.isoformat()`. Výsledek je skutečné datum, takže můžeš číst jeho
atributy, porovnat ho nebo s ním počítat.

- Očekává přesný ISO tvar; chybně utvořený nebo nemožný řetězec vyvolá `ValueError`,
  což jako vedlejší účinek validuje vstup.
- `.year`, `.month`, `.day` přečtou složky zpět jako celá čísla.
- Parsování na datum (místo abys řetězec sám řezal) je smyslem: hodnota je
  zkontrolovaná a ihned připravená pro kalendářní práci. Pro neISO rozvržení parsuje
  `datetime.strptime` podle explicitního formátu (13.7).

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
(d.year, d.month, d.day)     # (2026, 6, 20)
d < date.fromisoformat("2026-12-31")   # True
```
""",

"13.3 brief": r"""# 13.3 -- weekday: který den v týdnu

## Koncept

Daný datum, jaký je to den v týdnu? Spočítat to ručně znamená znát přestupné roky a
délku každého měsíce. Objekt `date` to už umí -- zeptej se ho:

```python
from datetime import date

date(2026, 6, 20).weekday()     # 5  (Saturday)
```

- **`.weekday()`** vrátí celé číslo: **pondělí je 0**, úterý 1, ... neděle 6.
- (`.isoweekday()` je tatáž myšlenka, ale pondělí=1 .. neděle=7.)

To je ten druh věci, který necháš dělat knihovnu: kóduje skutečný kalendář, takže
odpověď je správná pro libovolné datum, včetně přestupných roků.

## Příklad

```python
from datetime import date

def is_weekend(text):
    return date.fromisoformat(text).weekday() >= 5
```

## Tvůj úkol

Definuj `weekday(text)`, která bere řetězec `YYYY-MM-DD` a vrátí jeho den v týdnu
jako celé číslo, **pondělí=0 .. neděle=6**, pomocí `.weekday()` objektu data.

## Hotovo, když

- `weekday("2026-06-20")` vrátí `5` (sobota).
- `weekday("2000-01-01")` vrátí `5`.
- Odpověď pochází z `.weekday()` na rozparsovaném `date`.
""",

"13.3 hints": r"""Nejprve řetězec rozparsuj na datum pomocí `date.fromisoformat(text)`. Objekt data
ti umí říct svůj den v týdnu.

---

`.weekday()` vrátí 0 pro pondělí až 6 pro neděli. Zavolej ho na rozparsovaném datu a
vrať výsledek.

---

from datetime import date


def weekday(text):
    return date.fromisoformat(text).weekday()
""",

"13.3 reference": r"""**`date.weekday()`** vrátí den v týdnu jako celé číslo, **pondělí = 0** až
**neděle = 6**. Protože `date` kóduje skutečný kalendář — přestupné roky, různé délky
měsíců — spočítá to správně pro libovolné datum, což je přesně ten druh práce, který
deleguješ na knihovnu, místo abys ho odvozoval ručně.

- `.isoweekday()` je totéž, ale **pondělí = 1 .. neděle = 7** (ISO konvence).
- Časté použití je `weekday() >= 5` k testu na víkend.
- Doprovodné `.strftime("%A")` naformátuje **jméno** dne v týdnu, ale to závisí na
  lokalizaci; číselné `.weekday()` je stabilní všude.

```python
from datetime import date

date(2026, 6, 20).weekday()      # 5  (Saturday)
date(2026, 6, 22).weekday()      # 0  (Monday)
date(2026, 6, 20).weekday() >= 5 # True -- it's the weekend
```
""",

"13.4 brief": r"""# 13.4 -- timedelta: aritmetika dat

## Koncept

**`timedelta`** je **doba trvání** -- časový úsek. Přičti jednu k datu a dostaneš
jiné datum, se všemi kalendářními zmatky (délky měsíců, přechod roku, přestupné dny)
vyřešenými za tebe:

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)     # date(2026, 7, 30)
date(2026, 12, 25) + timedelta(days=10)    # date(2027, 1, 4)  -- crosses the year
```

- `timedelta(days=n)` je doba `n` dní (bere také `weeks=`, `hours=` atd.). `n` může
  být **záporné**, abys šel dozadu.
- `date + timedelta` dá nové `date`; `date - timedelta` jde opačně.
- Proto nikdy neděláš aritmetiku dat ručně: knihovna ví, že únor má v přestupném roce
  29 dní, a ty nemusíš.

## Příklad

```python
from datetime import date, timedelta

def tomorrow(text):
    return (date.fromisoformat(text) + timedelta(days=1)).isoformat()
```

## Tvůj úkol

Definuj `add_days(text, n)`, která bere řetězec `YYYY-MM-DD` a celé číslo `n` a vrátí
řetězec `YYYY-MM-DD` pro datum o `n` dní později (pomocí `timedelta`). `n` může být
záporné.

## Hotovo, když

- `add_days("2026-06-20", 40)` vrátí `"2026-07-30"`.
- `add_days("2026-01-01", -1)` vrátí `"2025-12-31"`.
- Posun používá `timedelta` na skutečném `date`, ne ručně psané počítání dní.
""",

"13.4 hints": r"""Naimportuj `date` i `timedelta`. Rozparsuj text, pak k datu přičti
`timedelta(days=n)`.

---

`date.fromisoformat(text) + timedelta(days=n)` dá nové datum; zavolej na něm
`.isoformat()` pro řetězec. Záporné `n` prostě funguje.

---

from datetime import date, timedelta


def add_days(text, n):
    return (date.fromisoformat(text) + timedelta(days=n)).isoformat()
""",

"13.4 reference": r"""**`timedelta`** představuje **dobu trvání** — časový úsek, ne bod v něm. Přičtení
jedné k `date` vyprodukuje jiné `date`, se vším kalendářním účetnictvím (délky
měsíců, hranice roku, přestupné dny) zpracovaným automaticky.

- `timedelta(days=n)` je `n` dní; přijímá také `weeks=`, `hours=`, `minutes=`,
  `seconds=`. `n` může být **záporné**, aby se posunulo dozadu.
- `date + timedelta` a `date - timedelta` dají nové datum; odečtení dvou *dat* dá
  `timedelta` (13.5).
- Proto aritmetika dat jde přes knihovnu: `date(2026, 12, 25) + timedelta(days=10)`
  správně přejde do dalšího roku a délka února nikdy není tvůj problém.

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)    # date(2026, 7, 30)
date(2026, 1, 1) - timedelta(days=1)      # date(2025, 12, 31)
date(2026, 6, 20) + timedelta(weeks=2)    # date(2026, 7, 4)
```
""",

"13.5 brief": r"""# 13.5 -- Odčítání dat: počet dní mezi

## Koncept

Přičtení doby k datu dá datum. Funguje i opak: **odečti jedno datum od druhého** a
dostaneš **`timedelta`** -- úsek mezi nimi:

```python
from datetime import date

gap = date(2026, 7, 1) - date(2026, 6, 20)
gap            # timedelta(days=11)
gap.days       # 11
```

- `date_b - date_a` je `timedelta`; jeho **`.days`** je celý počet dní mezi nimi.
- Pokud je `date_b` **dříve** než `date_a`, `.days` je **záporné**.
- Je to přesné napříč měsíci, roky a přestupnými dny -- počítá knihovna, ty ne.

## Příklad

```python
from datetime import date

def days_old(born, today):
    return (date.fromisoformat(today) - date.fromisoformat(born)).days
```

## Tvůj úkol

Definuj `days_between(a, b)`, která bere dva řetězce `YYYY-MM-DD` a vrátí počet dní
**od `a` do `b`** (takže pozdější `b` dá kladné číslo), pomocí odčítání dat.

## Hotovo, když

- `days_between("2026-06-20", "2026-07-01")` vrátí `11`.
- `days_between("2026-07-01", "2026-06-20")` vrátí `-11`.
- `days_between("2026-06-20", "2026-06-20")` vrátí `0`.
- Počet pochází z odečtení dvou objektů `date`, ne z ruční aritmetiky.
""",

"13.5 hints": r"""Rozparsuj oba řetězce na data, pak je odečti. `date_b - date_a` je timedelta.

---

timedelta má atribut `.days`. Pro „od a do b“ odečti `a` od `b`:
`(date.fromisoformat(b) - date.fromisoformat(a)).days`.

---

from datetime import date


def days_between(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days
""",

"13.5 reference": r"""Odečtení jednoho `date` od druhého dá **`timedelta`** — úsek mezi nimi — a jeho
atribut **`.days`** je celý počet dní, spočítaný přesně napříč měsíci, roky a
přestupnými dny.

- `date_b - date_a` měří od `a` do `b`: je-li `b` **dříve**, `.days` je **záporné**,
  takže znaménko ti řekne směr.
- Výsledek je doba trvání, takže se skládá: přičti ji zpět k datu, vynásob ji,
  porovnej dva úseky.
- To je počítací protějšek přičítání `timedelta` (13.4) — dohromady dělají z dat
  malou algebru: `datum + doba = datum`, `datum - datum = doba`.

```python
from datetime import date

(date(2026, 7, 1) - date(2026, 6, 20)).days     # 11
(date(2026, 6, 20) - date(2026, 7, 1)).days     # -11
(date(2026, 3, 1) - date(2024, 3, 1)).days      # 730  -- 2024 was a leap year
```
""",

"13.6 brief": r"""# 13.6 -- strftime: naformátuj datum po svém

## Koncept

`.isoformat()` vždy dá `YYYY-MM-DD`. Když potřebuješ jiné rozvržení, **`strftime`**
(„string format time“) vykreslí datum pomocí **formátovacích kódů**:

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y.%m.%d")     # '2026.06.20'
```

- `%d` je den, `%m` měsíc, `%Y` čtyřmístný rok -- každý doplněný nulami. Vše ostatní
  ve formátovacím řetězci (ta `/`, `.`, mezery) se zkopíruje doslovně.
- Existují i další kódy (`%H` hodina, `%M` minuta a jmenné kódy jako `%A`), ale ty
  číselné jsou základ.

Takže jeden objekt data se umí prezentovat, jakkoli zpráva nebo uživatel očekává.

## Příklad

```python
from datetime import date

def dotted(text):
    return date.fromisoformat(text).strftime("%Y.%m.%d")
```

## Tvůj úkol

Definuj `pretty(text)`, která bere řetězec `YYYY-MM-DD` a vrátí ho ve tvaru
**`DD/MM/YYYY`**, pomocí `strftime("%d/%m/%Y")` na rozparsovaném datu.

## Hotovo, když

- `pretty("2026-06-20")` vrátí `"20/06/2026"`.
- `pretty("1999-01-05")` vrátí `"05/01/1999"` (doplněné nulami).
- Formátování dělá `strftime`, ne přeskupování rozdělených kousků.
""",

"13.6 hints": r"""Rozparsuj datum pomocí `date.fromisoformat(text)`, pak na něm zavolej
`.strftime(...)` s rozvržením, které chceš.

---

Formátovací řetězec pro DD/MM/YYYY je `"%d/%m/%Y"`. Lomítka se kopírují doslovně;
kódy doplní čísla s nulami.

---

from datetime import date


def pretty(text):
    return date.fromisoformat(text).strftime("%d/%m/%Y")
""",

"13.6 reference": r"""**`strftime(format)`** („string-format-time“) vykreslí datum nebo datetime do
řetězce, který popíšeš **formátovacími kódy**. Kde `.isoformat()` dá jedno pevné
rozvržení, `strftime` dá libovolné.

- Časté kódy: `%Y` čtyřmístný rok, `%m` měsíc, `%d` den — všechny doplněné nulami;
  `%H` hodina, `%M` minuta, `%S` sekunda. Jakékoli jiné znaky (`/`, `.`, mezery) se
  kopírují doslovně.
- Jmenné kódy jako `%A` (den v týdnu) a `%B` (měsíc) **závisí na lokalizaci**, takže
  pro výstup, který musí být stabilní, dej přednost číselným kódům.
- `strptime` je inverze — *parsuje* řetězec podle formátu (13.7).

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y%m%d")       # '20260620'
d.strftime("%d.%m.%y")     # '20.06.26'  -- %y is the 2-digit year
```
""",

"13.7 brief": r"""# 13.7 -- strptime: parsuj podle formátu

## Koncept

`date.fromisoformat` čte jen jedno ISO rozvržení. Pro **libovolné** rozvržení --
datum s časem, vlastní pořadí -- použij **`datetime.strptime`** („parse time“). Dáš
mu řetězec **a** formát, který ho popisuje, se stejnými kódy jako `strftime`:

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.year     # 2026
dt.hour     # 14
dt.minute   # 30
```

- Formát musí odpovídat tvaru řetězce; neshoda vyvolá `ValueError`, takže při
  parsování validuje.
- Výsledek je **`datetime`** -- datum *a* čas -- s atributy `.year`, `.month`,
  `.day`, `.hour`, `.minute`, `.second`.

`strptime` parsuje, `strftime` formátuje: stejné kódy, opačné směry.

## Příklad

```python
from datetime import datetime

def year_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").year
```

## Tvůj úkol

Definuj `hour_of(text)`, která bere časové razítko jako `"2026-06-20 14:30"` a vrátí
**hodinu** jako celé číslo, tím, že ho rozparsuje pomocí `datetime.strptime` a
formátu `"%Y-%m-%d %H:%M"`.

## Hotovo, když

- `hour_of("2026-06-20 14:30")` vrátí `14`.
- `hour_of("1999-01-05 09:05")` vrátí `9`.
- Hodina pochází z rozparsovaného `datetime`, ne z řezání řetězce.
""",

"13.7 hints": r"""`datetime.strptime(text, format)` rozparsuje řetězec. Formát zrcadlí časové
razítko: `"%Y-%m-%d %H:%M"`.

---

Rozparsovaný objekt je datetime s atributem `.hour`. Ten vrať.

---

from datetime import datetime


def hour_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").hour
""",

"13.7 reference": r"""**`datetime.strptime(text, format)`** rozparsuje řetězec na **`datetime`** pomocí
stejných formátovacích kódů jako `strftime` — je to opačný směr. Kde
`date.fromisoformat` čte jen jedno ISO rozvržení, `strptime` čte **libovolné**
rozvržení, které umíš popsat.

- `format` musí přesně odpovídat tvaru řetězce (`"%Y-%m-%d %H:%M"` pro
  `"2026-06-20 14:30"`); neshoda vyvolá `ValueError`, čímž při parsování validuje.
- Výsledek je `datetime` — datum **a** čas — zpřístupňující `.year`, `.month`,
  `.day`, `.hour`, `.minute`, `.second`. (`.date()` a `.time()` vytáhnou jen jednu
  část.)
- Pamatuj si dvojici: **strptime** parsuje (řetězec → datetime), **strftime**
  formátuje (datetime → řetězec).

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.hour                      # 14
datetime.strptime("05/01/1999", "%d/%m/%Y").year   # 1999
```
""",

"13.8 brief": r"""# 13.8 -- Závěrečná: posuň časové razítko

## Koncept

Tohle stáhne kapitolu do jednoho okruhu tam a zpět: **rozparsuj** časové razítko,
**posuň** ho o dobu, **naformátuj** výsledek zpět -- každý krok nástroj, který jsi
potkal.

```python
from datetime import datetime, timedelta

dt = datetime.strptime("2026-06-20 23:30", "%Y-%m-%d %H:%M")  # parse
dt = dt + timedelta(hours=2)                                  # shift
dt.strftime("%Y-%m-%d %H:%M")                                 # '2026-06-21 01:30'
```

Všimni si, že posun přešel přes půlnoc do dalšího dne -- knihovna to automaticky
sleduje, napříč dny, měsíci a roky. Udělat to ručně by znamenalo znovu implementovat
kalendář a hodiny.

## Tvůj úkol

Definuj `add_hours(timestamp, hours)`, která bere řetězec `"YYYY-MM-DD HH:MM"` a celé
číslo `hours` (které může být záporné) a vrátí časové razítko posunuté o tolik hodin,
ve **stejném formátu `"YYYY-MM-DD HH:MM"`**.

Použij `datetime.strptime` k parsování, `timedelta(hours=...)` k posunu a `strftime`
k formátování.

## Hotovo, když

- `add_hours("2026-06-20 23:30", 2)` vrátí `"2026-06-21 01:30"`.
- `add_hours("2026-01-01 00:30", -1)` vrátí `"2025-12-31 23:30"`.
- Posun používá `timedelta` na rozparsovaném `datetime`, naformátovaný pomocí
  `strftime` -- ne ruční aritmetiku na řetězci.
""",

"13.8 hints": r"""Tři kroky, tři nástroje: `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` k
parsování, `+ timedelta(hours=hours)` k posunu, `.strftime("%Y-%m-%d %H:%M")` k
formátování.

---

Naimportuj `datetime` a `timedelta`. Rozparsuj na datetime, přičti timedelta, pak
vrať strftime výsledku. Záporné hodiny fungují stejně.

---

from datetime import datetime, timedelta


def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    dt = dt + timedelta(hours=hours)
    return dt.strftime("%Y-%m-%d %H:%M")
""",

"13.8 reference": r"""Závěrečná úloha je úplný **okruh tam a zpět** skrz modul, skládající tři jeho
nástroje:

1. **Parsuj** — `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` přečte řetězec na
   `datetime`.
2. **Posuň** — přičtení `timedelta(hours=h)` ho posune o dobu, přecházejíc napříč
   minutami, dny, měsíci a roky automaticky (a dozadu pro záporné `h`).
3. **Naformátuj** — `.strftime("%Y-%m-%d %H:%M")` vykreslí výsledek zpět do stejného
   rozvržení.

Smysl kapitoly v jedné funkci: každá nepříjemná hrana — čas přecházející půlnoc, den
přecházející do nového měsíce nebo roku, přestupný den — je zpracována typy
`datetime`, ne tebou. Ty popíšeš kroky; knihovna drží kalendář poctivý.

```python
from datetime import datetime, timedelta

def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    return (dt + timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M")

add_hours("2026-06-20 23:30", 2)    # '2026-06-21 01:30'
```
""",
}
