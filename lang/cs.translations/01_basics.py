# PyQuest translations -- language 'cs' -- chapter 01_basics -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"1.1 brief": r"""# 1.1 -- Hello, output

## Koncept

**Program** je seznam instrukcí, které počítač provádí shora dolů. Nejzákladnější
instrukcí je **vypsat** (print) -- zobrazit řádek textu na obrazovce. V Pythonu to
uděláš pomocí `print(...)`. Vypíše se cokoli, co vložíš dovnitř závorek do
uvozovek.

`print` je **funkce**: vestavěná akce, kterou spustíš tím, že napíšeš její jméno
následované závorkami. To, co je v uvozovkách, je **text** (Python textu říká
*řetězec* -- řetězec znaků).

## Příklad

```python
print("Good morning")
```

Když se to spustí, na obrazovce se objeví:

```
Good morning
```

Uvozovky vyznačují, kde text začíná a končí; samy se nevypisují. Python navíc na
konci automaticky přidá zalomení řádku, takže další print začne na novém řádku.

## Tvůj úkol

Zařiď, aby program vypsal přesně tento řádek:

```
Hello, output
```

Otevři pracovní soubor kapitoly `work.py`, napiš jeden `print(...)`, který vytvoří
tento řádek, **ulož soubor** a pak spusť `check`.

## Hotovo, když

- Spuštění `check` ukáže CHECK PASSED.
- Výstup zní `Hello, output` -- stejná slova, stejná čárka. (Kontrola ignoruje
  velikost písmen, ale přesné dodržení zadání je dobrý zvyk.)
""",

"1.1 hints": r"""Která vestavěná funkce vypíše text na obrazovku? Stačí ti jediný řádek.

---

Použij `print(...)`. Text patří dovnitř závorek, do dvojitých uvozovek:
`print("nějaký text")`. Dodrž přesné znění včetně čárky.

---

print("Hello, output")
""",

"1.1 reference": r"""`print` zapíše textovou reprezentaci každého argumentu na standardní výstup
(terminál), v pořadí, a pak zapíše `end` (ve výchozím nastavení znak nového
řádku). Je to hlavní způsob, jak program ukáže uživateli výsledek.

- Každá hodnota se nejprve převede na text pomocí `str()`, takže `print(42)` i
  `print("42")` zobrazí `42`.
- Při více argumentech se `sep` (výchozí jedna mezera) vkládá *mezi* sousední
  hodnoty — nikdy před první ani za poslední.
- `end` se přidá jednou, na úplný konec. Protože jeho výchozí hodnota je `"\n"`,
  každé volání `print` ukončí aktuální řádek a další výstup začne znovu.
- `print` vrací `None`; volá se kvůli svému vedlejšímu účinku, ne kvůli návratové
  hodnotě.

```python
print("Hello, World!")        # Hello, World!
print("a", "b", "c")          # a b c
```
""",

"1.2 brief": r"""# 1.2 -- Vypisování více hodnot

## Koncept

Dvě nové myšlenky, obě o `print`.

**1. Více printů běží v pořadí.** Každý `print(...)` umístí svůj text na vlastní
řádek a Python je provádí shora dolů. Tři řádky s `print` vytvoří tři řádky
výstupu.

**2. Jeden print může zobrazit více hodnot.** Vlož do závorek několik věcí
oddělených **čárkami** a `print` je zobrazí na jednom řádku s jednou mezerou mezi
nimi:

```python
print("a", "b", "c")
```

zobrazí:

```
a b c
```

Takto můžeš míchat text a čísla. Čísla uvozovky **nepotřebují**; text ano.

## Příklad

```python
print("Scores:")
print(10, 20, 30)
```

zobrazí:

```
Scores:
10 20 30
```

První řádek je jeden print; druhý print má tři hodnoty oddělené čárkami, takže
sdílejí jeden řádek s mezerami mezi sebou.

## Tvůj úkol

Vytvoř přesně tyto dva řádky:

```
Counting:
1 2 3
```

Použij dva příkazy `print`: první vypíše slovo, druhý vypíše tři čísla `1`, `2`,
`3` jako samostatné hodnoty (mezery nech doplnit `print`).

## Hotovo, když

- Výstup jsou přesně dva řádky: `Counting:` a pak `1 2 3`.
- Druhý řádek vznikne z čísel oddělených čárkami, ne z toho, že sám napíšeš text
  `"1 2 3"`.
