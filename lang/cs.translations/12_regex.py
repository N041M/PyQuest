# PyQuest translations -- language 'cs' -- chapter 12_regex -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"12.1 brief": r"""# 12.1 -- re.search: je tam ten vzor?

## Koncept

**Regulární výraz** („regex“) je malý jazyk pro popis vzorů v textu. Modul **`re`**
je hledá. Nejzákladnější otázka je „objevuje se tento vzor někde?“ -- **`re.search`**:

```python
import re

re.search(r"\d", "abc4")     # a match object (truthy)
re.search(r"\d", "abc")      # None
```

- Vzor se píše jako **surový řetězec** `r"..."`, aby zpětná lomítka znamenala to, co
  regex očekává (`r"\d"`, ne `"\d"`).
- `\d` odpovídá libovolné jediné **číslici**. Další zkratky: `\w` znak slova, `\s`
  bílý znak, `.` libovolný znak.
- `re.search` vrátí **objekt shody** (match object), pokud se vzor najde kdekoli,
  nebo **`None`**, pokud ne -- takže `re.search(...) is not None` je čisté ano/ne.

## Příklad

```python
import re

def has_letter(text):
    return re.search(r"[a-z]", text) is not None
```

## Tvůj úkol

Pomocí **`re.search`** definuj `has_digit(text)`, která vrátí `True`, pokud `text`
obsahuje alespoň jednu číslici, jinak `False`.

## Hotovo, když

- `has_digit("abc4")` je `True`, `has_digit("abc")` je `False`.
- `has_digit("")` je `False`.
- Test používá `re.search` s `\d`, ne ručně psané hledání číslic.
""",

"12.1 hints": r"""`import re`, pak `re.search(pattern, text)`. Vzor pro jedinou číslici je surový
řetězec `r"\d"`.

---

`re.search` vrátí objekt shody, když vzor najde, nebo `None`, když ne. Proměň to na
bool pomocí `is not None`.

---

import re


def has_digit(text):
    return re.search(r"\d", text) is not None
""",

"12.1 reference": r"""**Regulární výraz** je vzor popisující množinu řetězců; modul **`re`** je hledá v
textu. **`re.search(pattern, text)`** prohledá celý řetězec a najde **první** místo,
kde vzor sedí, a vrátí **objekt shody** (který je pravdivý) nebo **`None`**.

- Vzory piš jako **surové řetězce** — `r"\d"` — aby zpětná lomítka dosáhla regexového
  enginu, místo aby je nejprve interpretoval Python.
- Zkratkové třídy: `\d` číslice, `\w` znak slova `[A-Za-z0-9_]`, `\s` bílý znak a `.`
  libovolný znak kromě nového řádku.
- `re.search` hledá **kdekoli** v řetězci; `re.match` kontroluje jen začátek.
  Protože výsledek je objekt shody nebo `None`, `re.search(...) is not None` je
  čistý test přítomnosti.

```python
import re

re.search(r"\d", "abc4")     # <re.Match object; match='4'>
re.search(r"\d", "abc")      # None
bool(re.search(r"\s", "a b"))  # True -- contains whitespace
```
""",

"12.2 brief": r"""# 12.2 -- re.findall: každá shoda

## Koncept

`re.search` najde *první* shodu. **`re.findall`** vrátí **všechny**, jako seznam
řetězců:

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
```

- `\d+` znamená „jedna nebo více číslic“ -- `+` přiměje vzor pochytat celý úsek
  číslic, ne jen jednu. Takže každá shoda je celé číslo.
- `re.findall` vrátí **seznam řetězců** (nalezený text), zleva doprava,
  nepřekrývající se. Žádná shoda dá prázdný seznam `[]`.
- Shody jsou stále text; převeď pomocí `int(...)`, pokud chceš čísla.

## Příklad

```python
import re

def words(text):
    return re.findall(r"[a-z]+", text)
