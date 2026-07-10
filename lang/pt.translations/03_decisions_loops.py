# PyQuest translations -- language 'pt' -- chapter 03_decisions_loops -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"3.1 brief": r"""# 3.1 -- Booleanos e comparação

## Conceito

Um **booleano** é um valor que é `True` ou `False` -- uma resposta sim/não.
É o seu próprio tipo (`bool`), escrito com letra maiúscula.

Obténs booleanos ao **comparar** valores:

| operador | significado |
|---|---|
| `==` | igual a |
| `!=` | diferente de |
| `<`  | menor que |
| `>`  | maior que |
| `<=` | menor ou igual a |
| `>=` | maior ou igual a |

```python
print(3 < 5)      # True
print(3 == 5)     # False
print(7 >= 7)     # True
```

Repara que `==` (comparar) tem **dois** sinais de igual. Um único `=` *atribui* uma
variável; `==` *pergunta "isto é igual?"*.

## Exemplo

```python
a = 4
b = 9
print(a > b)      # False
```

## A tua tarefa

Lê dois números inteiros (cada um na sua própria linha). Imprime se o **primeiro é
maior do que o segundo** -- isto é, imprime o resultado de `first > second`
(que será `True` ou `False`).

Para a entrada `8` seguida de `3`, a saída é:

```
True
```

## Está feito quando

- Para `8` seguido de `3` imprime `True`; para `2` seguido de `5` imprime `False`.
- Quando os dois números são iguais imprime `False` (igual não é "maior").
""",

"3.1 hints": r"""Uma comparação como a > b já é True ou False -- podes imprimi-la diretamente.

---

Lê os dois números como inteiros e depois imprime a comparação:
`print(first > second)`.

---

a = int(input())
b = int(input())
print(a > b)
""",

"3.1 reference": r"""Um **booleano** é um de dois valores, `True` ou `False` (tipo `bool`). Os
**operadores de comparação** produzem um booleano ao comparar dois valores:

- `==` igual, `!=` diferente,
- `<` menor que, `>` maior que, `<=` no máximo, `>=` no mínimo.

`==` (uma pergunta, "isto é igual?") não é `=` (um comando, "atribuir"). Os números
comparam-se por valor; as strings comparam-se **lexicograficamente** (ordem
alfabética, por código de carácter, pelo que as maiúsculas ficam antes das
minúsculas). As comparações podem ser **encadeadas**: `0 <= x < 10` significa
`0 <= x and x < 10`.

```python
3 < 5        # True
3 == 3.0     # True   -- valores iguais, tipos diferentes
"a" < "b"    # True
```
""",

"3.2 brief": r"""# 3.2 -- if

## Conceito

Uma **instrução `if`** executa um bloco de código **apenas quando** uma condição é `True`:

```python
if condition:
    do_something()
    do_more()
```

Duas coisas a notar:

1. A linha termina com **dois pontos** `:`.
2. As linhas que devem ser executadas quando a condição é verdadeira estão **indentadas**
   (usa 4 espaços). A indentação é como o Python sabe quais linhas pertencem ao `if`.
   Quando a condição é `False`, as linhas indentadas são ignoradas.

```python
age = 20
if age >= 18:
    print("adult")     # runs only when age >= 18
```

Se `age` fosse `15`, nada seria impresso.

## Erro comum

A indentação não é decoração em Python -- ela define o bloco. Esquecer de
indentar (ou misturar espaços) é um erro de sintaxe.

## A tua tarefa

Lê um número inteiro. **Se for negativo**, imprime `negative`. Se não for
negativo, não imprimas nada.

Para a entrada `-4` a saída é:

```
negative
```

Para a entrada `7` não há saída.

## Está feito quando

- Um número negativo imprime `negative`.
- Zero e números positivos não imprimem nada (`0` não é negativo).
""",

"3.2 hints": r"""Um número é negativo quando é menor que 0:  n < 0.

