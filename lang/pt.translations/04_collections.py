# PyQuest translations -- language 'pt' -- chapter 04_collections -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"4.1 brief": r"""# 4.1 -- Listas e append

## Conceito

Uma **lista** guarda vários valores por ordem, numa única variável. Escreve-se uma
lista com parênteses retos, com os itens separados por vírgulas:

```python
nums = [10, 20, 30]
print(nums)        # [10, 20, 30]
print(nums[0])     # 10   (index like a string -- from 0)
print(len(nums))   # 3
```

Uma lista pode começar vazia e crescer. `.append(x)` adiciona `x` ao **fim**:

```python
nums = []
nums.append(10)
nums.append(20)
print(nums)        # [10, 20]
```

Este padrão de "começar vazia e acrescentar num ciclo" é a forma como se constrói
uma lista a partir da entrada.

## Exemplo

```python
items = []
items.append(1)
items.append(2)
print(items)       # [1, 2]
```

## A tua tarefa

Lê um número inteiro `n`, depois lê mais `n` números inteiros (um por linha). Junta-os
numa lista com `.append()`, e imprime a lista final.

Para a entrada `3`, seguida de `1`, `2`, `3`:

```
[1, 2, 3]
```

## Está feito quando

- `3` com `1, 2, 3` imprime `[1, 2, 3]`.
- Uma contagem de `0` imprime `[]` (uma lista vazia).
""",

"4.1 hints": r"""Começa com uma lista vazia [], depois acrescenta cada número dentro de um ciclo.

---

`nums = []`, lê n, depois `for _ in range(n): nums.append(int(input()))`.
Por fim `print(nums)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(nums)
""",

"4.1 reference": r"""A **lista** é uma sequência ordenada e mutável de valores, escrita entre parênteses retos:
`[10, 20, 30]`. A lista vazia é `[]`. Os itens são acedidos por índice tal como os
caracteres de uma cadeia de caracteres (`lst[0]`, `lst[-1]`).

- **`.append(x)`** adiciona `x` ao **fim**, aumentando a lista em um. Altera a
  lista no próprio local e devolve `None` (por isso nunca escrevas `lst = lst.append(x)`).
- O padrão de construir a partir do vazio: começa com `[]`, depois usa `.append` uma
  vez por cada passagem de um ciclo para juntar resultados.
- Ao contrário das cadeias de caracteres, uma lista pode conter valores de tipos diferentes.

```python
nums = []
for i in range(3):
    nums.append(i * i)   # -> [0, 1, 4]