```

## Tvůj úkol

Pomocí **`re.findall`** definuj `all_numbers(text)`, která vrátí seznam každého úseku
číslic v `text`, jako řetězce.

## Hotovo, když

- `all_numbers("a12b3c456")` vrátí `["12", "3", "456"]`.
- `all_numbers("nothing")` vrátí `[]`.
- Extrakce používá `re.findall` s `\d+`, ne ručně psané hledání.
""",

"12.2 hints": r"""`import re`, pak `re.findall(pattern, text)` vrátí seznam každé shody. Chceš úseky
číslic.

---

Vzor `r"\d+"` odpovídá jedné nebo více číslicím v řadě, takže každá shoda je celé
číslo. `re.findall(r"\d+", text)` je celá odpověď.

---

import re


def all_numbers(text):
    return re.findall(r"\d+", text)
""",

"12.2 reference": r"""**`re.findall(pattern, text)`** vrátí **seznam každé** nepřekrývající se shody
vzoru, zleva doprava — protějšek „vytáhni je všechny“ k „najdi první“ od
`re.search`.

- **Kvantifikátor** přiměje jeden vzor odpovídat úseku: `\d+` je „jedna nebo více
  číslic“, takže každá shoda je celé číslo, ne jediná číslice. (`+` jedna-či-více,
  `*` nula-či-více, `?` volitelné, `{n}` přesně n.)
- Každá položka ve vráceném seznamu je **nalezený text** (řetězec); žádná shoda dá
  `[]`. Převeď pomocí `int(...)`, když chceš čísla.
- Má-li vzor zachytávací skupiny, `findall` vrátí skupiny místo celé shody; s jednou
  skupinou je to seznam textu té skupiny (viz 12.5).

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
re.findall(r"[a-z]+", "Hi there!")  # ['i', 'there']
[int(n) for n in re.findall(r"\d+", "p1 p22")]   # [1, 22]
```
""",

"12.3 brief": r"""# 12.3 -- Znakové třídy: [aeiou]

## Koncept

**Znaková třída** `[...]` odpovídá **kterémukoli jednomu** ze znaků uvedených uvnitř:

```python
import re

re.findall(r"[aeiou]", "education")     # ['e', 'u', 'a', 'i', 'o']
```

- `[aeiou]` odpovídá jedné samohlásce; `[abc]` odpovídá `a`, `b` nebo `c`.
- **Rozsah** používá pomlčku: `[a-z]` je libovolné malé písmeno, `[0-9]` libovolná
  číslice (totéž co `\d`), `[A-Za-z0-9]` libovolné písmeno nebo číslice.
- Úvodní `^` třídu **neguje**: `[^aeiou]` je libovolný znak, který *není* samohláska.

Třída je jeden znak; přidej kvantifikátor (`[a-z]+`), abys odpovídal jejich úseku.

## Příklad

```python
import re

def count_letters(text):
    return len(re.findall(r"[a-z]", text))
```

## Tvůj úkol

Pomocí znakové třídy s **`re.findall`** definuj `count_vowels(text)`, která vrátí,
kolik samohlásek (`a e i o u`) je v `text`.

## Hotovo, když

- `count_vowels("education")` vrátí `5`, `count_vowels("xyz")` vrátí `0`.
- `count_vowels("")` vrátí `0`.
- Počítání používá `re.findall` se třídou `[aeiou]`, ne ruční kontrolu `in`.
""",

"12.3 hints": r"""Znaková třída v hranatých závorkách odpovídá jednomu z uvedených znaků. Pro
samohlásky je to `r"[aeiou]"`.

---

`re.findall(r"[aeiou]", text)` dá seznam každé nalezené samohlásky; `len(...)` toho
seznamu je počet.

---

import re


def count_vowels(text):
    return len(re.findall(r"[aeiou]", text))
""",

"12.3 reference": r"""**Znaková třída** `[...]` odpovídá **přesně jednomu** znaku z množiny uvedené
uvnitř. `[aeiou]` odpovídá libovolné jedné samohlásce; `[abc]` odpovídá `a`, `b`
nebo `c`.

- **Rozsah** s pomlčkou pokryje po sobě jdoucí znaky: `[a-z]` libovolné malé
  písmeno, `[0-9]` libovolná číslice, `[A-Za-z0-9]` libovolné písmeno nebo číslice.
  Množiny a rozsahy uvnitř jedné třídy volně kombinuj.
