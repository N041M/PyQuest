# PyQuest translations -- language 'cs' -- chapter 05_power_tools -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"5.1 brief": r"""# 5.1 -- in: testování příslušnosti

## Koncept

S `in` ses setkal u množin (4.11). Ve skutečnosti funguje skoro na všem:

```python
"e" in "hello"        # True   (substring of a string)
3 in [1, 2, 3]        # True   (item of a list)
"sam" in {"sam": 20}  # True   (KEY of a dict)
```

`x in s` je výraz, který dá **boolean** (`True`/`False`), takže ho zasadíš rovnou
do `if`:

```python
if "@" in address:
    print("looks like an email")
```

Existuje i opak, `not in`:

```python
if "x" not in word:
    print("no x here")
```

Srovnej to s kapitolou 2, kde jsi použil `s.find()` a kontroloval `-1`. `in` říká
totéž prostou řečí -- dej mu přednost, kdykoli potřebuješ jen *zda* tam něco je, ne
*kde*.

## Příklad

```python
word = "banana"
print("n" in word)     # True
print("z" in word)     # False
```

## Tvůj úkol

Přečti slovo, pak jediné písmeno. Vypiš `yes`, pokud se písmeno ve slově vyskytuje,
a `no`, pokud ne.

Pro vstup `banana`, pak `n`:

```
yes
```

## Hotovo, když

- Písmeno, které se vyskytuje, vypíše `yes`; to, které ne, vypíše `no`.
- Funguje i pro jednopísmenné slovo.
- Použil jsi operátor `in` (ne `.find()` ani `.count()`).
""",

"5.1 hints": r"""`letter in word` je už True nebo False -- dej ho rovnou do `if`.

---

Přečti slovo, přečti písmeno, pak se rozvětvi: `if letter in word:` vypiš yes,
`else:` vypiš no.

---

word = input()
letter = input()
if letter in word:
    print("yes")
else:
    print("no")
""",

"5.1 reference": r"""Operátor **`in`** testuje příslušnost a dává boolean, takže ho zasadíš rovnou do
`if` nebo `while`. `x in c` je `True`, když je `x` nalezeno v `c`.

- U **řetězce** `in` testuje **podřetězec**: `"cat" in "concatenate"` je `True`.
- U **seznamu** nebo **n-tice** testuje položku (prochází posloupnost).
- U **slovníku** nebo **množiny** testuje **klíč**/člena — a je rychlé (založené na
  hashování), na rozdíl od lineárního procházení seznamu.
- `x not in c` je čitelná negace.

```python
"a" in "cat"          # True
3 in [1, 2, 3]        # True
"key" in {"key": 1}   # True  -- tests keys
```
""",

"5.2 brief": r"""# 5.2 -- sum()

## Koncept

V 3.12 jsi napsal **vzor akumulátoru** ručně:

```python
total = 0
for x in nums:
    total = total + x
```

Tento vzor je tak častý, že ho Python dodává jako vestavěnou funkci:

```python
total = sum(nums)
```

`sum(seznam_čísel)` sečte každou položku a vrátí součet. U prázdného seznamu vrátí
`0` -- přesně to, čím tvůj ručně psaný akumulátor začínal.

Tato kapitola je plná takových **mocných nástrojů**: vestavěných funkcí, které
nahrazují cyklus, jejž sis už jednou sám napsal. Zkratku si zasloužíš tím, že víš,
co nahrazuje.

## Příklad

```python
nums = [3, 1, 4]
print(sum(nums))    # 8
print(sum([]))      # 0
```

## Tvůj úkol

Přečti počet `n`, pak `n` celých čísel (jedno na řádek). Vypiš jejich součet pomocí
`sum()`.

Pro vstup `3`, pak `3`, `1`, `4`:

```
8
```

## Hotovo, když

- `3, 1, 4` vypíše `8`; záporná čísla také fungují.
- Počet `0` vypíše `0`.
- Použil jsi `sum()` -- tentokrát ne ručně psaný cyklus.
""",

"5.2 hints": r"""Nejprve sestav seznam čísel (jako v 4.13), pak celý seznam předej jedinému volání
funkce.

---

`sum(nums)` vrátí součet -- ten vypiš. Žádné `total = 0` není potřeba.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(sum(nums))
""",

"5.2 reference": r"""**`sum(numbers)`** sečte iterovatelný objekt čísel a vrátí součet — akumulátorový
cyklus z 3.12 jako jedno vestavěné volání.

