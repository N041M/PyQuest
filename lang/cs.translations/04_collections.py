# PyQuest translations -- language 'cs' -- chapter 04_collections -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"4.1 brief": r"""# 4.1 -- Seznamy a append

## Koncept

**Seznam** drží několik hodnot v pořadí v jedné proměnné. Seznam zapíšeš hranatými
závorkami, položky oddělené čárkami:

```python
nums = [10, 20, 30]
print(nums)        # [10, 20, 30]
print(nums[0])     # 10   (index like a string -- from 0)
print(len(nums))   # 3
```

Seznam může začít prázdný a růst. `.append(x)` přidá `x` na **konec**:

```python
nums = []
nums.append(10)
nums.append(20)
print(nums)        # [10, 20]
```

Tento vzor „začni prázdný, přidávej v cyklu“ je způsob, jak sestavit seznam ze
vstupu.

## Příklad

```python
items = []
items.append(1)
items.append(2)
print(items)       # [1, 2]
```

## Tvůj úkol

Přečti celé číslo `n`, pak přečti dalších `n` celých čísel (jedno na řádek).
Posbírej je do seznamu pomocí `.append()` a vypiš hotový seznam.

Pro vstup `3`, pak `1`, `2`, `3`:

```
[1, 2, 3]
```

## Hotovo, když

- `3` s `1, 2, 3` vypíše `[1, 2, 3]`.
- Počet `0` vypíše `[]` (prázdný seznam).
""",

"4.1 hints": r"""Začni s prázdným seznamem [], pak v cyklu každé číslo přidej.

---

`nums = []`, přečti n, pak `for _ in range(n): nums.append(int(input()))`.
Nakonec `print(nums)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(nums)
""",

"4.1 reference": r"""**Seznam** je uspořádaná, měnitelná posloupnost hodnot, psaná v hranatých
závorkách: `[10, 20, 30]`. Prázdný seznam je `[]`. K položkám se dostaneš indexem
stejně jako ke znakům řetězce (`lst[0]`, `lst[-1]`).

- **`.append(x)`** přidá `x` na **konec** a zvětší seznam o jednu položku. Mění
  seznam na místě a vrací `None` (takže nikdy nepiš `lst = lst.append(x)`).
- Vzor stavění z prázdna: začni `[]`, pak `.append` jednou za každý průchod cyklu,
  abys posbíral výsledky.
- Na rozdíl od řetězců může seznam držet hodnoty různých typů.

```python
nums = []
for i in range(3):
    nums.append(i * i)   # -> [0, 1, 4]
