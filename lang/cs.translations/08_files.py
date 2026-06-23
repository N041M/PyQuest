# PyQuest translations -- language 'cs' -- chapter 08_files -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"8.1 brief": r"""# 8.1 -- Otevření souboru

## Koncept

Dosud každá hodnota pocházela z literálu, který jsi napsal, nebo z `input()`.
Skutečné programy také čtou **soubory** -- text, který už leží na disku.

`open(name)` ti podá *objekt souboru*. Čistý způsob, jak ho použít, je blok `with`:

```python
with open("note.txt") as f:
    text = f.read()
```

- `with open(...) as f:` soubor otevře a naváže ho na `f`;
- `f.read()` vrátí **celý obsah** souboru jako jeden řetězec;
- když blok skončí, Python **soubor za tebe zavře** -- i když kód uvnitř vyvolal
  chybu. To automatické zavření je celý důvod, proč dát `with` přednost před holým
  `open()`.

Soubor se hledá relativně k tomu, kde program běží, takže `"note.txt"` znamená
„soubor jménem note.txt vedle mě“.

## Příklad

Pokud `note.txt` obsahuje:

```
buy milk
call sam
```

pak `text` je řetězec `"buy milk\ncall sam\n"` -- včetně zalomení řádků.

## Tvůj úkol

Vedle tvého programu leží soubor jménem `note.txt`. Přečti jeho celý obsah a vypiš
ho.

## Hotovo, když

- Program vypíše přesně to, co `note.txt` obsahuje.
- Funguje, ať soubor drží cokoli -- jeden řádek, mnoho řádků, nebo nic.
- Soubor jsi otevřel příkazem `with`.
""",

"8.1 hints": r"""Blok `with open(name) as f:` ti dá soubor jako `f`. Uvnitř něj požádej soubor o
vše, co drží.

---

`f.read()` vrátí celý soubor jako jeden řetězec. Ulož ho, pak ho vypiš po (nebo
uvnitř) bloku.

---

with open("note.txt") as f:
    text = f.read()
print(text)
""",

"8.1 reference": r"""**`open(name)`** se připojí k souboru na disku; příkaz **`with`** ho spravuje tak,
že se soubor **automaticky zavře**, když blok skončí, i kdyby nastala chyba. Uvnitř
bloku poskytuje obsah objekt souboru `f`.

- `with open(name) as f:` otevře pro **čtení** textu (výchozí režim `"r"`) a naváže
  otevřený soubor na `f`.
- **`f.read()`** vrátí celý obsah jako jeden řetězec. (`f.read(n)` přečte nejvýše
  `n` znaků.)
- Otevření cesty, která neexistuje, vyvolá `FileNotFoundError`. Vždy používej
  `with` místo holého `open` — zaručí zavření.

```python
with open("notes.txt") as f:
    text = f.read()      # whole file as a string
# file is closed here
```
""",

"8.2 brief": r"""# 8.2 -- Soubor řádek po řádku

## Koncept

`f.read()` ti dá vše najednou. Častěji chceš soubor **po jednom řádku** -- a objekt
souboru je *iterovatelný*, takže cyklus `for` jeho řádky projde za tebe:

```python
with open("tasks.txt") as f:
    for line in f:
        ...
```

Jeden háček: každý `line` stále nese zalomení řádku, které ho ukončilo -- `"wash\n"`,
ne `"wash"`. Ořízni ho pomocí `line.strip()` (3.7), než text použiješ, jinak ti
výstup naroste o prázdné řádky.

## Příklad

Pro `tasks.txt` ve tvaru:

```
wash
cook
sleep
```

dá očíslování každého řádku:

```
1. wash
2. cook
3. sleep
```

`enumerate` (5.5) se přirozeně hodí -- začni od `1`:

```python
for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")
```

## Tvůj úkol

Přečti `tasks.txt` a vypiš každý řádek **číslovaný od 1**, ve tvaru `1. wash`. Zahoď
koncové zalomení řádku, aby nevznikly zbloudilé prázdné řádky.

## Hotovo, když

- Každý řádek se vypíše jako `<číslo>. <text>`, počínaje od 1.
- Funguje to pro soubor libovolné délky.
- Soubor jsi otevřel pomocí `with` a procházel ho pomocí `for`.
""",

"8.2 hints": r"""Objekt souboru je iterovatelný: `for line in f:` ti podá jeden řádek na průchod.

---

