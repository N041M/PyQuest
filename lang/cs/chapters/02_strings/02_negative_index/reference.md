**Záporný** index počítá od konce řetězce: `s[-1]` je poslední znak, `s[-2]`
předposlední a tak dále. Ušetří psaní `s[len(s) - 1]`.

- `s[-1]` a `s[len(s) - 1]` pojmenovávají stejný znak; záporný tvar jen
  nepotřebuje délku.
- Platný záporný rozsah je `-1` až `-len(s)`; jít dál (např. `s[-99]` u krátkého
  řetězce) vyvolá `IndexError`.
- `s[0]` je první znak; žádné `-0` neexistuje (to je prostě `0`).

```python
word = "Python"
word[-1]   # 'n'
word[-2]   # 'o'
```