""",

"1.2 hints": r"""Potřebuješ dva řádky s printem. První vypíše slovo; druhý vypíše čísla.

---

V druhém printu odděl čísla čárkami: `print(1, 2, 3)`. Mezery nech doplnit print
-- nepiš je sám.

---

print("Counting:")
print(1, 2, 3)
""",

"1.2 reference": r"""Program běží shora dolů, takže po sobě jdoucí příkazy `print` vytvoří po sobě
jdoucí řádky — každé volání vypíše své argumenty a pak nový řádek.

Předání **více hodnot jednomu `print`**, oddělených čárkami, je něco jiného než
více volání `print`: hodnoty se objeví na *jednom* řádku, spojené pomocí `sep` (ve
výchozím stavu mezerou). Jde o oddělení čárkami ve volání, ne o zřetězení řetězců
— hodnoty si ponechávají vlastní typy a převádějí se nezávisle.

```python
print("one")
print("two")          # two lines

print("x", "y", 3)    # one line:  x y 3
```
""",

"1.3 brief": r"""# 1.3 -- Volba oddělovače

## Koncept

Když dáš `print` více hodnot, ve výchozím stavu je spojí mezerou. Tento spojovací
řetězec můžeš změnit speciálním nastavením zvaným **`sep`** (zkratka za
*separator*, oddělovač).

Takové nastavení se píše jako `jméno=hodnota` uvnitř závorek, za tvými hodnotami:

```python
print("a", "b", "c", sep="-")
```

zobrazí:

```
a-b-c
```

`sep="-"` říká `print`, aby mezi hodnoty vkládal pomlčku místo mezery. Oddělovač
jde pouze *mezi* hodnoty -- ne před první ani za poslední. Jako oddělovač můžeš
použít libovolný text: `sep=", "`, `sep=""` (nic), `sep="/"` a tak dále.

`sep` se musí napsat přesně, bez mezery před `=`, a hodnota v uvozovkách, protože
je to text.

## Příklad

```python
print("home", "user", "docs", sep="/")
```

zobrazí:

```
home/user/docs
```

## Tvůj úkol

Vypiš přesně toto datum pomocí tří **čísel** spojených pomlčkami:

```
2024-12-25
```

Předej `2024`, `12`, `25` jedinému `print` a nastav `sep` tak, aby byly spojeny
`-`. Nepiš pomlčky sám jako součást textu.

## Hotovo, když

- Výstup je přesně `2024-12-25`.
- Vznikne ze tří čísel plus nastavení `sep`, ne z jednoho napsaného řetězce.
""",

"1.3 hints": r"""Dej printu tři čísla a pak přidej nastavení, které změní oddělovač.

---

Tím nastavením je `sep`. Za svá tři čísla přidej `sep="-"` do téhož printu:
`print(a, b, c, sep="-")`.

---

print(2024, 12, 25, sep="-")
""",

"1.3 reference": r"""`sep` a `end` jsou pouze klíčové argumenty (keyword-only), které řídí mezerování
kolem výstupu `print`.

- **`sep`** je řetězec vkládaný mezi každou dvojici sousedních hodnot. Výchozí je
  `" "`. Nikdy se neobjeví před první hodnotou ani za poslední, takže *N* hodnot
  vytvoří *N − 1* oddělovačů.
- **`end`** je řetězec zapsaný jednou za poslední hodnotou. Výchozí je `"\n"`,
  proto každý `print` ukončí svůj řádek. Nastav `end=""`, aby kurzor zůstal na
  stejném řádku a další `print` na něj navázal.

```python
print("2024", "01", "15", sep="-")   # 2024-01-15
print("loading", end="")
print("...")                          # loading... (one line)
```
""",

"1.4 brief": r"""# 1.4 -- Komentáře

## Koncept

**Komentář** je poznámka v kódu, kterou Python ignoruje. Cokoli za `#` na řádku se
při běhu programu přeskočí. Komentáře jsou pro lidi -- vysvětlují, co kód dělá.

```python
# This whole line is a note and does nothing.
print("Hi")   # Text after # on a code line is also ignored.
```

Výše se spustí pouze `print("Hi")`. Obě poznámky se přeskočí.

