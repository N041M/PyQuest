# PyQuest translations -- language 'pt' -- chapter 01_basics -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"1.1 brief": r"""# 1.1 -- Hello, output

## Conceito

Um **programa** é uma lista de instruções que o computador executa de cima para baixo.
A instrução mais básica é **imprimir** -- colocar uma linha de texto no
ecrã. Em Python fazes isso com `print(...)`. Tudo o que colocares dentro dos
parênteses, entre aspas, é mostrado.

`print` é uma **função**: uma ação nativa que ativas escrevendo o seu nome
seguido de parênteses. O que está entre aspas é **texto** (o Python chama texto de
*cadeia de caracteres* -- uma sequência de caracteres).

## Exemplo

```python
print("Good morning")
```

Quando isto corre, o ecrã mostra:

```
Good morning
```

As aspas marcam onde o texto começa e acaba; elas próprias não são impressas. O Python
também acrescenta automaticamente uma quebra de linha no final, por isso o próximo print
começa numa linha nova.

## A tua tarefa

Faz o programa imprimir exatamente esta linha:

```
Hello, output
```

Abre o ficheiro de trabalho do capítulo `work.py`, escreve um `print(...)` que produza essa
linha, **guarda o ficheiro**, e depois corre `check`.

## Está feito quando

- Correr `check` mostra CHECK PASSED.
- O resultado é `Hello, output` -- as mesmas palavras, a mesma vírgula. (A verificação
  ignora maiúsculas/minúsculas, mas seguir o enunciado à risca é um bom hábito.)
""",

"1.1 hints": r"""Qual é a função nativa que coloca texto no ecrã? Só precisas de uma linha.

---

Usa `print(...)`. O texto vai dentro dos parênteses, entre aspas duplas:
`print("some text")`. Segue exatamente as palavras, incluindo a vírgula.

---

print("Hello, output")
""",

"1.1 reference": r"""`print` escreve uma representação textual de cada argumento na saída padrão (o
terminal), por ordem, e depois escreve `end` (uma quebra de linha por omissão). É a
forma principal de um programa mostrar um resultado ao utilizador.

- Cada valor é primeiro convertido em texto com `str()`, por isso `print(42)` e
  `print("42")` mostram ambos `42`.
- Com vários argumentos, `sep` (por omissão um único espaço) é colocado *entre*
  valores adjacentes -- nunca antes do primeiro nem depois do último.
- `end` é acrescentado uma vez, depois de tudo o resto. Como o valor por omissão é `"\n"`,
  cada chamada a `print` termina a linha atual e o resultado seguinte começa de novo.
- `print` devolve `None`; é chamado pelo seu efeito, não pelo seu valor.

```python
print("Hello, World!")        # Hello, World!
print("a", "b", "c")          # a b c
```
""",

"1.2 brief": r"""# 1.2 -- Imprimir mais

## Conceito

Duas ideias novas, ambas sobre `print`.

**1. Vários prints correm por ordem.** Cada `print(...)` coloca o seu texto na sua própria linha,
e o Python corre-os de cima para baixo. Três linhas `print` produzem três linhas de saída.

**2. Um print pode mostrar vários valores.** Coloca várias coisas dentro dos
parênteses separadas por **vírgulas**, e o `print` mostra-as numa linha com um
único espaço entre cada uma:

```python
print("a", "b", "c")
```

mostra:

```
a b c
```

Podes misturar texto e números desta forma. Os números **não** precisam de aspas; o texto precisa.

## Exemplo

```python
print("Scores:")
print(10, 20, 30)
```

mostra:

```
Scores:
10 20 30
```

A primeira linha é um print; o segundo print tem três valores separados por
vírgulas, por isso partilham uma linha com espaços entre eles.

## A tua tarefa

Produz exatamente estas duas linhas:

```
Counting:
1 2 3
```

Usa duas instruções `print`: a primeira imprime a palavra, a segunda imprime os
três números `1`, `2`, `3` como valores separados (deixa o `print` acrescentar os espaços).

## Está feito quando

- O resultado é exatamente duas linhas: `Counting:` depois `1 2 3`.
- A segunda linha vem de números separados por vírgulas, não de escreveres tu mesmo
  o texto `"1 2 3"`.
