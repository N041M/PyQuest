# PyQuest translations -- language 'pt' -- chapter 11_standard_library -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"11.1 brief": r"""# 11.1 -- import: trazer um módulo

## Conceito

O Python vem com uma grande **biblioteca padrão**: ferramentas prontas agrupadas em
**módulos**. Não os tens de graça em cada ficheiro -- **importas**
o módulo de que precisas e depois acedes ao seu conteúdo através do seu nome.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
```

- `import math` executa-se uma vez no topo do ficheiro e associa o nome `math` a
  todo o módulo.
- A partir daí, `math.sqrt` é a função de raiz quadrada e `math.pi` a
  constante -- `module.name` acede a tudo o que o módulo disponibiliza.

A vantagem de importar é que alguém já escreveu e testou isto, por isso
chamas `math.sqrt` em vez de deduzires tu próprio uma raiz quadrada.

## Exemplo

```python
import math

def diagonal(side):
    return math.sqrt(2) * side
```

## A tua tarefa

Define `hypotenuse(a, b)` que devolve o comprimento da hipotenusa de um
triângulo retângulo com catetos `a` e `b` -- a raiz quadrada de `a*a + b*b` --
usando **`math.sqrt`** do módulo `math` importado.

## Está feito quando

- `hypotenuse(3, 4)` devolve `5.0`, `hypotenuse(5, 12)` devolve `13.0`.
- `hypotenuse(0, 0)` devolve `0.0`.
- A raiz quadrada vem de `math.sqrt`, através de `import math`.
""",

"11.1 hints": r"""A primeiríssima linha do ficheiro torna o módulo disponível: `import math`. A partir
daí podes usar tudo o que ele fornece como `math.something`.

---

`math.sqrt(x)` devolve a raiz quadrada de `x`. Queres a raiz quadrada de
`a*a + b*b`. Coloca o `import math` no topo e depois escreve a função.

---

import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)
""",

"11.1 reference": r"""Uma instrução **`import`** carrega um **módulo** — um ficheiro de código pronto da
biblioteca padrão — e associa-o a um nome. `import math` torna o objeto do módulo
disponível como `math`, e o seu conteúdo é acedido através dele: `math.sqrt`,
`math.pi`, `math.floor`.

- A instrução executa-se **uma vez**, convencionalmente no **topo** do ficheiro; o
  nome passa então a referir-se a todo o módulo durante o resto do programa.
- **`module.name`** (acesso a atributo) procura uma função ou constante *no*
  módulo, o que mantém os nomes de cada módulo no seu próprio espaço de nomes —
  `math.pi` e o teu próprio `pi` nunca colidem.
- Importar um nome que não existe gera `ModuleNotFoundError`; o código do
  módulo executa-se na primeira vez que é importado e fica depois em cache.
- A biblioteca padrão vem com o Python ("pilhas incluídas"), por isso estes
  módulos não precisam de instalação — apenas do import.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
math.floor(2.7)  # 2
```
""",

"11.2 brief": r"""# 11.2 -- from import: extrair um nome

## Conceito

`import math` traz o módulo *inteiro* e acedes-lhe através de
`math.something`. Muitas vezes só queres uma ferramenta, usada pelo seu nome simples. A
forma **`from ... import ...`** faz isso:

```python
from math import gcd

gcd(12, 18)      # 6  -- called directly, no math. prefix
```

- `from math import gcd` associa o nome único `gcd` ao teu ficheiro.
- Depois chamas-lo como `gcd(...)`, não como `math.gcd(...)`.
- Podes extrair vários de uma vez: `from math import gcd, sqrt, pi`.

`gcd(a, b)` é o **máximo divisor comum** -- o maior inteiro que
divide ambos. É exatamente o que precisas para simplificar uma fração aos
seus termos mais simples: divide o numerador e o denominador pelo seu gcd.

## Exemplo

```python
from math import gcd

def both_divisible_by(a, b):
    return gcd(a, b)
```

## A tua tarefa

