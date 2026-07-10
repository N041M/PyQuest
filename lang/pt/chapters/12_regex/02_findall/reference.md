**`re.findall(pattern, text)`** devolve uma **lista com todas** as
correspondências sem sobreposição do padrão, da esquerda para a direita — o
equivalente "extrai-as todas" ao "encontra a primeira" do `re.search`.

- Um **quantificador** faz um padrão corresponder a uma sequência: `\d+` é "um ou
  mais dígitos", por isso cada correspondência é um número inteiro em vez de um
  único dígito. (`+` um-ou-mais, `*` zero-ou-mais, `?` opcional, `{n}` exatamente
  n.)
- Cada elemento da lista devolvida é o **texto correspondido** (uma cadeia de
  caracteres); nenhuma correspondência dá `[]`. Converte com `int(...)` quando
  quiseres números.
- Se o padrão tiver grupos de captura, `findall` devolve os grupos em vez da
  correspondência inteira (ver 12.5); com um grupo, é uma lista do texto desse
  grupo.

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
re.findall(r"[a-z]+", "Hi there!")  # ['i', 'there']
[int(n) for n in re.findall(r"\d+", "p1 p22")]   # [1, 22]
```
