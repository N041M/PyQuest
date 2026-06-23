# PyQuest translations -- language 'cs' -- chapter 03_decisions_loops -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"3.1 brief": r"""# 3.1 -- Booleany a porovnávání

## Koncept

**Boolean** je hodnota, která je buď `True`, nebo `False` -- odpověď ano/ne. Je to
vlastní typ (`bool`), psaný s velkým písmenem.

Booleany získáš **porovnáváním** hodnot:

| operátor | význam |
|---|---|
| `==` | rovná se |
| `!=` | nerovná se |
| `<`  | menší než |
| `>`  | větší než |
| `<=` | menší nebo rovno |
| `>=` | větší nebo rovno |

```python
print(3 < 5)      # True
print(3 == 5)     # False
print(7 >= 7)     # True
```

Pozor, `==` (porovnání) jsou **dvě** rovnítka. Jedno `=` proměnnou *přiřadí*; `==`
se *ptá „rovnají se?“*.

## Příklad

```python
a = 4
b = 9
print(a > b)      # False
```

## Tvůj úkol

Přečti dvě celá čísla (každé na vlastním řádku). Vypiš, zda je **první větší než
druhé** -- tedy vypiš výsledek `first > second` (bude to `True`, nebo `False`).

Pro vstup `8` a pak `3` je výstup:

```
True
```

## Hotovo, když

- Pro `8` a pak `3` vypíše `True`; pro `2` a pak `5` vypíše `False`.
- Když se obě čísla rovnají, vypíše `False` (rovno není „větší“).
""",

"3.1 hints": r"""Porovnání jako a > b je už True nebo False -- můžeš ho vypsat přímo.

---

Přečti obě čísla jako int a pak vypiš porovnání:
`print(first > second)`.

---

a = int(input())
b = int(input())
print(a > b)
""",

"3.1 reference": r"""**Boolean** je jedna ze dvou hodnot, `True` nebo `False` (typ `bool`).
**Porovnávací operátory** ho vytvoří porovnáním dvou hodnot:

- `==` rovno, `!=` nerovno,
- `<` menší než, `>` větší než, `<=` nejvýše, `>=` nejméně.

`==` (otázka „rovnají se?“) není `=` (příkaz „přiřaď“). Čísla se porovnávají podle
hodnoty; řetězce se porovnávají **lexikograficky** (slovníkové pořadí, podle kódu
znaku, takže velká písmena se řadí před malá). Porovnání lze **řetězit**:
`0 <= x < 10` znamená `0 <= x and x < 10`.

```python
3 < 5        # True
3 == 3.0     # True   -- equal values, different types
"a" < "b"    # True
```
""",

"3.2 brief": r"""# 3.2 -- if

## Koncept

**Příkaz `if`** spustí blok kódu **jen když** je podmínka `True`:

```python
if condition:
    do_something()
    do_more()
```

Všimni si dvou věcí:

1. Řádek končí **dvojtečkou** `:`.
2. Řádky, které se mají spustit, když je podmínka pravdivá, jsou **odsazené**
   (použij 4 mezery). Podle odsazení Python pozná, které řádky patří k `if`. Když
   je podmínka `False`, odsazené řádky se přeskočí.

```python
age = 20
if age >= 18:
    print("adult")     # runs only when age >= 18
```

Kdyby `age` bylo `15`, nic by se nevypsalo.

## Častý omyl

Odsazení není v Pythonu dekorace -- definuje blok. Zapomenout odsadit (nebo míchat
mezery) je syntaktická chyba.

## Tvůj úkol

Přečti celé číslo. **Pokud je záporné**, vypiš `negative`. Pokud záporné není,
nevypisuj vůbec nic.

Pro vstup `-4` je výstup:

```
negative
```

Pro vstup `7` není žádný výstup.

## Hotovo, když

- Záporné číslo vypíše `negative`.
- Nula a kladná čísla nevypíšou nic (`0` není záporná).
""",

"3.2 hints": r"""Číslo je záporné, když je menší než 0:  n < 0.