""",

"1.2 hints": r"""Precisas de duas linhas de print. A primeira imprime uma palavra; a segunda imprime números.

---

No segundo print, separa os números com vírgulas: `print(1, 2, 3)`.
Deixa o print colocar os espaços -- não escrevas os espaços tu mesmo.

---

print("Counting:")
print(1, 2, 3)
""",

"1.2 reference": r"""Um programa corre de cima para baixo, por isso instruções `print` sucessivas produzem linhas
sucessivas — cada chamada emite os seus argumentos e depois uma quebra de linha.

Passar **vários valores a um só `print`**, separados por vírgulas, é diferente de
várias chamadas a `print`: os valores aparecem numa *única* linha, unidos por `sep` (um
espaço por omissão). Isto é separação por vírgulas na chamada, não concatenação de texto
— os valores mantêm os seus próprios tipos e são convertidos de forma independente.

```python
print("one")
print("two")          # two lines

print("x", "y", 3)    # one line:  x y 3
```
""",

"1.3 brief": r"""# 1.3 -- Escolher o separador

## Conceito

Quando dás ao `print` vários valores, ele junta-os com um espaço por omissão. Podes
mudar essa cadeia de junção com uma configuração especial chamada **`sep`** (abreviatura de
*separator*, separador).

Uma configuração como esta escreve-se `nome=valor` dentro dos parênteses, depois dos
teus valores:

```python
print("a", "b", "c", sep="-")
```

mostra:

```
a-b-c
```

`sep="-"` diz ao `print` para colocar um traço entre os valores em vez de um espaço. O
separador só aparece *entre* valores -- nunca antes do primeiro nem depois do último.
Podes usar qualquer texto como separador: `sep=", "`, `sep=""` (nada), `sep="/"`,
e assim por diante.

`sep` tem de ser escrito exatamente assim, sem espaço antes do `=`, e o valor entre
aspas porque é texto.

## Exemplo

```python
print("home", "user", "docs", sep="/")
```

mostra:

```
home/user/docs
```

## A tua tarefa

Imprime esta data exata, usando três **números** unidos por traços:

```
2024-12-25
```

Passa `2024`, `12`, `25` a um único `print` e define `sep` para que sejam unidos com
`-`. Não escrevas os traços como parte do texto tu mesmo.

## Está feito quando

- O resultado é exatamente `2024-12-25`.
- Vem de três números mais uma configuração `sep`, não de uma cadeia escrita à mão.
""",

"1.3 hints": r"""Dá ao print os três números, depois acrescenta uma configuração que muda o separador.

---

A configuração é `sep`. Depois dos teus três números, acrescenta `sep="-"` dentro do
mesmo print: `print(a, b, c, sep="-")`.

---

print(2024, 12, 25, sep="-")
""",

"1.3 reference": r"""`sep` e `end` são argumentos exclusivamente nomeados que controlam o espaçamento à volta
do resultado de um `print`.

- **`sep`** é a cadeia inserida entre cada par de valores adjacentes. O valor por
  omissão é `" "`. Nunca aparece antes do primeiro valor nem depois do último,
  por isso *N* valores produzem *N − 1* separadores.
- **`end`** é a cadeia escrita uma vez, depois do último valor. O valor por omissão é
  `"\n"`, motivo pelo qual cada `print` termina a sua linha. Define `end=""` para deixar o
  cursor na mesma linha, para que o próximo `print` a continue.

```python
print("2024", "01", "15", sep="-")   # 2024-01-15
print("loading", end="")
print("...")                          # loading... (one line)
```
""",

"1.4 brief": r"""# 1.4 -- Comentários

## Conceito

Um **comentário** é uma nota no teu código que o Python ignora. Tudo o que vier depois de um `#` numa
linha é ignorado quando o programa corre. Os comentários são para humanos -- para explicar
o que o código faz.

```python
# This whole line is a note and does nothing.
print("Hi")   # Text after # on a code line is also ignored.
```

Só `print("Hi")` corre acima. As duas notas são ignoradas.