- Funguje na libovolném iterovatelném objektu čísel (seznam, n-tice, range,
  generátor). `sum([])` je `0`.
- Volitelný druhý argument je **počáteční** hodnota: `sum(nums, 100)` začne součet
  na 100.
- Sčítá jen čísla; abys sečetl něco odvozeného z každé položky, předej mu
  komprehenzi nebo generátor, např. `sum(len(w) for w in words)`.

```python
sum([3, 1, 4])              # 8
sum(range(1, 101))          # 5050
sum(len(w) for w in words)  # total characters
```
""",

"5.3 brief": r"""# 5.3 -- min() a max()

## Koncept

Najít nejmenší nebo největší položku je další cyklus, který bys mohl napsat ručně
(„drž si dosud nejlepší, porovnávej každou položku“) -- a další cyklus, který Python
dodává jako vestavěný:

```python
nums = [3, 7, 1]
print(min(nums))    # 1
print(max(nums))    # 7
```

`min()` a `max()` vezmou seznam (vlastně jakoukoli neprázdnou kolekci) a vrátí jeho
nejmenší / největší položku. Fungují i na řetězcích -- „nejmenší“ pak znamená
nejdřívější v abecedním pořadí:

```python
min("cab")     # "a"
```

Jedno upozornění: u **prázdného** seznamu spadnou (z ničeho není nejmenší), takže
tato úloha zaručuje alespoň jedno číslo.

## Příklad

```python
nums = [4, -2, 9]
print(min(nums))    # -2
print(max(nums))    # 9
```

## Tvůj úkol

Přečti počet `n` (vždy alespoň 1), pak `n` celých čísel. Vypiš dva řádky: nejmenší,
pak největší.

Pro vstup `3`, pak `4`, `-2`, `9`:

```
-2
9
```

## Hotovo, když

- `4, -2, 9` vypíše `-2` pak `9`.
- Jediné číslo vypíše samo sebe dvakrát (je zároveň min i max).
- Použil jsi `min()` a `max()`.
""",

"5.3 hints": r"""Nejprve sestav seznam; nejmenší a největší jsou pak po jednom volání funkce.

---

`print(min(nums))` pak `print(max(nums))` -- dva řádky, dvě volání.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(min(nums))
print(max(nums))
""",

"5.3 reference": r"""**`min(items)`** a **`max(items)`** vrátí nejmenší a největší položku neprázdné
kolekce.

- Porovnávají pomocí `<`/`>`, takže fungují na číslech i na řetězcích (které se
  porovnávají lexikograficky).
- Zavolané na **prázdném** iterovatelném objektu vyvolají `ValueError`; předej
  `default=`, abys dodal náhradní hodnotu.
- Funkce `key=` řadí podle odvozené hodnoty místo podle samotné položky:
  `max(words, key=len)` vrátí **nejdelší** slovo.

```python
min([3, 1, 4])             # 1
max("apple", "pear")       # 'pear'
max(words, key=len)        # the longest word
```
""",

"5.4 brief": r"""# 5.4 -- sorted()

## Koncept

`sorted(nums)` vrátí **nový seznam** se stejnými položkami v pořadí, nejmenší
první:

```python
nums = [3, 1, 2]
print(sorted(nums))    # [1, 2, 3]
print(nums)            # [3, 1, 2]  -- the original is untouched
```

Dvě věci, které je dobré vědět:

- Vrací *kopii*; původní seznam si ponechá své pořadí. (Existuje i `nums.sort()`,
  metoda, která seznam přeuspořádá **na místě** -- hodí se později, ale `sorted()`
  je bezpečnější výchozí volba, protože se nic nemění za tvými zády.)
- Největší první je na jedno klíčové slovo: `sorted(nums, reverse=True)`.

Duplicity se zachovají -- řazení přeuspořádá, nikdy neodebírá.

## Příklad

```python
for x in sorted([3, 1, 2]):
    print(x)
# 1
# 2
# 3
```

## Tvůj úkol

Přečti počet `n`, pak `n` celých čísel. Vypiš je od nejmenšího po největší, jedno
na řádek.

Pro vstup `4`, pak `3`, `1`, `3`, `2`:

```
1
2
3
3
```

## Hotovo, když