---

Napiš `if n < 0:` a pak na další řádek odsazený `print("negative")`.

---

n = int(input())
if n < 0:
    print("negative")
""",

"3.2 reference": r"""Příkaz **`if`** spustí odsazený blok **jen když** je jeho podmínka pravdivá.
Podmínka se vyhodnotí na boolean; je-li pravdivá, blok se spustí; je-li
nepravdivá, přeskočí se a program pokračuje níže.

- Blok je vymezen **odsazením** (obvykle 4 mezery). Každý řádek odsazený pod `if`
  k němu patří; první řádek zpět na vnější úrovni ho ukončí.
- Podmínka nemusí být doslovné `True`/`False` — testuje se **pravdivost** libovolné
  hodnoty: `0`, `0.0`, `""` a prázdné kolekce jsou nepravdivé; vše ostatní je
  pravdivé.

```python
if temperature > 30:
    print("hot")        # runs only when the test is True
print("done")           # always runs -- not indented under the if
```
""",

"3.3 brief": r"""# 3.3 -- if / else

## Koncept

`else` dá `if` druhou větev: kód, který se spustí, když je podmínka **False**.
Spustí se přesně jeden ze dvou bloků.

```python
if temperature > 30:
    print("hot")
else:
    print("not hot")
```

`else:` je zarovnané s `if` (stejné odsazení) a jeho blok je odsazený stejně jako
blok `if`.

## Připomenutí

`n % 2` je zbytek po dělení `n` dvěma (s `%` ses setkal v kapitole 1). Číslo je
**sudé** právě tehdy, když `n % 2 == 0`.

## Příklad

```python
n = 7
if n % 2 == 0:
    print("even")
else:
    print("odd")
# prints: odd
```

## Tvůj úkol

Přečti celé číslo a vypiš `even`, je-li sudé, nebo `odd`, pokud není.

Pro vstup `10` je výstup:

```
even
```

## Hotovo, když

- Sudá čísla vypíšou `even`, lichá `odd`.
- Funguje pro `0` (sudá) i pro záporná čísla.
""",

"3.3 hints": r"""Sudé znamená, že zbytek po dělení 2 je nula:  n % 2 == 0.

---

Použij if/else: pokud `n % 2 == 0`, vypiš "even", jinak "odd".

---

n = int(input())
if n % 2 == 0:
    print("even")
else:
    print("odd")
""",

"3.3 reference": r"""Klauzule **`else`** dá `if` druhou větev: její blok se spustí přesně tehdy, když
je podmínka `if` **nepravdivá**. Společně tvoří dvojcestnou volbu — vždy se spustí
jedna, nebo druhá větev, nikdy obě.

- `else` nebere žádnou podmínku; je to záchytný případ pro „`if` byl nepravdivý“.
- Musí se párovat s `if` na stejném odsazení a jeho blok je odsazený stejně.

```python
if n % 2 == 0:
    print("even")
else:
    print("odd")        # runs only when n % 2 == 0 is False
```
""",

"3.4 brief": r"""# 3.4 -- elif

## Koncept

`elif` (zkratka za „else if“) přidá **další větve** mezi `if` a `else`. Python
kontroluje podmínky popořadě a spustí **první**, která je `True`; ostatní přeskočí.
`else` (volitelné) zachytí vše, co zbylo.

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

Na pořadí záleží: protože vítězí první pravdivá větev, obvykle postupuješ od
nejkonkrétnější nebo nejvyšší podmínky dolů.

## Příklad

```python
n = 0
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
# prints: zero
```

## Tvůj úkol

Přečti celé číslo a vypiš přesně jedno z:

- `negative`, je-li menší než 0,
- `zero`, je-li 0,
- `positive`, je-li větší než 0.

Pro vstup `0` je výstup:

```
zero
```

## Hotovo, když

- `-3` vypíše `negative`, `0` vypíše `zero`, `5` vypíše `positive`.
- Pro libovolný vstup se vypíše přesně jeden řádek.
""",

"3.4 hints": r"""Tři případy znamenají if ... elif ... else.

