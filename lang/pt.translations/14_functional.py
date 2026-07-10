# PyQuest translations -- language 'pt' -- chapter 14_functional -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"14.1 brief": r"""# 14.1 -- lambda: uma função numa expressão

## Conceito

Uma **`lambda`** é uma função minúscula escrita em linha, sem nome e sem `def`:

```python
double = lambda x: x * 2
double(5)      # 10
```

- `lambda args: expression` -- o valor da expressão é devolvido
  automaticamente (sem `return`, e só é permitida uma expressão).
- Uma lambda é um **valor**, por isso podes guardá-la, **devolvê-la** de outra
  função, ou passá-la como argumento (é aí que ela realmente mostra o seu valor --
  o resto deste capítulo).

Como uma lambda é definida dentro de outra função, ela pode **capturar** as
variáveis dessa função. `lambda x: x * n` recorda o `n` do local onde foi criada.

(Para algo mais longo do que uma expressão, usa um `def` normal -- as lambdas
são para pequenas funções em linha.)

## Exemplo

```python
def adder(n):
    return lambda x: x + n     # remembers n
```

## A tua tarefa

Define `multiplier(n)` que **devolve uma lambda** que multiplica o seu argumento
por `n`. Assim, `multiplier(3)` devolve uma função, e chamar essa função com `4`
dá `12`.

## Está feito quando

- `multiplier(3)(4)` é `12`; `multiplier(10)(5)` é `50`.
- `multiplier(0)(7)` é `0`.
- A função devolvida é uma `lambda`, não um `def` aninhado.
""",

"14.1 hints": r"""Uma lambda é `lambda args: expression`. Queres uma que receba um `x` e devolva
`x * n`.

---

`multiplier` devolve essa lambda. A lambda captura `n`, por isso cada chamada a
`multiplier` cria uma função ligada ao seu próprio `n`.

---

def multiplier(n):
    return lambda x: x * n
""",

"14.1 reference": r"""Uma **`lambda`** é uma função anónima escrita como uma única expressão:
`lambda args: expression`. O valor da expressão é devolvido automaticamente —
não há `return`, e o corpo tem de ser **uma** expressão.

- Uma lambda é um **valor** de primeira classe: atribui-a, devolve-a, ou
  passa-a como argumento. `f = lambda x: x * 2` é muito semelhante a
  `def f(x): return x * 2`, só que em linha e sem nome.
- Definida dentro de outra função, uma lambda **captura** as variáveis desse
  âmbito — `lambda x: x * n` captura `n` do local onde foi criada, por isso cada
  `multiplier(n)` produz uma função ligada ao seu próprio `n`.
- As lambdas servem para funções em linha *pequenas*, especialmente como o
  `key=` de `sorted` ou a função para `map`/`filter` (o resto deste capítulo).
  Para algo com várias instruções, usa um `def` com nome.

```python
double = lambda x: x * 2
double(5)                  # 10

def multiplier(n):
    return lambda x: x * n
multiplier(3)(4)           # 12
```
""",

"14.2 brief": r"""# 14.2 -- map: aplicar a cada item

## Conceito

**`map(func, iterable)`** executa `func` em **cada** item e produz os
resultados. É o padrão "aplicar a cada" como função de ordem superior -- uma
função que recebe outra função:

```python
list(map(str.upper, ["a", "b"]))     # ['A', 'B']
list(map(lambda x: x * x, [1, 2, 3])) # [1, 4, 9]
```

- `map` devolve um **iterador preguiçoso**, por isso envolve-o em `list(...)`
  para obteres uma lista.
- A função pode ser uma `lambda`, um `def`, ou uma função nativa como
  `str.upper` ou `int`.

(Uma compreensão de lista `[f(x) for x in items]` faz a mesma coisa e muitas
vezes lê-se de forma mais natural; este puzzle é sobre aprender o próprio `map`,
a ferramenta que vais encontrar em imenso código.)

## Exemplo

```python
def lengths(words):
    return list(map(len, words))
```

## A tua tarefa

Usando **`map`**, define `squares(nums)` que devolve uma lista com cada
número de `nums` elevado ao quadrado.

## Está feito quando

- `squares([1, 2, 3])` devolve `[1, 4, 9]`.
- `squares([])` devolve `[]`.
- O mapeamento é feito com `map`, não com uma compreensão ou um ciclo manual.
""",

"14.2 hints": r"""`map(func, nums)` aplica `func` a cada número. A tua `func` eleva a entrada ao
quadrado: `lambda x: x * x`.

