# 9.3 -- Stav, který si pamatuje

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