- `3, 1, 3, 2` vypíše `1, 2, 3, 3` -- duplicitní `3` se objeví dvakrát.
- Počet `0` nevypíše nic.
- Použil jsi `sorted()`.
""",

"5.4 hints": r"""Sestav seznam, pak procházej `sorted(nums)` místo `nums`.

---

`for x in sorted(nums):` navštíví položky od nejmenší; každou vypiš.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for x in sorted(nums):
    print(x)
""",

"5.4 reference": r"""**`sorted(items)`** vrátí **nový** seznam s položkami ve vzestupném pořadí a
originál nechá nedotčen.

- Přijímá libovolný iterovatelný objekt a vždy vrací seznam. Čísla se řadí číselně,
  řetězce lexikograficky.
- **`reverse=True`** řadí sestupně. **`key=`** řadí podle odvozené hodnoty:
  `sorted(words, key=len)` řadí podle délky, `sorted(d.items(), key=lambda kv:
  kv[1])` řadí páry slovníku podle hodnoty.
- Metoda seznamu `lst.sort()` řadí **na místě** a vrací `None`; použij `sorted`,
  když chceš nový seznam nebo řadíš něco, co není seznam.

```python
sorted([3, 1, 2])               # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
sorted(words, key=len)          # shortest to longest
```
""",

"5.5 brief": r"""# 5.5 -- enumerate()

## Koncept

Někdy cyklus potřebuje **položku** i její **pozici**. Mohl bys sledovat počítadlo
ručně, ale Python má přesně na tohle vestavěnou funkci:

```python
words = ["tea", "milk"]
for i, w in enumerate(words):
    print(i, w)
# 0 tea
# 1 milk
```

Při každém průchodu ti `enumerate` podá dvojici `(pozice, položka)`, kterou
rozbalíš do dvou proměnných (4.7) -- stejný trik jako `for k, v in d.items()`.

Počítat od `0` je zřídka to, co chceš člověku *ukázat*. Druhý argument nastaví
počáteční číslo:

```python
for i, w in enumerate(words, 1):
    print(i, w)
# 1 tea
# 2 milk
```

## Příklad

```python
for i, ch in enumerate("hi", 1):
    print(f"{i}. {ch}")
# 1. h
# 2. i
```

## Tvůj úkol

Přečti počet `n`, pak `n` slov. Vypiš je jako číslovaný seznam začínající od 1, ve
formátu `1. word` (tečka a mezera za číslem).

Pro vstup `3`, pak `tea`, `milk`, `sugar`:

```
1. tea
2. milk
3. sugar
```

## Hotovo, když

- Tři slova se vypíšou jako `1. ...`, `2. ...`, `3. ...`.
- Počet `0` nevypíše nic.
- Použil jsi `enumerate()` -- žádné ručně držené počítadlo.
""",

"5.5 hints": r"""`for i, w in enumerate(words, 1):` ti dá číslo a slovo dohromady, počínaje 1.

---

Uvnitř cyklu sestav řádek f-řetězcem: `f"{i}. {w}"`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i, w in enumerate(words, 1):
    print(f"{i}. {w}")
""",

"5.5 reference": r"""**`enumerate(items)`** spáruje každou položku s její pozicí, takže cyklus `for`
dostane obojí najednou — žádné ručně držené počítadlo.

- `for i, item in enumerate(lst):` naváže `i` na index (od 0) a `item` na hodnotu
  při každém průchodu.
- Druhý argument nastaví **počáteční číslo**: `enumerate(lst, 1)` čísluje od 1, což
  se hodí pro seznamy určené lidem.
- Je líný (vydává dvojice na vyžádání) a funguje na libovolném iterovatelném
  objektu.

```python
for i, name in enumerate(["a", "b"], 1):
    print(i, name)        # 1 a / 2 b
```
""",

"5.6 brief": r"""# 5.6 -- zip(): párování seznamů

## Koncept

Dva seznamy často patří k sobě položku po položce: jména a skóre, otázky a
odpovědi. `zip()` je prochází **v zákrytu** a podává ti jednu dvojici na průchod:

```python
names = ["amy", "ben"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
# amy 90
# ben 85
```

Stejně jako `enumerate` dá každý průchod dvojici, kterou rozbalíš do dvou
proměnných. Název odkazuje na zip: dvě řady zoubků spojené jeden k jednomu.

Pokud mají seznamy různou délku, `zip` se zastaví u toho **kratšího** -- položky
navíc v delším seznamu se prostě nikdy nenavštíví.