---

`map` é preguiçoso, por isso envolve-o: `list(map(lambda x: x * x, nums))`.

---

def squares(nums):
    return list(map(lambda x: x * x, nums))
""",

"14.2 reference": r"""**`map(func, iterable)`** aplica `func` a cada item e produz os resultados —
o padrão "transformar cada item" como função de ordem superior (uma que recebe
outra função como argumento).

- Devolve um **iterador preguiçoso**, calculando cada resultado à medida da
  necessidade; envolve-o em `list(...)` (ou `tuple`, ou alimenta um `for`) para
  o consumir.
- `func` pode ser uma `lambda`, um `def` com nome, ou qualquer chamável — uma
  função nativa como `len`, `str.upper`, ou `int` é comum.
- Dados vários iteráveis, `map(func, a, b)` chama `func(a_i, b_i)` em
  sincronia, parando no mais curto.
- Uma compreensão de lista `[func(x) for x in items]` exprime a mesma coisa e
  é muitas vezes mais clara; `map` é o equivalente em estilo funcional que vais
  ver com frequência.

```python
list(map(len, ["hi", "there"]))        # [2, 5]
list(map(lambda x: x * x, [1, 2, 3]))  # [1, 4, 9]
list(map(int, ["1", "2", "3"]))        # [1, 2, 3]
```
""",

"14.3 brief": r"""# 14.3 -- filter: manter o que passa

## Conceito

Enquanto `map` transforma cada item, **`filter`** mantém apenas **alguns**
deles. Dás-lhe um **predicado** -- uma função que devolve verdadeiro ou falso --
e ele mantém cada item ao qual o predicado diz que sim:

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))     # [2, 4]
```

- `filter(pred, iterable)` produz cada item para o qual `pred(item)` é
  verdadeiro, descartando o resto, por ordem.
- Tal como `map`, devolve um **iterador preguiçoso**, por isso envolve-o em
  `list(...)`.

(A compreensão `[x for x in items if pred(x)]` faz o mesmo; este puzzle é
sobre o próprio `filter`.)

## Exemplo

```python
def nonempty(strings):
    return list(filter(lambda s: s != "", strings))
```

## A tua tarefa

Usando **`filter`**, define `evens(nums)` que devolve uma lista apenas com os
números pares em `nums`.

## Está feito quando

- `evens([1, 2, 3, 4])` devolve `[2, 4]`.
- `evens([1, 3, 5])` devolve `[]`.
- A seleção é feita com `filter`, não com uma compreensão ou um ciclo manual.
""",

"14.3 hints": r"""`filter(pred, nums)` mantém cada número onde `pred` é verdadeiro. O teu
predicado testa a paridade: `lambda x: x % 2 == 0`.

---

Envolve-o em `list(...)`: `list(filter(lambda x: x % 2 == 0, nums))`.

---

def evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
""",

"14.3 reference": r"""**`filter(pred, iterable)`** mantém os itens para os quais o **predicado**
`pred` (uma função que devolve verdadeiro ou falso) é verdadeiro, descartando o
resto — a contrapartida "mantém se" do "transforma cada" de `map`.

- Devolve um **iterador preguiçoso** pela ordem original; envolve-o em
  `list(...)` para recolher.
- `pred` é qualquer chamável que devolva um valor verdadeiro/falso — uma
  `lambda`, um `def`, ou uma função nativa. Passar **`None`** como predicado
  (`filter(None, items)`) mantém os itens que são, eles próprios, verdadeiros,
  descartando `0`, `""`, `None`, etc.
- A compreensão `[x for x in items if pred(x)]` é o equivalente e muitas
  vezes lê-se melhor; `filter` é a forma funcional.

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))   # [2, 4]
list(filter(None, [0, 1, "", "a", None]))        # [1, 'a']
list(filter(str.isalpha, "a1b2"))                # ['a', 'b']
```
""",

"14.4 brief": r"""# 14.4 -- sorted(key=lambda): ordenar por um valor derivado

## Conceito

`sorted` (capítulo 5) ordena os itens pela sua ordem natural. O seu argumento
**`key=`** muda *aquilo* por que ordena: uma função que faz corresponder cada
item ao valor a comparar. Uma **lambda** em linha é a forma habitual de a
escrever:

```python
words = ["pear", "fig", "apple"]
sorted(words, key=len)                  # ['fig', 'pear', 'apple']
sorted(words, key=lambda w: w[-1])      # by last letter
```

