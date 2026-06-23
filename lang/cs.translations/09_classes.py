# PyQuest translations -- language 'cs' -- chapter 09_classes -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"9.1 brief": r"""# 9.1 -- První třída

## Koncept

**Třída** je předloha pro objekt, který svazuje související data dohromady. Dosud by
psí jméno a věk byly dvě volné proměnné; třída je sváže do jedné věci, kterou můžeš
posílat dál.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `class Dog:` pojmenuje předlohu.
- `__init__` je **konstruktor** -- spustí se, když vytváříš nového Doga, a jeho
  úkolem je nastavit data objektu.
- `self` je objekt, který se staví; `self.name = name` uloží hodnotu **na objekt**,
  takže tam je i později.

Jeden (*instanci*) vytvoříš tím, že třídu zavoláš jako funkci, a její data přečteš
tečkou:

```python
d = Dog("Rex", 3)
print(d.name)   # Rex
print(d.age)    # 3
```

## Tvůj úkol

Definuj třídu `Dog`, jejíž `__init__` bere `name` a `age` a každé uloží na objekt
jako `self.name` a `self.age`.

## Hotovo, když

- `Dog("Rex", 3)` vytvoří objekt, jehož `.name` je `"Rex"` a `.age` je `3`.
- Funguje pro libovolné jméno a věk.
- Použil jsi `class` s `__init__`, který uloží obě hodnoty na `self`.
""",

"9.1 hints": r"""Začni s `class Dog:` a dej mu metodu `__init__(self, name, age)`.

---

Uvnitř `__init__` zkopíruj každý parametr na objekt pomocí `self.`:
`self.name = name`. To je to, co hodnotu udrží.

---

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
""",

"9.1 reference": r"""**Třída** definuje nový typ objektu a svazuje související data do jedné hodnoty.
**`__init__`** je inicializátor: Python ho zavolá automaticky, když vytváříš
instanci, aby nastavil její počáteční data.

- `class Point:` otevře definici; volání `Point(3, 4)` vytvoří **instanci** a
  spustí `__init__`.
- **`self`** je instance, která se staví; `self.x = x` uloží hodnotu jako
  **atribut** na ni, kde ji každá metoda později dosáhne.
- První parametr `__init__` je vždy `self`; zbytek jsou argumenty, které volající
  předá.

```python
class Point:
    def __init__(self, x, y):
        self.x = x          # store data on the instance
        self.y = y

p = Point(3, 4)
p.x                         # 3
```
""",

"9.2 brief": r"""# 9.2 -- Metody: chování nad daty

## Koncept

Objekty nejen drží data -- mají **metody**, funkce, které žijí na objektu a pracují
s jeho vlastními daty skrze `self`.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

`area` je metoda: bere `self` (objekt, na kterém je volána) a používá `self.side`.
Voláš ji tečkou a závorkami -- `self` předávat netřeba, Python ho doplní:

```python
s = Square(5)
print(s.area())   # 25
```

Smysl metody je, že chování putuje *spolu* s daty: každý Square už ví, jak spočítat
svůj vlastní obsah.

## Tvůj úkol

Definuj třídu `Square`, jejíž `__init__` uloží `side`, a přidej metodu `area()`,
která vrátí obsah čtverce (`side * side`).

## Hotovo, když

- `Square(5).area()` vrátí `25`.
- Funguje pro libovolnou délku strany, včetně `0`.
- `area` je metoda na třídě a počítá z `self.side`.
""",

"9.2 hints": r"""Ulož stranu v `__init__` jako minule, pak přidej druhou metodu `area`.

---

Metoda bere `self` první: `def area(self):`. Uvnitř vrať
`self.side * self.side`.

---

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
""",

"9.2 reference": r"""**Metoda** je funkce definovaná uvnitř třídy. Vždy bere **`self`** první a počítá z
vlastních atributů objektu, takže chování žije s daty, na nichž působí.

- Voláš ji `instance.metoda()`; Python instanci automaticky předá jako `self`,
  takže `p.dist()` volá `dist(p)`.
- Uvnitř dosáhneš na data objektu skrze `self`: `self.x`, `self.y`.
- Metoda může brát další parametry za `self` a `return` hodnotu jako každá funkce.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

Point(3, 4).dist()      # 5.0
```
""",

"9.3 brief": r"""# 9.3 -- Stav, který si pamatuje

## Koncept

Data objektu žijí **mezi** voláními metod -- metoda může změnit `self` a další
volání tu změnu vidí. To je to, co dělá objekty užitečnými: *pamatují si*.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count = self.count + 1
        return self.count
```

