Objekt souboru je **iterovatelný**: procházení po něm vydá soubor **po jednom
řádku**, aniž by se celý načetl do paměti. To je standardní způsob zpracování
souboru řádek po řádku.

- `for line in f:` naváže `line` na každý řádek **včetně koncového zalomení**
  `"\n"`; zavolej `line.strip()` (nebo `.rstrip("\n")`), abys ho zahodil.
- Čte líně, takže pohodlně zvládá velké soubory.
- `f.readlines()` místo toho vrátí **seznam** všech řádků najednou — vhodné pro
  malé soubory, plýtvavé pro velké.

```python
with open("log.txt") as f:
    for line in f:
        print(line.strip())   # one line per pass, newline removed
```
