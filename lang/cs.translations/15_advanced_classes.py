# PyQuest translations -- language 'cs' -- chapter 15_advanced_classes -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"15.1 brief": r"""# 15.1 -- Dědičnost: stav na základní třídě

## Koncept

Kapitola 9 stavěla jednotlivé třídy. **Dědičnost** umožní jedné třídě stavět na
druhé: **podtřída** automaticky dostane metody **základní třídy**, pak přidá nebo
změní vlastní.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return self.name + " the animal"

class Dog(Animal):           # Dog IS an Animal
    def speak(self):
        return "Woof"
```

- `class Dog(Animal):` udělá z `Dog` podtřídu `Animal`. Instance `Dog` může zavolat
  `describe()` -- zděděné z `Animal` -- *i* `speak()`, svou vlastní.
- Vztah je „**je-**“ (is-a): `Dog` **je** `Animal`, takže `isinstance(dog, Animal)`
  je `True`.
- Sdílené chování žije jednou v základu; podtřídy ho neopakují.

## Tvůj úkol

Definuj základní třídu `Animal` s `__init__(self, name)` a `describe(self)`
vracejícím `"<name> the animal"`. Pak definuj `Dog(Animal)`, který z ní **dědí** a
přidá `speak(self)` vracející `"Woof"`.

## Hotovo, když

- `Dog("Rex").describe()` vrátí `"Rex the animal"` (zděděné).
- `Dog("Rex").speak()` vrátí `"Woof"`.
- `Dog` **je** `Animal`: dědí `describe`, místo aby ho kopíroval.
""",

"15.1 hints": r"""Nejprve napiš `Animal`, s `__init__` ukládajícím `self.name` a `describe`
vracejícím větu. Pak `class Dog(Animal):` -- to `(Animal)` je to, co dělá Doga
dědícím.

---

Uvnitř `Dog` píšeš jen `speak`; `describe` přijde zadarmo z `Animal`. Nepředefinovávej
`describe` v `Dog`.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name + " the animal"


class Dog(Animal):
    def speak(self):
        return "Woof"
""",

"15.1 reference": r"""**Dědičnost** umožní třídě stavět na druhé. Zápis `class Child(Parent):` udělá z
`Child` **podtřídu**: automaticky má všechny metody `Parent` a může přidat nové nebo
nahradit stávající.

- Vztah je **„je-“** (is-a): `Dog(Animal)` *je* `Animal`, takže
  `isinstance(dog, Animal)` je `True` a `Dog` funguje všude, kde se očekává
  `Animal`.
- Sdílené chování žije **jednou** v základní třídě; podtřídy ho dědí, místo aby ho
  kopírovaly, takže oprava v rodiči dosáhne na každého potomka.
- Python najde metodu procházením **MRO** (method resolution order, pořadí
  rozlišení metod): nejprve třída instance, pak její základy. `object` je implicitní
  základ každé třídy.

```python
class Animal:
    def __init__(self, name): self.name = name
    def describe(self): return self.name + " the animal"

class Dog(Animal):
    def speak(self): return "Woof"

d = Dog("Rex")
d.describe()              # 'Rex the animal'  -- inherited
isinstance(d, Animal)    # True
```
""",

"15.2 brief": r"""# 15.2 -- super(): rozšiř rodiče

## Koncept

Podtřída často potřebuje vše, co dělá rodičův `__init__`, **plus** trochu navíc.
**`super()`** ti dá rodiče, takže zavoláš jeho metodu a pak k ní přidáš -- místo
kopírování rodičova kódu:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # run Animal's __init__ (sets self.name)
        self.breed = breed         # then add Dog's own attribute
```

- `super().__init__(name)` zavolá **rodičův** `__init__` na této instanci, takže
  `self.name` nastaví `Animal`.
- Poté potomek přidá to, co je pro něj zvláštní (`self.breed`).
- Tím se rodičovo nastavení drží na jednom místě; pokud se `Animal.__init__` změní,
  `Dog` to převezme automaticky.

## Tvůj úkol

Definuj `Animal` s `__init__(self, name)` ukládajícím `self.name`. Pak definuj
`Dog(Animal)`, jehož `__init__(self, name, breed)` zavolá **`super().__init__(name)`**
a pak uloží `self.breed`.

## Hotovo, když

- `Dog("Rex", "Lab").name` je `"Rex"` (nastaveno přes `super().__init__`).
- `Dog("Rex", "Lab").breed` je `"Lab"`.
- `Dog` je `Animal` a jméno nastaví rodič, ne ruční přiřazení.
""",

"15.2 hints": r"""`Dog` bere dva argumenty. První, `name`, patří `Animal` -- předej ho nahoru pomocí
`super().__init__(name)`.