---

Escreve `if n < 0:` e depois, na linha seguinte, um `print("negative")` indentado.

---

n = int(input())
if n < 0:
    print("negative")
""",

"3.2 reference": r"""Uma instrução **`if`** executa um bloco indentado **apenas quando** a sua condição é verdadeira.
A condição é avaliada como um booleano; se for verdadeira, o bloco é executado; se for falsa, é
ignorado e o programa continua abaixo.

- O bloco é definido pela **indentação** (por convenção, 4 espaços). Todas as linhas
  indentadas sob o `if` pertencem-lhe; a primeira linha de volta ao nível exterior
  termina-o.
- A condição não precisa de ser um `True`/`False` literal — qualquer valor é testado quanto
  à sua **veracidade** (*truthiness*): `0`, `0.0`, `""` e coleções vazias são falsos; tudo o
  resto é verdadeiro.

```python
if temperature > 30:
    print("hot")        # runs only when the test is True
print("done")           # always runs -- not indented under the if
```
""",

"3.3 brief": r"""# 3.3 -- if / else

## Conceito

O `else` dá ao `if` um segundo ramo: código a executar quando a condição é
**False**. Executa-se exatamente um dos dois blocos.

```python
if temperature > 30:
    print("hot")
else:
    print("not hot")
```

O `else:` alinha-se com o `if` (mesma indentação), e o seu bloco é indentado
tal como o bloco do `if`.

## Um lembrete

`n % 2` é o resto da divisão de `n` por 2 (conheceste o `%` no capítulo 1). Um
número é **par** exatamente quando `n % 2 == 0`.

## Exemplo

```python
n = 7
if n % 2 == 0:
    print("even")
else:
    print("odd")
# prints: odd
```

## A tua tarefa

Lê um número inteiro e imprime `even` se for par, ou `odd` se não for.

Para a entrada `10` a saída é:

```
even
```

## Está feito quando

- Números pares imprimem `even`, números ímpares imprimem `odd`.
- Funciona para `0` (par) e também para números negativos.
""",

"3.3 hints": r"""Par significa que o resto da divisão por 2 é zero:  n % 2 == 0.

---

Usa if/else: se `n % 2 == 0` imprime "even", senão imprime "odd".

---

n = int(input())
if n % 2 == 0:
    print("even")
else:
    print("odd")
""",

"3.3 reference": r"""Uma cláusula **`else`** dá ao `if` um segundo ramo: o seu bloco é executado exatamente quando
a condição do `if` é **falsa**. Juntos formam uma escolha de dois caminhos — executa-se sempre
um ramo ou o outro, nunca os dois.

- O `else` não tem condição; é o caso genérico para "o `if` foi falso".
- Tem de estar emparelhado com um `if` à mesma indentação, e o seu bloco é indentado
  da mesma forma.

```python
if n % 2 == 0:
    print("even")
else:
    print("odd")        # runs only when n % 2 == 0 is False
```
""",

"3.4 brief": r"""# 3.4 -- elif

## Conceito

O `elif` (abreviatura de "else if") acrescenta **mais ramos** entre o `if` e o `else`.
O Python verifica cada condição por ordem e executa a **primeira** que for `True`;
as restantes são ignoradas. O `else` (opcional) apanha tudo o que sobrar.

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

A ordem importa: como o primeiro ramo verdadeiro é o que vence, normalmente vais da
condição mais específica ou mais elevada para baixo.

## Exemplo

```python
n = 0
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
# prints: zero
```

## A tua tarefa

Lê um número inteiro e imprime exatamente um destes:

- `negative` se for menor que 0,
- `zero` se for 0,
- `positive` se for maior que 0.

Para a entrada `0` a saída é:

```
zero
```

## Está feito quando

- `-3` imprime `negative`, `0` imprime `zero`, `5` imprime `positive`.
- Exatamente uma linha é impressa para qualquer entrada.
""",

"3.4 hints": r"""Três casos significa if ... elif ... else.

