Uma **classe de caracteres** `[...]` corresponde a **exatamente um** caractere
do conjunto listado dentro dela. `[aeiou]` corresponde a uma única vogal;
`[abc]` corresponde a `a`, `b`, ou `c`.

- Um **intervalo** com um hífen cobre caracteres consecutivos: `[a-z]` qualquer
  letra minúscula, `[0-9]` qualquer dígito, `[A-Za-z0-9]` qualquer letra ou
  dígito. Combina conjuntos e intervalos livremente dentro de uma classe.
- Um **`^`** inicial nega: `[^aeiou]` corresponde a qualquer caractere que *não*
  seja uma vogal.
- A classe corresponde a **um** caractere; adiciona um quantificador para uma
  sequência — `[a-z]+` é uma palavra, `[0-9]{4}` exatamente quatro dígitos.
  Dentro de uma classe, a maioria dos metacaracteres perde o seu significado
  especial (`[.]` é um ponto literal).

```python
import re

re.findall(r"[aeiou]", "education")   # ['e', 'u', 'a', 'i', 'o']
re.findall(r"[^a-z ]", "a1 b2!")      # ['1', '2', '!']
re.findall(r"[A-Z][a-z]+", "Ada Lovelace")   # ['Ada', 'Lovelace']
```
