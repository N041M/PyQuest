# PyQuest translations -- language 'pt' -- chapter 06_functions -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"6.1 brief": r"""# 6.1 -- def: a tua primeira função

## Conceito

Uma **função** é um pedaço de código nomeado e reutilizável. Já *chamaste* funções
o tempo todo -- `print()`, `len()`, `sorted()`. Agora vais **definir** a
tua própria:

```python
def double(x):
    return x * 2
```

- `def` inicia a definição; `double` é o nome que escolhes.
- `x` é um **parâmetro**: uma variável que recebe o valor que quem chama a
  função lhe passar.
- `return` devolve um valor **a quem chamou a função**. Chamar `double(3)` é então
  uma expressão que vale `6`:

```python
result = double(3)     # result is 6
print(double(10))      # 20
```

**Este capítulo verifica o teu código de forma diferente.** Até agora o teu ficheiro *corria* e
imprimia. A partir daqui, o verificador **importa** o teu ficheiro e **chama as tuas
funções diretamente**, passando muitos argumentos diferentes -- por isso não é preciso
`input()` nem `print()` nenhum. O teu ficheiro limita-se a definir a função.

## Exemplo

```python
def double(x):
    return x * 2
```

Esse ficheiro inteiro é uma resposta válida para este puzzle: define `double`, e
`double(21)` devolve `42`.

## A tua tarefa

Define uma função `double(x)` que **devolva** `x` duplicado.

## Está feito quando

- `double(3)` devolve `6`, `double(0)` devolve `0`, `double(-5)` devolve `-10`.
- O teu ficheiro só define a função -- sem `input()`, sem `print()`.
""",

"6.1 hints": r"""A forma é:  def nome(parâmetro):  depois um corpo indentado que devolve
algo.

---

`def double(x):` na primeira linha; o corpo é uma linha: devolve x vezes 2.

---

def double(x):
    return x * 2
""",

"6.1 reference": r"""Uma **função** embala um trabalho debaixo de um nome para que possa ser executado a pedido,
tantas vezes quantas forem necessárias. **`def`** introduz uma: um cabeçalho `def nome():` e um
corpo indentado.

- **Chamá-la** — `nome()` — corre o corpo. Definir uma função não a executa;
  a chamada é que executa.
- **`return valor`** devolve um resultado a quem chamou e termina a função
  de imediato. A expressão da chamada `nome()` *passa a ser* esse valor.
- Uma função sem `return` (ou com um `return` isolado) devolve `None`.

```python
def greet():
    return "hello"

greet()        # 'hello'  -- the call evaluates to the returned value
```
""",

"6.2 brief": r"""# 6.2 -- Dois parâmetros

## Conceito

Uma função pode receber vários parâmetros -- lista-os com vírgulas, e os
valores de quem chama chegam **pela mesma ordem**:

```python
def rect_area(width, height):
    return width * height

rect_area(3, 4)     # 12  (width=3, height=4)
```

Dentro do corpo, os parâmetros são variáveis normais. Tudo o que já sabes
funciona com eles -- aritmética, comparações, f-strings, ciclos.

Uma subtileza que vale a pena conhecer cedo: os parâmetros são **locais** à função. O
`width` dentro de `rect_area` só existe enquanto uma chamada está a correr; não é
visível (e não entra em conflito com) nada fora dela.

## Exemplo

```python
def diff(a, b):
    return a - b

print(diff(10, 4))   # 6
print(diff(4, 10))   # -6  -- order matters
```

## A tua tarefa

Define `rect_area(width, height)` que devolva a área de um retângulo
(largura vezes altura).

## Está feito quando

- `rect_area(3, 4)` devolve `12`; `rect_area(4, 3)` também.
- Um lado zero devolve `0`.
- Sem `input()`, sem `print()` -- o verificador passa os valores diretamente.
""",

"6.2 hints": r"""Dois parâmetros listam-se com uma vírgula:  def rect_area(width, height):

---

O corpo é uma linha: devolve o produto dos dois parâmetros.

---

def rect_area(width, height):
    return width * height