---

`if n < 0:` -> negative; `elif n == 0:` -> zero; `else:` -> positive.

---

n = int(input())
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
""",

"3.4 reference": r"""O **`elif`** ("else if") acrescenta mais ramos entre o `if` e o `else`. O Python verifica
cada condição **por ordem** e executa o bloco da **primeira** que for verdadeira,
ignorando as restantes. Um `else` final opcional trata o caso "nenhuma correspondeu".

- Apenas um ramo é executado — o primeiro que for verdadeiro. As condições seguintes nem
  sequer são avaliadas.
- Como a primeira correspondência vence, a ordem importa: coloca os testes mais
  específicos ou de maior prioridade primeiro.
- Uma cadeia de `elif` é mais plana e clara do que aninhar um `if` dentro de cada
  `else`.

```python
if score >= 90:
    grade = "A"
elif score >= 80:       # only checked if the first was False
    grade = "B"
else:
    grade = "C"
```
""",

"3.5 brief": r"""# 3.5 -- and / or / not

## Conceito

Podes combinar booleanos com três palavras:

- `and` -- True apenas se **ambos** os lados forem True.
- `or` -- True se **qualquer um** dos lados for True.
- `not` -- inverte um booleano: `not True` é `False`.

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

age = 25
print(age >= 18 and age < 65)   # True  (both hold)
```

Isto permite que uma única condição teste várias coisas ao mesmo tempo.

## Exemplo

```python
n = 12
print(n % 2 == 0 and n % 3 == 0)   # True  (12 is divisible by both)
```

## A tua tarefa

Lê um número inteiro. Imprime se é divisível **tanto** por 2 como por 3 -- isto
é, imprime o resultado de `(n % 2 == 0) and (n % 3 == 0)` (que é `True` ou
`False`).

Para a entrada `12` a saída é:

```
True
```

## Está feito quando

- `12` e `6` imprimem `True`; `4` e `9` imprimem `False`.
- `0` imprime `True` (0 é divisível por tudo).
""",

"3.5 hints": r""""Divisível por 2" é n % 2 == 0. Precisas disso E do mesmo para o 3.

---

Junta as duas verificações com `and`, e imprime tudo:
`print(n % 2 == 0 and n % 3 == 0)`.

---

n = int(input())
print(n % 2 == 0 and n % 3 == 0)
""",

"3.5 reference": r"""Os **operadores booleanos** combinam condições:

- **`and`** é verdadeiro apenas quando **ambos** os lados são verdadeiros.
- **`or`** é verdadeiro quando **pelo menos um** dos lados é verdadeiro.
- **`not`** inverte um único valor.

Fazem **avaliação em curto-circuito** (*short-circuit*): o `and` para no primeiro operando
falso, o `or` no primeiro verdadeiro, pelo que o lado direito não é avaliado quando o
esquerdo já decide o resultado. A precedência é `not` > `and` > `or`; os parênteses
tornam a intenção óbvia.

```python
0 < x and x < 100      # True only inside the range
done or out_of_time    # True if either holds
not finished           # flips the flag
```
""",

"3.6 brief": r"""# 3.6 -- Condições aninhadas

## Conceito

Um bloco `if` pode conter **outro** `if`. Isto chama-se **aninhamento** (*nesting*). A
verificação interior só acontece quando a condição exterior já é verdadeira. Cada nível
é indentado um passo mais.

```python
if logged_in:
    if is_admin:
        print("admin panel")
    else:
        print("user page")
else:
    print("please log in")