```
""",

"4.2 brief": r"""# 4.2 -- Alterar uma lista

## Conceito

Ao contrário das cadeias de caracteres, as listas podem ser **alteradas no próprio
local** (são *mutáveis*). Algumas formas:

- Substituir um item pelo índice: `nums[0] = 99`
- Remover e devolver o **último** item: `nums.pop()`
- Remover o primeiro **valor** correspondente: `nums.remove(20)`

```python
nums = [10, 20, 30]
nums[0] = 99      # [99, 20, 30]   replace by position
nums.pop()        # [99, 20]       drop the last item (returns 30)
print(nums)       # [99, 20]
```

Estas alterações mudam a lista já existente -- a variável continua a apontar para a
mesma lista, agora modificada.

## Exemplo

```python
xs = [1, 2, 3]
xs[1] = 0
xs.pop()
print(xs)         # [1, 0]
```

## A tua tarefa

Lê uma contagem `n` (pelo menos 1), depois `n` números, para uma lista. Depois:

1. **duplica o primeiro item** (substitui `nums[0]` por `nums[0] * 2`), e
2. **remove o último item** com `.pop()`.

Imprime a lista resultante. Para a entrada `3`, seguida de `5`, `2`, `9`:

```
[10, 2]
```

(`[5, 2, 9]` -> duplica o primeiro -> `[10, 2, 9]` -> pop -> `[10, 2]`.)

## Está feito quando

- `5, 2, 9` dá `[10, 2]`.
- Um único número `n=1` (por exemplo, apenas `4`) dá `[]` -- duplicado para `[8]`,
  e depois o último (e único) item é removido com pop.
""",

"4.2 hints": r"""Constrói a lista como antes, e depois altera-a no próprio local.

---

`nums[0] = nums[0] * 2` para duplicar o primeiro item; `nums.pop()` para eliminar o último.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums[0] = nums[0] * 2
nums.pop()
print(nums)
""",

"4.2 reference": r"""As listas são **mutáveis**: o seu conteúdo pode ser alterado no próprio local,
ao contrário das cadeias de caracteres.

- **`lst[i] = x`** substitui o item no índice `i`. O índice já tem de existir
  (atribuir além do fim gera um `IndexError`).
- **`.pop()`** remove e **devolve** o último item, reduzindo a lista;
  `.pop(i)` remove o item no índice `i`. Fazer pop de uma lista vazia gera um erro.
- Outras alterações no próprio local: `.insert(i, x)`, `.remove(value)`, `del lst[i]`.

Como a alteração é feita no próprio local, qualquer nome que se refira ao mesmo
objeto lista vê-a.

```python
lst = [10, 20, 30]
lst[1] = 99      # [10, 99, 30]
last = lst.pop() # last == 30, lst == [10, 99]
```
""",

"4.3 brief": r"""# 4.3 -- Percorrer uma lista num ciclo

## Conceito

Tal como uma cadeia de caracteres, uma lista é uma sequência -- por isso um ciclo
`for` percorre diretamente os seus itens, um por cada passagem:

```python
nums = [10, 20, 30]
for x in nums:
    print(x)        # 10, then 20, then 30
```

`len(nums)` dá o número de itens, e o slicing também funciona -- `nums[1:]` é tudo
menos o primeiro, `nums[:2]` são os dois primeiros:

```python
print(len(nums))    # 3
print(nums[:2])     # [10, 20]
```

## Exemplo

```python
xs = [1, 2, 3]
for x in xs:
    print(x * 10)   # 10, 20, 30
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números, para uma lista. Primeiro imprime quantos
números existem, depois imprime cada número **duplicado**, um por linha.

Para a entrada `3`, seguida de `5`, `2`, `9`:

```
3
10
4
18
```

## Está feito quando

- `5, 2, 9` imprime `3`, depois `10`, `4`, `18`.
- Uma contagem de `0` imprime apenas `0` (não há números para duplicar).
""",

"4.3 hints": r"""Depois de construir a lista, imprime len(nums), e depois percorre-a num ciclo.

---

`print(len(nums))`, depois `for x in nums: print(x * 2)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
for x in nums:
    print(x * 2)
""",

"4.3 reference": r"""Uma lista é iterável, por isso **`for x in lst`** visita cada item por ordem,
associando a variável do ciclo ao próprio item (não ao seu índice).

- Esta é a forma habitual de percorrer uma lista. Quando também precisas da
  posição, combina-a com `range(len(lst))` ou `enumerate` (capítulo 5).
- **`len(lst)`** dá a contagem de itens; o **slicing** (`lst[1:3]`, `lst[::-1]`)
  funciona exatamente como nas cadeias de caracteres e devolve uma lista nova.

```python
for name in ["Ada", "Linus"]:
    print(name)

total = 0
for n in [3, 1, 4]:
    total += n           # iterate and accumulate
