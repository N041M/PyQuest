# PyQuest translations -- language 'pt' -- chapter 12_regex -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"12.1 brief": r"""# 12.1 -- re.search: o padrão está lá?

## Conceito

Uma **expressão regular** ("regex") é uma pequena linguagem para descrever padrões
em texto. O módulo **`re`** faz a correspondência com eles. A pergunta mais básica
é "este padrão aparece nalgum lugar?" -- **`re.search`**:

```python
import re

re.search(r"\d", "abc4")     # a match object (truthy)
re.search(r"\d", "abc")      # None
```

- O padrão é escrito como uma **cadeia de caracteres em bruto** `r"..."` para que
  as barras invertidas signifiquem o que o regex espera (`r"\d"`, não `"\d"`).
- `\d` corresponde a qualquer **dígito** único. Outros atalhos: `\w` um caractere
  de palavra, `\s` espaço em branco, `.` qualquer caractere.
- `re.search` devolve um **objeto de correspondência** se o padrão for encontrado
  nalgum lugar, ou **`None`** se não -- por isso `re.search(...) is not None` é
  um sim/não limpo.

## Exemplo

```python
import re

def has_letter(text):
    return re.search(r"[a-z]", text) is not None
```

## A tua tarefa

Usando **`re.search`**, define `has_digit(text)` que devolve `True` se `text`
contiver pelo menos um dígito, `False` caso contrário.

## Está feito quando

- `has_digit("abc4")` é `True`, `has_digit("abc")` é `False`.
- `has_digit("")` é `False`.
- O teste usa `re.search` com `\d`, não uma verificação de dígitos escrita à mão.
""",

"12.1 hints": r"""`import re`, depois `re.search(pattern, text)`. O padrão para um único dígito é
a cadeia de caracteres em bruto `r"\d"`.

---

`re.search` devolve um objeto de correspondência quando encontra o padrão, ou
`None` quando não encontra. Transforma isso num booleano com `is not None`.

---

import re


def has_digit(text):
    return re.search(r"\d", text) is not None
""",

"12.1 reference": r"""Uma **expressão regular** é um padrão que descreve um conjunto de cadeias de
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
""",

"12.2 brief": r"""# 12.2 -- re.findall: todas as correspondências

## Conceito

`re.search` encontra a *primeira* correspondência. **`re.findall`** devolve
**todas** elas, como uma lista de cadeias de caracteres:

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
```

- `\d+` significa "um ou mais dígitos" -- o `+` faz o padrão capturar uma
  sequência inteira de dígitos, não apenas um. Assim, cada correspondência é um
  número completo.
- `re.findall` devolve uma **lista de cadeias de caracteres** (o texto
  correspondido), da esquerda para a direita, sem sobreposição. Nenhuma
  correspondência dá a lista vazia `[]`.
- As correspondências continuam a ser texto; converte com `int(...)` se
  quiseres números.

## Exemplo

```python
import re

def words(text):
    return re.findall(r"[a-z]+", text)