""",

"6.2 reference": r"""Um **parâmetro** é um nome no cabeçalho da função que representa um valor que
quem chama fornece. Os valores passados numa chamada são os **argumentos**, associados aos
parâmetros da esquerda para a direita.

- `def f(a, b):` declara dois parâmetros; `f(3, 4)` chama com `a = 3`, `b = 4`.
- Os parâmetros são **locais**: só existem durante a chamada e não entram em conflito com
  nomes de fora. A função trabalha com o que quer que lhe seja dado, o que a torna reutilizável.
- Passar o número errado de argumentos levanta `TypeError`.

```python
def add(a, b):
    return a + b

add(3, 4)      # 7
```
""",

"6.3 brief": r"""# 6.3 -- return, não print

## Conceito

`print()` e `return` parecem semelhantes quando testas a olho, mas fazem
trabalhos completamente diferentes:

- `print(x)` **mostra** `x` no ecrã -- e é só isso. Quem chamou não recebe
  nada.
- `return x` **devolve `x`** a quem chamou, que pode guardá-lo, compará-lo,
  ou passá-lo adiante.

Uma função que imprime em vez de devolver acaba na verdade por devolver `None` (o
valor de "sem valor"). A diferença morde no momento em que alguém *usa* o resultado:

```python
def shout_wrong(word):
    print(word.upper() + "!")     # shows it... returns None

answer = shout_wrong("hi")        # HI! appears, but...
print(answer)                     # None  -- the caller got nothing
```

A regra: **o trabalho de uma função é calcular e devolver.** Deixa que quem *chama*
decida se imprime ou não.

## Exemplo

```python
def shout(word):
    return word.upper() + "!"

print(shout("hi"))      # HI!  -- printed BY THE CALLER
loud = shout("ok")      # and it can be stored instead
```

## A tua tarefa

Define `shout(word)` que **devolva** a palavra em MAIÚSCULAS com um `!` colado
no final. (`.upper()` é de 2.7.)

## Está feito quando

- `shout("hi")` devolve `"HI!"`; `shout("")` devolve `"!"`.
- O valor é *devolvido* -- uma versão que só imprime vai falhar, porque o
  verificador recebe `None`.
""",

"6.3 hints": r"""Se o verificador disser que recebeu None, a tua função imprimiu em vez de devolver.

---

Constrói a string com .upper() e + "!", depois devolve-a -- sem print nenhum.

---

def shout(word):
    return word.upper() + "!"
""",

"6.3 reference": r"""**Devolver** um valor e **imprimi-lo** são ações diferentes, e confundi-las
é um erro comum.

- **`return`** devolve um valor ao código que chamou, que o pode guardar, fazer
  aritmética com ele, ou passá-lo adiante. O valor viaja.
- **`print`** escreve texto no ecrã e devolve `None`. O valor é mostrado mas
  não é capturado — `x = print(5)` faz com que `x` seja `None`.
- Uma função que imprime em vez de devolver não pode ser usada como base para outra coisa. Prefere
  fazer `return` do resultado e deixar que quem **chama** decida se imprime.

```python
def double(n):
    return n * 2        # caller can use it
print(double(5) + 1)    # 11  -- works because double returned
```
""",

"6.4 brief": r"""# 6.4 -- Valores por omissão

## Conceito

Um parâmetro pode ter um valor **por omissão**: o valor usado quando quem chama o
deixa de fora. Escreve-o com `=` na linha do `def`:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")              # "Hello, Ada!"   -- default used
greet("Ada", "Hi")        # "Hi, Ada!"      -- default overridden
```

Já *usaste* isto: `print(..., sep=" ")` de 1.3 -- `sep` tem um valor
por omissão de um espaço, que substituíste com `sep=", "`. Agora podes construir
a mesma flexibilidade nas tuas próprias funções.

Regras: os parâmetros com valores por omissão vêm **depois** dos que não têm, e o
valor por omissão só é usado quando quem chama omite esse argumento.

## Exemplo

```python
def repeat(word, times=2):
    return word * times