- Úvodní **`^`** neguje: `[^aeiou]` odpovídá libovolnému znaku, který *není*
  samohláska.
- Třída odpovídá **jednomu** znaku; přidej kvantifikátor pro úsek — `[a-z]+` je
  slovo, `[0-9]{4}` přesně čtyři číslice. Uvnitř třídy většina metaznaků ztrácí svůj
  speciální význam (`[.]` je doslovná tečka).

```python
import re

re.findall(r"[aeiou]", "education")   # ['e', 'u', 'a', 'i', 'o']
re.findall(r"[^a-z ]", "a1 b2!")      # ['1', '2', '!']
re.findall(r"[A-Z][a-z]+", "Ada Lovelace")   # ['Ada', 'Lovelace']
```
""",

"12.4 brief": r"""# 12.4 -- Kvantifikátory: + znamená jednou nebo víckrát

## Koncept

**Kvantifikátor** říká, kolikrát se vzor před ním smí opakovat:

- **`+`** -- jednou nebo víckrát (`[a-z]+` je úsek jednoho či více malých písmen)
- **`*`** -- nulakrát nebo víckrát
- **`?`** -- volitelné (nula nebo jedna)
- **`{n}`** -- přesně `n`; **`{n,m}`** -- mezi `n` a `m`

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")     # ['Hello', 'world']
```

Bez `+` by `[A-Za-z]` odpovídalo jednotlivým písmenům po jednom. `+` ho přiměje
pochytat **celé slovo** a zastavit se u prvního znaku, který nesedí (mezera, čárka,
číslice). Takto rozdělíš text na slova a přitom ignoruješ interpunkci.

## Příklad

```python
import re

def integers(text):
    return re.findall(r"\d+", text)
```

## Tvůj úkol

Pomocí **`re.findall`** s kvantifikátorem definuj `find_words(text)`, která vrátí
seznam slov v `text` -- každé úsek jednoho či více písmen (`[A-Za-z]+`), s ignorovanou
interpunkcí a mezerami.

## Hotovo, když

- `find_words("Hello, world!")` vrátí `["Hello", "world"]`.
- `find_words("one-two three")` vrátí `["one", "two", "three"]`.
- `find_words("")` vrátí `[]`.
- Slova jsou nalezena pomocí `[A-Za-z]+`, ne rozdělena ručně.
""",

"12.4 hints": r"""Slovo je jedno či více písmen v řadě. Znaková třída `[A-Za-z]` odpovídá jednomu
písmenu; kvantifikátor `+` ji přiměje odpovídat úseku.

---

`re.findall(r"[A-Za-z]+", text)` vrátí každé slovo a každou shodu zastaví u prvního
nepísmene. To je celá funkce.

---

import re


def find_words(text):
    return re.findall(r"[A-Za-z]+", text)
""",

"12.4 reference": r"""**Kvantifikátor** řídí, kolikrát se opakuje vzor bezprostředně před ním:

- **`+`** jednou nebo víckrát, **`*`** nulakrát nebo víckrát, **`?`** nula nebo jedna
  (volitelné),
- **`{n}`** přesně *n*, **`{n,m}`** mezi *n* a *m*, **`{n,}`** alespoň *n*.

`[A-Za-z]+` tedy odpovídá celému **slovu** — úseku jednoho či více písmen — a zastaví
se u prvního znaku, který nesedí, čímž tokenizuješ text a ignoruješ mezery a
interpunkci.

- Kvantifikátory jsou ve výchozím stavu **hladové**: odpovídají co nejvíce. Koncové
  `?` udělá jeden **líným** (`\d+?` odpovídá co nejmenšímu počtu číslic).
- Kvantifikátor se vztahuje na jedinou položku před ním — znak, třídu nebo skupinu v
  závorkách: `(ab)+` odpovídá `ababab`.

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")   # ['Hello', 'world']
re.findall(r"\d{4}", "y2024 y2025")          # ['2024', '2025']
re.search(r"colou?r", "color")               # matches (the u is optional)
```
""",

"12.5 brief": r"""# 12.5 -- Skupiny: zachyť části

## Koncept