Druhé, velmi praktické využití: **zakomentování** kódu. Když dáš `#` před řádek
skutečného kódu, ten řádek přestane běžet -- aniž bys ho smazal. Takto řádek
dočasně vypneš.

```python
# print("off")
print("on")
```

Vypíše se pouze `on`; první řádek je teď komentář.

## Častý omyl

Dát `#` před řádek ho **nesmaže** ani nezpůsobí chybu -- řádek se prostě nespustí.
Odeber `#` a spustí se znovu.

## Tvůj úkol

Výchozí soubor už obsahuje řádek, který vypíše `Hidden`. **Zakomentuj ho**, aby se
nespustil -- **nemaž** ho -- a přidej řádek, který vypíše `Visible`.

Program musí vypsat pouze:

```
Visible
```

## Hotovo, když

- Výstup je přesně `Visible`.
- Řádek `print("Hidden")` je stále v souboru, ale zakomentovaný pomocí `#`, takže
  se nespustí. (Tato úloha je o *zakomentování*, takže smazání řádku se nepočítá.)
""",

"1.4 hints": r"""Řádek začínající znakem # se ignoruje. Dej jeden před řádek s Hidden.

---

Změň `print("Hidden")` na `# print("Hidden")` a pak přidej `print("Visible")` na
vlastní řádek.

---

# print("Hidden")
print("Visible")
""",

"1.4 reference": r"""`#` zahajuje **komentář**: od `#` do konce daného řádku Python text ignoruje.
Komentáře vysvětlují, *proč* kód něco dělá; na samotný běh nemají vliv.

- Komentář může být na vlastním řádku nebo následovat za kódem na stejném řádku
  (`x = 1  # nastavení`).
- `#` uvnitř řetězcového literálu je jen znak, ne komentář (`"#1"` je text `#1`).
- Python **nemá syntaxi pro blokové komentáře**: okomentuj každý řádek pomocí `#`,
  nebo — pro jednorázový blok — použij řetězcový literál, který se vyhodnotí a
  zahodí.

„Zakomentování“ řádku (dání `#` před něj) je nejrychlejší způsob, jak ho vypnout
bez smazání.

```python
# this whole line is ignored
print("hi")   # and this trailing note is too
```
""",

"1.5 brief": r"""# 1.5 -- Uložení hodnoty

## Koncept

**Proměnná** je jméno, které drží hodnotu, abys ji mohl použít později. Vytvoříš
ji pomocí `=`, znaku **přiřazení**:

```python
score = 100
```

Čti to jako „ať je `score` rovno `100`.“ Jméno jde nalevo, hodnota napravo. Po
tomto řádku znamená napsání `score` kdekoli hodnotu `100`.

To se liší od `==` (s nímž se setkáš později u porovnávání). Jediné `=` *ukládá*.

Jakmile je hodnota uložená, můžeš jméno použít, kolikrát chceš:

```python
score = 100
print(score)
print(score)
```

zobrazí:

```
100
100
```

Všimni si, že `print(score)` nemá kolem `score` **žádné uvozovky**. Uvozovky by z
toho udělaly doslovný text „score“; bez uvozovek to znamená hodnotu proměnné,
`100`.

## Pravidla pojmenování (stručně)

Jméno proměnné může obsahovat písmena, číslice a podtržítka, ale nesmí začínat
číslicí a nesmí obsahovat mezery. Používej srozumitelná jména: `total`,
`user_name`, `count`.

## Tvůj úkol

Ulož číslo `42` do proměnné a pak tuto proměnnou vypiš **dvakrát**, aby výstup
byl:

```
42
42
```

V obou případech použij proměnnou -- nepiš `42` přímo do printů.

## Hotovo, když

- Výstup je `42` na dvou samostatných řádcích.
- Oba řádky vznikají vypsáním tvé proměnné (bez uvozovek kolem jejího jména).
""",

"1.5 hints": r"""Nejprve vytvoř proměnnou pomocí `=`, pak vypiš její jméno na dvou řádcích.

---

`n = 42` uloží hodnotu. Pak `print(n)` dvakrát. Žádné uvozovky kolem n.

---

n = 42
print(n)
print(n)
""",

"1.5 reference": r"""Přiřazení pomocí `=` sváže **jméno** s hodnotou. Poté jméno na tuto hodnotu
*odkazuje* a použití jména kdekoli se vyhodnotí jako ona. Při čtení kódu `=`
znamená „stává se“, ne „rovná se“ (rovnost je `==`).