repeat("ha")        # "haha"
repeat("ha", 3)     # "hahaha"
```

## A tua tarefa

Define `greet(name, greeting="Hello")` que devolva `"<greeting>, <name>!"` --
exatamente: o cumprimento, uma vírgula e um espaço, o nome, um ponto de exclamação.

## Está feito quando

- `greet("Ada")` devolve `"Hello, Ada!"` (o valor por omissão em ação).
- `greet("Ada", "Hi")` devolve `"Hi, Ada!"`.
- Sem o valor por omissão, a chamada com um só argumento rebentaria -- o verificador faz
  os dois tipos de chamada.
""",

"6.4 hints": r"""O valor por omissão vai na linha do def:  def greet(name, greeting="Hello"):

---

Constrói o resultado com uma f-string: o cumprimento, depois ", ", depois o nome,
depois "!".

---

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
""",

"6.4 reference": r"""Um **valor por omissão** no cabeçalho torna um parâmetro opcional: se quem chama omite
esse argumento, o valor por omissão é usado.

- `def greet(name, greeting="hi"):` pode ser chamada como `greet("Ada")` (usa `"hi"`) ou
  `greet("Ada", "hello")` (substitui-o).
- Os parâmetros **com** valores por omissão têm de vir **depois** dos que não têm.
- Usa um valor por omissão *novo* em cada chamada para tipos mutáveis — escreve `def f(items=None):`
  depois `if items is None: items = []`, nunca `def f(items=[]):` (uma única lista partilhada
  persiste entre chamadas).

```python
def power(base, exp=2):
    return base ** exp

power(5)       # 25  -- exp defaults to 2
power(5, 3)    # 125
```
""",

"6.5 brief": r"""# 6.5 -- return termina a função

## Conceito

`return` não se limita a devolver um valor -- **para a função no
momento**. Nada depois de um `return` executado corre. Isso torna as funções com
ramificações fáceis de ler: resolve cada caso e sai.

```python
def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
```

Repara que não há `else` -- não é preciso nenhum. Se o primeiro `return` disparou, a
função já terminou; chegar à última linha *significa* que `n` era positivo.
Este estilo chama-se **retorno antecipado**.

Uma função com vários `return` continua a devolver exatamente **um**
valor por chamada: o do primeiro `return` que executar.

## Exemplo

```python
sign(-3)    # "negative"
sign(0)     # "zero"
sign(42)    # "positive"
```

## A tua tarefa

Define `sign(n)` que devolva `"negative"`, `"zero"`, ou `"positive"` para um
número inteiro `n`.

## Está feito quando

- `sign(-3)`, `sign(0)`, `sign(42)` devolvem as três palavras acima.
- Os casos-limite `-1` e `1` também estão corretos.
""",

"6.5 hints": r"""Cada caso é um if com o seu próprio return. Assim que um return executa, a função
termina.

---

Verifica `n < 0` primeiro, depois `n == 0`; se nenhum devolveu, n tem de ser positivo --
basta devolver "positive" sem condição nenhuma.

---

def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
""",

"6.5 reference": r"""Um `return` pode aparecer **em qualquer lugar** de uma função, e alcançá-lo termina a chamada de
imediato — as linhas seguintes não correm. Um **retorno antecipado** usa isto para tratar um caso e
sair de imediato.

- Achata o código: trata o caso especial ou inválido logo à cabeça com uma guarda
  (`if bad: return ...`), depois escreve o caminho principal sem o aninhar num
  `else`.
- O primeiro `return` alcançado vence; nada depois dele nessa chamada é executado.

```python
def reciprocal(n):
    if n == 0:
        return None     # bail out early on the bad case
    return 1 / n        # main path, not indented under an else
```
""",

"6.6 brief": r"""# 6.6 -- Devolver dois valores

## Conceito

`return` pode devolver **vários valores de uma vez** -- separa-os com uma
vírgula e o Python empacota-os num **tuplo** (4.7):

```python
def min_max(nums):
    return min(nums), max(nums)
