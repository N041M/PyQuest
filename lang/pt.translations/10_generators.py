# PyQuest translations -- language 'pt' -- chapter 10_generators -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"10.1 brief": r"""# 10.1 -- yield: uma função que pausa

## Conceito

Uma função normal faz `return` **uma vez** e está feita. Um **gerador** é uma
função que usa `yield` em vez disso: cada `yield` devolve **um** valor e
**pausa** a função exatamente ali. Pede o próximo valor e ela **retoma**
a partir de onde parou.

```python
def two_words():
    yield "hello"
    yield "world"
```

Chamá-la **não** executa o corpo. Dá-te um **gerador** -- um objeto de onde
retiras valores, um de cada vez, normalmente com um ciclo `for`:

```python
for w in two_words():
    print(w)        # hello, then world
```

A recompensa: um gerador produz uma sequência **sem construir a lista toda
em memória**. Vais sentir isso em 10.3.

## Exemplo

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1
```

`list(count_up(3))` é `[1, 2, 3]` -- cada passagem do ciclo produz um número,
depois pausa até que o próximo seja pedido.

## A tua tarefa

Define um gerador `count_down(n)` que **produz** os números inteiros de `n`
até `1`, por essa ordem. Se `n` for `0` (ou menos), não produz nada.

## Está feito quando

- `list(count_down(5))` é `[5, 4, 3, 2, 1]`.
- `list(count_down(1))` é `[1]`; `list(count_down(0))` é `[]`.
- Usas `yield` -- portanto chamar `count_down` devolve um gerador, não uma
  lista.
""",

"10.1 hints": r"""Um gerador parece uma função normal, mas diz `yield` onde uma normal
construiria um resultado. Cada `yield` produz um número.

---

Conta com um ciclo de `n` para baixo e faz `yield` de cada valor. Um ciclo
`while`: começa `i` em `n`, `yield i`, depois `i = i - 1`, enquanto
`i >= 1`. (Um `for i in range(n, 0, -1):` também funciona.)

---

def count_down(n):
    i = n
    while i >= 1:
        yield i
        i = i - 1
""",

"10.1 reference": r"""Uma função que contém **`yield`** é uma **função geradora**. Chamá-la não
executa o corpo — devolve um **objeto gerador** que produz valores um de
cada vez, **pausando** em cada `yield` e retomando de onde parou quando é
pedido o seguinte.

- Cada `yield valor` entrega um valor a quem está a iterar, depois congela o
  estado da função até que o próximo valor seja pedido.
- Consomes um gerador iterando-o (`for x in gen:`) ou com `next(gen)`.
- Isto difere de `return`, que devolve **um** valor e termina a função
  definitivamente.

```python
def two():
    yield 1
    yield 2

for n in two():
    print(n)            # 1, then 2
```
""",

"10.2 brief": r"""# 10.2 -- yield dentro de um ciclo

## Conceito

O verdadeiro poder do `yield` aparece quando está **dentro de um ciclo**: uma
linha `yield` executa uma vez por passagem, transmitindo em fluxo uma
sequência transformada inteira -- um valor de cada vez, nunca a lista toda de
uma vez.

```python
def letters(word):
    for ch in word:
        yield ch.upper()
```

`list(letters("hi"))` é `["H", "I"]`. O ciclo percorre a entrada; o `yield`
emite um item transformado de cada vez, pausando entre eles.

## Exemplo

```python
def doubles(nums):
    for x in nums:
        yield x * 2
```

`list(doubles([1, 5, 9]))` é `[2, 10, 18]`.

## A tua tarefa

Define um gerador `squares(n)` que **produz** os quadrados dos números
inteiros de `0` até (mas sem incluir) `n`: `0, 1, 4, 9, ...`. Se `n` for `0`
(ou menos), não produz nada.

## Está feito quando

- `list(squares(4))` é `[0, 1, 4, 9]`.
- `list(squares(1))` é `[0]`; `list(squares(0))` é `[]`.
- Usas `yield` dentro de um ciclo -- não uma lista devolvida nem uma
  compreensão.
""",

"10.2 hints": r"""Percorre os números `0, 1, ..., n-1` com um ciclo, e faz `yield` de cada um
elevado ao quadrado.

---

`for i in range(n):` depois `yield i * i`. O ciclo dá-te cada número; o
yield emite o seu quadrado e pausa até que o próximo seja pedido.

---

def squares(n):
    for i in range(n):
        yield i * i
""",

"10.2 reference": r"""Colocar um **`yield` dentro de um ciclo** transmite uma sequência inteira em
fluxo: o gerador emite um valor transformado por passagem, pausando após
cada um e retomando no pedido seguinte.

- `for x in source: yield f(x)` produz `f(x)` para cada item — a forma
  geradora de construir uma lista com uma compreensão, mas produzida de
  forma preguiçosa.
- Nada é calculado até que algo itere o gerador, e só até onde for consumido.

```python
def squares(nums):
    for n in nums:
        yield n * n