- Jména se nedeklarují a nemají pevný typ — první přiřazení jméno vytvoří a to pak
  ukazuje na libovolný objekt, který přiřadíš.
- Jméno musí začínat písmenem nebo podtržítkem a obsahovat písmena, číslice nebo
  podtržítka; rozlišuje velikost písmen (`total` a `Total` jsou různá).
- Nejprve se plně vyhodnotí pravá strana, pak se výsledek sváže se jménem nalevo.

```python
greeting = "Hello"
print(greeting)        # Hello  -- the name stands in for the value
```
""",

"1.6 brief": r"""# 1.6 -- Přeřazení proměnné

## Koncept

Proměnnou lze po vytvoření **změnit**. Opětovné přiřazení témuž jménu nahradí
starou hodnotu novou. Jméno vždy odkazuje na to, co bylo uloženo **naposledy**.

```python
x = 10
print(x)   # 10
x = 20
print(x)   # 20
```

Na pořadí záleží: program běží shora dolů, takže první `print(x)` vidí `10` a `x`
se stane `20` až po druhém přiřazení.

Běžný a užitečný vzor je aktualizace proměnné pomocí její vlastní aktuální
hodnoty:

```python
x = 10
x = x + 5   # take the current x (10), add 5, store 15 back in x
print(x)    # 15
```

Nejprve se vyhodnotí pravá strana (`10 + 5`) a pak se výsledek uloží zpět do `x`.

## Častý omyl

Přeřazení nevytvoří druhou proměnnou. Stále existuje jen jedno `x`; jeho uložená
hodnota se vyměnila. Stará hodnota prostě zmizela.

## Tvůj úkol

Vytvoř proměnnou s hodnotou `10` a vypiš ji. Pak tutéž proměnnou přeřaď na `20` a
vypiš ji znovu. Výstup musí být:

```
10
20
```

## Hotovo, když

- Výstup je `10` a pak `20` na dvou řádcích.
- Oba řádky vypisují **stejnou** proměnnou, před změnou i po ní.
""",

"1.6 hints": r"""Vypiš proměnnou, pak přiřaď témuž jménu novou hodnotu a vypiš znovu.

---

Pořadí je: `x = 10`, `print(x)`, `x = 20`, `print(x)`.

---

x = 10
print(x)
x = 20
print(x)
""",

"1.6 reference": r"""Proměnná je jméno, ne krabice: opětovné přiřazení jméno **znovu sváže** s novou
hodnotou. Jméno vždy drží své nejnovější přiřazení; předchozí hodnota přes něj
prostě už není dosažitelná.

- Každé `=` nahradí to, na co jméno ukazuje. Na pořadí záleží — pozdější přiřazení
  vítězí.
- Pravá strana se vyhodnotí pomocí *aktuální* hodnoty jména, pak se výsledek znovu
  sváže, takže `x = x + 1` přečte staré `x` a uloží nové.
- Složené tvary (`x += 1`, `x *= 2`, …) jsou zkratkou přesně pro tohle: přečíst,
  zkombinovat, znovu svázat.

```python
score = 10
score = 25        # score is now 25
score = score + 5 # reads 25, stores 30
```
""",

"1.7 brief": r"""# 1.7 -- Text vs. číslo

## Koncept

Python rozlišuje dva druhy hodnot a hodně na tom záleží:

- **Číslo** jako `5` -- psané bez uvozovek. Celým číslům Python říká `int`
  (integer).
- **Řetězec** jako `"5"` -- psaný s uvozovkami. Je to *text*, který jen náhodou
  vypadá jako číslo. Python mu říká `str`.

Se znakem `+` se chovají odlišně:

- U čísel `+` **sčítá**: `5 + 5` je `10`.
- U řetězců `+` **spojuje** (tomu se říká **zřetězení**): `"5" + "5"` je `"55"` --
  dva kusy textu slepené dohromady.

```python
print(5 + 5)        # 10   (numbers add)
print("5" + "5")    # 55   (text joins)
print("ab" + "cd")  # abcd
```

Takže `"5"` a `5` vypadají na obrazovce stejně, ale jsou to různé typy a `+` s
nimi zachází úplně jinak.