```

Quem chama pode guardar o tuplo, ou desempacotá-lo diretamente em variáveis -- o
mesmo desempacotamento que usaste em `a, b = b, a`:

```python
pair = min_max([3, 1, 4])     # (1, 4)  -- one tuple
lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4  -- unpacked
```

É assim que as funções em Python devolvem "duas respostas" -- não há nenhum
truque especial, apenas um tuplo e desempacotamento.

## Exemplo

```python
def split_name(full):
    parts = full.split()
    return parts[0], parts[-1]

first, last = split_name("Ada King Lovelace")
# first = "Ada", last = "Lovelace"
```

## A tua tarefa

Define `min_max(nums)` que devolva o item mais pequeno e o maior de uma
lista não vazia, **por essa ordem**, como um tuplo. (`min()`/`max()` são de 5.3.)

## Está feito quando

- `min_max([3, 1, 4])` devolve `(1, 4)` -- um tuplo, o mais pequeno primeiro.
- `min_max([7])` devolve `(7, 7)`.
- Números negativos funcionam.
""",

"6.6 hints": r"""Dois valores depois de um return, separados por uma vírgula, voltam como um tuplo.

---

Já tens as duas metades de 5.3: `return min(nums), max(nums)`.

---

def min_max(nums):
    return min(nums), max(nums)
""",

"6.6 reference": r"""Uma função devolve **um** objeto, mas esse objeto pode ser um **tuplo**, por isso
`return a, b` devolve vários valores de uma vez (o Python empacota-os num tuplo).
Quem chama **desempacota**-os com nomes correspondentes.

- `return lo, hi` devolve o tuplo `(lo, hi)`; `low, high = bounds(xs)` desempacota-o
  em dois nomes.
- As contagens têm de corresponder no desempacotamento. Podes capturar o tuplo inteiro com um só nome se
  preferires: `result = bounds(xs)` depois `result[0]`, `result[1]`.

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4
```
""",

"6.7 brief": r"""# 6.7 -- Construir sobre funções nativas

## Conceito

As funções brilham quando embrulham uma pequena *receita* atrás de um bom nome. A
receita de uma média:

> o total, dividido pela quantidade de itens

Tens todos os ingredientes: `sum()` (5.2), `len()` (2.6), e `/` (1.9).
Lembra-te de 1.9 que `/` **devolve sempre um float** -- `4 / 2` é `2.0`,
não `2`. Isso está correto aqui: uma média é naturalmente um número decimal.

```python
def average(nums):
    return sum(nums) / len(nums)
```

Uma função, uma linha, instantaneamente reutilizável -- e o nome diz o que a linha
significa.

## Exemplo

```python
average([1, 2])        # 1.5
average([10, 20, 30])  # 20.0
```

## A tua tarefa

Define `average(nums)` que devolva a média de uma lista não vazia de
números.

## Está feito quando

- `average([1, 2])` devolve `1.5`; `average([10, 20, 30])` devolve `20.0`.
- O resultado é um **float** mesmo quando a divisão é exata (usa `/`,
  não `//`).
- Uma lista com um só item devolve esse item (como float).
""",

"6.7 hints": r"""Uma média é o total dividido pela contagem -- e tens uma função nativa para
cada metade.

---

`sum(nums)` sobre `len(nums)`, com `/` (a divisão em float de 1.9).

---

def average(nums):
    return sum(nums) / len(nums)
""",

"6.7 reference": r"""As funções **compõem funções nativas** numa operação nomeada e reutilizável. Uma função
`average` é o modelo: embrulha `sum` e `len` atrás de um nome claro.

- `return sum(nums) / len(nums)` calcula a média — mas `len(nums)` é `0` para uma
  lista vazia, o que levanta `ZeroDivisionError`, por isso protege-a com um retorno antecipado.
- Nomear a operação (`average(scores)`) faz com que o código que a chama se leia como intenção, e
  corrigir ou melhorar a lógica acontece num só sítio.

```python
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

average([2, 4, 9])    # 5.0
```
""",

"6.8 brief": r"""# 6.8 -- Funções a chamar funções

## Conceito