list(squares([1, 2, 3]))    # [1, 4, 9]
```
""",

"10.3 brief": r"""# 10.3 -- os geradores são preguiçosos

## Conceito

Este é o superpoder. Um gerador só faz trabalho **quando pedes o próximo
valor**. Nunca constrói a sequência toda antecipadamente -- portanto um
gerador pode ser **infinito** e ainda assim custar quase nada até retirares
dele.

```python
def naturals():
    i = 0
    while True:        # never stops on its own...
        yield i
        i = i + 1
```

`while True` numa função normal ficaria pendurado para sempre. Num gerador
está tudo bem: cada `yield` **pausa** o ciclo até que quem chama queira mais
um. Retiras apenas quantos precisares:

```python
from itertools import islice
list(islice(naturals(), 4))     # [0, 1, 2, 3] -- then it just stops asking
```

`islice(gen, k)` retira os primeiros `k` itens de um gerador e nada mais. O
gerador produz exatamente esses quatro, depois fica pausado.

## Exemplo

O `naturals()` acima produz `0, 1, 2, 3, ...` sem fim. Retirar 3 itens dá
`[0, 1, 2]`; retirar 10 dá `[0, 1, ..., 9]`. O mesmo gerador infinito,
pedido em quantidades diferentes.

## A tua tarefa

Define um gerador **infinito** `naturals()` que produz os números inteiros a
começar em `0`: `0, 1, 2, 3, ...` para sempre. Nunca se pode parar sozinho; o
verificador só alguma vez retira um punhado de valores dele.

## Está feito quando

- Os primeiros 5 valores de `naturals()` são `[0, 1, 2, 3, 4]`.
- É infinito -- retirar mais valores dá simplesmente mais números; nunca se
  esgota.
- Usas `yield`, portanto chamar `naturals()` devolve um gerador.
""",

"10.3 hints": r"""Precisas de um ciclo que nunca termina, produzindo um contador que sobe um
de cada vez. O `yield` é o que o impede de ficar pendurado.

---

Começa `i` em `0`. Depois `while True:` -- `yield i`, depois `i = i + 1`. O
ciclo "nunca termina", mas cada yield pausa-o até que o próximo valor seja
pedido.

---

def naturals():
    i = 0
    while True:
        yield i
        i = i + 1
""",

"10.3 reference": r"""Os geradores são **preguiçosos**: cada valor só é calculado quando pedido,
por isso um gerador pode descrever uma sequência **infinita** e ainda assim
ser útil — retiras apenas os valores de que precisas.

- Um `while True: yield n; n += 1` infinito nunca termina sozinho, mas quem
  consome pode parar mais cedo (um `break`, ou `next` chamado algumas
  vezes).
- A preguiça significa que um gerador guarda essencialmente **nenhuma
  memória** para a sequência — guarda apenas o seu estado atual, não cada
  valor — ao contrário de uma lista que os materializa todos.

```python
def naturals():
    n = 0
    while True:
        yield n             # endless, but only as far as asked
        n += 1

g = naturals(); next(g), next(g)   # (0, 1)
```
""",

"10.4 brief": r"""# 10.4 -- um gerador tem memória

## Conceito

Porque um gerador **pausa** em vez de terminar, as suas variáveis locais
mantêm-se vivas entre `yield`s. Um valor que vais construindo sobrevive a
cada pausa -- o gerador retoma exatamente onde parou, acumulador e tudo.

```python
def tally(words):
    seen = 0
    for w in words:
        seen = seen + 1
        yield seen          # 1, then 2, then 3, ... -- `seen` is remembered
