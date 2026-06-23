**Zpráva o četnosti** je třístupňové souborové potrubí: **přečti** soubor, **sečti**
do slovníku, pak **zapiš** seřazený souhrn.

- Procházej řádky (nebo slova) a počítej pomocí `counts[k] = counts.get(k, 0) + 1`.
- Seřaď výsledek pomocí `sorted(counts.items(), ...)` — podle klíče, nebo podle
  počtu pomocí `key=lambda kv: kv[1]` (přidej `reverse=True` pro nejčastější
  první).
- Zapiš každý pár jako naformátovaný řádek, např. `out.write(f"{word}: {n}\n")`.

Skládá souborové vstupy/výstupy této kapitoly s nástroji slovník a `sorted` z těch
dřívějších.

```python
counts = {}
with open("words.txt") as f:
    for line in f:
        w = line.strip()
        counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as out:
    for w, n in sorted(counts.items()):
        out.write(f"{w}: {n}\n")
```