Závorky **`(...)`** ve vzoru vyznačují **zachytávací skupinu**: kousek shody, který
chceš vytáhnout. Objekt shody ti pak každý vrátí:

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.group(1)     # '2026'
m.group(2)     # '06'
m.groups()     # ('2026', '06', '20')
```

- `re.match` odpovídá od **začátku** řetězce a vrací objekt shody (nebo `None`).
- `m.group(n)` vrátí text, který zachytila *n*-tá skupina (`group(0)` je celá
  shoda); `m.groups()` vrátí je všechny jako n-tici.
- Zachycený text je stále řetězec -- `int(m.group(1))`, pokud chceš číslo.

Jeden vzor tedy zároveň kontroluje tvar i extrahuje pole.

## Příklad

```python
import re

def split_pair(text):
    m = re.match(r"(\w+):(\w+)", text)
    return (m.group(1), m.group(2))
```

## Tvůj úkol

Pomocí **`re.match`** se zachytávacími skupinami definuj `parse_date(text)`, která
bere datum jako `"2026-06-20"` a vrátí n-tici **celých čísel** `(year, month, day)`.

## Hotovo, když

- `parse_date("2026-06-20")` vrátí `(2026, 6, 20)`.
- `parse_date("1999-01-05")` vrátí `(1999, 1, 5)`.
- Pole pocházejí ze zachytávacích skupin, ne z `text.split("-")`.
""",

"12.5 hints": r"""Obal každou část, kterou chceš, do závorek: `r"(\d+)-(\d+)-(\d+)"`. Každé `(...)` je
zachytávací skupina.

---

`m = re.match(pattern, text)` pak čti `m.group(1)`, `m.group(2)`, `m.group(3)`. Jsou
to řetězce, takže každý obal do `int(...)` pro n-tici.

---

import re


def parse_date(text):
    m = re.match(r"(\d+)-(\d+)-(\d+)", text)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
""",

"12.5 reference": r"""Závorky **`(...)`** ve vzoru vytvoří **zachytávací skupinu** — podčást shody, kterou
si engine zapamatuje, abys ji mohl přečíst zpět. Objekt shody je zpřístupní:

- **`m.group(n)`** vrátí text, který zachytila *n*-tá skupina, číslovaná zleva doprava
  od 1; **`m.group(0)`** (nebo `m.group()`) je celá shoda.
- **`m.groups()`** vrátí text každé skupiny jako n-tici — ideální k rozbalení.
- Zachycený text je **řetězec**; podle potřeby převeď pomocí `int(...)`. Skupina,
  která se nezúčastnila, je `None`.

Takže jeden vzor zároveň **validuje** tvar i **extrahuje** pole. `re.match` se ukotví
na začátku a vrátí objekt shody nebo `None`; než budeš číst skupiny, ošetři `None`,
když vstup nemusí sednout. Skupiny pojmenuj pomocí `(?P<name>...)` a čti je přes
`m.group("name")` pro přehlednost.

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.groups()                # ('2026', '06', '20')
tuple(int(p) for p in m.groups())   # (2026, 6, 20)
```
""",

"12.6 brief": r"""# 12.6 -- re.sub: najdi a nahraď podle vzoru

## Koncept

`str.replace` vymění pevný podřetězec. **`re.sub`** vymění vše, co odpovídá **vzoru**:

```python
import re

re.sub(r"\d+", "#", "call 555-1234 now")     # 'call #-# now'
```

- `re.sub(pattern, replacement, text)` vrátí **nový** řetězec s **každou** shodou
  `pattern` nahrazenou `replacement`.
- Protože `\d+` odpovídá celému úseku číslic, každý úsek se smrskne na jediné `#` --
  jedno nahrazení na shodu, ne na znak.
- Žádná shoda nechá text beze změny. Nahrazení může také odkazovat na zachycené
  skupiny (`\1`), ale prostý řetězec je běžný případ.

## Příklad

```python
import re

def squash_spaces(text):
    return re.sub(r"\s+", " ", text)
```

## Tvůj úkol

Pomocí **`re.sub`** definuj `redact(text)`, která nahradí každý úsek číslic v `text`
jediným `"#"`.

## Hotovo, když

