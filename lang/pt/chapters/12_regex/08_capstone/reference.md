O capstone compõe o capítulo: um único padrão com **vários grupos de
captura**, passado a **`re.findall`**, extrai registos estruturados num só
passo.

- Com mais de um grupo, `re.findall` devolve uma lista de **tuplos** — um por
  correspondência, contendo o texto de cada grupo: `re.findall(r"(\w+)=(\w+)",
  s)` produz `[(key, value), ...]`.
- Uma lista de pares `(key, value)` é exatamente o que **`dict(...)`** consome,
  por isso `dict(re.findall(...))` é um mini-analisador completo.
- `\w+` corresponde a uma sequência de caracteres de palavra (letras, dígitos,
  sublinhado); o `=` entre os grupos é correspondido **literalmente**. Nenhuma
  correspondência dá `[]`, por isso uma entrada vazia produz corretamente `{}`.

Este é o retorno do regex: descreve o formato de um registo, e o motor
encontra e dissecta todas as ocorrências por ti.

```python
import re

dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```