```
""",

"4.2 brief": r"""# 4.2 -- Změna seznamu

## Koncept

Na rozdíl od řetězců lze seznamy **měnit na místě** (jsou *měnitelné*). Několik
způsobů:

- Nahradit položku podle indexu: `nums[0] = 99`
- Odebrat a vrátit **poslední** položku: `nums.pop()`
- Odebrat první odpovídající **hodnotu**: `nums.remove(20)`

```python
nums = [10, 20, 30]
nums[0] = 99      # [99, 20, 30]   replace by position
nums.pop()        # [99, 20]       drop the last item (returns 30)
print(nums)       # [99, 20]
```

Tyto mění existující seznam -- proměnná stále ukazuje na tentýž seznam, nyní
pozměněný.

## Příklad

```python
xs = [1, 2, 3]
xs[1] = 0
xs.pop()
print(xs)         # [1, 0]
```

## Tvůj úkol

Přečti počet `n` (alespoň 1), pak `n` čísel, do seznamu. Pak:

1. **zdvojnásob první položku** (nahraď `nums[0]` hodnotou `nums[0] * 2`) a
2. **odeber poslední položku** pomocí `.pop()`.

Vypiš výsledný seznam. Pro vstup `3`, pak `5`, `2`, `9`:

```
[10, 2]
```

(`[5, 2, 9]` -> zdvojnásob první -> `[10, 2, 9]` -> pop -> `[10, 2]`.)

## Hotovo, když

- `5, 2, 9` dá `[10, 2]`.
- Jediné číslo `n=1` (např. jen `4`) dá `[]` -- zdvojnásobeno na `[8]`, pak je
  poslední (jediná) položka odebrána.
""",

"4.2 hints": r"""Sestav seznam jako dřív, pak ho změň na místě.

---

`nums[0] = nums[0] * 2` pro zdvojnásobení první položky; `nums.pop()` pro odebrání
poslední.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums[0] = nums[0] * 2
nums.pop()
print(nums)
""",

"4.2 reference": r"""Seznamy jsou **měnitelné**: jejich obsah se může měnit na místě, na rozdíl od
řetězců.

- **`lst[i] = x`** nahradí položku na indexu `i`. Index už musí existovat
  (přiřazení za konec vyvolá `IndexError`).
- **`.pop()`** odebere a **vrátí** poslední položku a zmenší seznam; `.pop(i)`
  odebere položku na indexu `i`. Pop z prázdného seznamu vyvolá chybu.
- Další změny na místě: `.insert(i, x)`, `.remove(value)`, `del lst[i]`.

Protože změna je na místě, vidí ji každé jméno odkazující na tentýž objekt seznamu.

```python
lst = [10, 20, 30]
lst[1] = 99      # [10, 99, 30]
last = lst.pop() # last == 30, lst == [10, 99]
```
""",

"4.3 brief": r"""# 4.3 -- Procházení seznamu

## Koncept

Stejně jako řetězec je seznam posloupnost -- takže cyklus `for` prochází přímo jeho
položky, jednu na průchod:

```python
nums = [10, 20, 30]
for x in nums:
    print(x)        # 10, then 20, then 30
```

`len(nums)` dá počet položek a funguje i řez -- `nums[1:]` je vše kromě první,
`nums[:2]` jsou první dvě:

```python
print(len(nums))    # 3
print(nums[:2])     # [10, 20]
```

## Příklad

```python
xs = [1, 2, 3]
for x in xs:
    print(x * 10)   # 10, 20, 30
```

## Tvůj úkol

Přečti počet `n`, pak `n` čísel, do seznamu. Nejprve vypiš, kolik čísel je, pak
vypiš každé číslo **zdvojnásobené**, jedno na řádek.

Pro vstup `3`, pak `5`, `2`, `9`:

```
3
10
4
18
```

## Hotovo, když

- `5, 2, 9` vypíše `3`, pak `10`, `4`, `18`.
- Počet `0` vypíše jen `0` (žádná čísla ke zdvojnásobení).
""",

"4.3 hints": r"""Po sestavení seznamu vypiš len(nums), pak ho projdi.

---

`print(len(nums))`, pak `for x in nums: print(x * 2)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
for x in nums:
    print(x * 2)
""",

"4.3 reference": r"""Seznam je iterovatelný, takže **`for x in lst`** navštíví každou položku v pořadí
a naváže řídicí proměnnou na samotnou položku (ne na její index).

- Tohle je obvyklý způsob, jak číst seznam. Když potřebuješ i pozici, spoj to s
  `range(len(lst))` nebo `enumerate` (kapitola 5).
- **`len(lst)`** dá počet položek; **řez** (`lst[1:3]`, `lst[::-1]`) funguje přesně
  jako u řetězců a vrací nový seznam.

```python
for name in ["Ada", "Linus"]:
    print(name)

total = 0
for n in [3, 1, 4]:
    total += n           # iterate and accumulate
```
""",

"4.4 brief": r"""# 4.4 -- split: text na seznam

## Koncept

`s.split()` rozdělí řetězec na **seznam kousků**. Bez argumentu dělí podle bílých
znaků, takže větu promění na její slova:

```python
"the quick brown fox".split()    # ['the', 'quick', 'brown', 'fox']
```

Výsledek je skutečný seznam, takže platí vše, co o seznamech víš -- `len`,
indexování, procházení:

```python
words = "a b c".split()
print(len(words))    # 3
print(words[0])      # a
```

Můžeš také dělit podle konkrétního oddělovače tím, že ho předáš:
`"a,b,c".split(",")` dá `['a', 'b', 'c']`.

## Příklad

