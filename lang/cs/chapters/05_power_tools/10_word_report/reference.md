**Zpráva o četnosti slov** skládá nástroje kapitoly do malého potrubí:

1. **`split()`** text na seznam slov;
2. **sečti** je do slovníku `slovo -> počet` pomocí `counts.get(w, 0) + 1`;
3. **`sorted`** na `dict.items()`, abys zprávu seřadil — podle slova, nebo podle
   počtu pomocí `key=lambda kv: kv[1]` (a `reverse=True` pro nejčastější první).

Každý krok je nástroj, který jsi potkal; dovednost je vidět, že skutečná úloha je
jejich složením.

```python
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
for word, n in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
    print(word, n)        # most frequent first
```