## Častý omyl

`"5"` není číslo pět. Uvozovky z toho dělají text. Nemůžeš s ním počítat a čekat
sčítání -- `"5" + "5"` dá `"55"`, ne `10`.

## Tvůj úkol

Vypiš tyto dva řádky, v tomto pořadí:

```
55
10
```

- První řádek musí vzniknout **spojením dvou řetězců** `"5"` a `"5"` pomocí `+`.
- Druhý řádek musí vzniknout **sečtením dvou čísel** `5` a `5` pomocí `+`.

## Hotovo, když

- Výstup je `55` a pak `10`.
- První řádek používá zřetězení řetězců; druhý řádek používá sčítání čísel.
""",

"1.7 hints": r"""Tady o všem rozhodují uvozovky. S uvozovkami + spojuje; bez uvozovek + sčítá.

---

První řádek: `print("5" + "5")`. Druhý řádek: `print(5 + 5)`. Všimni si uvozovek u
prvního a žádných u druhého.

---

print("5" + "5")
print(5 + 5)
""",

"1.7 reference": r"""Každá hodnota má **typ**. Dva základní se objevují hned:

- **řetězec** (`str`) je text psaný v uvozovkách: `"42"`, `"hello"`;
- **celé číslo** (`int`) je číslo psané jako holé číslice: `42`.

Celý rozdíl jsou uvozovky. `type("42")` je `str`; `type(42)` je `int`.

Typ rozhoduje, co operátor znamená. `+` mezi dvěma **řetězci** je *zřetězí*
(spojí); `+` mezi dvěma **čísly** je *sečte*:

```python
"2" + "2"   # "22"  -- text joined
 2  +  2    #  4    -- numbers added
```

Míchání obou pomocí `+` je chyba (`TypeError`), protože Python nebude hádat, jestli
jsi chtěl sčítat, nebo spojovat. Nejprve explicitně převeď: `int("2") + 2` je `4`
a `"$" + str(2)` je `"$2"`.
""",

"1.8 brief": r"""# 1.8 -- Aritmetika a pořadí

## Koncept

Python počítá pomocí těchto znaků (zvaných **operátory**):

- `+` sčítání
- `-` odčítání
- `*` násobení
- `/` dělení

```python
print(2 + 3)   # 5
print(10 - 4)  # 6
print(6 * 7)   # 42
```

**Na pořadí záleží.** Stejně jako ve školní matematice se `*` a `/` provádějí
**před** `+` a `-`. Takže:

```python
print(2 + 3 * 4)   # 14, not 20  -- 3*4 first, then +2
```

Chceš-li vynutit jiné pořadí, obal část do **závorek** `( )`. Cokoli je uvnitř
závorek, vyhodnotí se nejdřív:

```python
print((2 + 3) * 4)   # 20  -- 2+3 first, then *4
```

Tohle je vůbec nejčastější zdroj chyb typu „špatné číslo“, takže se vyplatí si to
teď osvojit.

## Příklad

```python
print(1 + 2 * 3)     # 7
print((1 + 2) * 3)   # 9
```

## Tvůj úkol

Vypiš tyto dva řádky:

```
14
20
```

- První řádek je `2 + 3 * 4` bez závorek (nejdřív násobení).
- Druhý řádek jsou stejná čísla, ale se závorkami, aby se nejdřív sčítalo:
  `(2 + 3) * 4`.

## Hotovo, když

- Výstup je `14` a pak `20`.
- Rozdíl mezi řádky vzniká pouze tím, že závorky mění pořadí.
""",

"1.8 hints": r"""Násobení proběhne před sčítáním, pokud závorky neřeknou jinak.

---

První řádek: `print(2 + 3 * 4)`. Druhý řádek: přidej závorky kolem 2 + 3:
`print((2 + 3) * 4)`.

---

print(2 + 3 * 4)
print((2 + 3) * 4)
""",

"1.8 reference": r"""Aritmetické operátory jsou `+` (sčítání), `-` (odčítání), `*` (násobení), `/`
(dělení), `//` (celočíselné dělení), `%` (zbytek) a `**` (mocnina).

Řídí se **prioritou** (pořadím operací), od nejvyšší po nejnižší:

1. `**`
2. unární `-` (negace)
3. `*`, `/`, `//`, `%`
4. `+`, `-`

