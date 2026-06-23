# PyQuest translations -- language 'cs' -- chapter 02_strings -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"2.1 brief": r"""# 2.1 -- Indexování

## Koncept

Řetězec je posloupnost znaků a každý znak má **pozici** (zvanou *index*). Počítá
se od **0**, ne od 1. Takže v řetězci `"cat"`:

```
znak:    c  a  t
index:   0  1  2
```

Jeden znak přečteš pomocí hranatých závorek: `s[index]`.

```python
word = "cat"
print(word[0])   # c
print(word[1])   # a
```

`word[0]` je první znak, protože indexování začíná od nuly. To zpočátku zaskočí
skoro každého: „první“ znak je na indexu 0.

## Příklad

```python
s = "python"
print(s[0])   # p
```

## Tvůj úkol

Přečti slovo pomocí `input()` a pak vypiš pouze jeho **první** znak.

Pro vstup `hello` je výstup:

```
h
```

## Hotovo, když

- Pro `hello` vypíše `h`.
- Funguje pro libovolné slovo, včetně jednopísmenného (kontrola jich zkouší
  několik).
""",

"2.1 hints": r"""Znaky jsou číslovány od 0. Hranaté závorky přečtou jeden z nich: s[0].

---

Nejprve ulož vstup, pak vypiš index 0: `s = input()` a pak `print(s[0])`.

---

s = input()
print(s[0])
""",

"2.1 reference": r"""Řetězec je uspořádaná posloupnost znaků a `s[index]` přečte ten na dané pozici.
Pozice jsou **číslovány od nuly**: první znak je `s[0]`, druhý `s[1]` a tak dále.

- Výsledek je sám o sobě jednoznakový řetězec (Python nemá samostatný typ pro
  znak).
- Index rovný délce nebo větší vyvolá `IndexError`; pro řetězec délky *n* jsou
  platné pozice `0` až `n - 1`.
- Řetězce jsou **neměnné** — indexování znak přečte, ale `s[0] = "x"` je chyba.
  Pro změnu textu vytvoříš nový řetězec.

```python
word = "Python"
word[0]    # 'P'
word[3]    # 'h'
```
""",

"2.2 brief": r"""# 2.2 -- Záporné indexování

## Koncept

Můžeš také počítat od **konce** řetězce pomocí záporných indexů. `-1` je poslední
znak, `-2` předposlední a tak dále.

```
znak:        c   a   t
index:       0   1   2
od konce:   -3  -2  -1
```

```python
word = "cat"
print(word[-1])   # t
print(word[-2])   # a
```

To se hodí, když nechceš počítat délku: `s[-1]` je vždy poslední znak, ať je
řetězec jakkoli dlouhý.

## Příklad

```python
s = "python"
print(s[-1])   # n
```

## Tvůj úkol

Přečti slovo a pak vypiš jeho **poslední** znak.

Pro vstup `hello` je výstup:

```
o
```

## Hotovo, když

- Pro `hello` vypíše `o`.
- Funguje i pro jednopísmenné slovo (`-1` ukazuje na ten jeden znak).
""",

"2.2 hints": r"""Záporné indexy počítají od konce. -1 je poslední znak.

---

`s = input()` a pak `print(s[-1])`.

---

s = input()
print(s[-1])
""",

"2.2 reference": r"""**Záporný** index počítá od konce řetězce: `s[-1]` je poslední znak, `s[-2]`
předposlední a tak dále. Ušetří psaní `s[len(s) - 1]`.

- `s[-1]` a `s[len(s) - 1]` pojmenovávají stejný znak; záporný tvar jen
  nepotřebuje délku.
- Platný záporný rozsah je `-1` až `-len(s)`; jít dál (např. `s[-99]` u krátkého
  řetězce) vyvolá `IndexError`.
- `s[0]` je první znak; žádné `-0` neexistuje (to je prostě `0`).

```python
word = "Python"
word[-1]   # 'n'
word[-2]   # 'o'
```
""",

"2.3 brief": r"""# 2.3 -- Řezy (slicing)

## Koncept

**Řez** (slice) vezme rozsah znaků najednou: `s[start:stop]`. Zahrne znak na pozici
`start` a jde **až po `stop`, ale ten nezahrnuje**. Tomu se říká *polootevřený*:
koncový index není součástí.

```python
s = "python"
print(s[0:3])   # pyt   (indexes 0, 1, 2 -- not 3)
print(s[2:5])   # tho   (indexes 2, 3, 4)
```

Vynech `start` a začne od 0; vynech `stop` a poběží až do konce:

```python
print(s[:3])    # pyt   (same as s[0:3])
print(s[3:])    # hon   (from index 3 to the end)
```

Protože `stop` není zahrnut, `s[0:3]` ti dá přesně **3** znaky.

## Příklad

```python
s = "rainbow"
print(s[0:4])   # rain
```

## Tvůj úkol

Přečti slovo a pak vypiš jeho **první tři** znaky.

Pro vstup `hello` je výstup:

```
hel
```

## Hotovo, když

- Pro `hello` vypíše `hel`.
- Pro slovo kratší než tři písmena vypíše celé slovo -- řez za konec je bezpečný a
  nechybuje. Kontrola zkouší `hi`.
""",

"2.3 hints": r"""Řez s[start:stop] vezme znaky od start až po stop (ten už ne).

---

První tři znaky jsou s[0:3], nebo prostě s[:3].

---

s = input()
print(s[:3])
""",

"2.3 reference": r"""**Řez** `s[start:stop]` vrátí nový řetězec se znaky od pozice `start` **až po
`stop`, ten už ne** — *polootevřený* rozsah. Délka výsledku je `stop - start`
(když jsou oba v rozsahu).

- `s[2:5]` dá znaky na indexech 2, 3, 4 — tři znaky.
- Kteroukoli mez lze vynechat: `s[:3]` začíná od začátku, `s[3:]` běží do konce a
  `s[:]` zkopíruje celý řetězec.
- Řez nikdy nevyvolá chybu při mezích mimo rozsah — ořízne je. `s[:100]` u
  krátkého řetězce prostě vrátí celý.

```python
s = "Python"
s[0:3]    # 'Pyt'
s[:2]     # 'Py'
s[2:]     # 'thon'
```
""",

"2.4 brief": r"""# 2.4 -- Řez prostředku

## Koncept

Řez se v pohodě kombinuje se zápornými indexy a řezy nikdy nespadnou -- pokud je
řez prázdný, prostě dostaneš prázdný řetězec `""`.

`s[1:-1]` znamená „od indexu 1 až po poslední znak (ten už ne)“ -- jinými slovy
zahodit první a poslední znak:

```python
s = "python"
print(s[1:-1])   # ytho
```

Pokud je řetězec příliš krátký na to, aby měl prostředek, řez je prostě prázdný:

```python
print("ab"[1:-1])   # (nothing -- an empty string)
print("a"[1:-1])    # (nothing)
```

Žádná chyba. Prázdný řez je normální, platný výsledek.

## Častý omyl

Jít s řezem „mimo rozsah“ **nespadne**, na rozdíl od indexování jednoho znaku.
`"hi"[5]` by byla chyba, ale `"hi"[1:5]` je v pořádku -- prostě se zastaví na
konci.

## Příklad

```python
s = "hello"
print(s[1:-1])   # ell
```

## Tvůj úkol

Přečti slovo a pak ho vypiš **bez prvního a posledního znaku**.

Pro vstup `hello` je výstup:

```
ell
```

## Hotovo, když

- Pro `hello` vypíše `ell`.
- Pro 1- nebo 2písmenné slovo vypíše prázdný řádek (žádný prostředek) a nespadne.
  Kontrola zkouší `ab` a `a`.
""",

"2.4 hints": r"""Index 1 je druhý znak; -1 je poslední. Udělej řez mezi nimi.

---

Použij s[1:-1], abys zahodil první a poslední znak.

---

s = input()
print(s[1:-1])
""",

"2.4 reference": r"""Meze řezu mohou být **záporné**, počítané od konce, a oba styly se volně
kombinují. `s[1:-1]` zahodí první a poslední znak — začni na indexu 1, skonči
těsně před posledním.

- Řez, jehož start je roven stopu nebo za ním, je **prázdný**, ne chyba: `s[3:3]`
  i `s[5:2]` dají `""`.
- Meze mimo rozsah se oříznou, takže řez je shovívavý tam, kde obyčejné
  indexování vyvolá chybu: `s[1:99]` je v pořádku.
- Protože stop je vyloučen, `s[:-1]` odstraní přesně poslední znak a `s[1:]`
  odstraní první.

```python
s = "Python"
s[1:-1]   # 'ytho'  -- both ends trimmed
s[2:2]    # ''      -- empty, not an error
```
""",

"2.5 brief": r"""# 2.5 -- Kroky a obracení

## Koncept

Řez může mít třetí číslo, **krok**: `s[start:stop:step]`. Krok říká, o kolik pozic
se pokaždé posunout. Krok `2` vezme každý druhý znak:

```python
s = "abcdef"
print(s[::2])   # ace   (every 2nd character)
```