Um segundo uso, muito prático: **comentar** código. Se colocares um `#` à frente
de uma linha de código real, essa linha deixa de correr -- sem a apagares. É assim
que desligas uma linha temporariamente.

```python
# print("off")
print("on")
```

Só `on` é impresso; a primeira linha é agora um comentário.

## Erro comum

Colocar `#` à frente de uma linha **não** a apaga nem causa um erro -- a
linha simplesmente não corre. Remove o `#` e ela volta a correr.

## A tua tarefa

O ficheiro inicial já contém uma linha que imprime `Hidden`. **Comenta-a**
para que não corra -- **não** a apagues -- e acrescenta uma linha que imprima
`Visible`.

O programa tem de imprimir apenas:

```
Visible
```

## Está feito quando

- O resultado é exatamente `Visible`.
- A linha `print("Hidden")` continua no ficheiro, mas comentada com um `#`
  para que não corra. (Este puzzle é sobre *comentar código*, por isso apagar a
  linha não conta.)
""",

"1.4 hints": r"""Uma linha que começa com # é ignorada. Coloca um à frente da linha Hidden.

---

Muda `print("Hidden")` para `# print("Hidden")`, depois acrescenta `print("Visible")`
na sua própria linha.

---

# print("Hidden")
print("Visible")
""",

"1.4 reference": r"""Um `#` inicia um **comentário**: do `#` até ao fim dessa linha, o texto é
ignorado pelo Python. Os comentários explicam *porquê* o código faz algo; não têm
efeito no que corre.

- Um comentário pode estar na sua própria linha ou seguir código na mesma linha
  (`x = 1  # set up`).
- Um `#` dentro de uma string literal é apenas um carácter, não um comentário
  (`"#1"` é o texto `#1`).
- O Python **não tem sintaxe de comentário em bloco**: comenta cada linha com `#`, ou — para um
  bloco descartável — usa uma string literal, que é avaliada e descartada.

"Comentar" uma linha (colocar `#` à frente) é a forma mais rápida de a desativar
sem a apagar.

```python
# this whole line is ignored
print("hi")   # and this trailing note is too
```
""",

"1.5 brief": r"""# 1.5 -- Guardar um valor

## Conceito

Uma **variável** é um nome que guarda um valor para poderes usá-lo mais tarde. Crias
uma com `=`, o sinal de **atribuição**:

```python
score = 100
```

Lê isto como "seja `score` igual a `100`." O nome fica do lado esquerdo, o valor do lado
direito. Depois dessa linha, escrever `score` em qualquer lado significa `100`.

Isto é diferente de `==` (que vais encontrar mais tarde para comparar). Um único
`=` *guarda*.

Uma vez guardado, podes usar o nome tantas vezes quantas quiseres:

```python
score = 100
print(score)
print(score)
```

mostra:

```
100
100
```

Repara que `print(score)` **não tem aspas** à volta de `score`. Aspas fariam disso o
texto literal "score"; sem aspas significa o valor da variável, `100`.

## Regras de nomeação (versão rápida)

Um nome de variável pode usar letras, dígitos e sublinhados, mas não pode começar com um
dígito nem conter espaços. Usa nomes claros: `total`, `user_name`, `count`.

## A tua tarefa

Guarda o número `42` numa variável, depois imprime essa variável **duas vezes** para que o
resultado seja:

```
42
42
```

Usa a variável nas duas vezes -- não escrevas `42` dentro dos prints.

## Está feito quando

- O resultado é `42` em duas linhas separadas.
- Ambas as linhas vêm de imprimir a tua variável (sem aspas à volta do seu nome).
""",

"1.5 hints": r"""Primeiro cria uma variável com `=`, depois imprime o seu nome em duas linhas.

---

`n = 42` guarda o valor. Depois `print(n)` duas vezes. Sem aspas à volta de n.

---

n = 42
print(n)
print(n)
""",

"1.5 reference": r"""A atribuição com `=` liga um **nome** a um valor. Depois disso o nome *refere-se a*
esse valor, e usar o nome em qualquer lado é equivalente a avaliá-lo. Ao ler código, `=` é
"passa a ser", não "é igual a" (a igualdade é `==`).