`enumerate(f, start=1)` dá `(1, prvnířádek), (2, druhýřádek), ...`. Každý řádek
stále končí na `\n` -- použij `line.strip()`, abys ho zahodil.

---

with open("tasks.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")
""",

"8.2 reference": r"""Objekt souboru je **iterovatelný**: procházení po něm vydá soubor **po jednom
řádku**, aniž by se celý načetl do paměti. To je standardní způsob zpracování
souboru řádek po řádku.

- `for line in f:` naváže `line` na každý řádek **včetně koncového zalomení**
  `"\n"`; zavolej `line.strip()` (nebo `.rstrip("\n")`), abys ho zahodil.
- Čte líně, takže pohodlně zvládá velké soubory.
- `f.readlines()` místo toho vrátí **seznam** všech řádků najednou — vhodné pro
  malé soubory, plýtvavé pro velké.

```python
with open("log.txt") as f:
    for line in f:
        print(line.strip())   # one line per pass, newline removed
```
""",

"8.3 brief": r"""# 8.3 -- Sčítání souboru

## Koncept

Soubor je vždy **text**. Řádek, který vypadá jako `42`, dorazí jako řetězec
`"42\n"`, ne jako číslo 42 -- takže než můžeš počítat, musíš ho převést pomocí
`int()` (1.11), přesně jako jsi to dělal s `input()`.

`int()` rád ignoruje okolní bílé znaky, takže `int("42\n")` je `42` -- ani nemusíš
nejdřív ořezávat.

```python
total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
```

## Příklad

Pro `prices.txt` ve tvaru:

```
10
25
7
```

je součet `42`.

## Tvůj úkol

`prices.txt` drží jedno celé číslo na řádek. Přečti je, všechna je sečti a vypiš
součet.

## Hotovo, když

- Program vypíše součet každého čísla v souboru.
- Záporná čísla i jednořádkový soubor fungují.
- Soubor jsi otevřel pomocí `with` a každý řádek převedl pomocí `int()`.
""",

"8.3 hints": r"""Začni průběžný součet na 0, otevři soubor a procházej jeho řádky.

---

Každý řádek je řetězec jako `"25\n"`. `int(line)` z něj udělá číslo, které můžeš
přičíst. Po cyklu vypiš součet.

---

total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
print(total)
""",

"8.3 reference": r"""Obsah souboru je vždy **text**, takže řádek jako `"42\n"` je *řetězec*. Abys mohl
počítat, musíš každý řádek nejprve převést na číslo.

- `int(line)` rozparsuje celé číslo; toleruje okolní bílé znaky (včetně koncového
  zalomení), takže `int("42\n")` je `42`. Pro desetinná použij `float(line)`.
- Prázdný nebo nečíselný řádek vyvolá `ValueError` — přeskoč prázdné
  (`if not line.strip(): continue`) nebo obal převod do `try`.
- Akumuluj průběžně: drž průběžný součet a přičítej každou rozparsovanou hodnotu.

```python
total = 0
with open("nums.txt") as f:
    for line in f:
        total += int(line)    # text -> number, then add
```
""",

"8.4 brief": r"""# 8.4 -- Zápis souboru

## Koncept

Čtení je polovina příběhu; programy také **vytvářejí** soubory. Otevři v režimu
`"w"` (pro *write*, zápis) a zavolej `.write()`:

```python
with open("out.txt", "w") as f:
    f.write("hello\n")
```

Dvě věci, které je dobré vědět:

- `"w"` vytvoří úplně nový soubor (nebo existující **vyprázdní**) a pak zapisuje.
- `.write()` položí **přesně** ten text, který mu dáš -- žádné automatické zalomení
  řádku, jaké přidává `print()`. Chceš-li zalomení řádků, zahrň `"\n"` sám.

Častý tvar je **přečti jeden soubor, zapiš jiný**:

```python
with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
```

## Příklad

Pokud `in.txt` obsahuje `quiet please`, pak `out.txt` má nakonec držet
`QUIET PLEASE`.

## Tvůj úkol

Přečti `in.txt` a zapiš jeho obsah **velkými písmeny** (`.upper()` z 2.7) do nového
souboru jménem `out.txt`.

## Hotovo, když

- `out.txt` obsahuje přesně text z `in.txt`, velkými písmeny.
- Prázdný `in.txt` vyprodukuje prázdný `out.txt` -- žádný pád.
- Použil jsi `with` a otevřel `out.txt` v režimu `"w"`.
""",

"8.4 hints": r"""Dva kroky: nejprve načti in.txt do řetězce, pak otevři out.txt v režimu `"w"` a
zapiš řetězec velkými písmeny.