```python
parts = "one two three".split()
print(len(parts))    # 3
```

## Tvůj úkol

Přečti řádek slov oddělených mezerami a vypiš, **kolik slov** obsahuje.

Pro vstup `the quick brown fox`:

```
4
```

## Hotovo, když

- `the quick brown fox` vypíše `4`; jedno slovo vypíše `1`.
- Prázdný řádek vypíše `0`.
""",

"4.4 hints": r""".split() promění řádek na seznam slov. Pak je spočítej.

---

`print(len(input().split()))`.

---

line = input()
print(len(line.split()))
""",

"4.4 reference": r"""**`s.split()`** rozdělí řetězec na **seznam kousků**. Bez argumentu dělí podle
úseků **bílých znaků** a zahodí mezery na začátku a konci — obvyklý způsob, jak
získat slova řádku.

- `s.split(sep)` dělí podle přesného oddělovače `sep` a ponechává prázdné kousky
  mezi sousedními oddělovači (`"a,,b".split(",")` je `["a", "", "b"]`).
- `s.split(sep, maxsplit)` dělí nejvýše `maxsplit`krát — hodí se k odloupnutí
  předpony, např. `"key=a=b".split("=", 1)` je `["key", "a=b"]`.
- Je to inverze k `join` (další).

```python
"the quick fox".split()        # ['the', 'quick', 'fox']
"2024-01-15".split("-")        # ['2024', '01', '15']
```
""",

"4.5 brief": r"""# 4.5 -- join: seznam na text

## Koncept

`.join()` je opak `split`: slepí **seznam řetězců** do jednoho řetězce a mezi každý
kousek vloží oddělovač. Voláš ho *na oddělovači*:

```python
words = ["a", "b", "c"]
print("-".join(words))    # a-b-c
print(", ".join(words))   # a, b, c
print("".join(words))     # abc   (no separator)
```

Čti to jako „spoj tato slova s tímto oddělovačem mezi nimi“. Seznam musí obsahovat
řetězce.

## Častá chyba

`join` se píše oddělovačem napřed: `"-".join(words)`, **ne** `words.join("-")`.

## Příklad

```python
parts = ["2024", "12", "25"]
print("/".join(parts))    # 2024/12/25
```

## Tvůj úkol

Přečti počet `n`, pak `n` slov (jedno na řádek), do seznamu. Vypiš je spojená
pomlčkou `-`.

Pro vstup `3`, pak `a`, `b`, `c`:

```
a-b-c
```

## Hotovo, když

- `a, b, c` vypíše `a-b-c`; jedno slovo vypíše jen to slovo.
- Počet `0` vypíše prázdný řádek (není co spojovat).
""",

"4.5 hints": r"""Posbírej slova do seznamu, pak je spoj. join se volá na oddělovači.

---

Sestav seznam, pak `print("-".join(words))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print("-".join(words))
""",

"4.5 reference": r"""**`sep.join(parts)`** slepí iterovatelný objekt **řetězců** do jednoho řetězce a
mezi sousední položky vloží `sep`. Oddělovač je řetězec, na kterém metodu voláš,
což zpočátku zní zvláštně, ale umožňuje, aby oddělovač byl libovolný řetězec.

- Každá položka už musí být řetězec; čísla vyvolají `TypeError`. Nejprve převeď,
  např. `", ".join(str(n) for n in nums)`.
- `"".join(parts)` zřetězí bez oddělovače — efektivní způsob, jak sestavit řetězec
  z mnoha kousků (mnohem lepší než opakované `+`).
- Je to inverze k `split`.

```python
"-".join(["2024", "01", "15"])   # '2024-01-15'
" ".join(["the", "fox"])          # 'the fox'
```
""",

"4.6 brief": r"""# 4.6 -- Seznamy v seznamech

## Koncept

Seznam může držet **jiné seznamy**. Takto reprezentuješ řádky dat, dvojice, mřížky
a podobně:

```python
pairs = [[1, 2], [3, 4], [5, 6]]
print(pairs)        # [[1, 2], [3, 4], [5, 6]]
print(pairs[0])     # [1, 2]        the first inner list
print(pairs[0][1])  # 2            first inner list, second item
```

Dva indexy: první vybere vnitřní seznam, druhý vybere položku uvnitř něj.
Procházení ti postupně dá každý vnitřní seznam:

```python
for p in pairs:
    print(p[0] + p[1])   # 3, 7, 11