```

## A tua tarefa

Usando **`re.findall`**, define `all_numbers(text)` que devolve uma lista de
cada sequência de dígitos em `text`, como cadeias de caracteres.

## Está feito quando

- `all_numbers("a12b3c456")` devolve `["12", "3", "456"]`.
- `all_numbers("nothing")` devolve `[]`.
- A extração usa `re.findall` com `\d+`, não uma verificação escrita à mão.
""",

"12.2 hints": r"""`import re`, depois `re.findall(pattern, text)` devolve uma lista de todas as
correspondências. Queres sequências de dígitos.

---

O padrão `r"\d+"` corresponde a um ou mais dígitos seguidos, por isso cada
correspondência é um número completo. `re.findall(r"\d+", text)` é a resposta
inteira.

---

import re


def all_numbers(text):
    return re.findall(r"\d+", text)
""",

"12.2 reference": r"""**`re.findall(pattern, text)`** devolve uma **lista com todas** as
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
""",

"12.3 brief": r"""# 12.3 -- Classes de caracteres: [aeiou]

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
""",

"12.3 hints": r"""Uma classe de caracteres entre parênteses retos corresponde a um dos
caracteres listados. Para vogais, isso é `r"[aeiou]"`.

---

`re.findall(r"[aeiou]", text)` dá uma lista de todas as vogais encontradas;
`len(...)` dessa lista é a contagem.

---

import re


def count_vowels(text):
    return len(re.findall(r"[aeiou]", text))
""",

"12.3 reference": r"""Uma **classe de caracteres** `[...]` corresponde a **exatamente um** caractere
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
""",

"12.4 brief": r"""# 12.4 -- Quantificadores: + significa um ou mais

## Conceito

Um **quantificador** diz quantas vezes o padrão anterior pode repetir-se:

- **`+`** -- um ou mais (`[a-z]+` é uma sequência de uma ou mais letras
  minúsculas)
- **`*`** -- zero ou mais
- **`?`** -- opcional (zero ou um)
- **`{n}`** -- exatamente `n`; **`{n,m}`** -- entre `n` e `m`

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")     # ['Hello', 'world']
```

Sem o `+`, `[A-Za-z]` corresponderia a letras únicas, uma de cada vez. O `+`
faz com que capture a **palavra inteira**, parando no primeiro caractere que
não se encaixe (um espaço, vírgula, dígito). É assim que se divide texto em
palavras ignorando a pontuação.

## Exemplo

```python
import re

def integers(text):
    return re.findall(r"\d+", text)
```

## A tua tarefa

Usando **`re.findall`** com um quantificador, define `find_words(text)` que
devolve uma lista das palavras em `text` -- cada uma uma sequência de uma ou
mais letras (`[A-Za-z]+`), ignorando pontuação e espaços.

## Está feito quando

- `find_words("Hello, world!")` devolve `["Hello", "world"]`.
- `find_words("one-two three")` devolve `["one", "two", "three"]`.
- `find_words("")` devolve `[]`.
- As palavras são correspondidas com `[A-Za-z]+`, não divididas à mão.
""",

"12.4 hints": r"""Uma palavra é uma ou mais letras seguidas. A classe de caracteres `[A-Za-z]`
corresponde a uma única letra; o quantificador `+` faz-a corresponder a uma
sequência.

---

`re.findall(r"[A-Za-z]+", text)` devolve todas as palavras, parando cada
correspondência no primeiro caractere que não seja letra. É a função inteira.

---

import re


def find_words(text):
    return re.findall(r"[A-Za-z]+", text)
""",

"12.4 reference": r"""Um **quantificador** controla quantas vezes o padrão imediatamente anterior se
repete:

- **`+`** um ou mais, **`*`** zero ou mais, **`?`** zero ou um (opcional),
- **`{n}`** exatamente *n*, **`{n,m}`** entre *n* e *m*, **`{n,}`** pelo menos
  *n*.

`[A-Za-z]+` corresponde assim a uma **palavra** inteira — uma sequência de uma
ou mais letras — parando no primeiro caractere que não se encaixe, que é como
se tokeniza texto ignorando espaços e pontuação.

- Os quantificadores são **gulosos** por defeito: correspondem ao máximo
  possível. Um `?` final torna um deles **preguiçoso** (`\d+?` corresponde ao
  menor número de dígitos possível).
- O quantificador aplica-se ao único elemento anterior — um caractere, uma
  classe, ou um grupo entre parênteses: `(ab)+` corresponde a `ababab`.

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")   # ['Hello', 'world']
re.findall(r"\d{4}", "y2024 y2025")          # ['2024', '2025']
re.search(r"colou?r", "color")               # matches (the u is optional)
```
""",

"12.5 brief": r"""# 12.5 -- Grupos: captura as partes

## Conceito

Parênteses **`(...)`** num padrão marcam um **grupo de captura**: uma parte da
correspondência que queres extrair. O objeto de correspondência devolve depois
cada um deles:

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.group(1)     # '2026'
m.group(2)     # '06'
m.groups()     # ('2026', '06', '20')
```

