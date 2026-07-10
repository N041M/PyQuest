# PyQuest translations -- language 'pt' -- chapter 05_power_tools -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"5.1 brief": r"""# 5.1 -- in: testar pertença

## Conceito

Encontraste o `in` com conjuntos (4.11). Na verdade funciona em quase tudo:

```python
"e" in "hello"        # True   (substring of a string)
3 in [1, 2, 3]        # True   (item of a list)
"sam" in {"sam": 20}  # True   (KEY of a dict)
```

`x in s` é uma expressão que dá um **booleano** (`True`/`False`), por isso
encaixa diretamente num `if`:

```python
if "@" in address:
    print("looks like an email")
```

Também existe o oposto, `not in`:

```python
if "x" not in word:
    print("no x here")
```

Compara com o capítulo 2, onde usaste `s.find()` e verificaste `-1`.
O `in` diz a mesma coisa em linguagem simples -- prefere-o sempre que só precises de saber
*se* algo está lá, não *onde*.

## Exemplo

```python
word = "banana"
print("n" in word)     # True
print("z" in word)     # False
```

## A tua tarefa

Lê uma palavra, depois uma única letra. Imprime `yes` se a letra aparecer na
palavra, e `no` se não aparecer.

Para a entrada `banana`, depois `n`:

```
yes
```

## Está feito quando

- Uma letra que aparece imprime `yes`; uma que não aparece imprime `no`.
- Também funciona para uma palavra de uma letra.
- Usaste o operador `in` (não `.find()` nem `.count()`).
""",

"5.1 hints": r"""`letter in word` já é True ou False -- coloca-o diretamente num `if`.

---

Lê a palavra, lê a letra, depois ramifica: `if letter in word:` imprime yes,
`else:` imprime no.

---

word = input()
letter = input()
if letter in word:
    print("yes")
else:
    print("no")
""",

"5.1 reference": r"""O operador **`in`** testa a pertença e devolve um booleano, por isso encaixa diretamente
num `if` ou `while`. `x in c` é `True` quando `x` é encontrado em `c`.

- Para uma **cadeia de caracteres**, `in` testa uma **substring**: `"cat" in "concatenate"` é
  `True`.
- Para uma **lista** ou **tuplo**, testa um item (percorrendo a sequência).
- Para um **dicionário** ou **conjunto**, testa uma **chave**/membro — e é rápido
  (baseado em hash), ao contrário da procura linear de uma lista.
- `x not in c` é a negação, e lê-se de forma natural.

```python
"a" in "cat"          # True
3 in [1, 2, 3]        # True
"key" in {"key": 1}   # True  -- tests keys
```
""",

"5.2 brief": r"""# 5.2 -- sum()

## Conceito

Em 3.12 escreveste o **padrão acumulador** à mão:

```python
total = 0
for x in nums:
    total = total + x
```

Esse padrão é tão comum que o Python o traz como função nativa:

```python
total = sum(nums)
```

`sum(list_of_numbers)` soma cada item e devolve o total. Numa lista vazia
devolve `0` -- exatamente o valor com que o teu acumulador escrito à mão começava.

Este capítulo está cheio destas **ferramentas poderosas**: funções nativas que substituem um
ciclo que já escreveste tu mesmo uma vez. Ganhas o atalho por saberes o que ele substitui.

## Exemplo