- `key` é chamada uma vez por item; `sorted` ordena então os itens por esses
  valores-chave.
- A lambda permite ordenar por qualquer coisa **derivada** de um item -- o
  seu comprimento, um campo, uma pontuação calculada -- sem alterar os próprios
  itens.
- `sorted` é **estável**: itens com chaves iguais mantêm a sua ordem
  original.

## Exemplo

```python
def by_size(nums):
    return sorted(nums, key=lambda n: abs(n))   # by distance from zero
```

## A tua tarefa

Usando **`sorted`** com um **`key=lambda`**, define `by_last(words)` que
devolve as palavras ordenadas pelo seu **último caráter**.

## Está feito quando

- `by_last(["pear", "fig", "kiwi"])` devolve `["fig", "kiwi", "pear"]`
  (as últimas letras g, i, r estão por ordem).
- `by_last([])` devolve `[]`.
- A ordem vem de `sorted(..., key=lambda ...)`, não de uma ordenação manual.
""",

"14.4 hints": r"""`sorted(words, key=...)` ordena pelo que quer que a função `key` devolva.
Queres ordenar pelo último caráter de cada palavra.

---

O último caráter de `w` é `w[-1]`, por isso a chave é `lambda w: w[-1]`:
`sorted(words, key=lambda w: w[-1])`.

---

def by_last(words):
    return sorted(words, key=lambda w: w[-1])
""",

"14.4 reference": r"""O argumento **`key=`** de `sorted` é uma função que faz corresponder cada
item ao valor pelo qual ordenar, permitindo-te ordenar por algo **derivado** dos
itens em vez dos próprios itens. Uma **`lambda`** em linha é a forma idiomática
de escrever essa chave.

- `key` é chamada **uma vez por item**; `sorted` ordena os itens pelos
  valores-chave resultantes, mas devolve os itens originais. `sorted(words,
  key=len)` ordena por comprimento, `sorted(words, key=lambda w: w[-1])` pela
  última letra.
- `sorted` é **estável**: itens com chaves iguais mantêm a ordem de entrada.
- Combina `key=` com **`reverse=True`** para ordenar de forma decrescente. O
  mesmo `key=` funciona em `list.sort`, `min`, e `max`.

```python
sorted(["pear", "fig", "apple"], key=len)            # ['fig', 'pear', 'apple']
sorted([-3, 1, -2], key=lambda n: abs(n))            # [1, -2, -3]
sorted(records, key=lambda r: r[1], reverse=True)    # by 2nd field, high first
```
""",

"14.5 brief": r"""# 14.5 -- any: há pelo menos um verdadeiro?

## Conceito

**`any(iterable)`** devolve `True` se **pelo menos um** item for verdadeiro,
`False` caso contrário. Alimentado com um gerador de testes, responde a
"*algum* item passa?":

```python
any(n < 0 for n in [1, 2, -3])     # True
any(n < 0 for n in [1, 2, 3])      # False
```

- Substitui o ciclo com uma bandeira (`found = False; for ...: if ...: found =
  True`) por uma única expressão.
- Tem **avaliação abreviada**: para e devolve `True` no primeiro item
  verdadeiro.
- `any([])` é `False` (nada passou).

O padrão é `any(<test> for <item> in <iterable>)` -- uma expressão geradora de
booleanos passada a `any`.

## Exemplo

```python
def has_blank(strings):
    return any(s == "" for s in strings)
```

## A tua tarefa

Usando **`any`**, define `has_negative(nums)` que devolve `True` se `nums`
contiver pelo menos um número negativo.

## Está feito quando

- `has_negative([1, 2, -3])` é `True`; `has_negative([1, 2, 3])` é `False`.
- `has_negative([])` é `False`.
- A resposta vem de `any(...)`, não de um ciclo escrito à mão com uma
  bandeira.
""",

"14.5 hints": r"""`any(...)` recebe uma sequência de valores verdadeiro/falso e devolve True se
algum for verdadeiro. Constrói essa sequência com uma expressão geradora.

---

`any(n < 0 for n in nums)` -- para cada número, o teste `n < 0` é True ou
False, e `any` informa se pelo menos um foi True.

---

def has_negative(nums):
    return any(n < 0 for n in nums)
""",

"14.5 reference": r"""**`any(iterable)`** devolve `True` assim que **um** item é verdadeiro, caso
contrário `False`. Recebendo um gerador de testes, responde a "algum item
passa?" numa única expressão, substituindo um ciclo que define uma bandeira.

