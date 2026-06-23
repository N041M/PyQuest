**`re.findall(pattern, text)`** vrátí **seznam každé** nepřekrývající se shody
vzoru, zleva doprava — protějšek „vytáhni je všechny“ k „najdi první“ od
`re.search`.

- **Kvantifikátor** přiměje jeden vzor odpovídat úseku: `\d+` je „jedna nebo více
  číslic“, takže každá shoda je celé číslo, ne jediná číslice. (`+` jedna-či-více,
  `*` nula-či-více, `?` volitelné, `{n}` přesně n.)
- Každá položka ve vráceném seznamu je **nalezený text** (řetězec); žádná shoda dá
  `[]`. Převeď pomocí `int(...)`, když chceš čísla.
- Má-li vzor zachytávací skupiny, `findall` vrátí skupiny místo celé shody; s jednou
  skupinou je to seznam textu té skupiny (viz 12.5).

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
re.findall(r"[a-z]+", "Hi there!")  # ['i', 'there']
[int(n) for n in re.findall(r"\d+", "p1 p22")]   # [1, 22]
```