Usando **`from math import gcd`**, define `simplify(num, den)` que devolve a
fração `num/den` simplificada aos termos mais simples, como um tuplo `(top, bottom)`: divide
`num` e `den` pelo respetivo `gcd`.

## Está feito quando

- `simplify(6, 8)` devolve `(3, 4)`, `simplify(10, 5)` devolve `(2, 1)`.
- `simplify(7, 7)` devolve `(1, 1)`.
- O gcd vem de `math`, importado com `from math import gcd`.
""",

"11.2 hints": r"""Começa o ficheiro com `from math import gcd`. Agora `gcd` é uma função que podes chamar
diretamente, sem `math.` à frente.

---

Calcula `g = gcd(num, den)`, depois devolve o tuplo `(num // g, den // g)`. Usa `//`
(divisão inteira) para que o resultado fique em números inteiros.

---

from math import gcd


def simplify(num, den):
    g = gcd(num, den)
    return (num // g, den // g)
""",

"11.2 reference": r"""A forma **`from module import name`** associa um nome específico de um módulo
*diretamente* ao teu ficheiro, por isso é chamado sem o prefixo do módulo. `from math
import gcd` torna `gcd` um nome simples; escreves `gcd(12, 18)`, não
`math.gcd(...)`.

- Vários nomes de uma vez: `from math import gcd, sqrt, pi`.
- Só importa o que nomeares — `math.floor` **não** está disponível a menos que
  também importes `floor`. (`import math` traz tudo mas mantém o prefixo; as
  duas formas trocam conveniência por clareza no espaço de nomes.)
- O módulo inteiro continua a executar-se e a ficar em cache; só escolheste
  quais dos seus nomes aterram no teu espaço de nomes. Como o nome chega nu,
  pode **ofuscar** um teu — `from math import e` esconderia uma variável
  chamada `e`.

```python
from math import gcd, sqrt

gcd(12, 18)    # 6
sqrt(16)       # 4.0
```
""",

"11.3 brief": r"""# 11.3 -- import as: renomear à entrada

## Conceito

Às vezes o nome de um módulo é longo, ou entra em conflito com um teu. **`import ... as
...`** traz o módulo sob um nome que **tu** escolhes:

```python
import statistics as stats

stats.mean([1, 2, 3, 4])    # 2.5
```

- `import statistics as stats` associa o módulo a `stats`; `stats.mean` é
  exatamente `statistics.mean`.
- O alias é só uma alcunha local -- o módulo mantém-se inalterado, e só o teu
  ficheiro vê o novo nome.
- É por isso que vais ver aliases convencionais por todo o lado (`import numpy as np`);
  aqui encurtamos `statistics`.

O módulo **`statistics`** faz as médias mais comuns por ti. `stats.mean(nums)`
é a média aritmética -- a soma dividida pela contagem -- sem teres de escrever
`sum(nums) / len(nums)`.

## Exemplo

```python
import statistics as stats

def midpoint(nums):
    return stats.median(nums)
```

## A tua tarefa

Usando **`import statistics as stats`**, define `average(nums)` que devolve a
média da lista `nums`, calculada com `stats.mean`.

## Está feito quando

- `average([2, 4, 6])` devolve `4`, `average([1, 2])` devolve `1.5`.
- `average([5])` devolve `5`.
- A média vem de `statistics.mean`, importado como `stats`.
""",

"11.3 hints": r"""Começa com `import statistics as stats`. A partir daí, `stats` é o teu nome para
o módulo.

---

`stats.mean(nums)` devolve a média da lista. A tua função inteira pode ser
uma única linha que a devolve.

---

import statistics as stats


def average(nums):
    return stats.mean(nums)
""",

"11.3 reference": r"""**`import module as alias`** importa um módulo, mas associa-o a um nome à tua
escolha. `import statistics as stats` torna o módulo disponível como `stats`;
`stats.mean` *é* `statistics.mean` — o alias só muda o nome local, não
o módulo.

- Usa-o para **encurtar** o nome longo de um módulo ou para **evitar um
  conflito** com um teu. Os aliases convencionais que vais encontrar (`import numpy as
  np`) são exatamente isto.
- O mesmo `as` funciona num único nome de um from-import: `from statistics
  import mean as avg`.
- Só o teu ficheiro vê o alias; outros módulos mantêm os seus próprios nomes
  para ele.

```python
import statistics as stats

stats.mean([1, 2, 3, 4])     # 2.5
stats.median([1, 5, 2])      # 2
```
""",

"11.4 brief": r"""# 11.4 -- random: acaso reprodutível

## Conceito

O módulo **`random`** produz valores pseudoaleatórios: `random.randint(1, 6)`
lança um dado, `random.shuffle(lst)` reordena uma lista no próprio local. São *pseudo*-
aleatórios -- calculados a partir de um estado interno -- o que significa que os podes tornar
**repetíveis** fixando esse estado com uma **seed**:

```python
import random

random.seed(42)
random.shuffle(deck)     # always the same order for seed 42
```

- `random.seed(n)` define o ponto de partida. Com a mesma seed, as mesmas
  chamadas produzem os mesmos resultados, em toda a execução, em toda a
  máquina.
- `random.shuffle(lst)` baralha **no próprio local** (devolve `None`), por
  isso baralha uma cópia se precisares de manter o original.

Definir a seed é a forma como um jogo repete um nível, ou como um teste verifica
código "aleatório".

## Exemplo

```python
import random

def pick(options, seed):
    random.seed(seed)
    return random.choice(options)
```

## A tua tarefa

Define `shuffled(items, seed)` que devolve uma lista **nova** com os itens
de `items` baralhados, tornada repetível ao definir a seed com `seed`
**antes** de baralhar. Não alteres o `items` original.

## Está feito quando

- `shuffled(items, seed)` dá o mesmo resultado todas as vezes para os mesmos
  `items` e `seed`.
- A lista original passada fica inalterada (baralha uma cópia).
- `shuffled([], 1)` devolve `[]`.
""",

"11.4 hints": r"""Precisas de três passos: copiar a lista, definir a seed do gerador, baralhar
a cópia. `out = list(items)` faz a cópia para que o original fique seguro.

---

`random.seed(seed)` fixa o ponto de partida; `random.shuffle(out)` reordena
`out` no próprio local (devolve None, por isso não faças `return
random.shuffle(...)`). Devolve `out` a seguir.

---

import random


def shuffled(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out
""",

"11.4 reference": r"""O módulo **`random`** gera valores pseudoaleatórios a partir de um estado
interno: `random.randint(a, b)` (um inteiro em `[a, b]`), `random.choice(seq)`
(um item aleatório), `random.shuffle(lst)` (reordena uma lista **no próprio
local**), `random.random()` (um float em `[0, 1)`).

- Os números são funções determinísticas do estado, por isso
  **`random.seed(n)`** torna-os **repetíveis**: com a mesma seed, as mesmas
  chamadas dão os mesmos resultados em toda a execução e máquina. Define a
  seed uma vez, antes dos sorteios que queres reproduzir.
- `random.shuffle` altera o seu argumento e devolve `None` — baralha uma
  **cópia** (`out = list(items)`) para manter o original, e nunca faças
  `return random.shuffle(...)`.
- O gerador por omissão (sem seed) recebe a seed a partir do sistema
  operativo, por isso, sem uma seed, cada execução é diferente. O `random`
  **não** é para criptografia — usa o módulo `secrets` para tokens e
  palavras-passe.

```python
import random

random.seed(42)
random.randint(1, 6)     # same value every run for seed 42
deck = [1, 2, 3, 4]
random.shuffle(deck)     # deck reordered in place
```
""",

"11.5 brief": r"""# 11.5 -- Counter: contagem num só passo

## Conceito

Lá no capítulo 5 fizeste a contagem à mão: `counts[k] = counts.get(k, 0) + 1`. O
módulo **`collections`** traz esse padrão, já escrito e testado, como
**`Counter`**:

```python
from collections import Counter

Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
```

- `Counter(items)` percorre qualquer iterável e devolve uma contagem de cada
  item distinto.
- Um `Counter` **é** um dict (é uma subclasse), por isso `counts[x]` e
  `for k, v in counts.items()` funcionam exatamente como esperarias -- e é
  igual, na comparação, a um dict simples com as mesmas contagens.
- Até trata da chave em falta: `counts["zzz"]` é `0`, e não um `KeyError`.

É essa a promessa da biblioteca padrão: o ciclo que escreverias já é uma
ferramenta.

## Exemplo

```python
from collections import Counter

def letter_counts(word):
    return Counter(word)
```

## A tua tarefa

Usando **`Counter`** de `collections`, define `tally(items)` que devolve
uma contagem de quantas vezes cada item aparece na lista `items`.

## Está feito quando

- `tally(["a", "b", "a"])` é igual a `{"a": 2, "b": 1}`.
- `tally([])` é igual a `{}`.
- A contagem é feita pelo `Counter`, não por um ciclo escrito à mão.
""",

"11.5 hints": r"""`from collections import Counter` no topo. O `Counter` faz toda a contagem
quando lhe entregas a lista.

---

`Counter(items)` já devolve as contagens, e um Counter é igual, na
comparação, ao dict simples com as mesmas contagens -- por isso podes
devolvê-lo diretamente.

---

from collections import Counter


def tally(items):
    return Counter(items)
""",

"11.5 reference": r"""**`Counter`** (do módulo **`collections`**) é uma subclasse de `dict` que
conta um iterável numa só chamada: `Counter(items)` devolve um mapeamento de
cada item distinto para quantas vezes aparece — o ciclo `counts.get(k, 0) +
1`, já escrito.

- Por ser um dict, suporta tudo o que um dict faz (`c[key]`, `c.items()`,
  `key in c`) e é **igual**, na comparação, a um dict simples com as mesmas
  contagens.
- Uma chave **em falta** lê-se como `0` em vez de gerar `KeyError`, o que é
  ideal para contar.
- **`c.most_common(n)`** devolve os `n` pares `(item, count)` com maior
  contagem, já ordenados — o passo do relatório de graça. Os Counters também
  somam e subtraem (`c1 + c2`) para combinar contagens.

```python
from collections import Counter

c = Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
c["a"]                    # 3
c["z"]                    # 0  -- no KeyError
c.most_common(1)          # [('a', 3)]
```
""",

"11.6 brief": r"""# 11.6 -- defaultdict: um valor por omissão para chaves em falta

## Conceito

Para agrupar itens num dict simples, primeiro tens de verificar se a chave
existe:

```python
if length not in groups:
    groups[length] = []
groups[length].append(word)
```

O **`defaultdict`** remove essa cerimónia. Dás-lhe uma **factory** -- uma
função que cria o valor por omissão -- e ele chama a factory automaticamente
na primeira vez que tocas numa chave em falta:

```python
from collections import defaultdict

groups = defaultdict(list)     # missing key -> a fresh []
groups[5].append("hello")      # no setup needed
```

- `defaultdict(list)` cria uma lista vazia para qualquer chave nova, por
  isso o `.append` funciona sem mais.
- `defaultdict(int)` cria `0` para qualquer chave nova -- uma contagem sem
  `.get`.
- De resto é um dict a sério; converte com `dict(groups)` se quiseres um
  simples.

## Exemplo

```python
from collections import defaultdict

def by_first_letter(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return dict(groups)
```

## A tua tarefa

Usando **`defaultdict`** de `collections`, define `group_by_length(words)`
que devolve um dict que mapeia cada **comprimento** de palavra à lista de
palavras desse comprimento, pela ordem original.

## Está feito quando

- `group_by_length(["hi", "ok", "bye"])` é igual a `{2: ["hi", "ok"], 3: ["bye"]}`.
- `group_by_length([])` é igual a `{}`.
- O agrupamento usa um `defaultdict(list)`, não uma verificação manual "if key in dict".
""",

"11.6 hints": r"""`from collections import defaultdict`, depois `groups = defaultdict(list)`.
O `list` é a factory: cada chave nova começa como uma lista vazia.

---

Percorre as palavras num ciclo; para cada uma, `groups[len(w)].append(w)`.
A chave é o comprimento, o valor é a lista que vai crescendo. Devolve
`dict(groups)` no final.

---

from collections import defaultdict


def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)
""",

"11.6 reference": r"""**`defaultdict`** (de **`collections`**) é um `dict` que fornece
automaticamente um valor por omissão para uma chave em falta. Passas-lhe uma
**factory** — um callable sem argumentos que constrói o valor por omissão —
e, na primeira vez que lês ou tocas numa chave ausente, ele chama a factory,
guarda o resultado e usa-o.

- `defaultdict(list)` cria um `[]` novo para cada chave nova, por isso
  `d[k].append(x)` funciona sem qualquer preparação "if key not in d" — o
  idioma de agrupamento.
- `defaultdict(int)` cria `0` para cada chave nova, por isso `d[k] += 1`
  conta.
- Só a **procura** de uma chave em falta desencadeia a factory; de resto é um
  dict normal. `dict(d)` converte para um dict simples, e uma chave
  *verdadeiramente* em falta continua a ler-se como o valor por omissão em
  vez de gerar um erro.

```python
from collections import defaultdict

groups = defaultdict(list)
groups[5].append("hello")    # key 5 auto-starts as []
groups                       # defaultdict(<class 'list'>, {5: ['hello']})
```
""",

"11.7 brief": r"""# 11.7 -- json: dados como texto

## Conceito

Para guardar dados num ficheiro ou enviá-los pela rede, precisas deles como
**texto**. O **JSON** é o formato de texto quase universal para dados
estruturados, e o módulo **`json`** converte nos dois sentidos:

```python
import json

json.dumps({"name": "Ada", "score": 90})   # '{"name": "Ada", "score": 90}'
json.loads('{"ok": true}')                  # {'ok': True}
```

- `json.dumps(obj)` -- "dump string" -- transforma um dict/list/número/str
  do Python numa **string** JSON.
- `json.loads(text)` -- "load string" -- interpreta uma string JSON de volta
  para valores Python.
- As duas são inversas: `json.loads(json.dumps(x))` devolve `x` de novo.

Repara que a grafia do JSON difere ligeiramente da do Python
(`true`/`false`/`null`), o que é exatamente a razão para deixares o módulo
tratar disso em vez de formatares à mão.

## Exemplo

```python
import json

def parse(text):
    return json.loads(text)
```

## A tua tarefa

Usando **`json.dumps`**, define `to_json(record)` que devolve a string
JSON do dicionário `record`.

## Está feito quando

- `to_json({"a": 1, "b": 2})` devolve `'{"a": 1, "b": 2}'`.
- `to_json({})` devolve `'{}'`.
- A string é produzida por `json.dumps`, não construída à mão.
""",

"11.7 hints": r"""`import json` no topo. A função que queres é `json.dumps`, que recebe um
objeto Python e devolve o seu texto JSON.

---

`json.dumps(record)` faz todo o trabalho. O corpo da função é uma linha
que o devolve.

---

import json


def to_json(record):
    return json.dumps(record)
""",

"11.7 reference": r"""O **JSON** (JavaScript Object Notation) é o formato **texto** padrão para
dados estruturados, e o módulo **`json`** converte valores Python de e para
ele.

- **`json.dumps(obj)`** ("dump string") serializa um `dict`, `list`, `str`,
  número, `bool` ou `None` do Python numa string JSON. As chaves tornam-se
  strings, e o `True`/`False`/`None` do Python é escrito como o
  `true`/`false`/`null` do JSON.
- **`json.loads(text)`** ("load string") interpreta uma string JSON de volta
  para valores Python. As duas são inversas: `json.loads(json.dumps(x)) == x`.
- `dumps` aceita opções — `indent=2` formata de forma legível, `sort_keys=True`
  ordena as chaves. As versões orientadas a ficheiro `json.dump(obj, f)` /
  `json.load(f)` escrevem e leem diretamente um objeto de ficheiro.
- Só os tipos compatíveis com JSON são serializados; um `set` ou um objeto
  personalizado gera `TypeError` a menos que digas ao `dumps` como o
  converter.

```python
import json

json.dumps({"name": "Ada", "ok": True})   # '{"name": "Ada", "ok": true}'
json.loads('[1, 2, 3]')                    # [1, 2, 3]
```
""",

"11.8 brief": r"""# 11.8 -- Capstone: um resumo estatístico a partir de JSON

## Conceito

A verdadeira lição deste capítulo é que o trabalho do dia a dia é
**compor ferramentas de biblioteca**: deixa um módulo ler os dados, outro
processá-los, e devolve o resultado. Aqui combinas dois dos módulos que
acabaste de conhecer.

A entrada é uma **string JSON** que contém uma lista de números, por
exemplo `"[4, 8, 15, 16]"`. Vais:

1. interpretá-la com **`json.loads`** para uma lista Python,
2. resumi-la com **`statistics`** e os nativos `max` / `min`,
3. devolver um dict simples com os resultados.

```python
import json
import statistics

data = json.loads("[4, 8, 15, 16]")     # [4, 8, 15, 16]
statistics.mean(data)                    # 10.75
```

## A tua tarefa

Define `summary(numbers_json)` que recebe uma string JSON de uma lista de
números e devolve um dict com estas chaves:

- `"count"` -- quantos números (`len`),
- `"mean"` -- a sua média (`statistics.mean`),
- `"max"` -- o maior (`max`),
- `"min"` -- o menor (`min`).

Interpreta a entrada com `json.loads`. Assume pelo menos um número.

## Está feito quando

- `summary("[2, 4, 6]")` é igual a
  `{"count": 3, "mean": 4, "max": 6, "min": 2}`.
- `summary("[5]")` é igual a `{"count": 1, "mean": 5, "max": 5, "min": 5}`.
- A entrada é interpretada com `json.loads`, não à mão.
""",

"11.8 hints": r"""Dois imports no topo: `import json` e `import statistics`. Primeiro
transforma o texto numa lista com `json.loads(numbers_json)`.

---

Depois de teres a lista `nums`, constrói o dict: `len(nums)` para count,
`statistics.mean(nums)` para mean, e os nativos `max(nums)` / `min(nums)`.

---

import json
import statistics


def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {
        "count": len(nums),
        "mean": statistics.mean(nums),
        "max": max(nums),
        "min": min(nums),
    }
""",

"11.8 reference": r"""O capstone é o verdadeiro ponto do capítulo: **compor módulos da
biblioteca padrão** num pequeno pipeline em vez de escrever cada passo de
raiz.

- **Ler** com `json` — `json.loads(text)` transforma a entrada JSON em
  valores Python (aqui, uma lista de números).
- **Resumir** com `statistics` e os nativos — `statistics.mean(nums)` para a
  média, `max(nums)` / `min(nums)` para os extremos, `len(nums)` para a
  contagem.
- **Devolver** um `dict` simples, para que quem chama a função receba valores
  Python comuns para usar.

Cada etapa é um módulo que outra pessoa escreveu e testou; o teu trabalho
é ligá-los entre si. É isso que a maioria dos programas reais são — cola
entre bibliotecas bem feitas.

```python
import json
import statistics

def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {"count": len(nums), "mean": statistics.mean(nums),
            "max": max(nums), "min": min(nums)}

summary("[2, 4, 6]")   # {'count': 3, 'mean': 4, 'max': 6, 'min': 2}
```
""",
}