---

`if n < 0:` -> negative; `elif n == 0:` -> zero; `else:` -> positive.

---

n = int(input())
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
""",

"3.4 reference": r"""**`elif`** („else if“) přidá další větve mezi `if` a `else`. Python kontroluje
každou podmínku **popořadě** a spustí blok **první**, která je pravdivá, pak
zbytek přeskočí. Volitelné závěrečné `else` ošetří „nic nesedělo“.

- Spustí se vždy jen jedna větev — první pravdivá. Pozdější podmínky se ani
  nevyhodnotí.
- Protože vítězí první shoda, na pořadí záleží: konkrétnější nebo přednostní testy
  dej dopředu.
- Řetěz `elif` je plošší a jasnější než vnořování `if` do každého `else`.

```python
if score >= 90:
    grade = "A"
elif score >= 80:       # only checked if the first was False
    grade = "B"
else:
    grade = "C"
```
""",

"3.5 brief": r"""# 3.5 -- and / or / not

## Koncept

Booleany můžeš kombinovat třemi slovy:

- `and` -- True jen když jsou **obě** strany True.
- `or` -- True když je True **alespoň jedna** strana.
- `not` -- otočí boolean: `not True` je `False`.

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

age = 25
print(age >= 18 and age < 65)   # True  (both hold)
```

Díky tomu může jedna podmínka testovat několik věcí najednou.

## Příklad

```python
n = 12
print(n % 2 == 0 and n % 3 == 0)   # True  (12 is divisible by both)
```

## Tvůj úkol

Přečti celé číslo. Vypiš, zda je dělitelné **zároveň** 2 i 3 -- tedy vypiš výsledek
`(n % 2 == 0) and (n % 3 == 0)` (což je `True`, nebo `False`).

Pro vstup `12` je výstup:

```
True
```

## Hotovo, když

- `12` a `6` vypíšou `True`; `4` a `9` vypíšou `False`.
- `0` vypíše `True` (0 je dělitelná vším).
""",

"3.5 hints": r"""„Dělitelné 2“ je n % 2 == 0. Potřebuješ to A totéž pro 3.

---

Spoj obě kontroly pomocí `and` a vypiš to celé:
`print(n % 2 == 0 and n % 3 == 0)`.

---

n = int(input())
print(n % 2 == 0 and n % 3 == 0)
""",

"3.5 reference": r"""**Booleovské operátory** kombinují podmínky:

- **`and`** je pravdivé jen když jsou **obě** strany pravdivé.
- **`or`** je pravdivé když je pravdivá **alespoň jedna** strana.
- **`not`** obrátí jednu hodnotu.

Vyhodnocují se **zkráceně** (short-circuit): `and` se zastaví u prvního
nepravdivého operandu, `or` u prvního pravdivého, takže pravá strana se
nevyhodnotí, když už levá rozhodla. Priorita je `not` > `and` > `or`; závorky
udělají záměr jasným.

```python
0 < x and x < 100      # True only inside the range
done or out_of_time    # True if either holds
not finished           # flips the flag
```
""",

"3.6 brief": r"""# 3.6 -- Vnořené podmínky

## Koncept

Blok `if` může obsahovat **další** `if`. Tomu se říká **vnořování**. Vnitřní
kontrola proběhne jen tehdy, když je vnější podmínka už pravdivá. Každá úroveň je
odsazená o krok dál.

```python
if logged_in:
    if is_admin:
        print("admin panel")
    else:
        print("user page")
else:
    print("please log in")
