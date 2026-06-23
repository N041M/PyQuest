# 7.4 -- IndexError a bezpečný přístup

## Koncept

Indexování za konec seznamu vyvolá `IndexError`:

```python
items = ["a", "b"]
items[5]      # IndexError!
```

„Bezpečné získání“ vrátí náhradní hodnotu místo pádu -- a je to další místo, kde
*zkoušení* poráží *předběžné testování*. Pamatuj, že záporné indexy jsou **platné**
(2.2): `items[-1]` je poslední položka, `items[-2]` ta před ní. Ručně psaná
kontrola mezí musí trefit `0 <= i`... ne počkat, `-len <= i < len`... přesně
správně, ve dvou směrech. Nebo to prostě zkusíš:

```python
try:
    return items[i]
except IndexError:
    return default
```

`except` je správný *z definice* -- vystřelí přesně tehdy, když sám Python řekne,
že je index špatný, záporné včetně.

## Příklad

```python
item_or(["a", "b"], 0, "?")     # "a"
item_or(["a", "b"], -1, "?")    # "b"   -- valid negative index
item_or(["a", "b"], 5, "?")     # "?"   -- out of range, fallback
```

## Tvůj úkol

Definuj `item_or(items, i, default)`, která vrátí `items[i]`, nebo `default`, když
je `i` mimo rozsah -- pomocí `try`/`except IndexError`.

## Hotovo, když

- `item_or(["a", "b"], 1, "?")` je `"b"`; index `5` dá `"?"`.
- `item_or(["a", "b"], -1, "?")` je `"b"` -- záporné, které se vejdou, jsou platné.
- `item_or([], 0, "?")` je `"?"` -- prázdný seznam nemá platný index.
- Použil jsi `try`/`except` -- aritmetika mezí se lekci vyhne a selže.
