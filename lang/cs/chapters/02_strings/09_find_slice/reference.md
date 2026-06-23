**`s.find(sub)`** vrátí index **prvního** výskytu `sub` v `s`, nebo **`-1`**,
pokud se nenajde (nikdy nevyvolá chybu). Ve spojení s řezem vytáhne text kolem
značky.

- Vrácený index je tam, kde `sub` začíná, takže `s[:i]` je část před ním a
  `s[i + len(sub):]` část za ním.
- Před použitím výsledku zkontroluj `-1` — `s.find` vracející `-1` by jinak řezal
  od konce.
- `.index(sub)` dělá totéž, ale při nepřítomnosti **vyvolá** `ValueError`; použij
  `.find`, když je „není přítomno“ běžný případ.

```python
s = "key=value"
i = s.find("=")     # 3
s[:i]               # 'key'
s[i + 1:]           # 'value'
```
