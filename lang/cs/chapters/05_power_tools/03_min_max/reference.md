**`min(items)`** a **`max(items)`** vrátí nejmenší a největší položku neprázdné
kolekce.

- Porovnávají pomocí `<`/`>`, takže fungují na číslech i na řetězcích (které se
  porovnávají lexikograficky).
- Zavolané na **prázdném** iterovatelném objektu vyvolají `ValueError`; předej
  `default=`, abys dodal náhradní hodnotu.
- Funkce `key=` řadí podle odvozené hodnoty místo podle samotné položky:
  `max(words, key=len)` vrátí **nejdelší** slovo.

```python
min([3, 1, 4])             # 1
max("apple", "pear")       # 'pear'
max(words, key=len)        # the longest word
```