```

Aqui, `is_admin` só é verificado quando `logged_in` é verdadeiro.

## Exemplo

```python
n = 250
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
# prints: big
```

## A tua tarefa

Lê um número inteiro e classifica-o:

- se for **0 ou negativo**, imprime `non-positive`;
- caso contrário (é positivo), imprime `small` quando for **menor que 100**, ou
  `big` quando for **100 ou mais**.

Usa um `if` aninhado (uma verificação exterior para positivo, uma interior para o
tamanho).

Para a entrada `42` a saída é:

```
small
```

## Está feito quando

- `-1` e `0` imprimem `non-positive`; `42` imprime `small`; `100` e `500` imprimem
  `big`.
""",

"3.6 hints": r"""Primeiro decide positivo ou não. Só se for positivo é que perguntas small ou big.

---

Exterior: `if n > 0:` ... `else: print("non-positive")`. Dentro do if, outro
if/else a comparar n com 100.

---

n = int(input())
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
""",

"3.6 reference": r"""Um bloco `if` pode conter, ele próprio, outro `if` — **aninhamento**. O teste interior
só é executado **quando** a condição exterior é verdadeira, pelo que o aninhamento
exprime "isto, e depois, dentro disso, aquilo".

- Cada nível acrescenta um passo de indentação; o bloco interior é indentado sob o
  `if` interior.
- O aninhamento e o `and` podem exprimir a mesma coisa — `if a: if b:` é como
  `if a and b:` — mas o aninhamento é a ferramenta certa quando o caso exterior precisa
  do seu próprio tratamento (por exemplo, um `else`) separado do interior.
- Mantém o aninhamento pouco profundo; pirâmides profundas são difíceis de ler, e uma
  cadeia de `elif` ou um `return` antecipado costumam ler-se melhor.

```python
if logged_in:
    if is_admin:
        show_admin_panel()   # only when logged_in AND is_admin
    else:
        show_user_panel()    # logged_in but not admin
```
""",

"3.7 brief": r"""# 3.7 -- while

## Conceito

Um **ciclo `while`** repete um bloco **enquanto** uma condição se mantiver `True`. Ele
verifica a condição, executa o bloco, e verifica outra vez -- sucessivamente:

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1   # move toward making the condition False
# prints 1, 2, 3
```

A linha `count = count + 1` é essencial: altera `count` para que a condição
acabe por se tornar `False`. Sem ela, o ciclo nunca para.

## Erro comum -- o ciclo sem fim

Se a condição nunca se tornar `False`, o ciclo executa-se para sempre. Certifica-te
sempre de que algo dentro do ciclo se aproxima do ponto de paragem. (Se o teu
programa parecer bloqueado, geralmente é um ciclo sem fim.)

## Exemplo

```python
n = 4
i = 1
while i <= n:
    print(i)
    i = i + 1
# prints 1, 2, 3, 4
```

## A tua tarefa

Lê um número inteiro `n` e depois imprime todos os números de `1` até `n`, cada um na
sua própria linha, usando um ciclo `while`.

Para a entrada `3` a saída é:

```
1
2
3
```

## Está feito quando

- `3` imprime `1`, `2`, `3`. `1` imprime apenas `1`.
- `0` (ou um número negativo) não imprime nada -- o corpo do ciclo nunca é executado.
""",

"3.7 hints": r"""Começa um contador em 1 e faz o ciclo enquanto ele ainda for <= n.

---

`i = 1`, depois `while i <= n:` imprime i e depois `i = i + 1`.

---

n = int(input())
i = 1
while i <= n:
    print(i)
    i = i + 1
""",

"3.7 reference": r"""Um ciclo **`while`** repete o seu bloco **enquanto** a sua condição se mantiver verdadeira.
A condição é verificada **antes** de cada passagem; quando se torna falsa, o ciclo
termina e o programa continua abaixo.

- Algo dentro do ciclo tem de acabar por tornar a condição falsa (por exemplo, avançar
  um contador), ou então o ciclo repete-se para sempre — um ciclo infinito.
- Se a condição for falsa logo na primeira verificação, o corpo executa-se zero vezes.
- Usa `while` quando não sabes de antemão o número de passagens (fazes o ciclo até
  algo acontecer); usa `for` quando estás a contar um intervalo conhecido.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1        # moves toward ending the loop -> 3, 2, 1
