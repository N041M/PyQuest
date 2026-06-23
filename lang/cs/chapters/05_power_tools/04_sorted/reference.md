**`sorted(items)`** vrátí **nový** seznam s položkami ve vzestupném pořadí a
originál nechá nedotčen.

- Přijímá libovolný iterovatelný objekt a vždy vrací seznam. Čísla se řadí číselně,
  řetězce lexikograficky.
- **`reverse=True`** řadí sestupně. **`key=`** řadí podle odvozené hodnoty:
  `sorted(words, key=len)` řadí podle délky, `sorted(d.items(), key=lambda kv:
  kv[1])` řadí páry slovníku podle hodnoty.
- Metoda seznamu `lst.sort()` řadí **na místě** a vrací `None`; použij `sorted`,
  když chceš nový seznam nebo řadíš něco, co není seznam.

```python
sorted([3, 1, 2])               # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
sorted(words, key=len)          # shortest to longest
```