```

Zde se `is_admin` kontroluje jen tehdy, když je `logged_in` pravdivé.

## Příklad

```python
n = 250
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
# prints: big
```

## Tvůj úkol

Přečti celé číslo a zařaď ho:

- je-li **0 nebo záporné**, vypiš `non-positive`;
- jinak (je kladné) vypiš `small`, je-li **menší než 100**, nebo `big`, je-li
  **100 a více**.

Použij vnořený `if` (vnější kontrola na kladnost, vnitřní na velikost).

Pro vstup `42` je výstup:

```
small
```

## Hotovo, když

- `-1` a `0` vypíšou `non-positive`; `42` vypíše `small`; `100` a `500` vypíšou
  `big`.
""",

"3.6 hints": r"""Nejprve rozhodni kladné vs. ne. Jen pokud je kladné, ptáš se na malé vs. velké.

---

Vnější: `if n > 0:` ... `else: print("non-positive")`. Uvnitř if další if/else
porovnávající n se 100.

---

n = int(input())
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
""",

"3.6 reference": r"""Blok `if` může sám obsahovat další `if` — **vnořování**. Vnitřní test proběhne
**jen když** byla vnější podmínka pravdivá, takže vnořování vyjadřuje „tohle, a pak
uvnitř toho tohle“.

- Každá úroveň přidá krok odsazení; vnitřní blok je odsazený pod vnitřní `if`.
- Vnořování a `and` mohou vyjádřit totéž — `if a: if b:` je jako `if a and b:` —
  ale vnořování je správný nástroj, když vnější případ potřebuje vlastní ošetření
  (např. `else`) oddělené od vnitřního.
- Drž vnoření mělké; hluboké pyramidy se špatně čtou a řetěz `elif` nebo časný
  `return` se často čte lépe.

```python
if logged_in:
    if is_admin:
        show_admin_panel()   # only when logged_in AND is_admin
    else:
        show_user_panel()    # logged_in but not admin
```
""",

"3.7 brief": r"""# 3.7 -- while

## Koncept

**Cyklus `while`** opakuje blok, **dokud** podmínka zůstává `True`. Zkontroluje
podmínku, spustí blok, pak zkontroluje znovu -- stále dokola:

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1   # move toward making the condition False
# prints 1, 2, 3
```

Řádek `count = count + 1` je zásadní: mění `count`, takže se podmínka nakonec stane
`False`. Bez něj se cyklus nikdy nezastaví.

## Častý omyl -- nekonečný cyklus

Pokud se podmínka nikdy nestane `False`, cyklus běží navždy. Vždy se ujisti, že se
něco uvnitř cyklu posouvá k bodu zastavení. (Pokud se zdá, že program zamrzl, je to
obvykle nekonečný cyklus.)

## Příklad

```python
n = 4
i = 1
while i <= n:
    print(i)
    i = i + 1
# prints 1, 2, 3, 4
```

## Tvůj úkol

Přečti celé číslo `n` a pak vypiš každé číslo od `1` do `n`, každé na vlastním
řádku, pomocí cyklu `while`.

Pro vstup `3` je výstup:

```
1
2
3
```

## Hotovo, když

- `3` vypíše `1`, `2`, `3`. `1` vypíše jen `1`.
- `0` (nebo záporné) nevypíše nic -- tělo cyklu se nikdy nespustí.
""",

"3.7 hints": r"""Začni počítadlo na 1 a opakuj, dokud je stále <= n.

---

`i = 1`, pak `while i <= n:` vypiš i a pak `i = i + 1`.

---

n = int(input())
i = 1
while i <= n:
    print(i)
    i = i + 1
""",

"3.7 reference": r"""Cyklus **`while`** opakuje svůj blok, **dokud** jeho podmínka zůstává pravdivá.
Podmínka se kontroluje **před** každým průchodem; jakmile se stane nepravdivou,
cyklus skončí a program pokračuje níže.

- Něco uvnitř cyklu musí nakonec podmínku zneplatnit (např. posun počítadla),
  jinak se točí navždy — nekonečný cyklus.
- Je-li podmínka nepravdivá hned při první kontrole, tělo se spustí nulakrát.
- Použij `while`, když dopředu neznáš počet průchodů (točíš se, dokud něco
  nenastane); použij `for`, když počítáš známý rozsah.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1        # moves toward ending the loop -> 3, 2, 1