## Příklad

```python
for a, b in zip("ab", [1, 2]):
    print(a, b)
# a 1
# b 2
```

## Tvůj úkol

Přečti počet `n`, pak `n` jmen, pak `n` skóre (celá čísla). Vypiš jeden řádek na
dvojici: jméno, mezera, skóre.

Pro vstup `2`, pak `amy`, `ben`, pak `90`, `85`:

```
amy 90
ben 85
```

## Hotovo, když

- Dvě jména a dvě skóre se vypíšou jako dva řádky `jméno skóre`, v pořadí.
- Počet `0` nevypíše nic.
- Použil jsi `zip()` ke spárování obou seznamů.
""",

"5.6 hints": r"""Nejprve přečti VŠECHNA jména do jednoho seznamu, pak všechna skóre do dalšího --
teprve potom je spáruj.

---

`for name, score in zip(names, scores):` dá jednu dvojici na průchod; vypiš obě s
mezerou mezi (to udělá prosté `print(name, score)`).

---

n = int(input())
names = []
for _ in range(n):
    names.append(input())
scores = []
for _ in range(n):
    scores.append(input())
for name, score in zip(names, scores):
    print(name, score)
""",

"5.6 reference": r"""**`zip(a, b)`** prochází několik iterovatelných objektů **v zákrytu** a vydává
jednu n-tici odpovídajících položek na průchod — *i*-tou z každého. Spáruje
paralelní posloupnosti bez indexování.

- `for x, y in zip(xs, ys):` naváže `x` a `y` na odpovídající položky při každém
  průchodu.
- Zastaví se u **nejkratšího** vstupu, takže položky navíc v delším se ignorují.
- Lze zipovat libovolný počet iterovatelných objektů; `dict(zip(keys, values))`
  sestaví slovník ze dvou paralelních seznamů.

```python
names, scores = ["Ada", "Linus"], [90, 85]
for n, s in zip(names, scores):
    print(n, s)           # Ada 90 / Linus 85
```
""",

"5.7 brief": r"""# 5.7 -- Seznamové komprehenze

## Koncept

Velmi častý tvar cyklu je *„sestav nový seznam tím, že s každou položkou něco
uděláš“*:

```python
doubled = []
for x in nums:
    doubled.append(x * 2)
```

Python má přesně pro to jednořádkový tvar, zvaný **seznamová komprehenze**:

```python
doubled = [x * 2 for x in nums]
```

Čti to zevnitř ven: *„pro každé `x` v `nums` dej `x * 2` do nového seznamu“*.
Hranaté závorky říkají „stavím seznam“; výraz před `for` je to, čím se každá
položka stane.

Funguje s čímkoli, co můžeš procházet -- včetně `range`. Čtení `n` čísel (které jsi
teď udělal už tucetkrát) se smrskne na:

```python
nums = [int(input()) for _ in range(n)]
```

## Příklad

```python
nums = [1, 2, 3]
squares = [x * x for x in nums]
print(squares)    # [1, 4, 9]
```

## Tvůj úkol

Přečti počet `n`, pak `n` celých čísel. Sestav nový seznam, kde je každé číslo
**zdvojnásobené**, pak vypiš jeho položky, jednu na řádek.

Pro vstup `3`, pak `4`, `-1`, `0`:

```
8
-2
0
```

## Hotovo, když

- `4, -1, 0` vypíše `8, -2, 0` -- každé zdvojnásobeno, pořadí zachováno.
- Počet `0` nevypíše nic.
- K sestavení seznamu jsi použil seznamovou komprehenzi.
""",

"5.7 hints": r"""Vzor je  new_list = [<čím se každá položka stane> for x in old_list].

---

`doubled = [x * 2 for x in nums]` -- pak prostý cyklus for vypíše každou položku.
(Čtení čísel může být také komprehenze: `[int(input()) for _ in range(n)]`.)

---

n = int(input())
nums = [int(input()) for _ in range(n)]
doubled = [x * 2 for x in nums]
for d in doubled:
    print(d)
""",

"5.7 reference": r"""**Seznamová komprehenze** sestaví nový seznam jediným výrazem: pro každé `x` v
`items` vyhodnotí `expr` a posbírá výsledky, v pořadí. Je to vzor „stav cyklem a
append“ stlačený do jednoho řádku.