**Záporný** krok jde pozpátku. Zkratka `s[::-1]` -- prázdný start, prázdný stop,
krok `-1` -- obrátí celý řetězec:

```python
s = "python"
print(s[::-1])   # nohtyp
```

`s[::-1]` je standardní pythonovský způsob, jak obrátit řetězec.

## Příklad

```python
print("hello"[::-1])   # olleh
```

## Tvůj úkol

Přečti slovo a pak ho vypiš **obrácené**.

Pro vstup `hello` je výstup:

```
olleh
```

## Hotovo, když

- Pro `hello` vypíše `olleh`.
- Pro jediné písmeno nebo slovo, které se čte stejně pozpátku (jako `level`),
  vypíše slovo beze změny. Kontrola zkouší obojí.
""",

"2.5 hints": r"""Řez může mít krok: s[start:stop:step]. Záporný krok jde pozpátku.

---

Obrať standardním idiomem: s[::-1].

---

s = input()
print(s[::-1])
""",

"2.5 reference": r"""Řez má třetí část, **krok**: `s[start:stop:step]` vezme každý `step`-tý znak.
Výchozí krok je 1.

- `s[::2]` vezme každý druhý znak (indexy 0, 2, 4, …).
- **Záporný** krok jde pozpátku. `s[::-1]` je idiomatický způsob, jak **obrátit**
  řetězec; se záporným krokem se výchozí start/stop přehodí na konec a začátek.
- `s[::-2]` vezme každý druhý znak, od konce směrem k začátku.

```python
s = "Python"
s[::2]    # 'Pto'
s[::-1]   # 'nohtyP'  -- reversed
```
""",

"2.6 brief": r"""# 2.6 -- Délka, spojování, opakování

## Koncept

Tři každodenní nástroje pro řetězce:

- `len(s)` dá **počet znaků** v `s` (číslo):
  ```python
  len("cat")    # 3
  ```
- `+` spojí dva řetězce (potkal jsi to v kapitole 1):
  ```python
  "cat" + "!"   # "cat!"
  ```
- `*` s číslem řetězec **opakuje**:
  ```python
  "ab" * 3      # "ababab"
  "-" * 5       # "-----"
  ```

`len` vrací číslo, takže s ním můžeš počítat. `+` a `*` staví nové řetězce.

## Příklad

```python
s = "hi"
print(len(s))    # 2
print(s + "!")   # hi!
print(s * 3)     # hihihi
```

## Tvůj úkol

Přečti slovo a vypiš tři řádky:

1. počet znaků ve slově
2. slovo s vykřičníkem přidaným na konec
3. slovo zopakované třikrát

Pro vstup `hi` je výstup:

```
2
hi!
hihihi
```

## Hotovo, když

- Pro `hi` jsou tři řádky `2`, `hi!`, `hihihi`.
- Funguje to i pro prázdný vstup: `0`, `!` a prázdný řádek. Kontrola to zkouší.
""",

"2.6 hints": r"""len(s) je číslo; + spojuje řetězce; * je opakuje.

---

print(len(s)) na počet, print(s + "!") na připojení, print(s * 3) na opakování.

---

s = input()
print(len(s))
print(s + "!")
print(s * 3)
""",

"2.6 reference": r"""Tři základní operace s řetězci:

- **`len(s)`** vrátí počet znaků v `s` jako `int`; `len("")` je `0`.
- **`+` zřetězí**: `"ab" + "cd"` je `"abcd"`. Oba operandy musí být řetězce —
  `"n" + 5` vyvolá `TypeError`; nejprve převeď pomocí `str(5)`.
- **`*` opakuje**: `s * n` (nebo `n * s`) spojí `n` kopií. `"ab" * 3` je
  `"ababab"`; `n <= 0` dá prázdný řetězec `""`.

Všechny tři vytvoří **nové** řetězce a originály nechají beze změny (řetězce jsou
neměnné).

```python
s = "ab"
len(s)    # 2
s + "c"   # 'abc'
s * 3     # 'ababab'
```
""",

"2.7 brief": r"""# 2.7 -- Čištění textu

## Koncept

Řetězce mají **metody** -- akce, které voláš s tečkou za řetězcem: `s.metoda()`.
Tři běžné:

- `s.upper()` -> kopie VELKÝMI písmeny
- `s.lower()` -> kopie malými písmeny
- `s.strip()` -> kopie s mezerami odstraněnými z **obou konců** (ne z prostředku)

```python
"Hello".upper()     # "HELLO"
"Hello".lower()     # "hello"
"  hi  ".strip()    # "hi"
```