```
""",

"3.8 brief": r"""# 3.8 -- Cyklus do zarážky (sentinel)

## Koncept

Cyklus nemusí počítat. Může běžet, dokud uživatel nezadá speciální hodnotu
**zarážku** (sentinel), která znamená „stop“. Trik je přečíst jednou *před* cyklem
a pak číst znovu *na konci* každého průchodu:

```python
line = input()
while line != "quit":
    print("you said:", line)
    line = input()        # read the next one
print("done")
```

Cyklus běží, dokud vstup není zarážka (zde `"quit"`). Jakmile zarážka přijde,
podmínka je nepravdivá a cyklus skončí.

## Příklad

Čti čísla a sčítej je, dokud není zadána `0`:

```python
total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
```

## Tvůj úkol

Čti celá čísla, jedno na řádek, a sčítej je. Zastav se, když je zadána `0` (`0`
nepřičítej). Pak vypiš součet.

Pro vstup `4`, `5`, `0` je výstup:

```
9
```

## Hotovo, když

- `4`, `5`, `0` vypíše `9`; samotná `0` vypíše `0`.
- Samotná `0` se nepřičítá; čísla mohou být záporná.
""",

"3.8 hints": r"""Přečti jedno číslo před cyklem a další čti na konci každého průchodu.

---

`total = 0`, přečti n, pak `while n != 0:` přičti k total a přečti další n.
Po cyklu vypiš total.

---

total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
""",

"3.8 reference": r"""Cyklus se **zarážkou** (sentinel) opakovaně čte hodnoty a zastaví se, když uvidí
speciální „stop“ hodnotu, ne po pevném počtu. Vzorem je `while`, jehož podmínka
porovnává nejnovější vstup se zarážkou.

- Přečti jednou před cyklem (nebo čti na začátku každého průchodu), pak porovnej
  se zarážkou, abys rozhodl, zda pokračovat.
- Samotná zarážka se **nezpracovává** — kontrola proběhne před prací, takže stop
  hodnota cyklus ukončí, místo aby se započítala.

```python
line = input()
while line != "quit":     # "quit" is the sentinel
    print("you said:", line)
    line = input()        # read the next, then re-check
```
""",

"3.9 brief": r"""# 3.9 -- for a range

## Koncept

**Cyklus `for`** spustí svůj blok jednou pro každou položku v posloupnosti. Ve
spojení s **`range`** je to obvyklý způsob, jak něco zopakovat určitý počet krát.

`range(n)` vytvoří čísla `0, 1, 2, ..., n-1` (zastaví se *před* `n`):

```python
for i in range(4):
    print(i)
# prints 0, 1, 2, 3
```

Při každém průchodu vezme řídicí proměnná (zde `i`) další hodnotu. Počítadlo si
nespravuješ sám -- `range` to dělá za tebe, takže nehrozí nekonečný cyklus.

`range` může mít také start a krok: `range(1, 5)` je `1,2,3,4`; `range(0, 10, 2)`
je `0,2,4,6,8`.

## Příklad

```python
for i in range(3):
    print(i)
# prints 0, 1, 2
```

## Tvůj úkol

Přečti celé číslo `n` a pak vypiš každé číslo od `0` do `n-1`, každé na vlastním
řádku, pomocí cyklu `for` s `range`.

Pro vstup `4` je výstup:

```
0
1
2
3
```

## Hotovo, když

- `4` vypíše `0,1,2,3` (každé na řádku). `1` vypíše jen `0`.
- `0` nevypíše nic.
""",

"3.9 hints": r"""range(n) dá 0, 1, ..., n-1. Procházej ho pomocí for.

---

`for i in range(n):` a pak odsazený `print(i)`.

---

n = int(input())
for i in range(n):
    print(i)
""",

"3.9 reference": r"""**`range(n)`** vytvoří celá čísla `0, 1, …, n - 1` — `n` čísel začínajících od
nuly — a cyklus **`for`** spustí svůj blok jednou pro každé, přičemž řídicí
proměnnou naváže na aktuální hodnotu.

- `range(n)` se zastaví **před** `n` (polootevřený), takže `range(5)` je
  `0,1,2,3,4` — pět průchodů.
- `range(start, stop)` začne na `start`; `range(start, stop, step)` počítá po
  `step` (který může být záporný pro odpočet).
- `range` je líný — vydává čísla na vyžádání, aniž by stavěl seznam — takže
  obrovský rozsah nic nestojí, dokud se neprochází.

```python
for i in range(3):
    print(i)              # 0, 1, 2