As tuas funções podem chamar-se **umas às outras**. Esse é o verdadeiro golpe de mestre: resolve um
problema pequeno uma vez, dá-lhe um nome, e constrói a função seguinte em cima dele.

```python
def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
```

`same_word` não repete a receita de retirar espaços e minusculizar -- **delega** em
`clean`. Se alguma vez melhorares `clean` (digamos, removendo também pontuação), todas as
funções construídas sobre ela melhoram de graça. Repetir a receita nos dois sítios
é como nascem os bugs: corriges uma cópia, esqueces a outra.

Repara que `same_word` devolve o resultado de uma comparação -- um **booleano**
(`True`/`False`), como em 3.1. Não é preciso `if`: `clean(a) == clean(b)` já
*é* a resposta.

## Exemplo

```python
clean("  Tea ")              # "tea"
same_word("  Tea ", "tea")   # True
same_word("tea", "milk")     # False
```

## A tua tarefa

Define **ambas** as funções:

- `clean(text)` -- devolve o texto sem os espaços à volta e em minúsculas
  (2.7).
- `same_word(a, b)` -- devolve `True` exatamente quando os dois textos são iguais
  depois de limpos. Tem de **chamar `clean`** em vez de refazer a receita.

## Está feito quando

- `clean("  Tea ")` devolve `"tea"`.
- `same_word("  Tea ", "tea")` é `True`; `same_word("tea", "milk")` é `False`.
- `same_word` chama `clean` -- o verificador procura a delegação.
""",

"6.8 hints": r"""Escreve primeiro clean e imagina-a a passar: .strip() depois .lower(),
encadeados.

---

same_word é uma linha: compara clean(a) com clean(b) usando == e devolve o
resultado -- uma comparação já É True ou False.

---

def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
""",

"6.8 reference": r"""As funções **chamam outras funções**, por isso uma tarefa maior é construída a partir de peças
pequenas e testadas. O resultado de uma torna-se o argumento ou bloco de construção da seguinte.

- Um auxiliar faz bem um trabalho; uma função de nível superior chama vários auxiliares e
  combina os seus resultados. Isto é o cerne de estruturar um programa.
- `f(g(x))` alimenta o resultado de `g` diretamente para `f`. Cada função mantém-se simples e
  verificável de forma independente.

```python
def clean(s):  return s.strip().lower()
def is_yes(s): return clean(s) == "yes"

is_yes("  YES ")   # True  -- is_yes builds on clean
```
""",

"6.9 brief": r"""# 6.9 -- Recursão: uma função a chamar-se a si própria

## Conceito

Uma função pode chamar-se **a si própria**. Isso chama-se **recursão**, e funciona
sempre que um problema contém uma cópia mais pequena do mesmo problema.

O fatorial é o clássico: `5!` significa `5 * 4 * 3 * 2 * 1`. Mas olha outra vez:

> `5!` é apenas `5 * 4!` -- e `4!` é `4 * 3!` ...

Uma função recursiva afirma exatamente isso, mais um **caso base** -- a entrada
mais pequena respondida diretamente, sem mais chamadas:

```python
def fact(n):
    if n == 0:
        return 1            # base case: 0! is 1
    return n * fact(n - 1)  # the smaller copy of the same problem
```

`fact(3)` corre como `3 * fact(2)` -> `3 * 2 * fact(1)` -> `3 * 2 * 1 * fact(0)`
-> `3 * 2 * 1 * 1` = `6`. Sem o caso base as chamadas nunca parariam --
a versão da recursão de um ciclo sem fim.

Podias calcular um fatorial com um ciclo `for` -- mas a *lição* aqui é a
auto-chamada, por isso este puzzle exige-a.

## Exemplo

```python
fact(0)    # 1
fact(3)    # 6
fact(5)    # 120
```

## A tua tarefa

Define `fact(n)` que devolva `n!` **recursivamente**: um caso base para `0`, e
`n * fact(n - 1)` para o resto. `n` nunca é negativo.

## Está feito quando