```python
nums = [3, 1, 4]
print(sum(nums))    # 8
print(sum([]))      # 0
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números inteiros (um por linha). Imprime o seu total
usando `sum()`.

Para a entrada `3`, depois `3`, `1`, `4`:

```
8
```

## Está feito quando

- `3, 1, 4` imprime `8`; negativos também funcionam.
- Uma contagem de `0` imprime `0`.
- Usaste `sum()` -- desta vez, não um ciclo escrito à mão.
""",

"5.2 hints": r"""Constrói primeiro a lista de números (como em 4.13), depois entrega a lista toda a uma só
chamada de função.

---

`sum(nums)` devolve o total -- imprime isso. Não precisas de `total = 0`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(sum(nums))
""",

"5.2 reference": r"""**`sum(numbers)`** soma um iterável de números e devolve o total — o
ciclo acumulador de 3.12 numa só chamada nativa.

- Funciona em qualquer iterável de números (lista, tuplo, range, gerador). `sum([])`
  é `0`.
- Um segundo argumento opcional é o valor **inicial**: `sum(nums, 100)` começa o
  total em 100.
- Só soma números; para totalizar algo derivado de cada item, alimenta-o com uma
  compreensão ou gerador, por exemplo `sum(len(w) for w in words)`.

```python
sum([3, 1, 4])              # 8
sum(range(1, 101))          # 5050
sum(len(w) for w in words)  # total characters
```
""",

"5.3 brief": r"""# 5.3 -- min() e max()

## Conceito

Encontrar o item mais pequeno ou maior é outro ciclo que podias escrever à mão
("guarda o melhor até agora, compara cada item") -- e outro ciclo que o Python traz como
função nativa:

```python
nums = [3, 7, 1]
print(min(nums))    # 1
print(max(nums))    # 7
```

`min()` e `max()` recebem uma lista (na verdade, qualquer coleção não vazia) e devolvem
o seu item mais pequeno / maior. Também funcionam com cadeias de caracteres -- "mais pequeno" então
significa mais cedo na ordem alfabética:

```python
min("cab")     # "a"
```

Um cuidado: numa lista **vazia** rebentam (não há mais pequeno de
nada), por isso este puzzle garante pelo menos um número.

## Exemplo

```python
nums = [4, -2, 9]
print(min(nums))    # -2
print(max(nums))    # 9
```

## A tua tarefa

Lê uma contagem `n` (sempre pelo menos 1), depois `n` números inteiros. Imprime duas linhas:
o mais pequeno, depois o maior.

Para a entrada `3`, depois `4`, `-2`, `9`:

```
-2
9
```

## Está feito quando

- `4, -2, 9` imprime `-2` depois `9`.
- Um único número imprime-se a si próprio duas vezes (é ao mesmo tempo o mínimo e o máximo).
- Usaste `min()` e `max()`.
""",

"5.3 hints": r"""Constrói primeiro a lista; depois o mais pequeno e o maior são cada um uma só chamada de função.

---

`print(min(nums))` depois `print(max(nums))` -- duas linhas, duas chamadas.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(min(nums))
print(max(nums))
""",

"5.3 reference": r"""**`min(items)`** e **`max(items)`** devolvem o item mais pequeno e o maior de uma
coleção não vazia.

- Comparam com `<`/`>`, por isso funcionam com números e com cadeias de caracteres (que
  se comparam lexicograficamente).
- Chamados sobre um iterável **vazio** levantam `ValueError`; passa `default=` para
  fornecer um valor alternativo.
- Uma função `key=` ordena por um valor derivado em vez do próprio item:
  `max(words, key=len)` devolve a palavra **mais comprida**.

```python
min([3, 1, 4])             # 1
max("apple", "pear")       # 'pear'
max(words, key=len)        # the longest word
```
""",

"5.4 brief": r"""# 5.4 -- sorted()

## Conceito

`sorted(nums)` devolve uma **nova lista** com os mesmos itens por ordem, do mais pequeno
primeiro:

```python
nums = [3, 1, 2]
print(sorted(nums))    # [1, 2, 3]
print(nums)            # [3, 1, 2]  -- the original is untouched
```

Duas coisas a saber:

- Devolve uma *cópia*; a lista original mantém a sua ordem. (Também existe
  `nums.sort()`, um método que reordena a lista **no próprio local** -- útil mais tarde,
  mas `sorted()` é a opção mais segura por omissão porque nada é alterado às escondidas.)
- Do maior para o mais pequeno é só uma palavra-chave de distância: `sorted(nums, reverse=True)`.

Os duplicados mantêm-se -- ordenar reorganiza, nunca remove.

## Exemplo

```python
for x in sorted([3, 1, 2]):
    print(x)
# 1
# 2
# 3
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números inteiros. Imprime-os do mais pequeno ao maior,
um por linha.

Para a entrada `4`, depois `3`, `1`, `3`, `2`:

```
1
2
3
3
```

## Está feito quando