---

Po řádku `super().__init__(name)` nastav `self.breed = breed` pro vlastní část Doga.

---

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
""",

"15.2 reference": r"""**`super()`** vrátí proxy na **rodičovskou třídu**, takže podtřída může zavolat
rodičovu metodu a stavět na ní, místo aby duplikovala jeho kód. Obvyklý případ je
`__init__`:

- `super().__init__(args)` spustí rodičův inicializátor na této instanci a nastaví
  vše, co rodič vlastní; potomek pak přidá své vlastní atributy.
- Drží rodičovu logiku na **jednom místě** — změň `Animal.__init__` a každá podtřída,
  která volá `super().__init__`, změnu zdědí.
- `super()` funguje pro libovolnou metodu, nejen `__init__`: přepisující metoda může
  zavolat `super().method()`, aby znovu použila rodičovu verzi a rozšířila ji.
- Bez `super().__init__` se rodičův inicializátor **nespustí**, takže atributy, které
  by nastavil, chybí.

```python
class Animal:
    def __init__(self, name): self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Animal sets self.name
        self.breed = breed         # Dog adds self.breed

Dog("Rex", "Lab").name             # 'Rex'
```
""",

"15.3 brief": r"""# 15.3 -- Přepsání: vlastní verze potomka

## Koncept

Podtřída může **přepsat** (override) rodičovu metodu -- definovat vlastní verzi
metody, kterou rodič už má. Pro instance podtřídy vítězí nová verze:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."          # generic

class Cat(Animal):
    def speak(self):
        return "Meow"         # Cat's own
```

- `Cat("Felix").speak()` vrátí `"Meow"`; prosté `Animal(...).speak()` stále vrátí
  `"..."`.
- To je **polymorfismus**: *stejné* volání, `x.speak()`, udělá správnou věc pro
  jakýkoli typ, jímž `x` je.
- Podtřída stále dědí vše, co nepřepíše (zde `__init__` a `self.name`).

## Tvůj úkol

Definuj `Animal` s `__init__(self, name)` a `speak(self)` vracejícím `"..."`. Pak
definuj `Cat(Animal)`, který **přepíše** `speak`, aby vracelo `"Meow"`.

## Hotovo, když

- `Cat("Felix").speak()` vrátí `"Meow"`.
- `Animal("thing").speak()` vrátí `"..."` (beze změny).
- `Cat("Felix").name` je `"Felix"` (zděděný `__init__`) a Cat je Animal.
""",

"15.3 hints": r"""Dej `Animal` jak `__init__`, tak `speak` (vracející "..."). Pak `Cat(Animal)`
definuje svůj vlastní `speak`.

---

`speak` Cata prostě vrátí "Meow". Nepředefinovávej `__init__` v Cat -- je zděděný.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"
""",

"15.3 reference": r"""**Přepsání** je definice metody, kterou rodič už má, v podtřídě. Pro instance
podtřídy najde Python verzi podtřídy první (je dřív v MRO), takže chování potomka
nahradí to rodičovo.

- To je **polymorfismus**: jedno místo volání, `x.speak()`, spustí správný kód pro
  jakýkoli typ, jímž `x` skutečně je — `Cat` řekne „Meow“, obecný `Animal` řekne
  „...“. Volající kód nemusí znát přesný typ.
- Podtřída stále **dědí** vše, co *nepřepíše* (zde `__init__`).
- Přepsání může znovu použít rodičovu verzi pomocí `super().method()` — rozšířit,
  místo úplně nahradit.

```python
class Animal:
    def speak(self): return "..."
class Cat(Animal):
    def speak(self): return "Meow"

for a in [Animal(), Cat()]:
    print(a.speak())     # '...' then 'Meow' -- same call, different result
```
""",

"15.4 brief": r"""# 15.4 -- @property: počítaný atribut

## Koncept

Někdy je hodnota **odvozená** z jiných -- obsah obdélníku z jeho šířky a výšky. Mohl
bys ji uložit, ale pak zastará, když se změní šířka. **`@property`** ji spočítá při
každém přístupu, a přitom se stále čte jako prostý atribut:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12   -- no parentheses, but the method runs
r.width = 5
r.area        # 20   -- recomputed from the new width
```

- `@property` nad metodou udělá z `obj.area` (bez `()`) volání té metody a vrácení
  jejího výsledku.