```

`list(tally(["a", "b", "c"]))` é `[1, 2, 3]`. O contador `seen` não é
reposto a cada passagem; mantém o seu valor ao longo dos yields.

## Exemplo

```python
def running_max(nums):
    best = None
    for n in nums:
        if best is None or n > best:
            best = n
        yield best
```

`list(running_max([3, 1, 5]))` é `[3, 3, 5]` -- cada item é o maior visto
**até agora**.

## A tua tarefa

Define um gerador `running_total(nums)` que produz a **soma acumulada** de
`nums`: cada valor é o total de todos os números até e incluindo o atual.
Uma lista vazia não produz nada.

## Está feito quando

- `list(running_total([3, 1, 2]))` é `[3, 4, 6]`.
- `list(running_total([5]))` é `[5]`; `list(running_total([]))` é `[]`.
- Usas `yield`, e uma variável que transporta o total ao longo dos yields.
""",

"10.4 hints": r"""Mantém uma variável `total` fora do ciclo, soma-lhe cada número dentro do
ciclo, e faz `yield` do total após cada adição.

---

`total = 0` antes do ciclo. Depois `for n in nums:` -- `total = total + n`,
depois `yield total`. O total é recordado ao longo dos yields, por isso
continua a crescer.

---

def running_total(nums):
    total = 0
    for n in nums:
        total = total + n
        yield total
""",

"10.4 reference": r"""Um gerador **recorda** as suas variáveis locais entre `yield`s: a execução
congela no `yield` e cada variável local mantém o seu valor até que o
próximo pedido retome a função. Isto permite que um gerador **transporte
estado** enquanto transmite em fluxo.

- Uma variável atualizada no ciclo (um total acumulado, um valor anterior)
  persiste entre yields sem qualquer objeto ou variável global.
- É isto que faz de um gerador um **acumulador corrente** natural — uma soma
  acumulada, por exemplo, que emite o total até então a cada passo.

```python
def running_sum(nums):
    total = 0
    for n in nums:
        total += n          # total survives across yields
        yield total

list(running_sum([1, 2, 3]))    # [1, 3, 6]
```
""",

"10.5 brief": r"""# 10.5 -- filtrar enquanto produzes

## Conceito

Um gerador não tem de produzir a cada passagem. Coloca o `yield` atrás de um
`if`, e **filtras** o fluxo à medida que corre -- saltando os itens que não
queres, emitindo apenas os que queres.

```python
def shouts(words):
    for w in words:
        if w.isupper():
            yield w          # only the all-caps words come out
```

`list(shouts(["hi", "STOP", "go", "NOW"]))` é `["STOP", "NOW"]`. O ciclo
visita cada palavra; o `yield` só executa quando o `if` é verdadeiro.

## Exemplo

```python
def positives(nums):
    for n in nums:
        if n > 0:
            yield n
```

`list(positives([-1, 4, 0, 2]))` é `[4, 2]`.

## A tua tarefa

Define um gerador `evens(nums)` que produz apenas os números **pares** de
`nums`, mantendo a sua ordem original. (Um número é par quando
`n % 2 == 0`.) Se nenhum for par, não produz nada.

## Está feito quando

- `list(evens([1, 2, 3, 4]))` é `[2, 4]`.
- `list(evens([1, 3, 5]))` é `[]`; `list(evens([]))` é `[]`.
- Usas `yield` atrás de um `if` -- não uma lista devolvida nem uma
  compreensão.
""",

"10.5 hints": r"""Percorre cada número, mas faz `yield` apenas dos que passam um teste de
paridade.

---

`for n in nums:` depois `if n % 2 == 0:` e, indentado sob o if, `yield n`.
Os números ímpares simplesmente passam sem serem produzidos.

---

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
""",

"10.5 reference": r"""Colocar **`yield` atrás de um `if`** filtra um fluxo à medida que corre: o
gerador emite apenas os itens que passam o teste e salta silenciosamente os
restantes — o equivalente preguiçoso da cláusula `if` de uma compreensão.

- `for x in source: if test(x): yield x` produz um fluxo filtrado sem
  construir qualquer lista intermédia.
- Por ser preguiçoso, compõe-se de forma limpa: um gerador de filtro pode
  alimentar outro gerador, cada um a tratar de uma etapa.

```python
def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n         # only the evens make it out