- `3, 1, 3, 2` imprime `1, 2, 3, 3` -- o `3` duplicado aparece duas vezes.
- Uma contagem de `0` não imprime nada.
- Usaste `sorted()`.
""",

"5.4 hints": r"""Constrói a lista, depois percorre `sorted(nums)` em vez de `nums`.

---

`for x in sorted(nums):` visita os itens do mais pequeno para o maior; imprime cada um.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for x in sorted(nums):
    print(x)
""",

"5.4 reference": r"""**`sorted(items)`** devolve uma **nova** lista com os itens em ordem crescente,
deixando o original intacto.

- Aceita qualquer iterável e devolve sempre uma lista. Números ordenam-se numericamente,
  cadeias de caracteres lexicograficamente.
- **`reverse=True`** ordena de forma decrescente. **`key=`** ordena por um valor derivado:
  `sorted(words, key=len)` ordena por comprimento, `sorted(d.items(), key=lambda kv:
  kv[1])` ordena os pares do dicionário pelo valor.
- O método de lista `lst.sort()` ordena **no próprio local** e devolve `None`; usa
  `sorted` quando queres uma lista nova ou estás a ordenar algo que não é uma lista.

```python
sorted([3, 1, 2])               # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
sorted(words, key=len)          # shortest to longest
```
""",

"5.5 brief": r"""# 5.5 -- enumerate()

## Conceito

Às vezes um ciclo precisa tanto do **item** como da sua **posição**. Podias controlar
um contador à mão, mas o Python tem uma função nativa exatamente para isto:

```python
words = ["tea", "milk"]
for i, w in enumerate(words):
    print(i, w)
# 0 tea
# 1 milk
```

Em cada passagem, o `enumerate` entrega-te um par `(posição, item)`, que desempacotas
em duas variáveis (4.7) -- o mesmo truque de `for k, v in d.items()`.

Contar a partir de `0` raramente é o que queres *mostrar* a uma pessoa. O segundo
argumento define o número inicial:

```python
for i, w in enumerate(words, 1):
    print(i, w)
# 1 tea
# 2 milk
```

## Exemplo

```python
for i, ch in enumerate("hi", 1):
    print(f"{i}. {ch}")
# 1. h
# 2. i
```

## A tua tarefa

Lê uma contagem `n`, depois `n` palavras. Imprime-as como uma lista numerada a começar em 1,
no formato `1. palavra` (um ponto e um espaço depois do número).

Para a entrada `3`, depois `tea`, `milk`, `sugar`:

```
1. tea
2. milk
3. sugar
```

## Está feito quando

- Três palavras imprimem-se como `1. ...`, `2. ...`, `3. ...`.
- Uma contagem de `0` não imprime nada.
- Usaste `enumerate()` -- sem contador guardado à mão.
""",

"5.5 hints": r"""`for i, w in enumerate(words, 1):` dá-te o número e a palavra juntos,
a começar em 1.

---

Dentro do ciclo, constrói a linha com uma f-string: `f"{i}. {w}"`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i, w in enumerate(words, 1):
    print(f"{i}. {w}")
""",

"5.5 reference": r"""**`enumerate(items)`** empareira cada item com a sua posição, para que um ciclo `for` obtenha
ambos de uma vez — sem contador guardado à mão.

- `for i, item in enumerate(lst):` liga `i` ao índice (a partir de 0) e `item` ao
  valor, em cada passagem.
- Um segundo argumento define o **número inicial**: `enumerate(lst, 1)` numera
  a partir de 1, útil para listas voltadas para pessoas.
- É preguiçoso (produz pares por pedido) e funciona em qualquer iterável.

```python
for i, name in enumerate(["a", "b"], 1):
    print(i, name)        # 1 a / 2 b
```
""",

"5.6 brief": r"""# 5.6 -- zip(): emparelhar listas

## Conceito

Duas listas muitas vezes andam juntas item a item: nomes e pontuações, perguntas e
respostas. `zip()` percorre-as **em sincronia**, entregando-te um par por passagem:

```python
names = ["amy", "ben"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
# amy 90
# ben 85
```

Como o `enumerate`, cada passagem dá um par que desempacotas em duas variáveis.
O nome vem da imagem de um fecho de correr: duas filas de dentes unidas uma a uma.

Se as listas tiverem comprimentos diferentes, o `zip` para na **mais curta** --
os itens extra na lista mais longa simplesmente nunca são visitados.