- Protože běží pokaždé, hodnota je vždy aktuální -- na rozdíl od hodnoty uložené
  jednou v `__init__`.

## Tvůj úkol

Definuj `Rectangle` s `__init__(self, width, height)` a **property** **`area`**,
která vrátí `width * height`.

## Hotovo, když

- `Rectangle(3, 4).area` je `12` (přístup bez závorek).
- Po `r = Rectangle(3, 4); r.width = 5` je `r.area` `20` -- přepočítáno, ne uloženo.
""",

"15.4 hints": r"""Napiš `area` jako normální metodu, která vrací `self.width * self.height`, pak dej
`@property` na řádek přímo nad `def area`.

---

S `@property` volající píší `r.area` (bez závorek) a metoda běží pokaždé, takže vždy
odráží aktuální šířku a výšku.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
""",

"15.4 reference": r"""**`@property`** je dekorátor, který promění metodu na **počítaný atribut jen pro
čtení**. `obj.area` (bez závorek) spustí metodu a vrátí její výsledek, takže
odvozená hodnota se přepočítá při každém přístupu a nikdy nezastará.

- Skryje fakt, že se děje práce: volající používají `obj.area`, ne `obj.area()`,
  přesně jako u uloženého atributu — ale hodnota vždy odráží aktuální stav.
- Holé `@property` je jen pro čtení; přiřazení do něj vyvolá `AttributeError`. Přidej
  odpovídající `@area.setter`, abys umožnil přiřazení s validací.
- Dej property přednost před hodnotou uloženou v `__init__`, kdykoli hodnota
  *závisí* na jiných atributech, které se mohou změnit.

```python
class Rectangle:
    def __init__(self, w, h): self.width, self.height = w, h
    @property
    def area(self): return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12
r.width = 5
r.area        # 20  -- recomputed
```
""",

"15.5 brief": r"""# 15.5 -- @classmethod: alternativní konstruktor

## Koncept

Normální metoda bere `self` (instanci). **`@classmethod`** bere **`cls`** (samotnou
třídu), takže může postavit a vrátit **novou instanci** -- šikovný způsob, jak
nabídnout alternativní, pojmenovaný konstruktor:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

p = Point.from_tuple((3, 4))     # called on the class, not an instance
p.x, p.y                          # (3, 4)
```

- `@classmethod` udělá z `cls` první parametr -- třídu, na které je metoda volána
  (zde `Point`).
- `cls(...)` je totéž co `Point(...)`, ale použití `cls` znamená, že podtřídy
  dostanou instanci *svého* typu zadarmo.
- Voláš ji na **třídě**: `Point.from_tuple(...)`.

## Tvůj úkol

Definuj `Point` s `__init__(self, x, y)` a **classmethodou** `from_tuple(cls, pair)`,
která sestaví `Point` z n-tice `(x, y)`.

## Hotovo, když

- `Point.from_tuple((3, 4)).x` je `3` a `.y` je `4`.
- `from_tuple` je `@classmethod` beroucí `cls` a staví bod pomocí `cls(...)`.
""",

"15.5 hints": r"""Napiš `__init__` jako obvykle. Pak přidej metodu dekorovanou `@classmethod`, jejíž
první parametr je `cls`, ne `self`.

---

Uvnitř `from_tuple` rozbal dvojici a postav objekt pomocí `cls`:
`return cls(pair[0], pair[1])`.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])
""",

"15.5 reference": r"""**`@classmethod`** je svázaná s **třídou**, ne s instancí: jejím prvním parametrem
je **`cls`** (samotná třída) místo `self`. Protože má třídu, může stavět instance —
klasické použití je **alternativní konstruktor**.

- Voláš ji na třídě: `Point.from_tuple((3, 4))`. Python předá `Point` jako `cls`.
- Stavění pomocí `cls(...)` místo doslovného jména třídy znamená, že **podtřída**,
  která volá zděděnou classmethodu, dostane instanci *sebe sama*.
- Kontrast s **`@staticmethod`**, která nebere ani `self`, ani `cls` — jen prostou
  funkci ve jmenném prostoru třídy, používanou, když metoda nepotřebuje přístup k
  instanci ani třídě.

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    @classmethod
    def from_tuple(cls, pair): return cls(pair[0], pair[1])

Point.from_tuple((3, 4)).x     # 3
```
""",

"15.6 brief": r"""# 15.6 -- __eq__: rovnost podle hodnoty

## Koncept