Operátory se stejnou prioritou se vyhodnocují **zleva doprava**, kromě `**`, který
je pravě asociativní (`2 ** 3 ** 2` je `2 ** 9`). **Závorky** tohle všechno
přebijí — vyhodnotí se jako první.

```python
2 + 3 * 4      # 14   -- * before +
(2 + 3) * 4    # 20   -- parentheses first
-3 ** 2        # -9   -- ** before unary minus
```
""",

"1.9 brief": r"""# 1.9 -- Tři druhy dělení

## Koncept

Dělení má v Pythonu tři užitečné operátory:

- `/`  běžné dělení -- vždy dá desetinné číslo (Python jim říká `float`). `7 / 2`
  je `3.5`.
- `//` celočíselné dělení -- vydělí a zahodí desetinnou část, takže dá celé číslo.
  `7 // 2` je `3`.
- `%`  modulo -- dá **zbytek** po dělení. `7 % 2` je `1` (protože 2 se do 7 vejde
  třikrát a 1 zbude).

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
```

Číslo s desetinnou tečkou, jako `3.5`, je `float`. Celé číslo bez tečky, jako `3`,
je `int`. Všimni si, že `/` dá `3.5`, i když dělí čísla vypadající beze zbytku:
`4 / 2` je `2.0`, ne `2`.

`%` je překvapivě šikovné: číslo je sudé právě tehdy, když `n % 2` je `0`.

## Častý omyl

`/` nezaokrouhluje na celé číslo. `7 / 2` je `3.5`, nikdy `3`. Pokud chceš
celočíselnou část, od toho je `//`.

## Tvůj úkol

Pomocí čísel 7 a 2 vypiš tyto tři řádky v pořadí:

```
3.5
3
1
```

Pro první použij `/`, pro druhý `//` a pro třetí `%`.

## Hotovo, když

- Výstup je přesně `3.5`, pak `3`, pak `1`.
- Každý řádek používá odpovídající operátor (`/`, `//`, `%`).
""",

"1.9 hints": r"""Existují tři operátory dělení: /, // a %. Jeden na řádek.

---

`print(7 / 2)` dá 3.5, `print(7 // 2)` dá 3, `print(7 % 2)` dá 1.

---