- `re.match` corresponde a partir do **início** da cadeia de caracteres e
  devolve um objeto de correspondência (ou `None`).
- `m.group(n)` devolve o texto que o *n*-ésimo grupo capturou (`group(0)` é a
  correspondência inteira); `m.groups()` devolve todos eles como um tuplo.
- O texto capturado continua a ser uma cadeia de caracteres -- `int(m.group(1))`
  se quiseres um número.

Assim, um único padrão verifica o formato e extrai os campos.

## Exemplo

```python
import re

def split_pair(text):
    m = re.match(r"(\w+):(\w+)", text)
    return (m.group(1), m.group(2))
```

## A tua tarefa

Usando **`re.match`** com grupos de captura, define `parse_date(text)` que
recebe uma data como `"2026-06-20"` e devolve o tuplo de **inteiros**
`(year, month, day)`.

## Está feito quando

- `parse_date("2026-06-20")` devolve `(2026, 6, 20)`.
- `parse_date("1999-01-05")` devolve `(1999, 1, 5)`.
- Os campos vêm de grupos de captura, não de `text.split("-")`.
""",

"12.5 hints": r"""Envolve cada parte que queres em parênteses: `r"(\d+)-(\d+)-(\d+)"`. Cada
`(...)` é um grupo de captura.

---

`m = re.match(pattern, text)` e depois lê `m.group(1)`, `m.group(2)`,
`m.group(3)`. São cadeias de caracteres, por isso envolve cada uma em
`int(...)` para o tuplo.

---

import re


def parse_date(text):
    m = re.match(r"(\d+)-(\d+)-(\d+)", text)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
""",

"12.5 reference": r"""Parênteses **`(...)`** num padrão criam um **grupo de captura** — uma
subparte da correspondência que o motor memoriza para que a possas ler depois.
O objeto de correspondência expõe-os:

- **`m.group(n)`** devolve o texto que o *n*-ésimo grupo capturou, numerado da
  esquerda para a direita a partir de 1; **`m.group(0)`** (ou `m.group()`) é a
  correspondência inteira.
- **`m.groups()`** devolve o texto de todos os grupos como um tuplo — ideal
  para desempacotar.
- O texto capturado é uma **cadeia de caracteres**; converte com `int(...)`
  conforme necessário. Um grupo que não participou é `None`.

Assim, um único padrão **valida** o formato e **extrai** os campos. `re.match`
ancora-se no início e devolve o objeto de correspondência ou `None`; protege-te
contra `None` antes de ler os grupos quando a entrada pode não corresponder.
Dá nomes aos grupos com `(?P<name>...)` e lê-os através de `m.group("name")`
para maior clareza.

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.groups()                # ('2026', '06', '20')
tuple(int(p) for p in m.groups())   # (2026, 6, 20)
```
""",

"12.6 brief": r"""# 12.6 -- re.sub: encontrar e substituir por padrão

## Conceito

`str.replace` troca uma subcadeia fixa. **`re.sub`** troca tudo o que
corresponda a um **padrão**:

```python
import re

re.sub(r"\d+", "#", "call 555-1234 now")     # 'call #-# now'
```

- `re.sub(pattern, replacement, text)` devolve uma **nova** cadeia de
  caracteres com **todas** as correspondências de `pattern` substituídas por
  `replacement`.
- Como `\d+` corresponde a uma sequência inteira de dígitos, cada sequência
  reduz-se a um único `#` -- uma substituição por correspondência, não por
  caractere.
- Sem correspondência, o texto fica inalterado. A substituição também pode
  referenciar grupos capturados (`\1`), mas uma cadeia de caracteres simples é
  o caso mais comum.

