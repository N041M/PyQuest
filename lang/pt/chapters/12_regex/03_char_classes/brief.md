# 12.3 -- Classes de caracteres: [aeiou]

## Conceito

Uma **classe de caracteres** `[...]` corresponde a **qualquer um** dos
caracteres listados dentro dela:

```python
import re

re.findall(r"[aeiou]", "education")     # ['e', 'u', 'a', 'i', 'o']
```

- `[aeiou]` corresponde a uma única vogal; `[abc]` corresponde a `a`, `b`, ou
  `c`.
- Um **intervalo** usa um hífen: `[a-z]` é qualquer letra minúscula, `[0-9]`
  qualquer dígito (o mesmo que `\d`), `[A-Za-z0-9]` qualquer letra ou dígito.
- Um `^` inicial **nega** a classe: `[^aeiou]` é qualquer caractere que *não*
  seja uma vogal.

Uma classe é um caractere; adiciona um quantificador (`[a-z]+`) para
corresponder a uma sequência deles.

## Exemplo

```python
import re

def count_letters(text):
    return len(re.findall(r"[a-z]", text))
```

## A tua tarefa

Usando uma classe de caracteres com **`re.findall`**, define `count_vowels(text)`
que devolve quantas vogais (`a e i o u`) há em `text`.

## Está feito quando

- `count_vowels("education")` devolve `5`, `count_vowels("xyz")` devolve `0`.
- `count_vowels("")` devolve `0`.
- A contagem usa `re.findall` com uma classe `[aeiou]`, não uma verificação
  manual com `in`.