```

## Příklad

```python
grid = [[1, 1], [2, 2]]
for row in grid:
    print(row[0] + row[1])   # 2, 4
```

## Tvůj úkol

Přečti počet `n`, pak `n` **dvojic** čísel (každá dvojice jsou dvě čísla na dvou
řádcích). Sestav seznam dvojic `[a, b]`. Nejprve vypiš celý vnořený seznam, pak
vypiš **součet každé dvojice**, jeden na řádek.

Pro vstup `2`, pak `1`, `2`, `3`, `4`:

```
[[1, 2], [3, 4]]
3
7
```

## Hotovo, když

- `1,2` a `3,4` vypíšou `[[1, 2], [3, 4]]` pak `3` pak `7`.
- Počet `0` vypíše `[]` a nic víc.
""",

"4.6 hints": r"""Pro každou dvojici přečti dvě čísla a přidej je jako dvoupoložkový seznam [a, b].

---

`pairs.append([a, b])` staví vnořený seznam. Vypiš ho, pak projdi:
`for p in pairs: print(p[0] + p[1])`.

---

n = int(input())
pairs = []
for _ in range(n):
    a = int(input())
    b = int(input())
    pairs.append([a, b])
print(pairs)
for p in pairs:
    print(p[0] + p[1])
""",

"4.6 reference": r"""Seznam může obsahovat jiné seznamy — **vnořený** seznam — modelující mřížku nebo
tabulku. `grid[r]` vybere vnitřní seznam (řádek); `grid[r][c]` pak z něj vybere
položku (sloupec), takže dva indexy dosáhnou na jednu buňku.

- První index vybere řádek, druhý položku v tom řádku.
- Cyklus `for row in grid:` vydá každý vnitřní seznam; vnoř druhý cyklus
  (`for cell in row:`), abys dosáhl na každou položku.
- Vnitřní seznamy jsou obyčejné seznamy — měnitelné a nezávisle velké (řádky
  nemusí mít stejnou délku).

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[0][2]    # 3   -- row 0, column 2
grid[1][0]    # 4
```
""",

"4.7 brief": r"""# 4.7 -- N-tice a rozbalování

## Koncept

**N-tice** (tuple) je jako seznam, ale **neměnná** -- jakmile je vytvořena, nelze
ji změnit. Zapíšeš ji závorkami (nebo jen čárkami):

```python
point = (3, 7)
print(point[0])    # 3
```

**Rozbalování** (unpacking) přiřadí několik proměnných najednou z n-tice (nebo
seznamu):

```python
x, y = point       # x = 3, y = 7
```

Jména vlevo odpovídají položkám vpravo, v pořadí. Pěkný trik, který to umožňuje, je
**prohození** dvou proměnných bez pomocné:

```python
a, b = 1, 2
a, b = b, a        # now a = 2, b = 1
```

Pravá strana `b, a` sestaví n-tici, která se pak rozbalí do `a, b`.

## Příklad

```python
a, b = 10, 20
a, b = b, a
print(a)    # 20
print(b)    # 10
```

## Tvůj úkol

Přečti dvě celá čísla (každé na vlastním řádku). **Prohoď** je pomocí rozbalování
n-tice, pak vypiš první, pak druhé.

Pro vstup `3` a pak `7`:

```
7
3
```

## Hotovo, když

- `3, 7` vypíše `7` pak `3`.
- Funguje pro libovolná dvě čísla (včetně dvou stejných).
""",

"4.7 hints": r"""Přečti obě čísla, pak je na jednom řádku prohoď pomocí a, b = b, a.

---

`a = int(input())`, `b = int(input())`, pak `a, b = b, a`, pak vypiš a a b.

---