- `fact(0)` é `1`, `fact(1)` é `1`, `fact(5)` é `120`.
- `fact` chama-se a si própria -- o verificador procura a auto-chamada, por isso uma versão
  com ciclo não vai passar.
""",

"6.9 hints": r"""Responde primeiro ao caso mais pequeno: se n é 0, devolve 1 -- não é preciso chamar nada.

---

Para todo o resto, confia na função que estás a escrever:
return n * fact(n - 1). O retorno antecipado (6.5) mantém o caso base limpo.

---

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
""",

"6.9 reference": r"""Uma função **recursiva** chama-se **a si própria** para resolver uma versão mais pequena do mesmo
problema. Duas partes são essenciais:

- um **caso base** que devolve diretamente **sem** recorrer — isto termina a
  recursão;
- um **caso recursivo** que chama a função sobre uma entrada mais pequena e constrói sobre
  o resultado, aproximando-se do caso base a cada vez.

Se o caso base falhar ou nunca for alcançado, as chamadas aninham-se até o Python levantar
`RecursionError`. Muitas recursões têm uma forma mais simples com ciclo; a recursão brilha quando
o problema é, em si, auto-semelhante.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # smaller subproblem

factorial(4)   # 24
```
""",

"6.10 brief": r"""# 6.10 -- Capítulo final: uma pequena biblioteca

## Conceito

Nada de novo -- este capítulo final é o capítulo em miniatura: várias funções,
cada uma com um trabalho claro, as últimas a **delegar** nas anteriores
(6.8). Um ficheiro de funções relacionadas como este é a semente de qualquer
*biblioteca* real que alguma vez vieres a importar.

As peças: `for ch in word` (3.10), `in` (5.1), a ideia da contagem (5.9),
f-strings (2.10), e retornos antecipados (6.5).

## Exemplo

```python
count_vowels("tea")        # 2   ("e" and "a")
count_vowels("xyz")        # 0
describe("tea")            # "tea has 2 vowels"
describe("xyz")            # "xyz has no vowels"
```

## A tua tarefa

Define **ambas** as funções:

- `count_vowels(word)` -- devolve quantos caracteres de `word` são vogais
  (`a`, `e`, `i`, `o`, `u`; as palavras estão em minúsculas).
- `describe(word)` -- devolve a string `"<word> has <n> vowels"`, exceto
  quando a contagem é zero: nesse caso é `"<word> has no vowels"`. Tem de **chamar
  `count_vowels`**.

## Está feito quando

- `count_vowels("tea")` é `2`; `count_vowels("xyz")` é `0`.
- `describe("tea")` é `"tea has 2 vowels"`; `describe("xyz")` é
  `"xyz has no vowels"`.
- `describe` delega em `count_vowels` -- o verificador procura a chamada.
""",

"6.10 hints": r"""count_vowels é uma contagem sobre os caracteres: percorre com `for ch in word` e
testa `ch in "aeiou"`.

---

describe chama count_vowels uma vez, guarda o número, depois faz um retorno antecipado com o
texto de "no vowels" quando é 0; caso contrário, uma f-string com a contagem.

---

def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count = count + 1
    return count

def describe(word):
    n = count_vowels(word)
    if n == 0:
        return f"{word} has no vowels"
    return f"{word} has {n} vowels"
""",

"6.10 reference": r"""Uma **biblioteca** aqui significa um conjunto de funções relacionadas que escreveste, cada uma nomeada
pelo seu trabalho, que juntas formam um conjunto de ferramentas reutilizável — a recompensa do capítulo.

- Constrói funções pequenas que fazem cada uma uma coisa e devolvem (`return`) o seu resultado; depois
  as funções de nível superior chamam-nas. O código que as chama lê-se como uma sequência de intenções.
- Manter a lógica dentro de funções nomeadas (em vez de copiada em linha) significa que uma correção ou
  melhoria acontece num só sítio e todos os que chamam beneficiam.

```python
def clean(s):    return s.strip().lower()
def words(s):    return clean(s).split()
def wordcount(s): return len(words(s))

wordcount("  The quick fox ")   # 3  -- each function builds on the last
```
""",
}