```
""",

"3.8 brief": r"""# 3.8 -- Repetir até uma sentinela

## Conceito

Um ciclo não precisa de contar. Pode continuar até o utilizador introduzir um valor
especial, a **sentinela**, que significa "parar". O truque é ler uma vez *antes*
do ciclo, e voltar a ler *no fim* de cada passagem:

```python
line = input()
while line != "quit":
    print("you said:", line)
    line = input()        # read the next one
print("done")
```

O ciclo continua a executar-se enquanto a entrada não for a sentinela (`"quit"`
neste caso). Assim que a sentinela chega, a condição é falsa e o ciclo termina.

## Exemplo

Lê números e soma-os até ser introduzido um `0`:

```python
total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
```

## A tua tarefa

Lê números inteiros, um por linha, e soma-os. Para quando o número `0` for
introduzido (não somes o `0`). Depois imprime o total.

Para a entrada `4`, `5`, `0` a saída é:

```
9
```

## Está feito quando

- `4`, `5`, `0` imprime `9`; um único `0` imprime `0`.
- O próprio `0` não é somado; os números podem ser negativos.
""",

"3.8 hints": r"""Lê um número antes do ciclo, e lê o seguinte no fim de cada passagem.

---

`total = 0`, lê n, depois `while n != 0:` soma ao total e lê o n seguinte.
Depois do ciclo, imprime total.

---

total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
""",

"3.8 reference": r"""Um ciclo com **sentinela** lê valores repetidamente e para quando encontra um valor
especial de "paragem", em vez de o fazer após uma contagem fixa. O padrão é um `while`
cuja condição testa a entrada mais recente contra a sentinela.

- Lê uma vez antes do ciclo (ou lê no início de cada passagem), e depois compara com
  a sentinela para decidir se continuas.
- A própria sentinela **não** é processada — a verificação acontece antes do trabalho,
  pelo que o valor de paragem termina o ciclo em vez de ser contado.

```python
line = input()
while line != "quit":     # "quit" is the sentinel
    print("you said:", line)
    line = input()        # read the next, then re-check
```
""",

"3.9 brief": r"""# 3.9 -- for e range

## Conceito

Um **ciclo `for`** executa o seu bloco uma vez para cada item de uma sequência.
Combinado com o **`range`**, é a forma habitual de repetir algo um número fixo de
vezes.

`range(n)` produz os números `0, 1, 2, ..., n-1` (para *antes* de `n`):

```python
for i in range(4):
    print(i)
# prints 0, 1, 2, 3
```

Em cada volta, a variável do ciclo (`i` aqui) assume o valor seguinte. Não geres
tu próprio um contador -- o `range` faz isso por ti, pelo que não há risco de
ciclo sem fim.

O `range` também pode receber um início e um passo: `range(1, 5)` é `1,2,3,4`;
`range(0, 10, 2)` é `0,2,4,6,8`.

## Exemplo

```python
for i in range(3):
    print(i)
# prints 0, 1, 2
```

## A tua tarefa

Lê um número inteiro `n` e depois imprime todos os números de `0` até `n-1`, cada
um na sua própria linha, usando um ciclo `for` com `range`.

Para a entrada `4` a saída é:

```
0
1
2
3
```

## Está feito quando

- `4` imprime `0,1,2,3` (cada um numa linha). `1` imprime apenas `0`.
- `0` não imprime nada.
""",

"3.9 hints": r"""range(n) dá 0, 1, ..., n-1. Percorre-o com for.

---

`for i in range(n):` depois um `print(i)` indentado.

---

n = int(input())
for i in range(n):
    print(i)
""",

"3.9 reference": r"""**`range(n)`** produz os inteiros `0, 1, …, n - 1` — `n` números a começar em
zero — e um ciclo **`for`** executa o seu bloco uma vez para cada um, associando a
variável do ciclo ao valor atual.

- `range(n)` para **antes** de `n` (intervalo semiaberto), pelo que `range(5)` é
  `0,1,2,3,4` — cinco passagens.
- `range(start, stop)` começa em `start`; `range(start, stop, step)` conta de
  `step` em `step` (que pode ser negativo para contar para trás).
- O `range` é preguiçoso (*lazy*) — produz números à medida que são pedidos, sem
  construir uma lista — pelo que um intervalo enorme não custa nada até ser
  percorrido.

```python
for i in range(3):
    print(i)              # 0, 1, 2