## Exemplo

```python
for a, b in zip("ab", [1, 2]):
    print(a, b)
# a 1
# b 2
```

## A tua tarefa

Lê uma contagem `n`, depois `n` nomes, depois `n` pontuações (números inteiros). Imprime uma
linha por par: o nome, um espaço, a pontuação.

Para a entrada `2`, depois `amy`, `ben`, depois `90`, `85`:

```
amy 90
ben 85
```

## Está feito quando

- Dois nomes e duas pontuações imprimem-se como duas linhas `nome pontuação`, por ordem.
- Uma contagem de `0` não imprime nada.
- Usaste `zip()` para emparelhar as duas listas.
""",

"5.6 hints": r"""Lê primeiro TODOS os nomes para uma lista, depois todas as pontuações para outra --
só depois os emparelhas.

---

`for name, score in zip(names, scores):` dá um par por passagem; imprime os
dois com um espaço entre eles (`print(name, score)` simples já faz isso).

---

n = int(input())
names = []
for _ in range(n):
    names.append(input())
scores = []
for _ in range(n):
    scores.append(input())
for name, score in zip(names, scores):
    print(name, score)
""",

"5.6 reference": r"""**`zip(a, b)`** percorre vários iteráveis **em sincronia**, produzindo um tuplo de
itens correspondentes por passagem — o *i*-ésimo de cada um. Empareira sequências paralelas
sem usar índices.

- `for x, y in zip(xs, ys):` liga `x` e `y` aos itens correspondentes em cada passagem.
- Para no iterável **mais curto**, por isso os itens extra num mais comprido são ignorados.
- Qualquer número de iteráveis pode ser combinado com `zip`; `dict(zip(keys, values))` constrói um dicionário
  a partir de duas listas paralelas.

```python
names, scores = ["Ada", "Linus"], [90, 85]
for n, s in zip(names, scores):
    print(n, s)           # Ada 90 / Linus 85
```
""",

"5.7 brief": r"""# 5.7 -- Compreensões de listas

## Conceito

Uma forma de ciclo muito comum é *"construir uma nova lista fazendo algo a cada
item"*:

```python
doubled = []
for x in nums:
    doubled.append(x * 2)
```

O Python tem uma forma de uma linha exatamente para isso, chamada **compreensão de
lista**:

```python
doubled = [x * 2 for x in nums]
```

Lê-a de dentro para fora: *"para cada `x` em `nums`, coloca `x * 2` numa lista nova"*. Os
parênteses retos dizem "estou a construir uma lista"; a expressão antes de `for` é
aquilo em que cada item se transforma.

Funciona com qualquer coisa que possas percorrer -- incluindo `range`. Ler `n`
números (o que já fizeste uma dúzia de vezes) reduz-se a:

```python
nums = [int(input()) for _ in range(n)]
```

## Exemplo