list(evens(range(10)))      # [0, 2, 4, 6, 8]
```
""",

"10.6 brief": r"""# 10.6 -- yield from: passar um fluxo inteiro adiante

## Conceito

Quando queres que um gerador reemita **todos** os itens de outro iterável,
podias percorrê-lo e fazer `yield` de cada um:

```python
def both(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
```

O Python tem um atalho para exatamente esse ciclo interno: **`yield from`**.

```python
def both(a, b):
    yield from a        # yield every item of a, one by one
    yield from b        # then every item of b
```

`yield from iterável` significa "faz yield de cada valor que este iterável
produz". As duas versões acima comportam-se de forma idêntica; `yield from`
apenas o diz numa linha.

## Exemplo

```python
def repeat_each(items):
    for x in items:
        yield from (x, x)      # yield x, then x again

list(repeat_each([1, 2]))      # [1, 1, 2, 2]
```

## A tua tarefa

Define um gerador `chain(a, b)` que produz **todos** os itens de `a`, depois
**todos** os itens de `b`, por ordem. Usa `yield from`. Qualquer uma das
listas pode estar vazia.

## Está feito quando

- `list(chain([1, 2], [3, 4]))` é `[1, 2, 3, 4]`.
- `list(chain([], [9]))` é `[9]`; `list(chain([], []))` é `[]`.
- Usas `yield from`, portanto chamar `chain` devolve um gerador.
""",

"10.6 hints": r"""Queres reemitir cada item de `a`, depois cada item de `b`. `yield from` faz
exatamente isso para um iterável de cada vez.

---

Duas linhas: `yield from a` depois `yield from b`. Cada uma transmite essa
lista inteira para a saída do gerador.

---

def chain(a, b):
    yield from a
    yield from b
""",

"10.6 reference": r"""**`yield from iterável`** reemite **todos** os itens que o iterável produz,
como se tivesses escrito um ciclo de `yield`s. Delega um subfluxo inteiro
numa linha.

- `yield from sub` é equivalente a `for x in sub: yield x`, mas mais curto e
  mais rápido — e funciona com listas, intervalos, outros geradores,
  qualquer iterável.
- É a ferramenta para **achatar** ou **encadear**: um gerador pode fazer
  `yield from` de várias fontes sucessivamente para unir os seus fluxos.

```python
def chain(a, b):
    yield from a
    yield from b            # splice two streams into one

list(chain([1, 2], [3, 4]))     # [1, 2, 3, 4]
```
""",

"10.7 brief": r"""# 10.7 -- parar mais cedo

## Conceito

Um gerador termina no momento em que a sua função termina -- e um `return`
simples (sem valor) dentro de um gerador significa "para agora, sem mais
itens". Portanto um gerador pode decidir **terminar mais cedo**, antes de a
entrada se esgotar.

```python
def before_blank(words):
    for w in words:
        if w == "":
            return          # stop the generator here
        yield w
```

`list(before_blank(["a", "b", "", "c"]))` é `["a", "b"]` -- assim que se
chega ao vazio, o `return` termina o gerador e `"c"` nunca é produzido.

## Exemplo

```python
def while_positive(nums):
    for n in nums:
        if n <= 0:
            return
        yield n

list(while_positive([3, 1, -1, 5]))    # [3, 1]
```

## A tua tarefa

Define um gerador `until_zero(nums)` que produz cada número **até chegar a
um `0`**, depois para. O próprio `0`, e tudo depois dele, **não** é
produzido. Se não houver nenhum `0`, produz a lista toda.

## Está feito quando

- `list(until_zero([1, 2, 0, 3]))` é `[1, 2]`.
- `list(until_zero([0, 9]))` é `[]`; `list(until_zero([1, 2, 3]))` é
  `[1, 2, 3]`.
- Usas `yield`, e paras mais cedo quando encontras um `0`.
""",

"10.7 hints": r"""Percorre os números. Assim que vires um `0`, para o gerador inteiro; caso
contrário faz `yield` do número.

---

`for n in nums:` -- primeiro `if n == 0: return` (isto termina o gerador),
depois `yield n` para tudo antes do zero.

---

def until_zero(nums):
    for n in nums:
        if n == 0:
            return
        yield n
""",

"10.7 reference": r"""Um **`return`** simples dentro de um gerador — ou simplesmente chegar ao fim
da função — **para-o**: a iteração termina e não chegam mais valores.
`return` num gerador não transporta **nenhum valor**; apenas assinala
"terminado".

- Isto permite que um gerador **pare mais cedo** por uma condição:
  `if x == sentinela: return` termina o fluxo nesse ponto.
- Para um ciclo `for`, um gerador parado é apenas um iterável que se
  esgotou — o ciclo termina naturalmente (internamente, o gerador levanta
  `StopIteration`).

```python
def until_zero(nums):
    for n in nums:
        if n == 0:
            return          # stop the stream here
        yield n

list(until_zero([3, 1, 0, 9]))  # [3, 1]
```
""",

"10.8 brief": r"""# 10.8 -- Peça de resistência: um pipeline em fluxo

## Conceito

Nada de novo -- esta peça de resistência é o capítulo em miniatura. A razão
real por que os geradores importam é que **se compõem**: a saída de um
gerador é a entrada de outro, por isso os dados fluem através de um
**pipeline**, um item de cada vez, sem nunca construir a lista completa
pelo meio.

Uma etapa de pipeline é apenas um gerador que percorre `stream` (qualquer
iterável -- uma lista, ou *outro gerador*) e vai produzindo à medida que
avança:

```python
def only_long(stream):
    for word in stream:
        if len(word) >= 4:
            yield word
```

Vais construir uma fonte, um filtro e uma etapa de reetiquetagem, depois
ligá-las entre si.

## Exemplo

```python
numbers(4)                              # yields 0, 1, 2, 3
keep_even(numbers(4))                   # yields 0, 2
labelled(keep_even(numbers(4)))         # yields "#0", "#2"
```

## A tua tarefa

Define **três** geradores:

- `numbers(n)` -- produz `0, 1, ..., n-1` (a fonte). `n <= 0` não produz
  nada.
- `keep_even(stream)` -- produz apenas os números pares de `stream`
  (qualquer iterável).
- `labelled(stream)` -- produz a cadeia de caracteres `"#x"` para cada `x`
  em `stream` (por exemplo, `7` torna-se `"#7"`).

Cada um tem de usar `yield`. `keep_even` e `labelled` têm de funcionar em
**qualquer** stream, incluindo a saída de outro gerador, para que se
componham.

## Está feito quando

- `list(numbers(4))` é `[0, 1, 2, 3]`; `list(numbers(0))` é `[]`.
- `list(keep_even([1, 2, 3, 4]))` é `[2, 4]`.
- `list(labelled([0, 2]))` é `["#0", "#2"]`.
- `list(labelled(keep_even(numbers(6))))` é `["#0", "#2", "#4"]`.
- Os três usam `yield`, e as etapas de filtro/reetiquetagem aceitam
  qualquer iterável.
""",

"10.8 hints": r"""Cada etapa é o seu próprio pequeno gerador. `numbers` percorre `range(n)` e
produz; `keep_even` percorre `stream` e produz apenas os pares; `labelled`
percorre `stream` e produz uma cadeia de caracteres formatada. Nenhum deles
constrói uma lista.

---

`keep_even` e `labelled` recebem um `stream` e `for x in stream:` -- esse
ciclo funciona quer `stream` seja uma lista quer outro gerador, o que é o
que te permite aninhá-los. Usa uma f-string para a etiqueta:
`yield f"#{x}"`.

---

def numbers(n):
    for i in range(n):
        yield i


def keep_even(stream):
    for x in stream:
        if x % 2 == 0:
            yield x


def labelled(stream):
    for x in stream:
        yield f"#{x}"
""",

"10.8 reference": r"""A peça de resistência compõe geradores num **pipeline em fluxo**: um
gerador **fonte** alimenta um gerador **filtro**, que alimenta um gerador
**transformação**. Cada etapa é preguiçosa, por isso os valores fluem um de
cada vez e nada é materializado por completo.

- Porque cada etapa consome a anterior de forma preguiçosa, o pipeline
  processa dados enormes ou infinitos com memória mínima — está apenas um
  item em trânsito de cada vez.
- As etapas mantêm-se pequenas e independentes: troca ou acrescenta uma
  etapa sem tocar nas outras. Este é o equivalente, em geradores, de compor
  funções.

```python
def reader(nums):  yield from nums
def keep_pos(src): yield from (n for n in src if n > 0)
def doubled(src):  yield from (n * 2 for n in src)

list(doubled(keep_pos(reader([-1, 2, -3, 4]))))   # [4, 8]
```
""",
}