## Exemplo

```python
import re

def squash_spaces(text):
    return re.sub(r"\s+", " ", text)
```

## A tua tarefa

Usando **`re.sub`**, define `redact(text)` que substitui cada sequência de
dígitos em `text` por um único `"#"`.

## Está feito quando

- `redact("call 555-1234")` devolve `"call #-#"`.
- `redact("no digits")` devolve `"no digits"`.
- Cada *sequência* de dígitos torna-se um `#` (usa `\d+`), através de `re.sub`
  -- não um ciclo de caracteres.
""",

"12.6 hints": r"""`re.sub(pattern, replacement, text)` substitui todas as correspondências. O
teu padrão é uma sequência de dígitos, a tua substituição é `"#"`.

---

`r"\d+"` corresponde a uma sequência inteira de dígitos, por isso cada
sequência torna-se um `#`: `re.sub(r"\d+", "#", text)` é a função inteira.

---

import re


def redact(text):
    return re.sub(r"\d+", "#", text)
""",

"12.6 reference": r"""**`re.sub(pattern, repl, text)`** é uma pesquisa-e-substituição orientada por
padrão: devolve uma **nova** cadeia de caracteres com **todas** as
correspondências sem sobreposição de `pattern` substituídas por `repl`. Onde
`str.replace` troca uma subcadeia fixa, `re.sub` troca tudo o que o padrão
descreve.

- Como um padrão quantificado corresponde a uma **sequência**, cada sequência
  reduz-se a uma substituição: `re.sub(r"\d+", "#", "a12b3")` é `"a#b#"`, não
  `"a##b#"`.
- Sem correspondência, o texto fica inalterado. Um `count=` opcional limita
  quantas substituições são feitas.
- `repl` pode referenciar grupos capturados com `\1`, `\2`, … (por exemplo,
  `re.sub(r"(\w+)@(\w+)", r"\2.\1", s)`), ou ser uma **função** que recebe cada
  correspondência e devolve a sua substituição, para lógica demasiado
  complexa para um modelo.

```python
import re

re.sub(r"\s+", " ", "too   many    spaces")   # 'too many spaces'
re.sub(r"\d+", "#", "call 555-1234")           # 'call #-#'
re.sub(r"(\d+)", r"[\1]", "x12")               # 'x[12]'
```
""",

"12.7 brief": r"""# 12.7 -- Âncoras: corresponder à cadeia de caracteres inteira

## Conceito

`re.search` fica satisfeito se o padrão aparecer **em qualquer lugar**. Para
**validar um formato**, precisas que a *cadeia de caracteres inteira*
corresponda -- sem caracteres sobrantes.

Duas formas de exigir isso:

- **Âncoras** no padrão: `^` prende-se ao **início**, `$` ao **fim**, por isso
  `r"^[A-Z]{2}\d{4}$"` tem de abranger a cadeia de caracteres inteira.
- **`re.fullmatch`**, que exige que o padrão cubra a cadeia de caracteres
  inteira por ti -- sem precisares de âncoras.

```python
import re

re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234")     # matches
re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")    # None -- trailing junk
re.search(r"[A-Z]{2}\d{4}", "AB1234x")       # matches -- search ignores the x
```

Aqui, um código de produto é duas letras maiúsculas seguidas de quatro
dígitos: `AB1234`.

## Exemplo

```python
import re

def is_word(text):
    return re.fullmatch(r"[a-z]+", text) is not None
```

## A tua tarefa

Usando **`re.fullmatch`** (ou `^...$`), define `is_valid_code(text)` que devolve
`True` apenas quando `text` é exatamente **duas letras maiúsculas seguidas de
quatro dígitos** (por exemplo, `"AB1234"`), `False` caso contrário.

## Está feito quando

- `is_valid_code("AB1234")` é `True`.
- `is_valid_code("ab1234")`, `is_valid_code("AB123")`, `is_valid_code("AB1234x")`
  são todos `False`.