Každé `tick()` posune `self.count` a vrátí novou hodnotu:

```python
c = Counter()
c.tick()   # 1
c.tick()   # 2
c.tick()   # 3
```

Klíčové je, že počet žije **na instanci** (`self.count`), takže dva čítače si vedou
oddělené součty -- tiknutí jednoho se nikdy nedotkne druhého.

## Tvůj úkol

Definuj třídu `Counter`, která začne svůj `count` na `0`. Přidej metodu `tick()`,
která přičte jedna k počtu a **vrátí nový počet**.

## Hotovo, když

- Čerstvý `Counter` tiknutý třikrát vrátí `1`, `2`, `3`.
- Dva čítače jsou nezávislé -- tiknutí jednoho nezmění druhý.
- Počet je uložený na `self`, ne sdílený mezi všemi čítači.
""",

"9.3 hints": r"""`__init__` nastaví výchozí bod: `self.count = 0`. Pak `tick` ho mění.

---

Uvnitř `tick` udělej `self.count = self.count + 1` (nebo `self.count += 1`), pak
`return self.count`. Drž počet na `self`, aby každý čítač měl svůj vlastní.

---

class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1
        return self.count
""",

"9.3 reference": r"""Objekt drží **stav** — data, která přetrvávají mezi voláními. Metoda může
**zmutovat** `self` a další volání metody tu změnu vidí, takže si objekt pamatuje,
co se s ním stalo.

- `self.count += 1` aktualizuje atribut na místě; nová hodnota žije, dokud se zase
  nezmění.
- To je smysl objektů: nesou svá data s sebou napříč voláními, na rozdíl od prosté
  funkce, jejíž lokální proměnné zmizí, když vrátí hodnotu.
- Každá instance má **vlastní** kopii atributů, takže dva čítače počítají nezávisle.

```python
class Counter:
    def __init__(self):
        self.n = 0
    def tick(self):
        self.n += 1         # remembered for next time

c = Counter(); c.tick(); c.tick(); c.n   # 2
```
""",

"9.4 brief": r"""# 9.4 -- Více dat, více metod

## Koncept

Třída může držet několik kusů dat a nabízet nad nimi několik metod. V syntaxi nic
nového -- jen víc téhož:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

Obě metody čtou stejná uložená data skrze `self`; každý Rectangle o sobě zodpoví
kteroukoli otázku:

```python
r = Rectangle(3, 4)
r.area()        # 12
r.perimeter()   # 14
```

## Tvůj úkol

Definuj třídu `Rectangle`, jejíž `__init__` uloží `width` a `height`, se dvěma
metodami: `area()` vrací `width * height` a `perimeter()` vrací
`2 * (width + height)`.

## Hotovo, když

- `Rectangle(3, 4).area()` je `12` a `.perimeter()` je `14`.
- Obojí funguje pro libovolnou šířku a výšku.
- Obojí jsou metody na třídě, počítající z `self`.
""",

"9.4 hints": r"""Ulož obě hodnoty v `__init__`: `self.width = width` a
`self.height = height`.

---

Přidej dvě metody. `area` vrací `self.width * self.height`; `perimeter` vrací
`2 * (self.width + self.height)`.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
""",

"9.4 reference": r"""Třída může držet **několik atributů** a nabízet **několik metod**, které nad nimi
spolupracují — modelujíce něco s více než jednou vlastností.

- `__init__` uloží každý kus dat (`self.width`, `self.height`); každá metoda čte
  atributy, které potřebuje.
- Metody mohou stavět na stejných datech pro různé odpovědi: `area` násobí,
  `perimeter` sčítá — jeden objekt, mnoho otázek.
- Držet data a operace v jedné třídě znamená, že se volající ptají objektu, místo
  aby žonglovali s volnými proměnnými.

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

