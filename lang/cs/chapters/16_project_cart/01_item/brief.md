# 16.1 -- Item: věc s cenou

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