- Os nomes não são declarados e não têm um tipo fixo — a primeira atribuição cria
  o nome, e este passa simplesmente a apontar para o que quer que atribuas.
- Um nome tem de começar com uma letra ou sublinhado e conter letras, dígitos ou
  sublinhados; é sensível a maiúsculas/minúsculas (`total` e `Total` são diferentes).
- O lado direito é totalmente avaliado primeiro, e só depois o resultado é ligado ao
  nome do lado esquerdo.

```python
greeting = "Hello"
print(greeting)        # Hello  -- the name stands in for the value
```
""",

"1.6 brief": r"""# 1.6 -- Reatribuir uma variável

## Conceito

Uma variável pode ser **alterada** depois de criada. Atribuir de novo ao mesmo nome
substitui o valor antigo por um novo. O nome refere-se sempre ao que
foi guardado **mais recentemente**.

```python
x = 10
print(x)   # 10
x = 20
print(x)   # 20
```

A ordem importa: o programa corre de cima para baixo, por isso o primeiro `print(x)` vê
`10`, e só depois da segunda atribuição é que `x` passa a `20`.

Um padrão comum e útil é atualizar uma variável usando o seu próprio valor atual:

```python
x = 10
x = x + 5   # take the current x (10), add 5, store 15 back in x
print(x)    # 15
```

O lado direito é calculado primeiro (`10 + 5`), e só depois o resultado é guardado de volta
em `x`.

## Erro comum

Reatribuir não cria uma segunda variável. Continua a haver apenas um `x`; o seu valor
guardado foi trocado. O valor antigo simplesmente desaparece.

## A tua tarefa

Cria uma variável com o valor `10` e imprime-a. Depois reatribui essa mesma variável para
`20` e imprime-a outra vez. O resultado tem de ser:

```
10
20
```

## Está feito quando

- O resultado é `10` depois `20` em duas linhas.
- Ambas as linhas imprimem a **mesma** variável, antes e depois de a alterares.
""",

"1.6 hints": r"""Imprime a variável, depois atribui um novo valor ao mesmo nome, depois imprime outra vez.

---

A ordem é: `x = 10`, `print(x)`, `x = 20`, `print(x)`.

---

x = 10
print(x)
x = 20
print(x)
""",

"1.6 reference": r"""Uma variável é um nome, não uma caixa: atribuir de novo **reassocia** o nome a um novo
valor. O nome guarda sempre a sua atribuição mais recente; o valor anterior
simplesmente deixa de ser alcançável através dele.

- Cada `=` substitui aquilo para onde o nome aponta. A ordem importa — as atribuições
  posteriores prevalecem.
- O lado direito é avaliado usando o valor *atual* do nome, e só depois o
  resultado é reassociado, por isso `x = x + 1` lê o `x` antigo e guarda o novo.
- As formas aumentadas (`x += 1`, `x *= 2`, …) são abreviaturas exatamente para isso:
  ler, combinar, reassociar.

```python
score = 10
score = 25        # score is now 25
score = score + 5 # reads 25, stores 30
```
""",

"1.7 brief": r"""# 1.7 -- Texto vs número

## Conceito

O Python distingue dois tipos de valores, e isso importa muito:

- Um **número** como `5` -- escrito sem aspas. O Python chama aos números inteiros
  `int` (integer).
- Uma **cadeia de caracteres** como `"5"` -- escrita entre aspas. É *texto* que por acaso
  se parece com um número. O Python chama-lhe `str`.

Comportam-se de forma diferente com o sinal `+`:

- Com números, `+` **soma**: `5 + 5` é `10`.
- Com cadeias de caracteres, `+` **junta** (a isto chama-se **concatenação**):
  `"5" + "5"` é `"55"` -- os dois pedaços de texto colados um ao outro.

```python
print(5 + 5)        # 10   (numbers add)
print("5" + "5")    # 55   (text joins)
print("ab" + "cd")  # abcd
```

Portanto `"5"` e `5` parecem iguais no ecrã mas são tipos diferentes, e `+` trata-os
de formas completamente diferentes.

## Erro comum

`"5"` não é o número cinco. As aspas fazem dele texto. Não podes fazer aritmética
com ele à espera de uma soma -- `"5" + "5"` dá `"55"`, não `10`.