- `redact("call 555-1234")` vrátí `"call #-#"`.
- `redact("no digits")` vrátí `"no digits"`.
- Každý *úsek* číslic se stane jedním `#` (použij `\d+`), přes `re.sub` -- ne cyklus
  přes znaky.
""",

"12.6 hints": r"""`re.sub(pattern, replacement, text)` nahradí každou shodu. Tvůj vzor je úsek číslic,
tvé nahrazení je `"#"`.

---

`r"\d+"` odpovídá celému úseku číslic, takže každý úsek se stane jedním `#`:
`re.sub(r"\d+", "#", text)` je celá funkce.

---

import re


def redact(text):
    return re.sub(r"\d+", "#", text)
""",

"12.6 reference": r"""**`re.sub(pattern, repl, text)`** je nahrazování řízené vzorem: vrátí **nový**
řetězec s **každou** nepřekrývající se shodou `pattern` nahrazenou `repl`. Kde
`str.replace` vymění pevný podřetězec, `re.sub` vymění cokoli, co vzor popisuje.

- Protože kvantifikovaný vzor odpovídá **úseku**, každý úsek se smrskne na jedno
  nahrazení: `re.sub(r"\d+", "#", "a12b3")` je `"a#b#"`, ne `"a##b#"`.
- Žádná shoda nechá text beze změny. Volitelné `count=` omezí, kolik nahrazení se
  provede.
- `repl` může odkazovat na zachycené skupiny pomocí `\1`, `\2`, … (např.
  `re.sub(r"(\w+)@(\w+)", r"\2.\1", s)`), nebo být **funkcí**, která dostane každou
  shodu a vrátí její nahrazení, pro logiku příliš složitou na šablonu.

```python
import re

re.sub(r"\s+", " ", "too   many    spaces")   # 'too many spaces'
re.sub(r"\d+", "#", "call 555-1234")           # 'call #-#'
re.sub(r"(\d+)", r"[\1]", "x12")               # 'x[12]'
```
""",

"12.7 brief": r"""# 12.7 -- Kotvy: shoda celého řetězce

## Koncept

`re.search` je spokojený, pokud se vzor objeví **kdekoli**. Abys **validoval
formát**, potřebuješ, aby odpovídal *celý* řetězec -- žádné zbylé znaky.

Dva způsoby, jak to vyžadovat:

- **Kotvy** ve vzoru: `^` váže na **začátek**, `$` na **konec**, takže
  `r"^[A-Z]{2}\d{4}$"` musí pokrýt celý řetězec.
- **`re.fullmatch`**, který za tebe vyžaduje, aby vzor pokryl celý řetězec -- žádné
  kotvy nejsou potřeba.

```python
import re

re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234")     # matches
re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")    # None -- trailing junk
re.search(r"[A-Z]{2}\d{4}", "AB1234x")       # matches -- search ignores the x
```

Kód produktu tady jsou dvě velká písmena, pak čtyři číslice: `AB1234`.

## Příklad

```python
import re

def is_word(text):
    return re.fullmatch(r"[a-z]+", text) is not None
```

## Tvůj úkol

Pomocí **`re.fullmatch`** (nebo `^...$`) definuj `is_valid_code(text)`, která vrátí
`True` jen tehdy, když je `text` přesně **dvě velká písmena následovaná čtyřmi
číslicemi** (např. `"AB1234"`), jinak `False`.

## Hotovo, když

- `is_valid_code("AB1234")` je `True`.
- `is_valid_code("ab1234")`, `is_valid_code("AB123")`, `is_valid_code("AB1234x")`
  jsou všechny `False`.
- Odpovídá celý řetězec (fullmatch nebo kotvy), ne ručně psaná kontrola délky.
""",

"12.7 hints": r"""Vzor pro kód je `r"[A-Z]{2}\d{4}"` -- dvě velká písmena, pak čtyři číslice. Trik je
přimět CELÝ řetězec, aby mu odpovídal.

---

`re.fullmatch(pattern, text)` vyžaduje, aby vzor pokryl celý řetězec, takže koncové
znaky selžou. Vrať, zda našel shodu, pomocí `is not None`.

---

import re


def is_valid_code(text):
    return re.fullmatch(r"[A-Z]{2}\d{4}", text) is not None