r = Rectangle(3, 4); r.area(), r.perimeter()   # (12, 14)
```
""",

"9.5 brief": r"""# 9.5 -- Tisk objektu: `__str__`

## Koncept

Vypiš objekt tak, jak je, a dostaneš něco nepoužitelného jako
`<__main__.Point object at 0x10f3d2b80>`. Abys řídil, jak objekt vypadá jako text,
definuj speciální metodu `__str__`, která vrátí řetězec, jejž má Python zobrazit.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

`__str__` je **dunder** (metoda s dvojitým podtržítkem) -- Python ji za tebe zavolá,
kdykoli se objekt mění na text, pomocí `print()` nebo `str()`:

```python
p = Point(3, 4)
print(p)        # (3, 4)
str(p)          # "(3, 4)"
```

`__str__` nikdy nevoláš sám; jen ji definuješ a `str(p)` ji spustí.

## Tvůj úkol

Definuj třídu `Point` ukládající `x` a `y`, s metodou `__str__` tak, aby
`str(Point(3, 4))` bylo přesně `"(3, 4)"` -- dvě hodnoty v závorkách, mezi nimi
čárka a mezera.

## Hotovo, když

- `str(Point(3, 4))` je `"(3, 4)"`.
- Funguje pro libovolné `x` a `y`, včetně záporných.
- Formátování pochází z metody `__str__` na třídě.
""",

"9.5 hints": r"""Ulož `x` a `y` v `__init__` jako obvykle, pak přidej metodu `__str__(self)`.

---

`__str__` musí text **vrátit** (ne ho vypsat). Sestav ho f-řetězcem:
`return f"({self.x}, {self.y})"`. Dej pozor na čárku a mezeru.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
""",

"9.5 reference": r"""**`__str__`** definuje čitelný text pro objekt. Když instanci `print`neš nebo na ni
zavoláš `str()`, Python zavolá `__str__` a použije to, co vrátí.

- Bez ní vypsání objektu ukáže neužitečnou výchozí podobu jako
  `<Point object at 0x...>`; `__str__` to nahradí něčím smysluplným.
- Musí **vrátit** řetězec (ne ho vypsat), obvykle sestavený f-řetězcem z atributů
  objektu.
- `__str__` je jedna z několika **dunder** („dvojité podtržítko“) metod, které
  Python volá za tebe, jako `__init__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(3, 4))      # (3, 4)
```
""",

"9.6 brief": r"""# 9.6 -- Rozumná výchozí hodnota

## Koncept

Konstruktor je jen funkce, takže může brát i **výchozí parametry** (6.4). To
umožní volajícímu vynechat to, co ho nezajímá, a přesto dostat funkční objekt.

```python
class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
```

Pokud pozdrav nepředáš, dostaneš `"Hello"`; pokud ano, použije se místo toho:

```python
Greeter().greet("Ada")        # "Hello, Ada!"
Greeter("Hi").greet("Bo")     # "Hi, Bo!"
```

Výchozí hodnota žije v signatuře `__init__` (`greeting="Hello"`), takže objekt se
nakonfiguruje jednou při stavbě a každý `greet` ji znovu použije.

## Tvůj úkol

Definuj třídu `Greeter`, jejíž `__init__` bere `greeting`, který **má výchozí
hodnotu `"Hello"`**, a uloží ho. Přidej metodu `greet(name)`, která vrátí
`"{greeting}, {name}!"`.

## Hotovo, když

- `Greeter().greet("Ada")` je `"Hello, Ada!"` (použita výchozí hodnota).
- `Greeter("Hi").greet("Bo")` je `"Hi, Bo!"` (výchozí hodnota přepsána).
- Výchozí hodnota je výchozí *parametr* `__init__`, ne `if` uvnitř něj.
""",

"9.6 hints": r"""Dej `__init__` parametr s výchozí hodnotou: `def __init__(self,
greeting="Hello"):`, pak ho ulož na `self`.

---

`greet` sestaví zprávu: `return f"{self.greeting}, {name}!"`. Výchozí hodnota
patří do signatury, takže nepiš místo toho `if greeting is None`.

---

class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
""",

"9.6 reference": r"""`__init__` je obyčejná funkce, takže její parametry mohou mít **výchozí hodnoty** —
což umožní objekt vytvořit s určitými argumenty i bez nich.

- `def __init__(self, balance=0):` dovolí `Account()` (začne na 0) nebo
  `Account(100)` (začne na 100).
- Platí stejná pravidla: parametry s výchozí hodnotou jdou za těmi bez ní a
  měnitelná výchozí hodnota potřebuje trik se sentinelem `None`
  (`def __init__(self, items=None): self.items = items or []`).
- Výchozí hodnoty dělají běžný případ bez námahy a zároveň drží možnost otevřenou.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance

Account().balance        # 0
Account(100).balance     # 100
```
""",

"9.7 brief": r"""# 9.7 -- Objekty spolupracující

## Koncept

Metoda může brát **jiný objekt** jako argument a postavit **nový** objekt jako svůj
výsledek. Takto se objekty kombinují, aniž by ztratily svou vlastní identitu.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

`add` sáhne do `other` (jiného Vectoru) pro jeho data a **vrátí úplně nový
`Vector`** -- nemění `self` ani `other`:

```python
a = Vector(1, 2)
b = Vector(3, 4)
c = a.add(b)      # Vector(4, 6)
a.x               # still 1 -- a is untouched
```

Stavět `Vector(...)` *uvnitř* vlastní metody Vectoru je normální: třída může použít
sama sebe.

## Tvůj úkol

Definuj třídu `Vector` ukládající `x` a `y`, s metodou `add(other)`, která vrátí
**nový** `Vector`, jehož souřadnice jsou souřadnice obou vektorů sečtené dohromady.
Originály musí zůstat beze změny.

## Hotovo, když

- `Vector(1, 2).add(Vector(3, 4))` je Vector s `.x == 4` a `.y == 6`.
- Oba vstupní vektory jsou poté beze změny.
- `add` vrací nový objekt `Vector` (ne n-tici), postavený uvnitř metody.
""",

"9.7 hints": r"""Ulož `x` a `y` v `__init__`. Metoda bere druhý vektor:
`def add(self, other):`.

---

Přečti oba vektory tečkou (`self.x`, `other.x`) a **vrať nový Vector**:
`return Vector(self.x + other.x, self.y + other.y)`. Nepřiřazuj zpět na `self`.

---

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
""",

"9.7 reference": r"""Objekty **spolupracují**: metoda může brát **jiný objekt** téže třídy jako
parametr, číst jeho atributy a **vrátit nový** objekt držící výsledek — přičemž oba
vstupy nechá beze změny.

- `def add(self, other):` sáhne na `self.x` a `other.x`, pak
  `return Vector(self.x + other.x, ...)`. Vrácení čerstvé instance drží operandy
  neměnné.
- Takto se skládají hodnotové objekty (body, vektory, peníze). Definice dunderu
  `__add__` by dokonce nechala `a + b` ji zavolat.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

Vector(1, 2).add(Vector(3, 4)).x    # 4
```
""",

"9.8 brief": r"""# 9.8 -- Závěrečná: bankovní účet

## Koncept

Čas spojit kapitolu: třída se stavem, několik metod, rozumná výchozí hodnota a
pravidlo, které vymáhá.

`BankAccount` drží `balance`. Můžeš vložit (roste) i vybrat (klesá) -- ale výběr,
který by účet přečerpal, musí být **odmítnut** a zůstatek ponechán beze změny.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

- `balance` má výchozí hodnotu `0`, takže `BankAccount()` je prázdný účet.
- `deposit` a `withdraw` mění uložený zůstatek (stav, který přetrvává).
- `withdraw` **vrátí `True`**, když uspěje, a **`False`**, když odmítne -- a při
  odmítnutí se zůstatek nemění.

```python
acc = BankAccount(100)
acc.deposit(50)       # balance 150
acc.withdraw(70)      # True,  balance 80
acc.withdraw(999)     # False, balance still 80
```

## Tvůj úkol

Definuj `BankAccount` přesně jako výše: `balance` s výchozí hodnotou `0`, metodu
`deposit(amount)` a metodu `withdraw(amount)`, která odečte a vrátí `True` jen
tehdy, když je dost prostředků -- jinak nic nezmění a vrátí `False`.

## Hotovo, když

- `BankAccount()` začne na `0`; `BankAccount(100)` začne na `100`.
- `deposit` a `withdraw` aktualizují `balance` a výběr příliš velký vrátí `False` a
  nechá `balance` beze změny.
- Výběr přesně zůstatku je povolen.
""",

"9.8 hints": r"""`__init__(self, balance=0)` uloží počáteční zůstatek. `deposit` jen přičte k
`self.balance`.

---

`withdraw` potřebuje stráž: `if amount <= self.balance:` odečti a
`return True`; jinak nic neměň a `return False`.

---

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
""",

"9.8 reference": r"""Závěrečná úloha je **stavová třída**, která spojuje kapitolu: výchozí hodnota v
`__init__`, metody, které **mutují** stav, **stráž**, která vyvolá chybu při
neplatných operacích, a `__str__` pro zobrazení.

- `__init__` nastaví počáteční zůstatek (s výchozí hodnotou); `deposit` a
  `withdraw` mění `self.balance` na místě.
- Stráž chrání invariant: `withdraw` zkontroluje prostředky a
  `raise ValueError(...)`, místo aby povolil nemožný stav.
- `__str__` vykreslí objekt pro tisk. Dohromady to dělá objekt, který je spolehlivé
  používat a příjemné číst.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
    def __str__(self):
        return f"balance: {self.balance}"
```
""",
}
