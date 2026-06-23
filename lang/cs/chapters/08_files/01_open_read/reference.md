**`open(name)`** se připojí k souboru na disku; příkaz **`with`** ho spravuje tak,
že se soubor **automaticky zavře**, když blok skončí, i kdyby nastala chyba. Uvnitř
bloku poskytuje obsah objekt souboru `f`.

- `with open(name) as f:` otevře pro **čtení** textu (výchozí režim `"r"`) a naváže
  otevřený soubor na `f`.
- **`f.read()`** vrátí celý obsah jako jeden řetězec. (`f.read(n)` přečte nejvýše
  `n` znaků.)
- Otevření cesty, která neexistuje, vyvolá `FileNotFoundError`. Vždy používej
  `with` místo holého `open` — zaručí zavření.

```python
with open("notes.txt") as f:
    text = f.read()      # whole file as a string
# file is closed here
```
