Uma **expressão regular** é um padrão que descreve um conjunto de cadeias de
caracteres; o módulo **`re`** faz a correspondência delas com o texto.
**`re.search(pattern, text)`** percorre a cadeia de caracteres inteira à procura
do **primeiro** local onde o padrão corresponde e devolve um **objeto de
correspondência** (que é verdadeiro em contexto booleano) ou **`None`**.

- Escreve os padrões como **cadeias de caracteres em bruto** — `r"\d"` — para que
  as barras invertidas cheguem ao motor de regex em vez de serem interpretadas
  primeiro pelo Python.
- Classes abreviadas: `\d` um dígito, `\w` um caractere de palavra
  `[A-Za-z0-9_]`, `\s` espaço em branco, e `.` qualquer caractere exceto nova
  linha.
- `re.search` procura **em qualquer lugar** da cadeia de caracteres; `re.match`
  só verifica o início. Como o resultado é um objeto de correspondência ou
  `None`, `re.search(...) is not None` é um teste de pertença limpo.

```python
import re

re.search(r"\d", "abc4")     # <re.Match object; match='4'>
re.search(r"\d", "abc")      # None
bool(re.search(r"\s", "a b"))  # True -- contains whitespace
```