Metody vracejí **nový** řetězec; originál nemění. Můžeš je řetězit -- každá pracuje
na výsledku té předchozí:

```python
"  Hi  ".strip().upper()   # "HI"
```

## Příklad

```python
s = "  python  "
print(s.strip().upper())   # PYTHON
```

## Tvůj úkol

Přečti řádek, odstraň kolem něj mezery a vypiš ho **velkými písmeny**.

Pro vstup `  hello  ` je výstup:

```
HELLO
```

## Hotovo, když

- Pro `  hello  ` vypíše `HELLO`.
- Mezery uprostřed zůstanou; oříznou se jen konce. Kontrola zkouší i řádek tvořený
  jen mezerami (výsledkem je prázdný řádek).
""",

"2.7 hints": r"""Metody se volají s tečkou: s.strip(), s.upper(). Vracejí nové řetězce.

---

Zřetěz je: s.strip() odstraní koncové mezery, .upper() převede výsledek na velká
písmena.

---

s = input()
print(s.strip().upper())
""",

"2.7 reference": r"""Řetězce nesou **metody** — funkce volané syntaxí `s.metoda()`, které z řetězce
něco spočítají.

- **`.strip()`** vrátí řetězec s odstraněnými **bílými znaky** na začátku a konci
  (mezery, tabulátory, nové řádky). `.lstrip()` / `.rstrip()` oříznou jednu
  stranu.
- **`.upper()`** / **`.lower()`** vrátí řetězec s každým písmenem velkým, resp.
  malým.

Protože každá metoda vrací **nový** řetězec (originál se nikdy nezmění), volání se
**řetězí**: každé působí na výsledek předchozího.

```python
"  Hi  ".strip()            # 'Hi'
"Hi".upper()                # 'HI'
"  Hello  ".strip().lower() # 'hello'  -- trimmed, then lowered
```
""",

"2.8 brief": r"""# 2.8 -- Nahrazování a počítání

## Koncept

Další dvě metody řetězců:

- `s.replace(old, new)` vrátí kopii `s`, kde je **každý** výskyt `old` nahrazen
  `new`:
  ```python
  "banana".replace("a", "o")   # "bonono"
  ```
- `s.count(sub)` vrátí, **kolikrát** se `sub` vyskytuje (číslo):
  ```python
  "banana".count("a")          # 3
  ```

Pokud `old` chybí, `replace` vrátí řetězec beze změny; pokud `sub` chybí, `count`
vrátí `0`.

## Příklad

```python
s = "foo bar"
print(s.replace("o", "0"))   # f00 bar
print(s.count("o"))          # 2
```

## Tvůj úkol

Přečti řádek a vypiš dva řádky:

1. řádek, kde je každé písmeno `o` nahrazeno nulou `0`
2. kolik `o` bylo v **původním** řádku

Pro vstup `foobar` je výstup:

```
f00bar
2
```

## Hotovo, když

- Pro `foobar` jsou řádky `f00bar` a `2`.
- Pro řádek bez `o` vypíše řádek beze změny a `0`. Kontrola to zkouší.
""",

"2.8 hints": r"""replace nahradí každou shodu; count řekne, kolik shod tam je.

---

print(s.replace("o", "0")) a pak print(s.count("o")).

---

s = input()
print(s.replace("o", "0"))
print(s.count("o"))
""",

"2.8 reference": r"""Dvě metody pro hledání a přehled:

- **`s.replace(old, new)`** vrátí nový řetězec s **každým** nepřekrývajícím se
  výskytem `old` nahrazeným `new`. Nahradí všechny shody, ne jen první; pokud se
  `old` nevyskytne, řetězec se vrátí beze změny.
- **`s.count(sub)`** vrátí, kolikrát se `sub` vyskytuje, počítá nepřekrývající se
  shody zleva doprava. `"aaa".count("aa")` je `1`, ne 2.

Obě jen čtou `s` a vracejí novou informaci; původní řetězec zůstává nedotčen.

```python
"a-b-c".replace("-", "_")   # 'a_b_c'  -- every match
"banana".count("a")          # 3
```
""",

"2.9 brief": r"""# 2.9 -- Hledání pozice

## Koncept

`s.find(sub)` vrátí **index**, kde se `sub` poprvé objeví -- číslo, které pak můžeš
použít pro řez. (Pokud se `sub` nenajde, vrátí `-1`.)

```python
s = "name=Sam"
i = s.find("=")    # 4
print(i)           # 4
print(s[i+1:])     # Sam   (everything after the "=")
```