```
""",

"4.4 brief": r"""# 4.4 -- split: de texto para lista

## Conceito

`s.split()` divide uma cadeia de caracteres em **uma lista de partes**. Sem
argumentos, divide pelos espaços em branco, transformando assim uma frase nas suas
palavras:

```python
"the quick brown fox".split()    # ['the', 'quick', 'brown', 'fox']
```

O resultado é uma lista verdadeira, por isso tudo o que já sabes sobre listas se
aplica -- `len`, indexação, ciclos:

```python
words = "a b c".split()
print(len(words))    # 3
print(words[0])      # a
```

Também podes dividir por um separador específico passando-o como argumento:
`"a,b,c".split(",")` dá `['a', 'b', 'c']`.

## Exemplo

```python
parts = "one two three".split()
print(len(parts))    # 3
```

## A tua tarefa

Lê uma linha de palavras separadas por espaços, e imprime **quantas palavras** ela
contém.

Para a entrada `the quick brown fox`:

```
4
```

## Está feito quando

- `the quick brown fox` imprime `4`; uma única palavra imprime `1`.
- Uma linha vazia imprime `0`.
""",

"4.4 hints": r""".split() transforma a linha numa lista de palavras. Depois conta-as.

---

`print(len(input().split()))`.

---

line = input()
print(len(line.split()))
""",

"4.4 reference": r"""**`s.split()`** divide uma cadeia de caracteres numa **lista de partes**. Sem
argumentos, divide em sequências de **espaço em branco** e descarta os espaços no
início/fim — a forma habitual de obter as palavras de uma linha.

- `s.split(sep)` divide exatamente pelo separador `sep`, mantendo partes vazias
  entre separadores adjacentes (`"a,,b".split(",")` é `["a", "", "b"]`).
- `s.split(sep, maxsplit)` divide no máximo `maxsplit` vezes — útil para separar um
  prefixo, por exemplo `"key=a=b".split("=", 1)` é `["key", "a=b"]`.
- É o inverso de `join` (a seguir).

```python
"the quick fox".split()        # ['the', 'quick', 'fox']
"2024-01-15".split("-")        # ['2024', '01', '15']
```
""",

"4.5 brief": r"""# 4.5 -- join: de lista para texto

## Conceito

`.join()` é o oposto de `split`: cola uma **lista de cadeias de caracteres** numa só
cadeia, colocando um separador entre cada parte. Chama-se este método *sobre o
separador*:

```python
words = ["a", "b", "c"]
print("-".join(words))    # a-b-c
print(", ".join(words))   # a, b, c
print("".join(words))     # abc   (no separator)
```

Lê-se como "junta estas palavras com este separador entre elas". A lista tem de
conter cadeias de caracteres.

## Erro comum

`join` escreve-se com o separador primeiro: `"-".join(words)`, **não**
`words.join("-")`.

## Exemplo

```python
parts = ["2024", "12", "25"]
print("/".join(parts))    # 2024/12/25
```

## A tua tarefa

Lê uma contagem `n`, depois `n` palavras (uma por linha), para uma lista. Imprime-as
juntas com um traço `-`.

Para a entrada `3`, seguida de `a`, `b`, `c`:

```
a-b-c
```

## Está feito quando

- `a, b, c` imprime `a-b-c`; uma única palavra imprime apenas essa palavra.
- Uma contagem de `0` imprime uma linha vazia (nada para juntar).
""",

"4.5 hints": r"""Reúne as palavras numa lista, e depois junta-as. O join é chamado sobre o separador.

---

Constrói a lista, depois `print("-".join(words))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print("-".join(words))
""",

"4.5 reference": r"""**`sep.join(parts)`** cola um iterável de **cadeias de caracteres** numa só cadeia,
colocando `sep` entre itens adjacentes. O separador é a cadeia sobre a qual se
chama o método, o que parece estranho à primeira vista mas permite que o separador
seja qualquer cadeia de caracteres.

- Cada item já tem de ser uma cadeia de caracteres; números geram `TypeError`.
  Converte primeiro, por exemplo `", ".join(str(n) for n in nums)`.
- `"".join(parts)` concatena sem separador — a forma eficiente de construir uma
  cadeia a partir de muitas partes (muito melhor do que `+` repetido).
- É o inverso de `split`.

```python
"-".join(["2024", "01", "15"])   # '2024-01-15'
" ".join(["the", "fox"])          # 'the fox'
```
""",

"4.6 brief": r"""# 4.6 -- Listas dentro de listas

## Conceito

Uma lista pode conter **outras listas**. É assim que se representam linhas de
dados, pares, grelhas, etc.:

```python
pairs = [[1, 2], [3, 4], [5, 6]]
print(pairs)        # [[1, 2], [3, 4], [5, 6]]
print(pairs[0])     # [1, 2]        the first inner list
print(pairs[0][1])  # 2            first inner list, second item
```

Dois índices: o primeiro escolhe uma lista interna, o segundo escolhe um item
dentro dela. Um ciclo dá-te cada lista interna, uma de cada vez:

```python
for p in pairs:
    print(p[0] + p[1])   # 3, 7, 11
```

## Exemplo

```python
grid = [[1, 1], [2, 2]]
for row in grid:
    print(row[0] + row[1])   # 2, 4
```

## A tua tarefa

Lê uma contagem `n`, depois `n` **pares** de números (cada par são dois números, em
duas linhas). Constrói uma lista de pares `[a, b]`. Primeiro imprime a lista
aninhada completa, depois imprime a **soma de cada par**, uma por linha.

Para a entrada `2`, seguida de `1`, `2`, `3`, `4`:

```
[[1, 2], [3, 4]]
3
7
```

## Está feito quando

- `1,2` e `3,4` imprimem `[[1, 2], [3, 4]]`, depois `3`, depois `7`.
- Uma contagem de `0` imprime `[]` e mais nada.
""",

"4.6 hints": r"""Para cada par, lê dois números e acrescenta-os como uma lista de dois itens [a, b].

---

`pairs.append([a, b])` constrói a lista aninhada. Imprime-a, depois percorre num
ciclo: `for p in pairs: print(p[0] + p[1])`.

---

n = int(input())
pairs = []
for _ in range(n):
    a = int(input())
    b = int(input())
    pairs.append([a, b])
print(pairs)
for p in pairs:
    print(p[0] + p[1])
""",

"4.6 reference": r"""Uma lista pode conter outras listas — uma lista **aninhada** — modelando uma
grelha ou tabela. `grid[r]` seleciona uma lista interna (uma linha); `grid[r][c]`
depois seleciona um item dentro dela (uma coluna), pelo que dois índices chegam a
uma célula.

- O primeiro índice escolhe a linha, o segundo o item dentro dessa linha.
- Um ciclo `for row in grid:` produz cada lista interna; aninha um segundo ciclo
  (`for cell in row:`) para chegar a cada item.
