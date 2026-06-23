# PyQuest translations -- language 'cs' -- chapter 16_project_cart -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"16.1 brief": r"""# 16.1 -- Item: věc s cenou

## Projekt: Nákupní košík

Tato kapitola je **projekt**. Ve čtyřech krocích postavíš malý nákupní košík a pak ho
s malou pomocí poskládáš. Lekce máš teď za sebou -- tady je dáš do práce.

## Krok 1

Každý obchod potřebuje **položky**. Postav třídu `Item`.

- `__init__(self, name, price)` uloží jméno a cenu.
- `label(self)` vrátí položku jako řetězec `"name: $price"`, s cenou na **dvě
  desetinná místa** -- např. `"Apple: $1.50"`.

## Hotovo, když

- `Item("Apple", 1.5).name` je `"Apple"` a `.price` je `1.5`.
- `Item("Apple", 1.5).label()` je `"Apple: $1.50"`.
- `Item("Bread", 2).label()` je `"Bread: $2.00"`.
""",

"16.1 hints": r"""Ulož `name` a `price` v `__init__`, pak napiš `label`, aby vrátil naformátovaný
řetězec.

---

f-řetězec s formátovacím předpisem zvládne dvě desetinná místa:
`f"{self.name}: ${self.price:.2f}"`.
""",

"16.2 brief": r"""# 16.2 -- Cart: drž položky a sečti je

## Krok 2

Teď samotný **košík**. Postav třídu `Cart`, která sbírá položky podle jména a ceny a
sčítá účet.

- `__init__(self)` začne prázdný košík.
- `add(self, name, price)` přidá jednu položku do košíku.
- `total(self)` vrátí součet všech cen (0 pro prázdný košík).

## Hotovo, když

- Nový `Cart()` má `total()` `0`.
- Po `add("Apple", 1.5)` a `add("Bread", 2.0)` je `total()` `3.5`.
- `add` lze zavolat libovolněkrát před `total`.
""",

"16.2 hints": r"""Drž na košíku seznam (`self.items = []` v `__init__`); `add` do něj přidává.

---

`total` sečte ceny -- `sum(price for name, price in self.items)`, pokud ukládáš
dvojice `(name, price)`.
""",

"16.3 brief": r"""# 16.3 -- Ladění: sleva je špatně

## Krok 3 -- oprav chybu

Tentokrát je kód **už napsaný** -- a má chybu. `Cart` s metodou
`discounted_total(percent)` má z celku strhnout `percent` **procent**. Zákazníci ale
hlásí, že sleva je nehorázně příliš velká: 10% kupón na košík za \$50 účtuje \$40
místo \$45.

Otevři pracovní soubor, přečti `discounted_total`, zjisti, co vlastně dělá, a oprav
to. Zbytek třídy nech být.

## Hotovo, když

- `discounted_total(0)` se rovná plnému `total()` (žádná sleva).
- 10% sleva na košík za \$50 dá `45.0`, ne `40.0`.
- Pro libovolný celek `t` a procento `p` je `discounted_total(p)` rovno
  `t * (1 - p/100)`.
""",

"16.3 hints": r"""Procentuální sleva celek škáluje -- neodečítá pevnou částku. Ponechat `p`% ze `100%`
znamená násobit `(1 - p/100)`.
""",

"16.4 brief": r"""# 16.4 -- Závěrečná: vypiš účtenku

## Krok 4 -- závěr, sám

Tentokrát žádný návod. Poskládej díly dohromady.

Napiš funkci `receipt(items)`, kde `items` je seznam dvojic `(name, price)`. Vrátí
víceřádkový řetězec: **jeden řádek na položku** ve tvaru `"name: $price"` (dvě
desetinná místa), pak závěrečný řádek **`"TOTAL: $<total>"`**.

Pro `receipt([("Apple", 1.5), ("Bread", 2.0)])`:

```
Apple: $1.50
Bread: $2.00
TOTAL: $3.50
```

## Hotovo, když

- Každá položka je vlastní řádek, naformátovaný `"name: $price"` na dvě desetinná
  místa.
- Poslední řádek je `"TOTAL: $<součet cen>"`, také na dvě desetinná místa.
- Prázdný seznam vrátí jen `"TOTAL: $0.00"`.
""",
}
