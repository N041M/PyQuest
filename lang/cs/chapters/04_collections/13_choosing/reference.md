Tři základní kolekce se hodí na různé úlohy — volba té správné dělá kód
jednodušším a rychlejším:

- **list** — **uspořádaná** posloupnost, která se může opakovat. Použij ho k
  uchování každé hodnoty, v pořadí (záznam, fronta položek ke zpracování).
- **set** — neuspořádaná skupina **odlišných** položek s rychlou příslušností.
  Použij ji k zahození duplicit nebo k otázce „viděl jsem to už?“.
- **dict** — mapování z **klíčů na hodnoty**. Použij ho k vyhledání něčeho podle
  jména (počet na slovo, cena na položku).

Ptej se: potřebuji pořadí a opakování (list), jedinečnost a příslušnost (set), nebo
vyhledávání podle klíče (dict)?

```python
order  = ["a", "b", "a"]    # keep all, in order
unique = {"a", "b"}         # distinct only
price  = {"a": 2, "b": 5}   # look up by key
```