for i in range(2, 6):
    print(i)              # 2, 3, 4, 5
```
""",

"3.10 brief": r"""# 3.10 -- Percorrer uma string

## Conceito

Um ciclo `for` funciona com mais do que intervalos. Uma **string é uma sequência de
caracteres**, por isso podes percorrê-la diretamente -- um carácter por passagem:

```python
for ch in "cat":
    print(ch)
# prints:
# c
# a
# t
```

Não é preciso indexar: `ch` é, sucessivamente, cada carácter. (Podes percorrer
muitos tipos de sequências desta forma; as strings são o primeiro exemplo.)

## Exemplo

```python
word = "hi"
for ch in word:
    print(ch)
# prints h then i
```

## A tua tarefa

Lê uma palavra e imprime cada um dos seus caracteres na sua própria linha, usando
um ciclo `for` sobre a string.

Para a entrada `cat` a saída é:

```
c
a
t
```

## Está feito quando

- `cat` imprime `c`, `a`, `t` em linhas separadas.
- Uma única letra imprime essa letra; uma entrada vazia não imprime nada.
""",

"3.10 hints": r"""Podes percorrer diretamente uma string -- cada passagem dá um carácter.

---

`for ch in word:` depois um `print(ch)` indentado.

---

word = input()
for ch in word:
    print(ch)
""",

"3.10 reference": r"""Uma string é **iterável**, pelo que um ciclo `for` percorre-a **um carácter de cada vez**,
por ordem, associando a variável do ciclo a cada carácter. Não indexas manualmente.

- Cada passagem dá uma string de um único carácter; o ciclo executa-se `len(s)` vezes.
- Esta é a forma direta de examinar ou contabilizar caracteres — combina-a com um `if`
  dentro do ciclo para agir sobre determinados caracteres.
- A mesma forma `for ... in` percorre qualquer sequência (listas, ranges, …), não
  apenas strings.

```python
for ch in "cat":
    print(ch)             # c, then a, then t
```
""",

"3.11 brief": r"""# 3.11 -- break e continue

## Conceito

Duas palavras-chave alteram o fluxo de um ciclo:

- **`break`** para o ciclo **imediatamente** -- não há mais passagens.
- **`continue`** salta o **resto da passagem atual** e avança para a
  seguinte.

```python
for ch in "a,b,c":
    if ch == ",":
        continue        # skip commas
    print(ch)
# prints a, b, c (commas skipped)

for n in range(100):
    if n == 3:
        break           # stop the whole loop at 3
    print(n)
# prints 0, 1, 2
```

O `continue` salta um item; o `break` termina o ciclo.

## Exemplo

```python
for ch in "abxcd":
    if ch == "x":
        break
    print(ch)