## A tua tarefa

Imprime estas duas linhas, por esta ordem:

```
55
10
```

- A primeira linha tem de vir de **juntar duas cadeias de caracteres** `"5"` e `"5"` com `+`.
- A segunda linha tem de vir de **somar dois números** `5` e `5` com `+`.

## Está feito quando

- O resultado é `55` depois `10`.
- A primeira linha usa concatenação de texto; a segunda usa soma de números.
""",

"1.7 hints": r"""As aspas decidem tudo aqui. Com aspas, + junta; sem aspas, + soma.

---

Primeira linha: `print("5" + "5")`. Segunda linha: `print(5 + 5)`. Repara nas aspas
na primeira e na ausência delas na segunda.

---

print("5" + "5")
print(5 + 5)
""",

"1.7 reference": r"""Todo o valor tem um **tipo**. Dois tipos fundamentais aparecem logo de início:

- uma **cadeia de caracteres** (`str`) é texto, escrito entre aspas: `"42"`, `"hello"`;
- um **inteiro** (`int`) é um número, escrito como dígitos simples: `42`.

As aspas são toda a diferença. `type("42")` é `str`; `type(42)` é `int`.

O tipo decide o que um operador significa. `+` entre duas **cadeias de caracteres**
*concatena* (junta) -as; `+` entre dois **números** *soma*-os:

```python
"2" + "2"   # "22"  -- text joined
 2  +  2    #  4    -- numbers added
```

Misturar os dois com `+` é um erro (`TypeError`), porque o Python não vai adivinhar
se querias somar ou juntar. Converte explicitamente primeiro: `int("2") + 2` é
`4`, e `"$" + str(2)` é `"$2"`.
""",

"1.8 brief": r"""# 1.8 -- Aritmética e ordem

## Conceito

O Python faz contas com estes sinais (chamados **operadores**):

- `+` somar
- `-` subtrair
- `*` multiplicar
- `/` dividir

```python
print(2 + 3)   # 5
print(10 - 4)  # 6
print(6 * 7)   # 42
```

**A ordem importa.** Tal como na matemática da escola, `*` e `/` acontecem **antes**
de `+` e `-`. Portanto:

```python
print(2 + 3 * 4)   # 14, not 20  -- 3*4 first, then +2
```

Para forçar uma ordem diferente, envolve uma parte em **parênteses** `( )`. O que estiver
dentro dos parênteses é calculado primeiro:

```python
print((2 + 3) * 4)   # 20  -- 2+3 first, then *4
```

Esta é a fonte mais comum de erros de "número errado", por isso vale a pena
familiarizares-te com isto já.

## Exemplo

```python
print(1 + 2 * 3)     # 7
print((1 + 2) * 3)   # 9
```

## A tua tarefa

Imprime estas duas linhas:

```
14
20
```

- A primeira linha é `2 + 3 * 4` sem parênteses (multiplicação primeiro).
- A segunda linha usa os mesmos números mas com parênteses para que a soma
  aconteça primeiro: `(2 + 3) * 4`.

## Está feito quando

- O resultado é `14` depois `20`.
- A diferença entre as linhas vem apenas dos parênteses a mudar a
  ordem.
""",

"1.8 hints": r"""A multiplicação corre antes da soma, a não ser que os parênteses digam o contrário.

---

Primeira linha: `print(2 + 3 * 4)`. Segunda linha: acrescenta parênteses à volta de 2 + 3:
`print((2 + 3) * 4)`.

---

print(2 + 3 * 4)
print((2 + 3) * 4)
""",

"1.8 reference": r"""Os operadores aritméticos são `+` (somar), `-` (subtrair), `*` (multiplicar),
`/` (dividir), `//` (divisão inteira), `%` (resto), e `**` (potência).

Seguem uma **precedência** (ordem das operações), da mais alta para a mais baixa:

1. `**`
2. `-` unário (negação)
3. `*`, `/`, `//`, `%`
4. `+`, `-`

Operadores com a mesma precedência são avaliados **da esquerda para a direita**, exceto `**`, que é
associativo à direita (`2 ** 3 ** 2` é `2 ** 9`). Os **parênteses** sobrepõem-se a
tudo isto — são avaliados primeiro.