- As listas internas são listas normais — mutáveis e de tamanho independente (as
  linhas não têm de ter o mesmo comprimento).

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[0][2]    # 3   -- row 0, column 2
grid[1][0]    # 4
```
""",

"4.7 brief": r"""# 4.7 -- Tuplos e desempacotamento

## Conceito

Um **tuplo** é como uma lista, mas **imutável** -- uma vez criado, não pode ser
alterado. Escreve-se um com parênteses (ou apenas com vírgulas):

```python
point = (3, 7)
print(point[0])    # 3
```

O **desempacotamento** atribui vários valores a várias variáveis de uma só vez, a
partir de um tuplo (ou lista):

```python
x, y = point       # x = 3, y = 7
```

Os nomes do lado esquerdo correspondem aos itens do lado direito, por ordem. Um
truque interessante que isto permite é **trocar** duas variáveis sem uma variável
temporária:

```python
a, b = 1, 2
a, b = b, a        # now a = 2, b = 1
```

O lado direito `b, a` constrói um tuplo, que é depois desempacotado para `a, b`.

## Exemplo

```python
a, b = 10, 20
a, b = b, a
print(a)    # 20
print(b)    # 10
```

## A tua tarefa

Lê dois números inteiros (cada um na sua própria linha). **Troca-os** usando
desempacotamento de tuplos, depois imprime o primeiro, depois o segundo.

Para a entrada `3` seguida de `7`:

```
7
3
```

## Está feito quando

- `3, 7` imprime `7` depois `3`.
- Funciona para quaisquer dois números (incluindo dois números iguais).
""",

"4.7 hints": r"""Lê os dois números, depois troca-os numa única linha com a, b = b, a.

---

`a = int(input())`, `b = int(input())`, depois `a, b = b, a`, depois imprime a e b.

---

a = int(input())
b = int(input())
a, b = b, a
print(a)
print(b)
""",

"4.7 reference": r"""Um **tuplo** é uma sequência ordenada e **imutável**, escrita com vírgulas
(frequentemente entre parênteses): `(3, 4)`, ou apenas `3, 4`. Uma vez criado, não
pode ser alterado.

- O **desempacotamento** atribui os itens de uma sequência a vários nomes de uma
  só vez: `a, b = point`. A contagem em cada lado tem de corresponder.
- Isto permite a **troca** numa só linha `a, b = b, a`: o lado direito é primeiro
  construído como um tuplo, e depois desempacotado, por isso não é preciso nenhuma
  variável temporária.
- Usa um tuplo para um grupo fixo de valores relacionados (uma coordenada, um
  registo); usa uma lista quando a coleção cresce ou muda.

```python
point = (3, 4)
x, y = point        # x = 3, y = 4
a, b = b, a         # swap in one line
```
""",

"4.8 brief": r"""# 4.8 -- Dicionários

## Conceito

Um **dicionário** (`dict`) associa **chaves** a **valores** -- uma tabela de
consulta. Escreve-se um com chavetas e pares `chave: valor`:

```python
ages = {"sam": 20, "ada": 36}
print(ages["sam"])     # 20      look up by key
ages["lee"] = 41       # add a new key
ages["sam"] = 21       # update an existing key
```

Procuram-se coisas pela **chave** (não pela posição), o que torna os dicionários
rápidos e úteis para "dado X, qual é o seu Y?". Começa vazio com `{}` e preenche-o:

```python
d = {}
d["x"] = 1
```

## Exemplo

```python
prices = {}
prices["apple"] = 3
print(prices["apple"])   # 3
```

## A tua tarefa

Lê uma contagem `n`, depois `n` pares de uma **palavra** e um **número** (palavra
numa linha, número na seguinte) para um dicionário (a palavra é a chave, o número o
valor). Depois lê mais uma **palavra de consulta** e imprime o número guardado
para ela.

Para a entrada `2`, `apple`, `3`, `banana`, `5`, seguida da consulta `banana`:

```
5
```

## Está feito quando

- Construir `{apple: 3, banana: 5}` e consultar `banana` imprime `5`.
- Um par posterior com a mesma chave atualiza-a (o teste depende do último valor
  para qualquer chave repetida).
""",

"4.8 hints": r"""Cria um dicionário vazio, e depois guarda cada par como d[word] = number.

---

`d = {}`, percorre num ciclo lendo palavra + número com `d[word] = int(input())`,
depois lê a consulta e `print(d[query])`.

---

n = int(input())
d = {}
for _ in range(n):
    word = input()
    d[word] = int(input())
query = input()
print(d[query])
""",

"4.8 reference": r"""Um **dicionário** (`dict`) associa **chaves** a **valores**: `{"a": 1, "b": 2}`. É
a ferramenta para consultas pelo nome em vez de pela posição.

- **`d[key]`** lê o valor de uma chave; **`d[key] = value`** adiciona a chave (se
  for nova) ou atualiza-a (se já existir). As chaves são únicas — atribuir a uma
  chave existente sobrescreve-a.
- Ler uma chave **inexistente** com `d[key]` gera `KeyError` (ver `.get`, 4.10).
- As chaves têm de ser imutáveis (cadeias de caracteres, números, tuplos); os
  valores podem ser qualquer coisa. `len(d)` conta os pares; `key in d` testa a
  existência de uma chave.

```python
ages = {"Ada": 36}
ages["Ada"]          # 36
ages["Linus"] = 21   # add a new pair
```
""",

"4.9 brief": r"""# 4.9 -- Percorrer um dicionário num ciclo

## Conceito

Para visitar tudo num dicionário, percorre `.items()` num ciclo, que dá cada
**chave e valor** em conjunto:

```python
ages = {"sam": 20, "ada": 36}
for name, age in ages.items():
    print(name, age)      # sam 20, then ada 36
