# 9.1 -- První třída

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
