Režim **`"a"`** otevře soubor pro **připojení**: zápisy jdou na **konec** a
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