```

A parte `for name, age in ...` está a desempacotar cada par em duas variáveis. Os
dicionários lembram-se da ordem em que as chaves foram inseridas, por isso
obténs-las de volta por essa ordem.

Existem também `.keys()` (apenas as chaves) e `.values()` (apenas os valores), mas
`.items()` é o habitual quando precisas de ambos.

## Exemplo

```python
d = {"x": 1, "y": 2}
for k, v in d.items():
    print(f"{k}={v}")     # x=1, then y=2
```

## A tua tarefa

Lê uma contagem `n`, depois `n` pares de uma **palavra** e um **número** para um
dicionário. Depois imprime uma linha `key=value` para cada par, pela ordem em que
foram adicionados.

Para a entrada `2`, `a`, `1`, `b`, `2`:

```
a=1
b=2
```

## Está feito quando

- `a=1`, `b=2` são impressos pela ordem de inserção.
- Uma contagem de `0` não imprime nada.
""",

"4.9 hints": r"""Constrói o dicionário, depois percorre d.items() num ciclo para obter cada chave e valor.

---

`for k, v in d.items(): print(f"{k}={v}")`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
for k, v in d.items():
    print(f"{k}={v}")
""",

"4.9 reference": r"""**`d.items()`** produz cada par `(key, value)`, por isso um ciclo `for` com duas
variáveis percorre todo o dicionário, desempacotando cada par à medida que avança.

- `for k, v in d.items():` associa `k` à chave e `v` ao seu valor em cada passagem.
- `d.keys()` e `d.values()` iteram apenas as chaves ou apenas os valores; percorrer
  o dicionário diretamente (`for k in d`) itera as **chaves**.
- A ordem de iteração é a **ordem de inserção** (a ordem em que as chaves foram
  adicionadas pela primeira vez).

```python
prices = {"pen": 2, "ink": 5}
for item, cost in prices.items():
    print(item, cost)        # pen 2 / ink 5
```
""",

"4.10 brief": r"""# 4.10 -- Chaves inexistentes e .get()

## Conceito

Procurar uma chave que não está no dicionário com `d[key]` **falha** (gera um
`KeyError`):

```python
ages = {"sam": 20}
print(ages["lee"])    # KeyError!
```

`.get()` é a forma segura. Devolve `None` para uma chave inexistente em vez de
falhar -- ou um **valor por omissão** que forneças:

```python
print(ages.get("lee"))        # None
print(ages.get("lee", 0))     # 0      (your default)
print(ages.get("sam", 0))     # 20     (key exists, so its value)
```

Portanto, `d.get(key, default)` significa "o valor se a chave existir, caso
contrário `default`".

## Exemplo

```python
d = {"a": 1}
print(d.get("a", 0))    # 1
print(d.get("z", 0))    # 0
```

## A tua tarefa

Lê uma contagem `n`, depois `n` pares de uma palavra e um número para um
dicionário. Depois lê uma **palavra de consulta** e imprime o seu número -- mas se
a palavra não estiver no dicionário, imprime `0` em vez disso (não falhes).

Para a entrada `2`, `a`, `1`, `b`, `2`, seguida da consulta `c`:

```
0
```

(`c` não é uma chave, por isso é impresso o valor por omissão `0`.)

## Está feito quando

- Uma chave existente imprime o seu valor; uma chave inexistente imprime `0`.
- Nunca falha com uma chave inexistente (usa `.get`).
""",

"4.10 hints": r"""d[key] falha se a chave não existir. d.get(key, 0) devolve 0 em vez disso.

---

Depois de construir o dicionário e ler a consulta, `print(d.get(query, 0))`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
query = input()
print(d.get(query, 0))
""",

"4.10 reference": r"""**`d.get(key, default)`** procura uma chave de forma segura: devolve o valor se a
chave existir, caso contrário o `default` — sem gerar um erro. Sem valor por
omissão, devolve `None` para uma chave inexistente.

- Usa-o em vez de `d[key]` sempre que uma chave inexistente for um caso normal e
  esperado, e não um erro.
- É a base do idioma de **contagem**: `counts[k] = counts.get(k, 0) + 1` lê a
  contagem corrente (0 na primeira vez) e escreve a nova.
- `.get` só lê; nunca insere a chave (ao contrário de `setdefault`).

```python
ages = {"Ada": 36}
ages.get("Ada", 0)     # 36
ages.get("Nobody", 0)  # 0  -- no KeyError
```
""",

"4.11 brief": r"""# 4.11 -- Conjuntos

## Conceito

Um **conjunto** é uma coleção não ordenada de itens **únicos** -- descarta
automaticamente duplicados. Escreve-se um com chavetas, ou constrói-se um a partir
de uma lista com `set(...)`:

```python
s = {1, 2, 2, 3}
print(s)              # {1, 2, 3}   (the duplicate 2 is gone)