```python
nums = [1, 2, 3]
squares = [x * x for x in nums]
print(squares)    # [1, 4, 9]
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números inteiros. Constrói uma nova lista onde cada
número está **duplicado**, depois imprime os seus itens um por linha.

Para a entrada `3`, depois `4`, `-1`, `0`:

```
8
-2
0
```

## Está feito quando

- `4, -1, 0` imprime `8, -2, 0` -- cada um duplicado, ordem mantida.
- Uma contagem de `0` não imprime nada.
- Usaste uma compreensão de lista para construir uma lista.
""",

"5.7 hints": r"""O padrão é  nova_lista = [<o que cada item se torna> for x in lista_antiga].

---

`doubled = [x * 2 for x in nums]` -- depois um `for` simples imprime cada item.
(Ler os números também pode ser uma compreensão: `[int(input()) for _ in range(n)]`.)

---

n = int(input())
nums = [int(input()) for _ in range(n)]
doubled = [x * 2 for x in nums]
for d in doubled:
    print(d)
""",

"5.7 reference": r"""Uma **compreensão de lista** constrói uma nova lista numa só expressão: para cada `x` em
`items`, avalia `expr` e reúne os resultados, por ordem. É o
padrão construir-por-ciclo-e-append comprimido numa linha.

- `[expr for x in items]` equivale a começar com `result = []` e
  `result.append(expr)` num ciclo — o mesmo resultado, mais direto.
- `expr` pode ser qualquer expressão em `x`: `[n * n for n in nums]`,
  `[w.upper() for w in words]`.
- As compreensões também constroem conjuntos (`{...}`) e dicionários (`{k: v for ...}`).

```python
[n * n for n in range(5)]       # [0, 1, 4, 9, 16]
[w.upper() for w in ["a", "b"]] # ['A', 'B']
```
""",

"5.8 brief": r"""# 5.8 -- Filtrar com compreensões

## Conceito

Uma compreensão também pode **escolher** que itens manter. Acrescenta um `if` no
final:

```python
evens = [x for x in nums if x % 2 == 0]
```

Lê-a: *"cada `x` de `nums` -- mas só se `x % 2 == 0`"*. Os itens que falham
o teste são simplesmente deixados de fora.

As duas partes são independentes e combinam-se livremente:

```python
[x * 2 for x in nums]                 # transform every item   (5.7)
[x for x in nums if x > 0]            # keep some, unchanged   (this puzzle)
[x * 2 for x in nums if x > 0]        # keep some AND transform
```

Lembrete de 1.9: `x % 2` é o resto da divisão por 2, por isso é `0`
exatamente para números pares -- e isso inclui o próprio `0` e negativos como
`-4`.

## Exemplo

```python
nums = [1, 2, 3, 4]
print([x for x in nums if x % 2 == 0])    # [2, 4]
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números inteiros. Mantém apenas os **pares** (na
sua ordem original) e imprime-os um por linha.

Para a entrada `5`, depois `1`, `2`, `3`, `4`, `-6`:

```
2
4
-6
```

## Está feito quando

- `1, 2, 3, 4, -6` imprime `2, 4, -6` -- negativos e zero contam como pares.
- Se nenhum número for par, nada é impresso.
- Usaste uma compreensão com uma cláusula `if`.
""",

"5.8 hints": r""""Par" significa que o resto da divisão por 2 é zero: `x % 2 == 0`.

---

Coloca esse teste no final da compreensão:
`evens = [x for x in nums if x % 2 == 0]` -- depois imprime cada item.

---

n = int(input())
nums = [int(input()) for _ in range(n)]
evens = [x for x in nums if x % 2 == 0]
for e in evens:
    print(e)
""",

"5.8 reference": r"""Acrescentar um **`if`** a uma compreensão mantém apenas os itens que passam o teste.
`[x for x in items if test]` reúne cada `x` para o qual `test` é verdadeiro,
**ignorando** os restantes.

- A cláusula `if` filtra; a expressão inicial continua a transformar, por isso as duas
  combinam-se: `[n * n for n in nums if n % 2 == 0]` eleva ao quadrado apenas os pares.
- Substitui o padrão ciclo-com-`if`-e-`append`.
- Não a confundas com uma **expressão condicional** na posição do valor
  (`[a if cond else b for x in items]`), que escolhe por item em vez de
  filtrar.

```python
[n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
[w for w in words if len(w) > 3]       # only long words
```
""",

"5.9 brief": r"""# 5.9 -- Contar com um dicionário

## Conceito

*"Quantas vezes aparece cada coisa?"* é uma das perguntas mais úteis na programação.
A resposta é o **padrão de contagem**: um dicionário onde cada chave é uma
coisa que já viste e o seu valor é quantas vezes já a viste.

O truque todo é uma linha, construída sobre o `.get()` de 4.10:

```python
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

Lê a linha devagar: *"a contagem de `w` passa a ser o que era -- ou 0 se
`w` for novo -- mais um."* `.get(w, 0)` é o que faz a primeira aparição funcionar:
ainda não há entrada, por isso conta a partir de 0.

Depois do ciclo, `counts.get(coisa, 0)` responde "quantas vezes?" para qualquer coisa --
incluindo coisas nunca vistas, que dão `0`, e não um erro.

## Exemplo

```python
words = ["tea", "milk", "tea"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts.get("tea", 0))     # 2
print(counts.get("cocoa", 0))   # 0
```

## A tua tarefa

Lê uma linha de palavras (separa-as com `.split()`, como em 4.4), depois lê uma
**palavra de consulta** numa segunda linha. Imprime quantas vezes a consulta aparece na
linha.

Para a entrada `tea milk tea`, depois `tea`:

```
2
```

## Está feito quando

- `tea milk tea` com a consulta `tea` imprime `2`; a consulta `milk` imprime `1`.
- Uma consulta que nunca aparece imprime `0` (sem erro).
- Construíste uma contagem com dicionário (não uma verificação pontual).
""",

"5.9 hints": r"""Divide a linha numa lista de palavras, depois percorre-a construindo o dicionário de contagem.

---

A linha de contagem é  counts[w] = counts.get(w, 0) + 1  -- e a resposta final é
outro .get com um valor por omissão: counts.get(query, 0).

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
query = input()
print(counts.get(query, 0))
""",

"5.9 reference": r"""O padrão de **contagem** conta quantas vezes aparece cada coisa distinta, usando um
dicionário cujas chaves são as coisas e cujos valores são contagens correntes.

- Para cada item, `counts[k] = counts.get(k, 0) + 1` lê a contagem atual
  (`0` na primeira vez que a chave é vista, através do valor por omissão do `.get`) e escreve mais um.
- Começa a partir de um dicionário vazio `{}`; as chaves aparecem à medida que são encontradas pela primeira vez.
- O `collections.Counter` da biblioteca padrão faz isto num só passo, mas o
  idioma `.get(k, 0) + 1` mostra exatamente o que está a acontecer.

```python
counts = {}
for w in ["a", "b", "a"]:
    counts[w] = counts.get(w, 0) + 1   # {'a': 2, 'b': 1}
```
""",

"5.10 brief": r"""# 5.10 -- Capítulo final: relatório de palavras

## Conceito

Nada de novo desta vez -- este puzzle combina o capítulo (e o capítulo 4) num
único programa pequeno e real: um **relatório de frequência de palavras**, o coração de
todas as funcionalidades de "palavras mais comuns" que já viste.

As peças, todas as quais já tens:

- `.split()` -- a linha em palavras (4.4)
- o padrão de contagem -- contar cada palavra (5.9)
- `sorted()` -- ordenar o relatório (5.4). Uma nova conveniência: percorrer um
  dicionário visita as suas **chaves**, por isso `sorted(counts)` são simplesmente as chaves em
  ordem alfabética.
- imprimir uma palavra e a sua contagem numa linha (1.2)

## Exemplo

Para a linha `b a b`:

```python
counts = {"b": 2, "a": 1}
for w in sorted(counts):
    print(w, counts[w])
# a 1
# b 2
```

## A tua tarefa

Lê uma linha de palavras. Imprime uma linha por palavra **distinta** -- a palavra, um
espaço, e quantas vezes apareceu -- em ordem **alfabética**.

Para a entrada `tea milk tea`:

```
milk 1
tea 2
```

## Está feito quando

- `tea milk tea` imprime `milk 1` depois `tea 2` -- palavras distintas, ordem alfabética.
- Uma única palavra repetida imprime uma linha com a sua contagem total.
- Uma linha vazia não imprime nada.
- Usaste uma contagem com dicionário e `sorted()`.
""",

"5.10 hints": r"""Três passos: divide a linha, conta as palavras (5.9), depois imprime -- e
`sorted(counts)` dá as chaves do dicionário em ordem alfabética.

---

Depois do ciclo de contagem:  `for w in sorted(counts): print(w, counts[w])`.

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
for w in sorted(counts):
    print(w, counts[w])
""",

"5.10 reference": r"""Um **relatório de frequência de palavras** compõe as ferramentas do capítulo num pequeno pipeline:

1. **`split()`** o texto numa lista de palavras;
2. **conta**-as num dicionário de `palavra -> contagem` com `counts.get(w, 0) + 1`;
3. **`sorted`** os `dict.items()` para ordenar o relatório — por palavra, ou por contagem
   com `key=lambda kv: kv[1]` (e `reverse=True` para a mais frequente primeiro).

Cada passo é uma ferramenta que já conheces; a competência está em ver que uma tarefa real é a sua
composição.

```python
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
for word, n in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
    print(word, n)        # most frequent first
```
""",
}