---

`open("out.txt", "w")` je polovina pro zápis; `text.upper()` udělá velká písmena.
`.write()` zapíše řetězec tak, jak je.

---

with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
""",

"8.4 reference": r"""Otevření v režimu **`"w"`** otevře soubor pro **zápis**. Soubor **vytvoří**, pokud
chybí, a **zkrátí** ho (vyprázdní), pokud už existuje, takže stávající obsah se
ztratí.

- **`f.write(text)`** zapíše řetězec a, na rozdíl od `print`, **nepřidá** žádné
  koncové zalomení — zahrň `"\n"` sám tam, kde chceš zalomení řádků.
- `f.write` bere jen řetězce; čísla nejprve převeď pomocí `str()` nebo f-řetězce.
- Použij `with`, aby se data vyprázdnila do souboru a soubor se správně zavřel.

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")   # newlines are explicit
```
""",

"8.5 brief": r"""# 8.5 -- Připojuj, nepřepisuj

## Koncept

Režim `"w"` je nemilosrdný: před zápisem soubor **vyprázdní**. To je špatně, když
chceš do souboru *přidávat* -- třeba log, který stále rozšiřuješ. Na to existuje
režim `"a"` (pro *append*, připojení):

```python
with open("log.txt", "a") as f:
    f.write("another line\n")
```

`"a"` nechá vše, co už v souboru je, nedotčené a tvůj nový text zapíše **za** něj (a
pokud soubor ještě neexistuje, `"a"` ho prostě vytvoří). Stejné `.write()`, stejná
potřeba přidat vlastní `"\n"` -- mění se jen písmeno režimu, a to jedno písmeno je
celý rozdíl mezi „přidat k“ a „smazat a nahradit“. Celý smysl `"a"` je, že soubor
*nečteš* nejdřív -- prostě zapisuješ na konec.

## Příklad

Pokud `log.txt` už obsahuje:

```
woke up
ate
```

pak připojení řádku `ran` ho nechá držet `woke up`, `ate`, `ran` -- všechny tři, v
pořadí.

## Tvůj úkol

Soubor `log.txt` už existuje. Přečti jeden řádek textu ze vstupu (`input()`) a
**připoj** ho do `log.txt` jako nový řádek, přičemž zachovej vše, co tam už je.

## Hotovo, když

- Původní obsah `log.txt` je stále přítomen, v pořadí.
- Nový záznam je přidán jako vlastní řádek na konci.
- Použití `"w"` by smazalo staré řádky -- takže musíš použít `"a"`.
""",

"8.5 hints": r"""Přečti záznam pomocí `input()`, pak otevři soubor v režimu, který *zachová* to, co
už tam je.

---

Režim `"a"` připojuje místo mazání. Nezapomeň na `"\n"`, aby nový záznam seděl na
vlastním řádku.

---

entry = input()
with open("log.txt", "a") as f:
    f.write(entry + "\n")
""",

"8.5 reference": r"""Režim **`"a"`** otevře soubor pro **připojení**: zápisy jdou na **konec** a
jakýkoli stávající obsah se zachová. Je to nedestruktivní protějšek `"w"`.

- `"a"` soubor vytvoří, pokud neexistuje; pokud existuje, `f.write` přidá za to, co
  už tam je — nic se nepřepíše.
- `"w"` soubor nejdřív vyprázdní; sáhni po `"a"`, abys rozšiřoval log nebo
  akumuloval výsledky napříč spuštěními.
- Stejně jako u `"w"` se zalomení řádků nepřidávají za tebe.

```python
with open("log.txt", "a") as f:
    f.write("another entry\n")   # added at the end, old lines kept
```
""",

"8.6 brief": r"""# 8.6 -- Filtrování řádků do nového souboru

## Koncept

Spoj čtení a zápis a dostaneš každodenní datovou rutinu: projdi vstupní soubor řádek
po řádku, **rozhodni**, které řádky ponechat (`if`, 3.2), a zapiš jen ty do
výstupního souboru.

```python
with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if keep(line):
            f.write(line)
```

`f.readlines()` přečte celý soubor do seznamu řádků předem -- hodí se, když chceš
dočíst, než začneš zapisovat.

Řádek, který je prázdný nebo jen mezery, je „prázdný“: `line.strip()` pro něj vrátí
`""`, a prázdný řetězec je nepravdivý (3.1), takže `if line.strip():` je úhledný
test na „tento řádek má skutečný obsah“.

## Příklad

Z `lines.txt` ve tvaru:

```
keep me