nums = [1, 1, 2, 3, 3]
print(set(nums))      # {1, 2, 3}
print(len(set(nums))) # 3           how many *distinct* values
```

Os conjuntos são ótimos para "quantas coisas diferentes?" e para testes rápidos de
pertença com `in`:

```python
print(2 in s)         # True
```

(Os conjuntos não têm ordem nem indexação -- não podes fazer `s[0]`.)

## Exemplo

```python
words = ["a", "b", "a"]
print(len(set(words)))   # 2
```

## A tua tarefa

Lê uma contagem `n`, depois `n` palavras. Imprime quantas palavras **distintas**
existem.

Para a entrada `4`, `a`, `b`, `a`, `c`:

```
3
```

(`a` aparece duas vezes mas conta uma só vez.)

## Está feito quando

- `a, b, a, c` imprime `3`.
- Uma contagem de `0` imprime `0`.
""",

"4.11 hints": r"""Um conjunto descarta duplicados. Coloca as palavras num conjunto, e depois conta-o.

---

Reúne as palavras numa lista, depois `print(len(set(words)))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(len(set(words)))
""",

"4.11 reference": r"""Um **conjunto** é uma coleção não ordenada de itens **únicos**: `{1, 2, 3}`.
Modela "um grupo de coisas distintas" e testa a pertença rapidamente.

- Construir um conjunto a partir de uma sequência **descarta duplicados**:
  `set([1, 1, 2])` é `{1, 2}`. O conjunto vazio é `set()` — `{}` é um *dicionário*
  vazio.
- **`x in s`** testa a pertença e é muito mais rápido do que percorrer uma lista,
  porque os conjuntos são baseados em hash.
- Os conjuntos não são ordenados (sem indexação, sem slicing) e só contêm itens
  imutáveis. Adiciona com `.add(x)`, remove com `.discard(x)`.

```python
seen = set()
seen.add("a"); seen.add("a")   # {'a'} -- duplicate ignored
"a" in seen                    # True
set([3, 1, 3, 2])              # {1, 2, 3}
```
""",

"4.12 brief": r"""# 4.12 -- Combinar conjuntos

## Conceito

Os conjuntos podem ser combinados como na matemática:

- **interseção** `a & b` -- itens em **ambos**
- **união** `a | b` -- itens em **qualquer um**
- **diferença** `a - b` -- itens em `a` mas não em `b`

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # {2, 3}
print(a | b)    # {1, 2, 3, 4}
print(a - b)    # {1}
```

Estas respondem a perguntas como "que itens dois grupos partilham?" sem escrever
um ciclo. (`a.intersection(b)` e `a.union(b)` fazem o mesmo que `&` e `|`.)

## Exemplo

```python
x = {"a", "b"}
y = {"b", "c"}
print(len(x & y))   # 1   (just "b")
```

## A tua tarefa

Lê um primeiro grupo: uma contagem `n`, depois `n` palavras. Depois um segundo
grupo: uma contagem `m`, depois `m` palavras. Imprime **quantas palavras distintas
aparecem em ambos** os grupos.

Para o primeiro grupo `a`, `b` e o segundo grupo `b`, `c`:

```
1
```

(Apenas `b` está em ambos.)

## Está feito quando

- `{a, b}` e `{b, c}` imprimem `1`.
- Grupos vazios dão `0`; duplicados dentro de um grupo contam uma só vez.
""",

"4.12 hints": r"""Coloca cada grupo num conjunto, depois usa a interseção dos dois.

---

Constrói o conjunto `a` e o conjunto `b`, depois `print(len(a & b))`.

---

n = int(input())
a = set()
for _ in range(n):
    a.add(input())
m = int(input())
b = set()
for _ in range(m):
    b.add(input())
print(len(a & b))
""",

"4.12 reference": r"""Os conjuntos suportam a álgebra de coleções:

- **`a & b`** (interseção) — itens em **ambos**.
- **`a | b`** (união) — itens em **qualquer um**.
- **`a - b`** (diferença) — itens em `a` mas **não** em `b`.

Cada uma devolve um **novo** conjunto. (`^` é a diferença simétrica — em
exatamente um.) Estas expressam perguntas sobre conjuntos diretamente,
substituindo ciclos escritos à mão que comparam duas coleções.

```python
a, b = {1, 2, 3}, {2, 3, 4}
a & b     # {2, 3}
a | b     # {1, 2, 3, 4}
a - b     # {1}
```
""",

"4.13 brief": r"""# 4.13 -- Escolher a coleção certa

## Conceito

Já tens quatro coleções. Escolher a certa torna um problema fácil:

- **lista** -- itens ordenados, duplicados permitidos (`[1, 2, 2]`). Usa para sequências.
- **tuplo** -- como uma lista mas fixo/imutável. Usa para grupos fixos.
- **conjunto** -- itens não ordenados e **únicos**. Usa para "distintos" e pertença rápida.
- **dicionário** -- consulta chave -> valor. Usa para "dado X, encontra o seu Y".

Este puzzle combina algumas:

- `len(nums)` -- quantos itens (uma **lista** guarda todos os valores, incluindo repetidos).
- `len(set(nums))` -- quantos valores **distintos** (um **conjunto** descarta duplicados).
- a **soma** -- um ciclo com um acumulador (ou `sum(nums)`).

## Exemplo

```python
nums = [1, 2, 2, 3]
print(len(nums))        # 4
print(len(set(nums)))   # 3
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números. Imprime três linhas:

1. quantos números existem,
2. quantos números **distintos** existem,
3. o seu **total**.

Para a entrada `4`, seguida de `1`, `2`, `2`, `3`:

```
4
3
8
```

## Está feito quando

- `1, 2, 2, 3` imprime `4`, `3`, `8`.
- Uma contagem de `0` imprime `0`, `0`, `0`.
""",

"4.13 hints": r"""Constrói a lista. A contagem é len(nums); a contagem de distintos usa um conjunto.

---

`print(len(nums))`, `print(len(set(nums)))`, depois o total (um ciclo, ou sum).

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
print(len(set(nums)))
total = 0
for x in nums:
    total = total + x
print(total)
""",

"4.13 reference": r"""As três coleções principais servem para tarefas diferentes — escolher a certa
torna o código mais simples e mais rápido:

- **lista** — uma sequência **ordenada** que pode repetir valores. Usa-a para
  guardar todos os valores, por ordem (um registo, uma fila de itens a processar).
- **conjunto** — um grupo não ordenado de itens **distintos** com pertença rápida.
  Usa-o para descartar duplicados ou perguntar "já vi isto?".
- **dicionário** — um mapeamento de **chaves para valores**. Usa-o para procurar
  algo pelo nome (uma contagem por palavra, um preço por item).

Pergunta: preciso de ordem e repetições (lista), unicidade e pertença (conjunto),
ou consulta por chave (dicionário)?

```python
order  = ["a", "b", "a"]    # keep all, in order
unique = {"a", "b"}         # distinct only
price  = {"a": 2, "b": 5}   # look up by key
```
""",
}