Ve výchozím stavu se `==` na objektech ptá „jsou to **tentýž objekt**?“ -- takže dva
samostatně postavené objekty se stejnými daty si *nejsou* rovné. Dunder metoda
**`__eq__`** to změní na **rovnost podle hodnoty**:

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):
        return self.cents == other.cents

Money(500) == Money(500)     # True   -- same value
Money(500) == Money(750)     # False
```

- Python volá `a.__eq__(b)` pro `a == b`. Vrátíš, zda se mají počítat jako rovné --
  obvykle porovnáním atributů, které definují hodnotu.
- `!=` se vyřeší za tebe (je to negace `__eq__`).
- (Definice `__eq__` je také to, co umožní porovnávat tvé objekty podle hodnoty v
  testech, seznamech a kontrolách `in`.)

## Tvůj úkol

Definuj `Money` s `__init__(self, cents)` a **`__eq__`** tak, aby si dva objekty
`Money` byly rovné právě tehdy, když se shodují jejich `cents`.

## Hotovo, když

- `Money(500) == Money(500)` je `True`.
- `Money(500) == Money(750)` je `False`.
- Rovnost porovnává `cents`, ne identitu objektu.
""",

"15.6 hints": r"""Přidej do Money metodu `__eq__(self, other)`. Python ji volá pro `==`.

---

Vrať porovnání hodnot: `return self.cents == other.cents`.

---

class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        return self.cents == other.cents
""",

"15.6 reference": r"""Ve výchozím stavu `==` mezi objekty testuje **identitu** — zda jsou ten úplně
stejný objekt — takže dva nezávisle postavené objekty se stejnými daty se porovnají
jako nerovné. Definice **`__eq__(self, other)`** předefinuje `==` na **rovnost podle
hodnoty**.

- Python volá `a.__eq__(b)` k vyhodnocení `a == b`; vrať, zda se mají počítat jako
  rovné, obvykle porovnáním definujících atributů. `!=` následuje automaticky jako
  jeho negace.
- Rovnost podle hodnoty je to, co dělá objekty intuitivními v testech `==`, v
  příslušnosti k `list` (`in`) a při porovnávání výsledků.
- Pokud definuješ `__eq__`, třída se stane **nehashovatelnou** (její `__hash__` se
  nastaví na `None`), takže nemůže do `set` ani jako klíč `dict`, dokud nedefinuješ
  i `__hash__` — často `return hash(self.cents)`.

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other): return self.cents == other.cents

Money(500) == Money(500)     # True
Money(500) == Money(750)     # False
```
""",

"15.7 brief": r"""# 15.7 -- __lt__: učiň objekty řaditelnými

## Koncept

`sorted`, `min` i `max` všechny řadí věci pomocí operátoru **`<`**. Ve výchozím
stavu Python neví, jak porovnat dva tvé objekty -- jejich řazení vyvolá `TypeError`.
Definuj **`__lt__`** („less than“, menší než) a stanou se řaditelnými:

```python
class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees
    def __lt__(self, other):
        return self.degrees < other.degrees

temps = [Temperature(30), Temperature(10), Temperature(20)]
sorted(temps)        # ordered 10, 20, 30 -- by degrees
```

- Python volá `a.__lt__(b)` pro `a < b`. Vrátíš, zda má `a` přijít **před** `b` --
  obvykle porovnáním atributu, podle něhož chceš řadit.
- `sorted` potřebuje jen `<`, takže samotné `__lt__` udělá seznam tvých objektů
  řaditelným.

## Tvůj úkol

Definuj `Temperature` s `__init__(self, degrees)` a **`__lt__`** tak, aby se teploty
porovnávaly podle `degrees`.

## Hotovo, když

- `Temperature(10) < Temperature(20)` je `True`.
- `sorted([Temperature(30), Temperature(10), Temperature(20)])` je seřazeno
  `10, 20, 30` podle stupňů.
- Porovnání používá `degrees`.
""",

"15.7 hints": r"""Přidej do Temperature `__lt__(self, other)`. Python ho volá pro `<` a `sorted`
používá `<`.

---

Vrať porovnání hodnot: `return self.degrees < other.degrees`. Ta jediná metoda
stačí, aby byl seznam řaditelný.

---

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __lt__(self, other):
        return self.degrees < other.degrees
""",

"15.7 reference": r"""**`__lt__(self, other)`** definuje operátor **`<`** pro tvé objekty a `<` je přesně
to, co **`sorted`**, **`min`** a **`max`** používají k řazení věcí. Bez něj porovnání
dvou tvých objektů vyvolá `TypeError`; s ním se seznam z nich řadí přímo.