`find` tedy najde značku a řez vůči ní vytáhne část, kterou chceš. Zde `s[i+1:]`
znamená „od jedné pozice za `=` až do konce“.

## Příklad

```python
s = "color=blue"
i = s.find("=")
print(s[i+1:])     # blue
```

## Tvůj úkol

Každý vstup je řádek tvaru `key=value` (s jedním `=`). Vypiš jen **hodnotu** -- vše
za `=`.

Pro vstup `color=blue` je výstup:

```
blue
```

## Hotovo, když

- Pro `color=blue` vypíše `blue`.
- Pro `x=1` vypíše `1`; pro `a=` vypíše prázdný řádek; pro `k=a=b` vypíše `a=b`
  (rozdělí ho jen první `=`). Kontrola je zkouší.
""",

"2.9 hints": r"""find ti řekne, kde je „=“. Pak udělej řez od pozice hned za ním.

---

i = s.find("=") dá pozici; s[i+1:] je vše za ním.

---

s = input()
i = s.find("=")
print(s[i+1:])
""",

"2.9 reference": r"""**`s.find(sub)`** vrátí index **prvního** výskytu `sub` v `s`, nebo **`-1`**,
pokud se nenajde (nikdy nevyvolá chybu). Ve spojení s řezem vytáhne text kolem
značky.

- Vrácený index je tam, kde `sub` začíná, takže `s[:i]` je část před ním a
  `s[i + len(sub):]` část za ním.
- Před použitím výsledku zkontroluj `-1` — `s.find` vracející `-1` by jinak řezal
  od konce.
- `.index(sub)` dělá totéž, ale při nepřítomnosti **vyvolá** `ValueError`; použij
  `.find`, když je „není přítomno“ běžný případ.

```python
s = "key=value"
i = s.find("=")     # 3
s[:i]               # 'key'
s[i + 1:]           # 'value'
```
""",

"2.10 brief": r"""# 2.10 -- f-řetězce

## Koncept

**f-řetězec** ti umožní vložit hodnoty přímo do textu. Dej `f` před úvodní uvozovku
a pak napiš `{...}` všude, kam má přijít hodnota:

```python
name = "Sam"
print(f"Hello, {name}!")     # Hello, Sam!
```

Do `{}` můžeš vložit libovolný výraz, ne jen prostou proměnnou -- vyhodnotí se a
jeho výsledek se vloží do textu:

```python
word = "cat"
print(f"{word} has {len(word)} letters")    # cat has 3 letters
print(f"{word} reversed is {word[::-1]}")   # cat reversed is tac
```

f-řetězce jsou nejpřehlednější způsob, jak sestavit text z hodnot -- mnohem
úhlednější než spojování kousků pomocí `+`.

## Příklad

```python
s = "python"
print(f"{s} reversed is {s[::-1]}")   # python reversed is nohtyp
```

## Tvůj úkol

Přečti slovo a pak pomocí f-řetězce vypiš přesně tuto větu:

```
WORD reversed is REVERSED
```

kde `WORD` je vstup a `REVERSED` je pozpátku. Pro vstup `hello`:

```
hello reversed is olleh
```

## Hotovo, když

- Pro `hello` vypíše `hello reversed is olleh`.
- Funguje pro libovolné slovo, včetně jednoho písmene. Kontrola jich zkouší
  několik.
""",

"2.10 hints": r"""f-řetězec začíná f" a vkládá hodnoty do { }.

---

Do složených závorek můžeš dát výraz: f"{w} reversed is {w[::-1]}".

---

w = input()
print(f"{w} reversed is {w[::-1]}")
""",

"2.10 reference": r"""**f-řetězec** (formátovaný řetězcový literál) je řetězec s předponou `f`, v němž
`{ }` obsahuje pythonovský **výraz**; výraz se vyhodnotí a jeho hodnota se vloží,
převedená na text.

- Do složených závorek se vejde libovolný výraz: `f"{name}"`, `f"{a + b}"`,
  `f"{nums[0]}"`.
- Doslovnou složenou závorku napíšeš jejím zdvojením: `f"{{literal}}"` zobrazí
  `{literal}`.
- Formátovací předpis za dvojtečkou řídí zobrazení, např. `f"{price:.2f}"`
  zobrazí dvě desetinná místa a `f"{n:>5}"` zarovná vpravo do pole širokého 5.

f-řetězce jsou nejpřehlednější způsob, jak sestavit text z hodnot, a nahrazují
řetězce `+` a `str()`.

```python
name, n = "Ada", 3
f"{name} solved {n} puzzles"   # 'Ada solved 3 puzzles'
f"{1/3:.2f}"                    # '0.33'
```
""",
}