a = int(input())
b = int(input())
a, b = b, a
print(a)
print(b)
""",

"4.7 reference": r"""**N-tice** je uspořádaná, **neměnná** posloupnost psaná čárkami (často v
závorkách): `(3, 4)`, nebo jen `3, 4`. Jakmile je vytvořena, nelze ji změnit.

- **Rozbalování** přiřadí položky posloupnosti několika jménům najednou:
  `a, b = point`. Počet na obou stranách se musí shodovat.
- Tím je umožněno jednořádkové **prohození** `a, b = b, a`: pravá strana se
  nejprve sestaví do n-tice, pak se rozbalí, takže není potřeba žádná pomocná
  proměnná.
- N-tici použij pro pevnou skupinu souvisejících hodnot (souřadnice, záznam);
  seznam použij, když kolekce roste nebo se mění.

```python
point = (3, 4)
x, y = point        # x = 3, y = 4
a, b = b, a         # swap in one line
```
""",

"4.8 brief": r"""# 4.8 -- Slovníky

## Koncept

**Slovník** (`dict`) mapuje **klíče** na **hodnoty** -- vyhledávací tabulka. Zapíšeš
ho složenými závorkami a páry `klíč: hodnota`:

```python
ages = {"sam": 20, "ada": 36}
print(ages["sam"])     # 20      look up by key
ages["lee"] = 41       # add a new key
ages["sam"] = 21       # update an existing key
```

Věci vyhledáváš podle **klíče** (ne podle pozice), což dělá slovníky rychlými a
šikovnými pro „dané X, jaké je jeho Y?“. Začni z prázdna pomocí `{}` a naplň ho:

```python
d = {}
d["x"] = 1
```

## Příklad

```python
prices = {}
prices["apple"] = 3
print(prices["apple"])   # 3
```

## Tvůj úkol

Přečti počet `n`, pak `n` dvojic **slova** a **čísla** (slovo na jednom řádku,
číslo na dalším) do slovníku (slovo je klíč, číslo hodnota). Pak přečti ještě jedno
**dotazové slovo** a vypiš číslo uložené pro něj.

Pro vstup `2`, `apple`, `3`, `banana`, `5`, pak dotaz `banana`:

```
5
```

## Hotovo, když

- Sestavení `{apple: 3, banana: 5}` a dotaz `banana` vypíše `5`.
- Pozdější dvojice se stejným klíčem ho aktualizuje (test se spoléhá na poslední
  hodnotu pro každý opakovaný klíč).
""",

"4.8 hints": r"""Vytvoř prázdný slovník, pak ukládej každou dvojici jako d[word] = number.

---

`d = {}`, v cyklu čti slovo + číslo pomocí `d[word] = int(input())`, pak přečti
dotaz a `print(d[query])`.

---

n = int(input())
d = {}
for _ in range(n):
    word = input()
    d[word] = int(input())
query = input()
print(d[query])
""",

"4.8 reference": r"""**Slovník** (`dict`) mapuje **klíče** na **hodnoty**: `{"a": 1, "b": 2}`. Je to
nástroj pro vyhledávání podle jména, ne podle pozice.

- **`d[key]`** přečte hodnotu pro klíč; **`d[key] = value`** klíč přidá (je-li
  nový) nebo aktualizuje (je-li přítomen). Klíče jsou jedinečné — přiřazení
  existujícího klíče přepíše.
- Čtení **chybějícího** klíče pomocí `d[key]` vyvolá `KeyError` (viz `.get`, 4.10).
- Klíče musí být neměnné (řetězce, čísla, n-tice); hodnoty mohou být cokoli.
  `len(d)` počítá páry; `key in d` testuje přítomnost klíče.

```python
ages = {"Ada": 36}
ages["Ada"]          # 36
ages["Linus"] = 21   # add a new pair
```
""",

"4.9 brief": r"""# 4.9 -- Procházení slovníku

## Koncept

Abys navštívil vše ve slovníku, procházej `.items()`, který dá každý **klíč a
hodnotu** dohromady:

```python
ages = {"sam": 20, "ada": 36}
for name, age in ages.items():
    print(name, age)      # sam 20, then ada 36
```