- Tem **avaliação abreviada**: a avaliação para no primeiro item verdadeiro,
  por isso é eficiente e funciona em iteráveis infinitos/preguiçosos.
- `any([])` é `False` — não há nada que seja verdadeiro.
- O idioma é `any(<test> for <item> in <iterable>)`: uma expressão geradora de
  booleanos. (O seu parceiro `all` é o 14.6.)

```python
any(n < 0 for n in [1, 2, -3])    # True
any(c.isdigit() for c in "abc")   # False
any([])                           # False
```
""",

"14.6 brief": r"""# 14.6 -- all: são todos verdadeiros?

## Conceito

**`all(iterable)`** é o parceiro de `any`: devolve `True` apenas se **todos**
os itens forem verdadeiros. Responde a "passam *todos*?":

```python
all(n > 0 for n in [1, 2, 3])      # True
all(n > 0 for n in [1, -2, 3])     # False
```

- Tem **avaliação abreviada** no sentido oposto: para e devolve `False` no
  primeiro item que falha.
- `all([])` é `True` -- vacuamente, já que nenhum item falhou. (Uma surpresa
  comum: "todos de nada" é verdadeiro.)

Mesma forma que `any`: `all(<test> for <item> in <iterable>)`.

## Exemplo

```python
def all_words(strings):
    return all(s.isalpha() for s in strings)
```

## A tua tarefa

Usando **`all`**, define `all_positive(nums)` que devolve `True` se **todos**
os números em `nums` forem maiores que zero.

## Está feito quando

- `all_positive([1, 2, 3])` é `True`; `all_positive([1, -2, 3])` é `False`.
- `all_positive([])` é `True` (nada falha).
- A resposta vem de `all(...)`, não de um ciclo escrito à mão com uma
  bandeira.
""",

"14.6 hints": r"""`all(...)` devolve True apenas se todos os valores na sequência forem
verdadeiros. Constrói a sequência de testes com uma expressão geradora.

---

`all(n > 0 for n in nums)` -- cada `n > 0` é True ou False, e `all` é True
apenas se nenhum for False.

---

def all_positive(nums):
    return all(n > 0 for n in nums)
""",

"14.6 reference": r"""**`all(iterable)`** devolve `True` apenas se **todos** os itens forem
verdadeiros — o parceiro de `any`. Responde a "passam todos?" numa única
expressão.

- Tem **avaliação abreviada** no primeiro item falso, devolvendo `False`
  imediatamente.
- `all([])` é `True` — *vacuamente*, já que nenhum item falhou. Esta regra de
  "todos de nada é verdadeiro" é uma surpresa comum; protege-te contra o caso
  vazio se isso importar.
- Mesma forma que `any`: `all(<test> for <item> in <iterable>)`. Juntos,
  exprimem as questões universal ("para todos") e existencial ("existe") sobre
  uma sequência.

```python
all(n > 0 for n in [1, 2, 3])     # True
all(n > 0 for n in [1, -2, 3])    # False
all([])                           # True  -- vacuously
```
""",

"14.7 brief": r"""# 14.7 -- reduce: dobrar uma sequência num único valor

## Conceito

**`reduce`** (de `functools`) **dobra** uma sequência inteira num único valor,
aplicando uma função de dois argumentos cumulativamente, da esquerda para a
direita:

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])     # 10  ((((1+2)+3)+4))
reduce(lambda a, b: a * b, [1, 2, 3, 4])     # 24
```

- `reduce(func, items)` calcula `func(func(func(i0, i1), i2), i3)...` -- cada
  passo combina o resultado corrente com o próximo item.
- Um terceiro argumento é um valor **inicial**: `reduce(func, items, start)`
  começa a dobragem a partir de `start`, que também define a resposta para uma
  sequência **vazia**.
- É o ciclo acumulador (capítulo 3) como função de ordem superior. (`sum` é o
  caso especial para `+`; `reduce` permite-te dobrar com *qualquer*
  combinador.)

## Exemplo

```python
from functools import reduce

def total(nums):
    return reduce(lambda a, b: a + b, nums, 0)