and me
```

se prázdný prostřední řádek zahodí a zůstanou `keep me` a `and me`.

## Tvůj úkol

Přečti `lines.txt` a zapiš jen jeho **neprázdné** řádky do `kept.txt`, ve stejném
pořadí. Zahoď každý řádek, který je prázdný nebo jen bílé znaky.

## Hotovo, když

- `kept.txt` drží přesně neprázdné řádky z `lines.txt`, v pořadí.
- Soubor bez prázdných řádků se zkopíruje beze změny; soubor jen z prázdných řádků
  dá prázdný `kept.txt`.
- Použil jsi `with`, cyklus a `if`, abys rozhodl, co ponechat.
""",

"8.6 hints": r"""Nejprve přečti všechny řádky, pak otevři výstupní soubor v režimu `"w"` a procházej,
přičemž zapisuj jen ty, které chceš ponechat.

---

`if line.strip():` je pravda jen tehdy, když má řádek skutečný obsah. Zapiš původní
`line` (už končí na `\n`), ne oříznutou kopii.

---

with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)
""",

"8.6 reference": r"""**Filtrovací** průchod přečte jeden soubor, ponechá jen řádky, které přijme `if`,
a zapíše je do jiného — souborová podoba vzoru komprehenze-s-`if`.

- Otevři zdroj pro čtení a cíl pro zápis, projdi zdroj a `f_out.write(line)` jen
  tehdy, když řádek projde tvým testem.
- Řádky ze vstupu si ponechají zalomení, takže jejich zpětný zápis reprodukuje
  zalomení řádků, aniž by nějaké přidal.
- Číst a zapisovat **tutéž** cestu najednou je nebezpečné; zapisuj do nového
  souboru (nebo posbírej výsledky a pak zapiš).

```python
with open("all.txt") as src, open("kept.txt", "w") as out:
    for line in src:
        if "ERROR" in line:
            out.write(line)       # keep only matching lines
```
""",

"8.7 brief": r"""# 8.7 -- Zpráva o četnosti

## Koncept

Tato úloha spojuje kapitolu se slovníkovým sčítáním z 5.9: přečti soubor, **spočítej**
v něm něco a výsledek zapiš do jiného souboru.

Načti slova, pak je sečti slovníkem (vzor `dict.get`):

```python
with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

`f.read().split()` přečte celý soubor a rozdělí podle libovolných bílých znaků,
takže ti podá plochý seznam slov, ať byla rozmístěna jakkoli.

Pak zapiš zprávu, **seřazenou podle počtu, nejvyšší první**, shody řešené abecedně.
`sorted` s `key` (5.4) udělá obojí najednou:

```python
for w in sorted(counts, key=lambda w: (-counts[w], w)):
    f.write(f"{w}: {counts[w]}\n")
```

Klíč `(-counts[w], w)` řadí podle sestupného počtu (znegovaného) a pak podle
samotného slova u shod.

## Příklad

`words.txt` ve tvaru `fig fig pear fig pear` se stane `report.txt` ve tvaru:

```
fig: 3
pear: 2
```

## Tvůj úkol

Spočítej, jak často se každé slovo objeví ve `words.txt`, a zapiš `report.txt` s
jedním řádkem `slovo: počet` na každé odlišné slovo -- seřazeným podle počtu
(nejvyšší první), shody v abecedním pořadí.

## Hotovo, když

- Každé odlišné slovo se objeví jednou, jako `slovo: počet`.
- Řádky jsou seřazeny podle sestupného počtu, abecedně v rámci shody.
- Použil jsi `with`, slovník ke sčítání a přečetl slova ze souboru.
""",

"8.7 hints": r"""Načti slova do seznamu, pak sestav slovník počtů vzorem
`counts[w] = counts.get(w, 0) + 1` z 5.9.

---

K seřazení zprávy seřaď klíče slovníku s klíčovou funkcí:
`sorted(counts, key=lambda w: (-counts[w], w))` dá nejvyšší počet první, abecedně
v rámci shod. Zapiš každé `f"{w}: {counts[w]}\n"`.

---

with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as f:
    for w in sorted(counts, key=lambda w: (-counts[w], w)):
        f.write(f"{w}: {counts[w]}\n")