Část `for name, age in ...` rozbaluje každý pár do dvou proměnných. Slovníky si
pamatují pořadí, ve kterém jsi klíče vložil, takže je dostaneš zpět v tomto pořadí.

Jsou tu také `.keys()` (jen klíče) a `.values()` (jen hodnoty), ale `.items()` je
ten obvyklý, když potřebuješ obojí.

## Příklad

```python
d = {"x": 1, "y": 2}
for k, v in d.items():
    print(f"{k}={v}")     # x=1, then y=2
```

## Tvůj úkol

Přečti počet `n`, pak `n` dvojic **slova** a **čísla** do slovníku. Pak vypiš jeden
řádek `key=value` pro každou dvojici, v pořadí, v jakém byly přidány.

Pro vstup `2`, `a`, `1`, `b`, `2`:

```
a=1
b=2
```

## Hotovo, když

- `a=1`, `b=2` se vypíšou v pořadí vkládání.
- Počet `0` nevypíše nic.
""",

"4.9 hints": r"""Sestav slovník, pak projdi d.items(), abys získal každý klíč a hodnotu.

---

`for k, v in d.items(): print(f"{k}={v}")`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
for k, v in d.items():
    print(f"{k}={v}")
""",

"4.9 reference": r"""**`d.items()`** vydá každý pár `(klíč, hodnota)`, takže cyklus `for` se dvěma
proměnnými projde celý slovník a každý pár průběžně rozbaluje.

- `for k, v in d.items():` naváže `k` na klíč a `v` na jeho hodnotu při každém
  průchodu.
- `d.keys()` a `d.values()` procházejí jen klíče nebo jen hodnoty; procházení
  slovníku přímo (`for k in d`) prochází **klíče**.
- Pořadí iterace je **pořadí vkládání** (pořadí, v jakém byly klíče poprvé
  přidány).

```python
prices = {"pen": 2, "ink": 5}
for item, cost in prices.items():
    print(item, cost)        # pen 2 / ink 5
```
""",

"4.10 brief": r"""# 4.10 -- Chybějící klíče a .get()

## Koncept

Vyhledání klíče, který ve slovníku není, pomocí `d[key]` **spadne** (`KeyError`):

```python
ages = {"sam": 20}
print(ages["lee"])    # KeyError!
```

`.get()` je bezpečný způsob. Pro chybějící klíč vrátí `None` místo pádu -- nebo
**výchozí hodnotu**, kterou dodáš:

```python
print(ages.get("lee"))        # None
print(ages.get("lee", 0))     # 0      (your default)
print(ages.get("sam", 0))     # 20     (key exists, so its value)
```

Takže `d.get(key, default)` znamená „hodnota, pokud klíč existuje, jinak
`default`“.

## Příklad

```python
d = {"a": 1}
print(d.get("a", 0))    # 1
print(d.get("z", 0))    # 0
```

## Tvůj úkol

Přečti počet `n`, pak `n` dvojic slova a čísla do slovníku. Pak přečti **dotazové
slovo** a vypiš jeho číslo -- ale pokud slovo ve slovníku není, vypiš místo toho
`0` (nespadni).

Pro vstup `2`, `a`, `1`, `b`, `2`, pak dotaz `c`:

```
0
```

(`c` není klíč, takže se vypíše výchozí `0`.)

## Hotovo, když

- Přítomný klíč vypíše svou hodnotu; chybějící klíč vypíše `0`.
- Při chybějícím klíči nikdy nespadne (použij `.get`).
""",

"4.10 hints": r"""d[key] spadne, pokud klíč chybí. d.get(key, 0) místo toho vrátí 0.

---

Po sestavení slovníku a přečtení dotazu `print(d.get(query, 0))`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
query = input()
print(d.get(query, 0))
""",

"4.10 reference": r"""**`d.get(key, default)`** vyhledá klíč bezpečně: vrátí hodnotu, je-li klíč
přítomen, jinak `default` — bez vyvolání chyby. Bez výchozí hodnoty vrátí pro
chybějící klíč `None`.

- Použij ho místo `d[key]`, kdykoli je chybějící klíč normální, očekávaný případ,
  ne chyba.