# prints a, b   (stops at x)
```

## A tua tarefa

Lê uma palavra e percorre os seus caracteres:

- **salta** a letra `o` (usa `continue` -- não a imprimas),
- **para** completamente na letra `x` (usa `break` -- não imprimas nada a partir
  do `x`),
- imprime todos os outros caracteres, cada um na sua própria linha.

Para a entrada `boxes` a saída é:

```
b
```

(`b`, depois `o` é saltado, depois `x` para o ciclo.)

## Está feito quando

- `boxes` imprime `b`; `good` imprime `g` e depois `d` (os `o`s são saltados);
  `abc` imprime `a`, `b`, `c`.
""",

"3.11 hints": r"""Dentro do ciclo, verifica primeiro "x" (break), depois "o" (continue), depois imprime.

---

`for ch in word:` -> `if ch == "x": break`, depois `if ch == "o": continue`,
depois `print(ch)`.

---

word = input()
for ch in word:
    if ch == "x":
        break
    if ch == "o":
        continue
    print(ch)
""",

"3.11 reference": r"""Duas instruções alteram o fluxo de um ciclo a partir de dentro dele:

- **`break`** termina o ciclo **imediatamente**, saltando quaisquer passagens
  restantes e avançando para o código depois do ciclo. Usa-o para parar assim que
  encontrares o que procuravas.
- **`continue`** salta o **resto da passagem atual** e avança diretamente para a
  iteração seguinte do ciclo (voltando a verificar a condição / passando para o
  item seguinte).

Ambos afetam apenas o ciclo **mais interior** que os envolve.

```python
for n in range(10):
    if n == 5:
        break             # stop the whole loop at 5
    if n % 2 == 0:
        continue          # skip evens, go to the next n
    print(n)              # 1, 3
```
""",

"3.12 brief": r"""# 3.12 -- O padrão acumulador

## Conceito

Um padrão de ciclo muito comum: manter um **total corrente** numa variável, começá-la
em `0`, e somar-lhe algo em cada passagem. A variável "acumula" o resultado.

```python
total = 0
for n in [4, 2, 9]:
    total = total + n
print(total)        # 15
```

Os passos-chave são: **começar em 0 antes do ciclo**, **somar dentro do ciclo**,
**usar o resultado depois do ciclo**. A mesma forma serve para contar (começar em 0,
somar 1 de cada vez) ou construir uma string (começar em "", somar um pedaço de
cada vez).

Este puzzle combina o que já aprendeste: um ciclo `for`, `range`, ler entrada, e
um acumulador.

## Exemplo

```python
total = 0
for _ in range(3):
    total = total + int(input())
print(total)
```

(`_` é um nome de variável comum, usado quando não precisas do valor do ciclo.)

## A tua tarefa

Lê um número inteiro `n` (uma contagem). Depois lê mais `n` números inteiros, um
por linha, e imprime a sua **soma**.

Para a entrada `3`, seguida de `10`, `20`, `5`, a saída é:

```
35
```

## Está feito quando

- Contagem `3` com `10, 20, 5` imprime `35`.
- Uma contagem de `0` não lê mais nenhum número e imprime `0`.
- Os números podem ser negativos.
""",

"3.12 hints": r"""Lê primeiro a contagem. Começa um total em 0 e depois repete esse número de
vezes, somando cada número.

---

`n = int(input())`, `total = 0`, depois `for _ in range(n):` soma `int(input())`
ao total. Imprime total depois do ciclo.

---

n = int(input())
total = 0
for _ in range(n):
    total = total + int(input())
print(total)
""",

"3.12 reference": r"""O padrão **acumulador** constrói um resultado ao longo de um ciclo. Inicializas uma
variável **antes** do ciclo, depois atualizas-a em **cada** passagem; depois do ciclo,
ela contém o resultado combinado.

- Para uma soma, começa o total em `0` e soma cada valor (`total = total + x`, ou
  `total += x`). Começar em `0` é o elemento neutro da `+`, pelo que um ciclo vazio
  o deixa em `0`.
- A mesma forma conta (começar em 0, `+= 1` por correspondência), constrói uma
  string (começar em `""`, `+=`), ou reúne uma lista (começar em `[]`, `.append`).
- O acumulador tem de viver **fora** do ciclo — declará-lo dentro reiniciá-lo-ia a
  cada passagem.

```python
total = 0
for n in [3, 1, 4]:
    total += n            # 3, then 4, then 8
print(total)             # 8
```
""",
}
