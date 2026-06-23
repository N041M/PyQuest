**Znaková třída** `[...]` odpovídá **přesně jednomu** znaku z množiny uvedené
uvnitř. `[aeiou]` odpovídá libovolné jedné samohlásce; `[abc]` odpovídá `a`, `b`
nebo `c`.

- **Rozsah** s pomlčkou pokryje po sobě jdoucí znaky: `[a-z]` libovolné malé
  písmeno, `[0-9]` libovolná číslice, `[A-Za-z0-9]` libovolné písmeno nebo číslice.
  Množiny a rozsahy uvnitř jedné třídy volně kombinuj.
- Úvodní **`^`** neguje: `[^aeiou]` odpovídá libovolnému znaku, který *není*
  samohláska.
- Třída odpovídá **jednomu** znaku; přidej kvantifikátor pro úsek — `[a-z]+` je
  slovo, `[0-9]{4}` přesně čtyři číslice. Uvnitř třídy většina metaznaků ztrácí svůj
  speciální význam (`[.]` je doslovná tečka).

```python
import re

re.findall(r"[aeiou]", "education")   # ['e', 'u', 'a', 'i', 'o']
re.findall(r"[^a-z ]", "a1 b2!")      # ['1', '2', '!']
re.findall(r"[A-Z][a-z]+", "Ada Lovelace")   # ['Ada', 'Lovelace']
```