- Pohání **sčítací** idiom: `counts[k] = counts.get(k, 0) + 1` přečte průběžný
  počet (poprvé 0) a zapíše nový.
- `.get` jen čte; nikdy klíč nevloží (na rozdíl od `setdefault`).

```python
ages = {"Ada": 36}
ages.get("Ada", 0)     # 36
ages.get("Nobody", 0)  # 0  -- no KeyError
```
""",

"4.11 brief": r"""# 4.11 -- Množiny

## Koncept

**Množina** (set) je neuspořádaná kolekce **jedinečných** položek -- automaticky
zahazuje duplicity. Zapíšeš ji složenými závorkami, nebo sestavíš ze seznamu pomocí
`set(...)`:

```python
s = {1, 2, 2, 3}
print(s)              # {1, 2, 3}   (the duplicate 2 is gone)

nums = [1, 1, 2, 3, 3]
print(set(nums))      # {1, 2, 3}
print(len(set(nums))) # 3           how many *distinct* values
```

Množiny jsou skvělé pro „kolik různých věcí?“ a pro rychlé testy příslušnosti
pomocí `in`:

```python
print(2 in s)         # True
```

(Množiny nemají pořadí ani indexování -- nemůžeš udělat `s[0]`.)

## Příklad

```python
words = ["a", "b", "a"]
print(len(set(words)))   # 2
```

## Tvůj úkol

Přečti počet `n`, pak `n` slov. Vypiš, kolik je **odlišných** slov.

Pro vstup `4`, `a`, `b`, `a`, `c`:

```
3
```

(`a` se objeví dvakrát, ale počítá se jednou.)

## Hotovo, když

- `a, b, a, c` vypíše `3`.
- Počet `0` vypíše `0`.
""",

"4.11 hints": r"""Množina zahodí duplicity. Dej slova do množiny, pak ji spočítej.

---

Posbírej slova do seznamu, pak `print(len(set(words)))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(len(set(words)))
""",

"4.11 reference": r"""**Množina** je neuspořádaná kolekce **jedinečných** položek: `{1, 2, 3}`. Modeluje
„skupinu odlišných věcí“ a rychle testuje příslušnost.

- Sestavení množiny z posloupnosti **zahodí duplicity**: `set([1, 1, 2])` je
  `{1, 2}`. Prázdná množina je `set()` — `{}` je prázdný *slovník*.
- **`x in s`** testuje příslušnost a je mnohem rychlejší než procházení seznamu,
  protože množiny jsou založené na hashování.
- Množiny jsou neuspořádané (žádné indexování, žádné řezy) a drží jen neměnné
  položky. Přidávej pomocí `.add(x)`, odebírej pomocí `.discard(x)`.

```python
seen = set()
seen.add("a"); seen.add("a")   # {'a'} -- duplicate ignored
"a" in seen                    # True
set([3, 1, 3, 2])              # {1, 2, 3}
```
""",

"4.12 brief": r"""# 4.12 -- Kombinování množin

## Koncept

Množiny lze kombinovat jako v matematice:

- **průnik** `a & b` -- položky v **obou**
- **sjednocení** `a | b` -- položky v **kterékoli**
- **rozdíl** `a - b` -- položky v `a`, ale ne v `b`

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # {2, 3}
print(a | b)    # {1, 2, 3, 4}
print(a - b)    # {1}
```

Tyto odpovídají na otázky jako „které položky dvě skupiny sdílejí?“ bez psaní
cyklu. (`a.intersection(b)` a `a.union(b)` dělají totéž co `&` a `|`.)

## Příklad

```python
x = {"a", "b"}
y = {"b", "c"}
print(len(x & y))   # 1   (just "b")
```

## Tvůj úkol

Přečti první skupinu: počet `n`, pak `n` slov. Pak druhou skupinu: počet `m`, pak
`m` slov. Vypiš, **kolik odlišných slov se objeví v obou** skupinách.

Pro první skupinu `a`, `b` a druhou skupinu `b`, `c`:

```
1
```

(V obou je jen `b`.)