```python
2 + 3 * 4      # 14   -- * before +
(2 + 3) * 4    # 20   -- parentheses first
-3 ** 2        # -9   -- ** before unary minus
```
""",

"1.9 brief": r"""# 1.9 -- Três tipos de divisão

## Conceito

Dividir tem três operadores úteis em Python:

- `/`  divisão normal -- dá sempre um número decimal (o Python chama-lhes
  `float`). `7 / 2` é `3.5`.
- `//` divisão inteira -- divide e descarta a parte fracionária, dando um
  número inteiro. `7 // 2` é `3`.
- `%`  módulo -- dá o **resto** depois da divisão. `7 % 2` é `1`
  (porque o 2 cabe três vezes no 7, sobrando 1).

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
```

Um número com um ponto decimal, como `3.5`, é um `float`. Um número inteiro sem
ponto, como `3`, é um `int`. Repara que `/` dá `3.5` mesmo quando divide
números que parecem dar um resultado exato: `4 / 2` é `2.0`, não `2`.

`%` é surpreendentemente útil: um número é par exatamente quando `n % 2` é `0`.

## Erro comum

`/` não arredonda para um número inteiro. `7 / 2` é `3.5`, nunca `3`. Se quiseres a
parte inteira, é para isso que serve o `//`.

## A tua tarefa

Usando os números 7 e 2, imprime estas três linhas por ordem:

```
3.5
3
1
```

Usa `/` para a primeira, `//` para a segunda, e `%` para a terceira.

## Está feito quando

- O resultado é exatamente `3.5`, depois `3`, depois `1`.
- Cada linha usa o operador correspondente (`/`, `//`, `%`).
""",

"1.9 hints": r"""Há três operadores de divisão: /, // e %. Um por linha.

---

`print(7 / 2)` dá 3.5, `print(7 // 2)` dá 3, `print(7 % 2)` dá 1.

---