""",

"8.7 reference": r"""**Zpráva o četnosti** je třístupňové souborové potrubí: **přečti** soubor, **sečti**
do slovníku, pak **zapiš** seřazený souhrn.

- Procházej řádky (nebo slova) a počítej pomocí `counts[k] = counts.get(k, 0) + 1`.
- Seřaď výsledek pomocí `sorted(counts.items(), ...)` — podle klíče, nebo podle
  počtu pomocí `key=lambda kv: kv[1]` (přidej `reverse=True` pro nejčastější
  první).
- Zapiš každý pár jako naformátovaný řádek, např. `out.write(f"{word}: {n}\n")`.

Skládá souborové vstupy/výstupy této kapitoly s nástroji slovník a `sorted` z těch
dřívějších.

```python
counts = {}
with open("words.txt") as f:
    for line in f:
        w = line.strip()
        counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as out:
    for w, n in sorted(counts.items()):
        out.write(f"{w}: {n}\n")
```
""",

"8.8 brief": r"""# 8.8 -- Závěrečná: žebříčková zpráva

## Koncept

Tato závěrečná úloha je skutečný malý program: přečti soubor záznamů, seřaď je podle
pořadí a zapiš naformátovanou zprávu -- s použitím split (4.4), rozbalování (4.7),
`int()` (1.11), `sorted` s klíčem (5.4), f-řetězců (2.10) a souborů (tato kapitola)
dohromady.

`scores.txt` má jeden záznam na řádek, jméno a skóre oddělené mezerou:

```
alice 40
bob 25
cara 40
```

Každý řádek se rozdělí na svá dvě pole:

```python
name, score = line.split()
score = int(score)
```

Chceš, aby `ranking.txt` vypsal hráče od nejvyššího skóre po nejnižší (shody v
abecedním pořadí), pak závěrečný řádek se součtem:

```
alice - 40
cara - 40
bob - 25
Total: 105
```

Všimni si přesného formátu: `jméno - skóre` na hráče (mezery kolem pomlčky) a
závěrečný řádek `Total: <součet>`.

## Tvůj úkol

Přečti `scores.txt` a zapiš `ranking.txt` s jedním řádkem `jméno - skóre` na hráče
seřazeným podle skóre (nejvyšší první, shody abecedně), následovaným závěrečným
řádkem `Total: <součet všech skóre>`.

## Hotovo, když

- Hráči jsou vypsáni `jméno - skóre`, nejvyšší skóre první, shody abecedně.
- Poslední řádek je `Total: ` následované součtem každého skóre.
- Jednohráčový soubor funguje a pro oba soubory jsi použil `with`.
""",

"8.8 hints": r"""Přečti řádky a pro každý `name, score = line.split()`; skóre převeď pomocí `int()`.
Posbírej dvojice do seznamu.

---

Seřaď s `key=lambda p: (-p[1], p[0])` pro nejvyšší skóre první, shody abecedně.
Zapiš každé `f"{name} - {score}\n"`, pak závěrečné `f"Total: {součet_skóre}\n"`.

---

with open("scores.txt") as f:
    lines = f.read().splitlines()
players = []
for line in lines:
    name, score = line.split()
    players.append((name, int(score)))
players.sort(key=lambda p: (-p[1], p[0]))
total = sum(score for name, score in players)
with open("ranking.txt", "w") as f:
    for name, score in players:
        f.write(f"{name} - {score}\n")
    f.write(f"Total: {total}\n")
""",

"8.8 reference": r"""Závěrečná úloha čte **záznamy**, každý rozparsuje na použitelná pole, seřadí je a
zapíše **naformátovanou zprávu** — podobu skutečné datové práce.

- **Parsuj**: rozděl každý řádek na pole a převeď typy (např.
  `name, score = line.split(","); score = int(score)`), přičemž záznamy sbíráš do
  seznamu.
- **Seřaď**: `sorted(records, key=..., reverse=True)` seřadí podle pole, na kterém
  záleží.
- **Naformátuj**: zapiš zarovnané, čitelné řádky pomocí šířek polí f-řetězce
  (`f"{name:<12}{score:>5}"`), aby sloupce lícovaly.

```python
records = []
with open("scores.csv") as f:
    for line in f:
        name, score = line.strip().split(",")
        records.append((name, int(score)))
with open("ranked.txt", "w") as out:
    for name, score in sorted(records, key=lambda r: r[1], reverse=True):
        out.write(f"{name:<12}{score:>5}\n")
```
""",
}