## Hotovo, když

- `{a, b}` a `{b, c}` vypíšou `1`.
- Prázdné skupiny dají `0`; duplicity uvnitř skupiny se počítají jednou.
""",

"4.12 hints": r"""Dej každou skupinu do množiny, pak použij jejich průnik.

---

Sestav množinu `a` a množinu `b`, pak `print(len(a & b))`.

---

n = int(input())
a = set()
for _ in range(n):
    a.add(input())
m = int(input())
b = set()
for _ in range(m):
    b.add(input())
print(len(a & b))
""",

"4.12 reference": r"""Množiny podporují algebru kolekcí:

- **`a & b`** (průnik) — položky v **obou**.
- **`a | b`** (sjednocení) — položky v **kterékoli**.
- **`a - b`** (rozdíl) — položky v `a`, ale **ne** v `b`.

Každá vrátí **novou** množinu. (`^` je symetrický rozdíl — v právě jedné.) Tyto
vyjadřují množinové otázky přímo a nahrazují ručně psané cykly, které porovnávají
dvě kolekce.

```python
a, b = {1, 2, 3}, {2, 3, 4}
a & b     # {2, 3}
a | b     # {1, 2, 3, 4}
a - b     # {1}
```
""",

"4.13 brief": r"""# 4.13 -- Volba správné kolekce

## Koncept

Teď máš čtyři kolekce. Volba té správné dělá problém snadným:

- **list** -- uspořádané položky, duplicity povoleny (`[1, 2, 2]`). Použij pro
  posloupnosti.
- **tuple** -- jako seznam, ale pevná/neměnná. Použij pro pevné skupiny.
- **set** -- neuspořádané, **jedinečné** položky. Použij pro „odlišné“ a rychlou
  příslušnost.
- **dict** -- vyhledávání klíč -> hodnota. Použij pro „dané X, najdi jeho Y“.

Tato úloha jich pár kombinuje:

- `len(nums)` -- kolik položek (**seznam** zachová každou hodnotu, včetně
  opakování).
- `len(set(nums))` -- kolik **odlišných** hodnot (**množina** zahodí duplicity).
- **součet** -- cyklus s akumulátorem (nebo `sum(nums)`).

## Příklad

```python
nums = [1, 2, 2, 3]
print(len(nums))        # 4
print(len(set(nums)))   # 3
```

## Tvůj úkol

Přečti počet `n`, pak `n` čísel. Vypiš tři řádky:

1. kolik čísel je,
2. kolik je **odlišných** čísel,
3. jejich **součet**.

Pro vstup `4`, pak `1`, `2`, `2`, `3`:

```
4
3
8
```

## Hotovo, když

- `1, 2, 2, 3` vypíše `4`, `3`, `8`.
- Počet `0` vypíše `0`, `0`, `0`.
""",

"4.13 hints": r"""Sestav seznam. Počet je len(nums); počet odlišných používá množinu.

---

`print(len(nums))`, `print(len(set(nums)))`, pak součet (cyklus, nebo sum).

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
print(len(set(nums)))
total = 0
for x in nums:
    total = total + x
print(total)
""",

"4.13 reference": r"""Tři základní kolekce se hodí na různé úlohy — volba té správné dělá kód
jednodušším a rychlejším:

- **list** — **uspořádaná** posloupnost, která se může opakovat. Použij ho k
  uchování každé hodnoty, v pořadí (záznam, fronta položek ke zpracování).
- **set** — neuspořádaná skupina **odlišných** položek s rychlou příslušností.
  Použij ji k zahození duplicit nebo k otázce „viděl jsem to už?“.
- **dict** — mapování z **klíčů na hodnoty**. Použij ho k vyhledání něčeho podle
  jména (počet na slovo, cena na položku).

Ptej se: potřebuji pořadí a opakování (list), jedinečnost a příslušnost (set), nebo
vyhledávání podle klíče (dict)?

```python
order  = ["a", "b", "a"]    # keep all, in order
unique = {"a", "b"}         # distinct only
price  = {"a": 2, "b": 5}   # look up by key
```
""",
}