print(7 / 2)
print(7 // 2)
print(7 % 2)
""",

"1.9 reference": r"""O Python tem três operadores de divisão:

- **`/` divisão verdadeira** produz sempre um **`float`**, mesmo quando o resultado é
  inteiro: `7 / 2 == 3.5`, e `4 / 2 == 2.0` (repara no `.0`).
- **`//` divisão inteira** divide e arredonda *para baixo*, em direção ao infinito negativo,
  dando um `int` para dois inteiros: `7 // 2 == 3`. Com um operando negativo continua a
  arredondar para baixo, por isso `-7 // 2 == -4`, não `-3`.
- **`%` resto (módulo)** é o que sobra: `7 % 2 == 1`. Em Python o
  resultado tem o **sinal do divisor**, por isso `-7 % 2 == 1`.

Para quaisquer inteiros, `a == (a // b) * b + (a % b)` é verdade. `divmod(a, b)` devolve o
par `(a // b, a % b)` de uma só vez. Dividir por zero levanta `ZeroDivisionError`.

```python
17 / 5    # 3.4
17 // 5   # 3
17 % 5    # 2   -- 3*5 + 2 == 17
```
""",

"1.10 brief": r"""# 1.10 -- Perguntar ao utilizador

## Conceito

`input()` pausa o programa, deixa a pessoa escrever uma linha, e **devolve o que
ela escreveu como texto** (uma cadeia de caracteres). Normalmente guardas isso numa variável:

```python
name = input()
print("Hi, " + name)
```

Se a pessoa escrever `Sam`, o programa imprime `Hi, Sam`.

`input()` devolve sempre uma **cadeia de caracteres**, mesmo que a pessoa escreva dígitos. (Vais
lidar com isso no próximo puzzle.)

Podes juntar o texto escrito com outro texto usando `+`, tal como no puzzle 1.7:

```python
city = input()
print("You live in " + city)
```

> Nota: quando corres `check`, o verificador fornece a entrada por ti automaticamente
> -- não precisas de escrever nada à mão.

## Exemplo

Entrada escrita: `Berlin`

```python
city = input()
print("Welcome to " + city)
```

Resultado:

```
Welcome to Berlin
```

## A tua tarefa

Lê uma linha de entrada (um nome) e cumprimenta-a. Se a entrada for `World`, o resultado
tem de ser exatamente:

```
Hello, World
```

Portanto: lê o nome com `input()`, depois imprime `Hello, ` unido ao nome. Presta atenção
à vírgula e ao único espaço depois dela.

## Está feito quando

- Dada a entrada `World`, o resultado é `Hello, World`.
- Dado qualquer outro nome, cumprimenta esse nome da mesma forma (o verificador tenta
  mais do que um).
""",

"1.10 hints": r"""Guarda o que `input()` devolve numa variável, depois constrói o cumprimento com +.

---

`name = input()` depois `print("Hello, " + name)`. O texto antes do nome
inclui a vírgula e um espaço: "Hello, ".

---

name = input()
print("Hello, " + name)
""",

"1.10 reference": r"""`input` lê **uma linha** da entrada padrão — tudo o que o utilizador escreve até
premir Enter — remove a quebra de linha final, e devolve-a como uma **cadeia de caracteres**.

- O valor devolvido é *sempre* um `str`, mesmo que o utilizador tenha escrito dígitos:
  `input()` sobre `42` devolve `"42"`, não `42`. Para fazer aritmética, converte-o
  (vê `int()`).
- O argumento opcional `prompt` é escrito no ecrã primeiro, sem uma
  quebra de linha final, para que o utilizador escreva na mesma linha.
- Se o fluxo de entrada terminar sem haver linha para ler (fim de ficheiro), `input` levanta
  `EOFError`.

```python
name = input("Your name? ")   # prompts, then reads a line
print("Hi, " + name)
```
""",

"1.11 brief": r"""# 1.11 -- Um número a partir da entrada

## Conceito

`input()` devolve sempre **texto**, mesmo quando a pessoa escreve dígitos. Se tentares
fazer contas com isso, `+` vai juntar em vez de somar -- lembra-te do puzzle 1.7:

```python
n = input()      # user types 21  ->  n is the string "21"
print(n + n)     # "2121", not 42
```

Para fazer aritmética, primeiro **converte** o texto num número com `int(...)`:

```python
n = int(input())   # "21" -> 21, a real number now
print(n * 2)       # 42
```

`int(...)` pega em texto que se parece com um número inteiro e transforma-o num `int`
com que podes calcular. Este padrão -- `int(input())` -- é extremamente comum.

## Erro comum

`int` não se limita a "remover as aspas"; produz um tipo diferente. Depois de
`int(input())` o valor é um número, por isso `+`, `*`, `//` e companhia fazem contas a sério.

## A tua tarefa

Lê um número inteiro da entrada, depois imprime-o **duplicado**. Exemplos:

- entrada `21` -> resultado `42`
- entrada `0`  -> resultado `0`
- entrada `-5` -> resultado `-10`

Portanto: lê com `input()`, converte com `int(...)`, multiplica por 2, imprime o resultado.

## Está feito quando

- Para a entrada `21` o resultado é `42`.
- Também funciona para `0` e para um número negativo como `-5` (o verificador testa
  estes casos).
""",

"1.11 hints": r"""`input()` dá texto. Tens de o transformar num número antes de fazeres contas.

---

Envolve o input em int: `n = int(input())`. Depois `print(n * 2)`.

---

n = int(input())
print(n * 2)
""",

"1.11 reference": r"""`int` converte um valor num **inteiro**. O seu uso mais comum é transformar a
**cadeia de caracteres** que `input()` devolve num número com que podes calcular.

- `int("42")` é `42`. Espaços em branco à volta são ignorados (`int(" 42 ")` funciona);
  um sinal inicial é permitido (`int("-5")`).
- Texto que não seja um número inteiro levanta `ValueError` — `int("3.5")` e
  `int("ten")` falham ambos. Para decimais, usa `float("3.5")`.
- Chamado sobre um `float`, `int` trunca *em direção a zero* (`int(3.9)` é `3`,
  `int(-3.9)` é `-3`).

Como `input()` produz sempre texto, ler um número é um idioma de dois passos:

```python
n = int(input("How many? "))   # read text, then parse it to an int
print(n * 2)
```
""",
}
