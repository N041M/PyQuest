# 16.2 -- Cart: drž položky a sečti je

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