- Python volá `a.__lt__(b)` pro `a < b`; vrať, zda má `a` přijít **před** `b`,
  obvykle porovnáním atributu, podle něhož řadíš.
- `sorted` potřebuje jen `<`, takže samotné `__lt__` udělá objekty řaditelnými. Úplná
  sada řadicích dunderů je `__lt__`, `__le__`, `__gt__`, `__ge__`.
- `functools.total_ordering` je dekorátor třídy, který doplní zbylé tři z `__lt__` a
  `__eq__`, pokud chceš všechna porovnání.

```python
class Temperature:
    def __init__(self, degrees): self.degrees = degrees
    def __lt__(self, other): return self.degrees < other.degrees

sorted([Temperature(30), Temperature(10), Temperature(20)])   # 10, 20, 30
min([Temperature(30), Temperature(10)]).degrees               # 10
```
""",

"15.8 brief": r"""# 15.8 -- Závěrečná: hierarchie tvarů

## Koncept

Stáhni kapitolu do jedné malé hierarchie. Základní `Shape` drží jméno a umí se
popsat; `Rectangle` z něj dědí, přidá velikost, spočítá svůj obsah jako property a
porovnává se s jinými obdélníky podle obsahu.

```python
class Shape:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return "%s with area %d" % (self.name, self.area)   # uses the property

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
    def __eq__(self, other):
        return self.area == other.area
    def __lt__(self, other):
        return self.area < other.area
```

Všimni si, že `Shape.describe` používá `self.area`, který definuje jen `Rectangle`
-- metoda základu funguje skrz property podtřídy (polymorfismus).

## Tvůj úkol

Postav přesně dvě výše uvedené třídy:

- `Shape.__init__(self, name)` a `describe(self)` -> `"<name> with area <area>"`.
- `Rectangle(Shape)`: `__init__(self, width, height)` nastaví jméno na
  `"rectangle"` přes `super()`, uloží width/height; property `area`; a
  `__eq__` / `__lt__` porovnávající podle `area`.

## Hotovo, když

- `Rectangle(3, 4).area` je `12`; `.name` je `"rectangle"`; `.describe()` je
  `"rectangle with area 12"`; je to `Shape`.
- `Rectangle(2, 6) == Rectangle(3, 4)` je `True` (stejné obsahy).
- `sorted([Rectangle(3, 4), Rectangle(1, 1), Rectangle(2, 5)])` je seřazeno podle
  obsahu (1, 10, 12).
""",

"15.8 hints": r"""Začni se `Shape`: `__init__(self, name)` a `describe` vracející
`"%s with area %d" % (self.name, self.area)`. Odkazuje na `self.area`, který poskytne
podtřída.

---

`Rectangle(Shape)`: v `__init__` zavolej `super().__init__("rectangle")`, ulož
width/height; přidej `@property area` vracející `width * height`; přidej `__eq__` a
`__lt__`, které porovnávají `self.area` s `other.area`.

---

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "%s with area %d" % (self.name, self.area)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area
""",

"15.8 reference": r"""Závěrečná úloha smísí kapitolu do jedné hierarchie, tak, jak se skutečné třídy
staví:

- **Dědičnost** — `Rectangle(Shape)` *je* `Shape`, takže dostane `describe` zadarmo a
  `isinstance(r, Shape)` je pravda.
- **`super()`** — `Rectangle.__init__` volá `super().__init__("rectangle")`, aby
  základ nastavil `self.name`, pak přidá vlastní šířku a výšku.
- **`@property`** — `area` se počítá ze šířky a výšky při každém přístupu, takže
  zůstává správná, když se strana změní.
- **Polymorfismus** — `Shape.describe` čte `self.area`, který definuje jen
  `Rectangle`; metoda základu funguje skrz property podtřídy.
- **Dundery** — `__eq__` a `__lt__` (oba podle obsahu) dělají z obdélníků věci, které
  se porovnávají a řadí jako vestavěné hodnoty, takže `==` a `sorted` prostě fungují.

Dohromady tyto promění prostý objekt na takový, který se chová jako prvotřídní
hodnota: má identitu v hierarchii, odvozená data a smysluplnou rovnost a uspořádání
— odměnu celé kapitoly.

```python
r = Rectangle(3, 4)
r.describe()                              # 'rectangle with area 12'
Rectangle(2, 6) == Rectangle(3, 4)        # True  -- equal areas
sorted([Rectangle(3, 4), Rectangle(1, 1)])   # by area: 1, then 12
```
""",
}