""",

"12.7 reference": r"""Ve výchozím stavu může vzor odpovídat **kdekoli** v řetězci. Validovat *formát*
znamená, že musí vyhovět **celý** řetězec — žádné zbylé znaky. Dva způsoby, jak to
vyžadovat:

- **Kotvy** ve vzoru: **`^`** odpovídá začátku řetězce, **`$`** konci.
  `r"^[A-Z]{2}\d{4}$"` musí pokrýt celý vstup.
- **`re.fullmatch(pattern, text)`** za tebe vyžaduje, aby vzor pokryl celý řetězec —
  žádné kotvy nejsou potřeba. Vrátí objekt shody nebo `None`.

Kontrast: `re.search(r"[A-Z]{2}\d{4}", "AB1234x")` **odpovídá** (vzor se vyskytuje),
ale `re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")` je **`None`** (`x` zbylo). Použij
`search`/`findall` k *hledání* podřetězců, `fullmatch`/kotvy k *validaci* celé
hodnoty.

```python
import re

bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234"))    # True
bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x"))   # False
bool(re.match(r"^\d{5}$", "12345"))               # True -- anchored form
```
""",

"12.8 brief": r"""# 12.8 -- Závěrečná: parsování konfigurace key=value

## Koncept

Čas zkombinovat nástroje kapitoly. Když `re.findall` dostane vzor s **několika
zachytávacími skupinami**, vrátí seznam **n-tic** -- jednu na shodu, se zachycenými
kousky uvnitř:

```python
import re

re.findall(r"(\w+)=(\w+)", "host=local port=8080")
# [('host', 'local'), ('port', '8080')]
```

Seznam dvojic `(klíč, hodnota)` je přesně to, co **`dict(...)`** promění ve slovník.
Takže jeden vzor plus `dict` rozparsuje celý konfigurační řetězec:

```python
dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```

`\w+` odpovídá úseku znaků slova (písmena, číslice, podtržítko), takže každý klíč a
hodnota se pochytá celý a `=` mezi nimi se shoduje doslovně.

## Tvůj úkol

Definuj `parse_config(text)`, která rozparsuje mezerami oddělený řetězec dvojic
`key=value` na slovník, pomocí **`re.findall`** se dvěma zachytávacími skupinami.

## Hotovo, když

- `parse_config("host=local port=8080")` se rovná
  `{"host": "local", "port": "8080"}`.
- `parse_config("debug=on")` se rovná `{"debug": "on"}`.
- `parse_config("")` se rovná `{}`.
- Dvojice jsou zachyceny jedním vzorem `(\w+)=(\w+)`, ne rozděleny ručně.
""",

"12.8 hints": r"""Použij dvě zachytávací skupiny, jednu pro klíč a jednu pro hodnotu, s doslovným `=`
mezi nimi: `r"(\w+)=(\w+)"`.

---

Se dvěma skupinami `re.findall(pattern, text)` vrátí seznam n-tic `(klíč, hodnota)`.
`dict(...)` toho seznamu je konfigurační slovník.

---

import re


def parse_config(text):
    return dict(re.findall(r"(\w+)=(\w+)", text))
""",

"12.8 reference": r"""Závěrečná úloha skládá kapitolu: jediný vzor s **více zachytávacími skupinami**,
předaný **`re.findall`**, extrahuje strukturované záznamy v jednom kroku.

- S více než jednou skupinou vrátí `re.findall` seznam **n-tic** — jednu na shodu,
  držící text každé skupiny: `re.findall(r"(\w+)=(\w+)", s)` dá
  `[(klíč, hodnota), ...]`.
- Seznam dvojic `(klíč, hodnota)` je přesně to, co **`dict(...)`** konzumuje, takže
  `dict(re.findall(...))` je úplný mini-parser.
- `\w+` odpovídá úseku znaků slova (písmena, číslice, podtržítko); `=` mezi skupinami
  se shoduje **doslovně**. Žádná shoda dá `[]`, takže prázdný vstup čistě dá `{}`.

To je odměna regexu: popiš tvar jednoho záznamu a engine za tebe najde a rozebere
každý výskyt.

```python
import re

dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```
""",
}