for i in range(2, 6):
    print(i)              # 2, 3, 4, 5
```
""",

"3.10 brief": r"""# 3.10 -- Procházení řetězce

## Koncept

Cyklus `for` nefunguje jen na rozsazích. **Řetězec je posloupnost znaků**, takže ho
můžeš procházet přímo -- jeden znak na průchod:

```python
for ch in "cat":
    print(ch)
# prints:
# c
# a
# t
```

Žádné indexování není potřeba: `ch` je postupně každý znak. (Takto můžeš procházet
mnoho druhů posloupností; řetězce jsou první.)

## Příklad

```python
word = "hi"
for ch in word:
    print(ch)
# prints h then i
```

## Tvůj úkol

Přečti slovo a vypiš každý jeho znak na vlastním řádku pomocí cyklu `for` přes
řetězec.

Pro vstup `cat` je výstup:

```
c
a
t
```

## Hotovo, když

- `cat` vypíše `c`, `a`, `t` na samostatných řádcích.
- Jediné písmeno vypíše to písmeno; prázdný vstup nevypíše nic.
""",

"3.10 hints": r"""Řetězec můžeš procházet přímo -- každý průchod dá jeden znak.

---

`for ch in word:` a pak odsazený `print(ch)`.

---

word = input()
for ch in word:
    print(ch)
""",

"3.10 reference": r"""Řetězec je **iterovatelný**, takže cyklus `for` ho prochází **po jednom znaku**,
v pořadí, přičemž řídicí proměnnou naváže na každý znak. Neindexuješ ručně.

- Každý průchod dá jednoznakový řetězec; cyklus proběhne `len(s)`krát.
- Tohle je přímý způsob, jak zkoumat nebo počítat znaky — spoj to s `if` uvnitř
  cyklu, abys reagoval na určité z nich.
- Stejný tvar `for ... in` prochází libovolnou posloupnost (seznamy, rozsahy, …),
  ne jen řetězce.

```python
for ch in "cat":
    print(ch)             # c, then a, then t
```
""",

"3.11 brief": r"""# 3.11 -- break a continue

## Koncept

Dvě klíčová slova mění tok cyklu:

- **`break`** zastaví cyklus **okamžitě** -- žádné další průchody.
- **`continue`** přeskočí **zbytek aktuálního průchodu** a skočí na další.

```python
for ch in "a,b,c":
    if ch == ",":
        continue        # skip commas
    print(ch)
# prints a, b, c (commas skipped)

for n in range(100):
    if n == 3:
        break           # stop the whole loop at 3
    print(n)
# prints 0, 1, 2
```

`continue` přeskočí jednu položku; `break` cyklus ukončí.

## Příklad

```python
for ch in "abxcd":
    if ch == "x":
        break
    print(ch)