```

## A tua tarefa

Usando **`reduce`** de `functools`, define `product(nums)` que devolve o
produto de todos os números (com um valor inicial de `1`, para que a lista
vazia dê `1`).

## Está feito quando

- `product([1, 2, 3, 4])` devolve `24`; `product([5])` devolve `5`.
- `product([])` devolve `1`.
- A dobragem usa `reduce`, não um ciclo acumulador manual.
""",

"14.7 hints": r"""`from functools import reduce`. Recebe um combinador de dois argumentos, os
itens, e um valor inicial.

---

O combinador multiplica o resultado corrente pelo próximo número:
`reduce(lambda a, b: a * b, nums, 1)`. O valor inicial `1` faz com que a lista
vazia dê 1.

---

from functools import reduce


def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)
""",

"14.7 reference": r"""**`functools.reduce(func, iterable[, start])`** **dobra** uma sequência num
único valor, aplicando uma `func` de dois argumentos cumulativamente, da
esquerda para a direita: `func(func(func(i0, i1), i2), i3)...`. Cada passo
combina o resultado corrente com o próximo item.

- Um valor **inicial** (`reduce(func, items, start)`) semeia a dobragem e
  define o resultado para uma sequência **vazia**; sem ele, reduzir um
  iterável vazio lança `TypeError`.
- Generaliza o ciclo acumulador para *qualquer* combinador: `+` dá uma soma,
  `*` um produto, `max` o maior. O `sum` dedicado é o caso especial de `+`, e
  `math.prod` o de `*` — mas `reduce` dobra com a função que fornecires.
- `reduce` vive em `functools` (não é uma função nativa), por isso tem de ser
  importada.

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])      # 10
reduce(lambda a, b: a * b, [1, 2, 3, 4], 1)   # 24
reduce(lambda a, b: a if a > b else b, [3, 9, 2])   # 9  (max)
```
""",

"14.8 brief": r"""# 14.8 -- Capstone: uma lista restrita classificada

## Conceito

As ferramentas do capítulo encadeiam-se num **pipeline**. Dada uma lista de
registos `(name, score)`, constrói uma lista restrita:

1. **`filter`** para os registos que atingem um limiar,
2. **`sorted`** com um `key=lambda` (e `reverse=True`) para os classificar do
mais alto para o mais baixo,
3. **`map`** para extrair apenas os nomes.

```python
records = [("Ada", 90), ("Linus", 70), ("Grace", 95)]
qualified = filter(lambda r: r[1] >= 80, records)
ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
list(map(lambda r: r[0], ranked))     # ['Grace', 'Ada']
```

Cada registo é um tuplo, por isso `r[0]` é o nome e `r[1]` a pontuação.

## A tua tarefa

Define `passing(records, threshold)` que recebe uma lista de tuplos `(name,
score)` e devolve os **nomes** daqueles com `score >= threshold`, ordenados
pela pontuação **da mais alta para a mais baixa**, construído com `filter`,
`sorted(key=lambda ...)`, e `map`.

## Está feito quando

- `passing([("Ada", 90), ("Linus", 70), ("Grace", 95)], 80)` devolve
  `["Grace", "Ada"]`.
- `passing([], 50)` devolve `[]`; um limiar acima de todas as pontuações
  devolve `[]`.
- O resultado é construído filtrando, ordenando por uma chave lambda, e
  mapeando -- um pipeline das ferramentas do capítulo.
""",

"14.8 hints": r"""Três passos. Primeiro, `filter(lambda r: r[1] >= threshold, records)` mantém
os registos que se qualificam (r[1] é a pontuação).

---

Depois, `sorted(qualified, key=lambda r: r[1], reverse=True)` classifica-os
do mais alto para o mais baixo, e `map(lambda r: r[0], ...)` extrai os nomes.
Envolve o map em `list`.

---

def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
""",

"14.8 reference": r"""O capstone encadeia as funções de ordem superior do capítulo num **pipeline
de dados** — a forma de muito processamento real:

1. **`filter(lambda r: r[1] >= threshold, records)`** restringe aos registos
   que se qualificam;
2. **`sorted(..., key=lambda r: r[1], reverse=True)`** classifica-os por
   pontuação, do mais alto para o mais baixo (estável, por isso pontuações
   iguais mantêm a sua ordem);
3. **`map(lambda r: r[0], ...)`** projeta apenas o campo que queres — o nome.

Cada etapa recebe uma função e um iterável e produz outro iterável, por isso
compõem-se diretamente: o filter alimenta o sort, o sort alimenta o map. O
mesmo pipeline podia ser escrito com compreensões; expressá-lo como
`filter`/`sorted`/`map` é o estilo funcional, e ver uma tarefa *como* um
pipeline de transformações é a competência para a qual o capítulo conduz.

```python
def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
```
""",
}