print(7 / 2)
print(7 // 2)
print(7 % 2)
""",

"1.9 reference": r"""Python má tři operátory dělení:

- **`/` pravé dělení** vždy vytvoří **`float`**, i když je výsledek celé číslo:
  `7 / 2 == 3.5` a `4 / 2 == 2.0` (všimni si `.0`).
- **`//` celočíselné dělení** dělí a zaokrouhluje *dolů* k zápornému nekonečnu, u
  dvou celých čísel dává `int`: `7 // 2 == 3`. Se záporným operandem stále
  zaokrouhluje dolů, takže `-7 // 2 == -4`, ne `-3`.
- **`%` zbytek (modulo)** je to, co zbude: `7 % 2 == 1`. V Pythonu má výsledek
  **znaménko dělitele**, takže `-7 % 2 == 1`.

Pro libovolná celá čísla platí `a == (a // b) * b + (a % b)`. `divmod(a, b)` vrátí
dvojici `(a // b, a % b)` najednou. Dělení nulou vyvolá `ZeroDivisionError`.

```python
17 / 5    # 3.4
17 // 5   # 3
17 % 5    # 2   -- 3*5 + 2 == 17
```
""",

"1.10 brief": r"""# 1.10 -- Dotaz na uživatele

## Koncept

`input()` pozastaví program, nechá člověka napsat řádek a **vrátí to, co napsal,
jako text** (řetězec). Obvykle to uložíš do proměnné:

```python
name = input()
print("Hi, " + name)
```

Když člověk napíše `Sam`, program vypíše `Hi, Sam`.

`input()` vždy vrátí **řetězec**, i když člověk napíše číslice. (To budeš řešit v
další úloze.)

Napsaný text můžeš spojit s jiným textem pomocí `+`, přesně jako v úloze 1.7:

```python
city = input()
print("You live in " + city)
```

> Poznámka: když spustíš `check`, kontrola za tebe vstup dodá automaticky -- nic
> nepíšeš ručně.

## Příklad

Zadaný vstup: `Berlin`

```python
city = input()
print("Welcome to " + city)
```

Výstup:

```
Welcome to Berlin
```

## Tvůj úkol

Přečti jeden řádek vstupu (jméno) a pozdrav ho. Pokud je vstup `World`, výstup musí
být přesně:

```
Hello, World
```

Tedy: přečti jméno pomocí `input()` a pak vypiš `Hello, ` spojené se jménem. Dej
pozor na čárku a jednu mezeru za ní.

## Hotovo, když

- Pro vstup `World` je výstup `Hello, World`.
- Pro libovolné jiné jméno pozdraví stejným způsobem (kontrola jich zkouší více).
""",

"1.10 hints": r"""Ulož to, co vrátí input(), do proměnné a pak sestav pozdrav pomocí +.

---

`name = input()` a pak `print("Hello, " + name)`. Text před jménem obsahuje čárku
a mezeru: „Hello, “.

---

name = input()
print("Hello, " + name)
""",

"1.10 reference": r"""`input` přečte **jeden řádek** ze standardního vstupu — vše, co uživatel napíše,
než stiskne Enter — odstraní koncový znak nového řádku a vrátí to jako **řetězec**.

- Návratová hodnota je *vždy* `str`, i když uživatel napsal číslice: `input()` při
  `42` vrátí `"42"`, ne `42`. Pro počítání to převeď (viz `int()`).
- Volitelný argument `prompt` se nejprve vypíše na obrazovku, bez koncového nového
  řádku, takže uživatel píše na stejný řádek.
- Pokud vstupní proud skončí a není co číst (konec souboru), `input` vyvolá
  `EOFError`.

```python
name = input("Your name? ")   # prompts, then reads a line
print("Hi, " + name)
```
""",

"1.11 brief": r"""# 1.11 -- Číslo ze vstupu

## Koncept

`input()` vždy vrátí **text**, i když člověk napíše číslice. Pokud s ním zkusíš
počítat, `+` bude místo sčítání spojovat -- vzpomeň si na úlohu 1.7:

```python
n = input()      # user types 21  ->  n is the string "21"
print(n + n)     # "2121", not 42
```

Pro počítání nejprve **převeď** text na číslo pomocí `int(...)`:

```python
n = int(input())   # "21" -> 21, a real number now
print(n * 2)       # 42
```

`int(...)` vezme text, který vypadá jako celé číslo, a udělá z něj `int`, se kterým
můžeš počítat. Tento vzor -- `int(input())` -- je nesmírně častý.

## Častý omyl

`int` jen „neodstraní uvozovky“; vytvoří jiný typ. Po `int(input())` je hodnota
číslo, takže `+`, `*`, `//` a spol. počítají doopravdy.

## Tvůj úkol

Přečti ze vstupu celé číslo a pak vypiš jeho **dvojnásobek**. Příklady:

- vstup `21` -> výstup `42`
- vstup `0`  -> výstup `0`
- vstup `-5` -> výstup `-10`

Tedy: přečti pomocí `input()`, převeď pomocí `int(...)`, vynásob dvěma a vypiš
výsledek.

## Hotovo, když

- Pro vstup `21` je výstup `42`.
- Funguje to i pro `0` a pro záporné číslo jako `-5` (kontrola je zkouší).
""",

"1.11 hints": r"""input() vrací text. Než začneš počítat, musíš ho převést na číslo.

---

Obal input do int: `n = int(input())`. Pak `print(n * 2)`.

---

n = int(input())
print(n * 2)
""",

"1.11 reference": r"""`int` převede hodnotu na **celé číslo**. Nejčastěji se používá k převodu
**řetězce**, který vrací `input()`, na číslo, se kterým můžeš počítat.

- `int("42")` je `42`. Okolní mezery se ignorují (`int(" 42 ")` funguje); úvodní
  znaménko je povoleno (`int("-5")`).
- Text, který není celé číslo, vyvolá `ValueError` — `int("3.5")` i `int("ten")`
  selžou. Pro desetinná čísla použij `float("3.5")`.
- Zavolané na `float` `int` ořeže *směrem k nule* (`int(3.9)` je `3`, `int(-3.9)`
  je `-3`).

Protože `input()` vždy vrací text, čtení čísla je dvoukrokový idiom:

```python
n = int(input("How many? "))   # read text, then parse it to an int
print(n * 2)
```
""",
}