# prints a, b   (stops at x)
```

## Tvůj úkol

Přečti slovo a procházej jeho znaky:

- písmeno `o` **přeskoč** (použij `continue` -- nevypisuj ho),
- u písmena `x` se úplně **zastav** (použij `break` -- od `x` dál nic nevypisuj),
- každý jiný znak vypiš na vlastním řádku.

Pro vstup `boxes` je výstup:

```
b
```

(`b`, pak se `o` přeskočí, pak `x` cyklus zastaví.)

## Hotovo, když

- `boxes` vypíše `b`; `good` vypíše `g` a pak `d` (`o` přeskočeny); `abc` vypíše
  `a`, `b`, `c`.
""",

"3.11 hints": r"""Uvnitř cyklu nejprve zkontroluj "x" (break), pak "o" (continue), pak vypiš.

---

`for ch in word:` -> `if ch == "x": break`, pak `if ch == "o": continue`,
pak `print(ch)`.

---

word = input()
for ch in word:
    if ch == "x":
        break
    if ch == "o":
        continue
    print(ch)
""",

"3.11 reference": r"""Dva příkazy mění tok cyklu zevnitř:

- **`break`** cyklus **okamžitě** ukončí, přeskočí všechny zbývající průchody a
  skočí na kód za cyklem. Použij ho, abys zastavil, jakmile najdeš, co potřebuješ.
- **`continue`** přeskočí **zbytek aktuálního průchodu** a skočí rovnou na další
  iteraci cyklu (znovu zkontroluje podmínku / vezme další položku).

Oba ovlivňují pouze **nejvnitřnější** cyklus, který je obklopuje.

```python
for n in range(10):
    if n == 5:
        break             # stop the whole loop at 5
    if n % 2 == 0:
        continue          # skip evens, go to the next n
    print(n)              # 1, 3
```
""",

"3.12 brief": r"""# 3.12 -- Vzor akumulátoru

## Koncept

Velmi častý vzor cyklu: drž v proměnné **průběžný součet**, začni na `0` a v každém
průchodu k němu přičítej. Proměnná výsledek „akumuluje“.

```python
total = 0
for n in [4, 2, 9]:
    total = total + n
print(total)        # 15
```

Klíčové kroky jsou: **začni na 0 před cyklem**, **přičítej uvnitř cyklu**, **použij
výsledek po cyklu**. Stejný tvar funguje pro počítání (začni na 0, pokaždé přičti
1) nebo stavění řetězce (začni na "", pokaždé přidej kousek).

Tato úloha kombinuje, co ses naučil: cyklus `for`, `range`, čtení vstupu a
akumulátor.

## Příklad

```python
total = 0
for _ in range(3):
    total = total + int(input())
print(total)
```

(`_` je normální jméno proměnné, často používané, když nepotřebuješ hodnotu
cyklu.)

## Tvůj úkol

Přečti celé číslo `n` (počet). Pak přečti dalších `n` celých čísel, jedno na řádek,
a vypiš jejich **součet**.

Pro vstup `3`, pak `10`, `20`, `5` je výstup:

```
35
```

## Hotovo, když

- Počet `3` s `10, 20, 5` vypíše `35`.
- Počet `0` nečte žádná další čísla a vypíše `0`.
- Čísla mohou být záporná.
""",

"3.12 hints": r"""Nejprve přečti počet. Začni total na 0, pak se tolikrát zatoč a každé číslo
přičti.

---

`n = int(input())`, `total = 0`, pak `for _ in range(n):` přičti `int(input())`
k total. Po cyklu vypiš total.

---

n = int(input())
total = 0
for _ in range(n):
    total = total + int(input())
print(total)
""",

"3.12 reference": r"""Vzor **akumulátoru** buduje výsledek napříč cyklem. Proměnnou inicializuješ
**před** cyklem, pak ji aktualizuješ při **každém** průchodu; po cyklu drží
zkombinovaný výsledek.

- U součtu začni total na `0` a přičítej každou hodnotu (`total = total + x`, nebo
  `total += x`). Začátek na `0` je neutrální prvek pro `+`, takže prázdný cyklus ho
  nechá `0`.
- Stejný tvar počítá (začni na 0, `+= 1` za shodu), staví řetězec (začni `""`,
  `+=`) nebo sbírá seznam (začni `[]`, `.append`).
- Akumulátor musí žít **mimo** cyklus — deklarovat ho uvnitř by ho resetovalo při
  každém průchodu.

```python
total = 0
for n in [3, 1, 4]:
    total += n            # 3, then 4, then 8
print(total)             # 8
```
""",
}