- `[expr for x in items]` je ekvivalentní tomu, že začneš `result = []` a v cyklu
  `result.append(expr)` — stejný výsledek, přímější.
- `expr` může být libovolný výraz v `x`: `[n * n for n in nums]`,
  `[w.upper() for w in words]`.
- Komprehenze staví i množiny (`{...}`) a slovníky (`{k: v for ...}`).

```python
[n * n for n in range(5)]       # [0, 1, 4, 9, 16]
[w.upper() for w in ["a", "b"]] # ['A', 'B']
```
""",

"5.8 brief": r"""# 5.8 -- Filtrování komprehenzemi

## Koncept

Komprehenze může také **vybírat**, které položky ponechat. Přidej `if` na konec:

```python
evens = [x for x in nums if x % 2 == 0]
```

Čti to: *„každé `x` z `nums` -- ale jen pokud `x % 2 == 0`“*. Položky, které testem
neprojdou, se prostě vynechají.

Obě části jsou nezávislé a volně se kombinují:

```python
[x * 2 for x in nums]                 # transform every item   (5.7)
[x for x in nums if x > 0]            # keep some, unchanged   (this puzzle)
[x * 2 for x in nums if x > 0]        # keep some AND transform
```

Připomenutí z 1.9: `x % 2` je zbytek po dělení 2, takže je `0` právě pro sudá čísla
-- a to zahrnuje i `0` samotnou a záporná jako `-4`.

## Příklad

```python
nums = [1, 2, 3, 4]
print([x for x in nums if x % 2 == 0])    # [2, 4]
```

## Tvůj úkol

Přečti počet `n`, pak `n` celých čísel. Ponech jen ta **sudá** (v původním pořadí)
a vypiš je, jedno na řádek.

Pro vstup `5`, pak `1`, `2`, `3`, `4`, `-6`:

```
2
4
-6
```

## Hotovo, když

- `1, 2, 3, 4, -6` vypíše `2, 4, -6` -- záporná čísla a nula se počítají jako sudá.
- Pokud žádné číslo není sudé, nic se nevypíše.
- Použil jsi komprehenzi s klauzulí `if`.
""",

"5.8 hints": r"""„Sudé“ znamená, že zbytek po dělení 2 je nula: `x % 2 == 0`.

---

Dej ten test na konec komprehenze:
`evens = [x for x in nums if x % 2 == 0]` -- pak vypiš každou položku.

---

n = int(input())
nums = [int(input()) for _ in range(n)]
evens = [x for x in nums if x % 2 == 0]
for e in evens:
    print(e)
""",

"5.8 reference": r"""Přidání **`if`** do komprehenze ponechá jen položky, které projdou testem.
`[x for x in items if test]` posbírá každé `x`, pro které je `test` pravdivý, a
zbytek **přeskočí**.

- Klauzule `if` filtruje; úvodní výraz stále transformuje, takže se obojí
  kombinuje: `[n * n for n in nums if n % 2 == 0]` umocní jen sudá.
- Nahrazuje vzor cyklus-s-`if`-a-`append`.
- Neplést si s **podmíněným výrazem** v pozici hodnoty
  (`[a if cond else b for x in items]`), který vybírá u každé položky, místo aby
  filtroval.

```python
[n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
[w for w in words if len(w) > 3]       # only long words
```
""",

"5.9 brief": r"""# 5.9 -- Počítání pomocí slovníku

## Koncept

*„Kolikrát se každá věc objeví?“* je jedna z nejužitečnějších otázek v
programování. Odpovědí je **sčítací vzor** (tally): slovník, kde každý klíč je věc,
kterou jsi viděl, a jeho hodnota je, kolikrát jsi ji viděl.

Celý trik je jeden řádek, postavený na `.get()` z 4.10:

```python
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

Čti ten řádek pomalu: *„počet pro `w` se stane tím, čím byl -- nebo 0, je-li `w`
nové -- plus jedna.“* `.get(w, 0)` je to, co rozběhne první spatření: ještě tam
není žádný záznam, takže se počítá od 0.

Po cyklu `counts.get(thing, 0)` odpoví na „kolik?“ pro cokoli -- včetně věcí nikdy
neviděných, které jsou `0`, ne pád.

## Příklad

```python
words = ["tea", "milk", "tea"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts.get("tea", 0))     # 2
print(counts.get("cocoa", 0))   # 0
```

## Tvůj úkol

Přečti jeden řádek slov (odděl je pomocí `.split()`, jako v 4.4), pak přečti
**dotazové slovo** na druhém řádku. Vypiš, kolikrát se dotaz na řádku vyskytuje.

Pro vstup `tea milk tea`, pak `tea`:

```
2
```

## Hotovo, když

- `tea milk tea` s dotazem `tea` vypíše `2`; dotaz `milk` vypíše `1`.
- Dotaz, který se nikdy neobjeví, vypíše `0` (žádný pád).
- Sestavil jsi sčítací slovník (ne jednorázové projití).
""",

"5.9 hints": r"""Rozděl řádek na seznam slov, pak ho projdi a stav sčítací slovník.

---

Sčítací řádek je  counts[w] = counts.get(w, 0) + 1  -- a konečná odpověď je další
.get s výchozí hodnotou: counts.get(query, 0).

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
query = input()
print(counts.get(query, 0))
""",

"5.9 reference": r"""**Sčítací** vzor počítá, kolikrát se každá odlišná věc objeví, pomocí slovníku,
jehož klíče jsou ty věci a jehož hodnoty jsou průběžné počty.

- Pro každou položku `counts[k] = counts.get(k, 0) + 1` přečte aktuální počet (`0`,
  když je klíč viděn poprvé, díky výchozí hodnotě `.get`) a zapíše o jeden víc.
- Začni z prázdného slovníku `{}`; klíče se objevují, jak jsou poprvé potkány.
- `collections.Counter` ze standardní knihovny to udělá v jednom kroku, ale idiom
  `.get(k, 0) + 1` ukazuje přesně, co se děje.

```python
counts = {}
for w in ["a", "b", "a"]:
    counts[w] = counts.get(w, 0) + 1   # {'a': 2, 'b': 1}
```
""",

"5.10 brief": r"""# 5.10 -- Závěrečná: zpráva o slovech

## Koncept

Tentokrát nic nového -- tato úloha spojuje celou kapitolu (a kapitolu 4) do jednoho
malého, skutečného programu: **zprávy o četnosti slov**, srdce každé funkce
„nejčastější slova“, jakou jsi kdy viděl.

Díly, které všechny máš:

- `.split()` -- řádek na slova (4.4)
- sčítací vzor -- spočítej každé slovo (5.9)
- `sorted()` -- seřaď zprávu (5.4). Jedno nové pohodlí: procházení slovníku
  navštěvuje jeho **klíče**, takže `sorted(counts)` jsou prostě klíče v abecedním
  pořadí.
- vypsání slova a jeho počtu na jeden řádek (1.2)

## Příklad

Pro řádek `b a b`:

```python
counts = {"b": 2, "a": 1}
for w in sorted(counts):
    print(w, counts[w])
# a 1
# b 2
```

## Tvůj úkol

Přečti jeden řádek slov. Vypiš jeden řádek na každé **odlišné** slovo -- slovo,
mezeru a kolikrát se objevilo -- v **abecedním** pořadí.

Pro vstup `tea milk tea`:

```
milk 1
tea 2
```

## Hotovo, když

- `tea milk tea` vypíše `milk 1` pak `tea 2` -- odlišná slova, abecedně.
- Jediné opakované slovo vypíše jeden řádek s jeho úplným počtem.
- Prázdný řádek nevypíše nic.
- Použil jsi sčítací slovník a `sorted()`.
""",

"5.10 hints": r"""Tři kroky: rozděl řádek, sečti slova (5.9), pak vypiš -- a `sorted(counts)` dá
klíče slovníku v abecedním pořadí.

---

Po sčítacím cyklu:  `for w in sorted(counts): print(w, counts[w])`.

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
for w in sorted(counts):
    print(w, counts[w])
""",

"5.10 reference": r"""**Zpráva o četnosti slov** skládá nástroje kapitoly do malého potrubí:

1. **`split()`** text na seznam slov;
2. **sečti** je do slovníku `slovo -> počet` pomocí `counts.get(w, 0) + 1`;
3. **`sorted`** na `dict.items()`, abys zprávu seřadil — podle slova, nebo podle
   počtu pomocí `key=lambda kv: kv[1]` (a `reverse=True` pro nejčastější první).

Každý krok je nástroj, který jsi potkal; dovednost je vidět, že skutečná úloha je
jejich složením.

```python
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
for word, n in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
    print(word, n)        # most frequent first
```
""",
}