- A cadeia de caracteres inteira é correspondida (fullmatch ou âncoras), não
  uma verificação de comprimento escrita à mão.
""",

"12.7 hints": r"""O padrão para o código é `r"[A-Z]{2}\d{4}"` -- duas letras maiúsculas, depois
quatro dígitos. O truque é fazer com que a cadeia de caracteres INTEIRA lhe
corresponda.

---

`re.fullmatch(pattern, text)` exige que o padrão cubra a cadeia de caracteres
inteira, por isso caracteres sobrantes falham. Devolve se encontrou uma
correspondência com `is not None`.

---

import re


def is_valid_code(text):
    return re.fullmatch(r"[A-Z]{2}\d{4}", text) is not None
""",

"12.7 reference": r"""Por defeito, um padrão pode corresponder **em qualquer lugar** da cadeia de
caracteres. Validar um *formato* significa que a cadeia de caracteres
**inteira** tem de estar conforme — sem caracteres sobrantes. Duas formas de
exigir isso:

- **Âncoras** no padrão: **`^`** corresponde ao início da cadeia de
  caracteres, **`$`** ao fim. `r"^[A-Z]{2}\d{4}$"` tem de abranger toda a
  entrada.
- **`re.fullmatch(pattern, text)`** exige que o padrão cubra a cadeia de
  caracteres inteira por ti — sem precisares de âncoras. Devolve um objeto de
  correspondência ou `None`.

O contraste: `re.search(r"[A-Z]{2}\d{4}", "AB1234x")` **corresponde** (o
padrão ocorre), mas `re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")` é **`None`**
(o `x` sobra). Usa `search`/`findall` para *encontrar* subcadeias,
`fullmatch`/âncoras para *validar* um valor inteiro.

```python
import re

bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234"))    # True
bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x"))   # False
bool(re.match(r"^\d{5}$", "12345"))               # True -- anchored form
```
""",

"12.8 brief": r"""# 12.8 -- Capstone: analisar configuração key=value

## Conceito

Está na hora de combinar as ferramentas do capítulo. Quando `re.findall` recebe
um padrão com **vários grupos de captura**, devolve uma lista de **tuplos** --
um por correspondência, com as partes capturadas dentro:

```python
import re

re.findall(r"(\w+)=(\w+)", "host=local port=8080")
# [('host', 'local'), ('port', '8080')]
```

Uma lista de pares `(key, value)` é exatamente o que **`dict(...)`**
transforma num dicionário. Assim, um padrão mais `dict` analisa uma cadeia de
configuração inteira:

```python
dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```

`\w+` corresponde a uma sequência de caracteres de palavra (letras, dígitos,
sublinhado), por isso cada chave e valor é capturado por inteiro, e o `=`
entre eles é correspondido literalmente.

## A tua tarefa

Define `parse_config(text)` que analisa uma cadeia de pares `key=value`
separados por espaços num dicionário, usando **`re.findall`** com dois grupos
de captura.

## Está feito quando

- `parse_config("host=local port=8080")` é igual a
  `{"host": "local", "port": "8080"}`.
- `parse_config("debug=on")` é igual a `{"debug": "on"}`.
- `parse_config("")` é igual a `{}`.
- Os pares são capturados com um único padrão `(\w+)=(\w+)`, não divididos à
  mão.
""",

"12.8 hints": r"""Usa dois grupos de captura, um para a chave e outro para o valor, com um `=`
literal entre eles: `r"(\w+)=(\w+)"`.

---

Com dois grupos, `re.findall(pattern, text)` devolve uma lista de tuplos
`(key, value)`. `dict(...)` dessa lista é o dicionário de configuração.

---

import re


def parse_config(text):
    return dict(re.findall(r"(\w+)=(\w+)", text))
""",

"12.8 reference": r"""O capstone compõe o capítulo: um único padrão com **vários grupos de
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
""",
}

