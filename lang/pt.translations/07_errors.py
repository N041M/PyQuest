# PyQuest translations -- language 'pt' -- chapter 07_errors -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"7.1 brief": r"""# 7.1 -- try / except

## Conceito

Já *causaste* bastantes erros até agora. Chegou a altura de **tratares** de um.

Quando o Python encontra algo impossível -- como `int("hello")` -- **levanta uma
exceção**: o fluxo normal para de repente e, a menos que alguém trate disso, o
programa falha com um traceback. `try`/`except` é a forma de tratares disso:

```python
try:
    n = int(text)
    print("a number!")
except ValueError:
    print("not a number")
```

Como isto funciona:

- O bloco `try` corre normalmente -- **até** uma linha levantar uma exceção.
- Se nada levantar uma exceção, o bloco `except` é ignorado por completo.
- Se `int(text)` levantar um `ValueError` (a sua queixa sobre texto que não é
  convertível), o resto do bloco `try` é abandonado e o bloco `except` corre
  em vez disso. **Sem falha.**

O programa *recupera*: escolheu o que a falha significa, em vez de simplesmente cair.

## Exemplo

A entrada `7` imprime `14`. A entrada `seven` imprime `not a number` -- o mesmo
código, sem falhar em nenhum dos casos.

## A tua tarefa

Lê uma linha. Se ela se converter num número inteiro, imprime esse número
**duplicado**. Se não se converter, imprime exatamente `not a number`. (Este é
outra vez um puzzle de script: `input()` e `print()` estão de volta.)

## Está feito quando

- `7` imprime `14`; `-3` imprime `-6`.
- `seven` e `12abc` imprimem `not a number` -- e o programa termina de forma
  limpa, sem traceback.
- Usaste `try`/`except` -- o verificador exige mesmo isso.
""",

"7.1 hints": r"""int("seven") levanta um ValueError -- põe a conversão dentro de um bloco try.

---

try: converte e imprime o dobro. except ValueError: imprime a mensagem.
O bloco except só corre quando a conversão falhou.

---

line = input()
try:
    n = int(line)
    print(n * 2)
except ValueError:
    print("not a number")
""",

"7.1 reference": r"""Uma instrução **`try` / `except`** corre código arriscado e apanha o erro se
falhar, em vez de deixar o programa cair. O bloco `try` contém o código que
pode **levantar** uma exceção; o bloco `except` só corre se isso acontecer.

- Se o bloco `try` for bem-sucedido, o `except` é completamente ignorado.
- Se uma instrução em `try` levantar uma exceção, o **resto do `try` é
  abandonado** e o controlo salta para o `except` correspondente; o programa
  continua depois disso.
- Um erro não apanhado desenrola o programa inteiro com um traceback —
  `except` é a forma de intervires.

```python
try:
    n = int(text)        # may raise ValueError
except ValueError:
    n = 0                # recover instead of crashing
```
""",

"7.2 brief": r"""# 7.2 -- Apanha o erro CERTO

## Conceito

`except` pode indicar qual o erro que trata -- e deve fazê-lo. Erros que não
esperavas são **informação**, e engoli-los esconde bugs.

```python
try:
    n = int(text)
except ValueError:        # exactly the error int() raises for bad TEXT
    n = None
```

O atalho tentador é um `except:` (ou `except Exception:`) sem nome -- "apanha
tudo, não pode falhar!" Mas *tudo* inclui erros que significam que **o teu
código está a ser usado incorretamente**. `int([1, 2])` não levanta um
`ValueError` -- levanta um `TypeError` ("um tipo de coisa completamente
errado"), e esse *deveria* falhar ruidosamente para que o bug de quem chamou
a função seja encontrado, não escondido.

A regra: **apanha exatamente o que esperas; deixa tudo o resto escapar.**

## Exemplo

```python
safe_int("42")      # 42
safe_int("nope")    # None         (ValueError, handled)
safe_int([1, 2])    # TypeError!   (NOT handled -- a misuse, let it crash)
```

## A tua tarefa

Define `safe_int(text)` que devolve `int(text)`, ou `None` quando o texto não
é um número válido. Apanha **apenas** `ValueError` -- um `TypeError` vindo de
algo que não é uma string tem de escapar.

## Está feito quando

- `safe_int("42")` é `42`; `safe_int("-7")` é `-7`.
- `safe_int("nope")` e `safe_int("")` são `None`.
- `safe_int([1, 2])` levanta `TypeError` -- o verificador chama-o de propósito
  com uma lista, por isso apanhar de mais falha.
""",

"7.2 hints": r"""return int(text) dentro do try; o except devolve None em vez disso.

---

Nomeia o erro: `except ValueError:` -- não nomear nada (ou Exception) também
apanha o TypeError que o verificador envia, e esse tem de escapar.

---

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None
""",

"7.2 reference": r"""Um `except` deve indicar a exceção **específica** que esperas. Apanhar
exatamente o tipo certo permite que erros inesperados apareçam como bugs em
vez de serem silenciosamente engolidos.

- `except ValueError:` apanha apenas esse tipo; uma falha não relacionada
  (um nome mal escrito que levanta `NameError`) continua a propagar-se, o que
  é o que queres.
- Um `except:` sem nome (ou `except Exception:`) apanha **tudo**, incluindo
  bugs que preferirias ver — evita-o a menos que queiras mesmo dizer
  "qualquer falha".
- Faz corresponder o tipo à operação: `int()` levanta `ValueError`, indexar
  levanta `IndexError`, uma pesquisa num dicionário levanta `KeyError`.

```python
try:
    value = data[key]
except KeyError:         # only a missing key, not other bugs
    value = None
```
""",

"7.3 brief": r"""# 7.3 -- ZeroDivisionError: pede perdão

## Conceito

Dividir por zero levanta `ZeroDivisionError`. Há duas formas de escrever uma
divisão que sobrevive a isso:

```python
# "look before you leap": test first
if b == 0:
    return None
return a / b

# "easier to ask forgiveness": just try it
try:
    return a / b
except ZeroDivisionError:
    return None
```

Ambas se comportam da mesma forma *aqui* -- mas o estilo do Python favorece
fortemente a segunda, e este puzzle exige-a. Porquê:

- O `try` nomeia o acontecimento real ("a divisão falhou") em vez de uma
  pré-condição que tens de manter sincronizada com ele.
- Verificações prévias não escalam: operações reais podem falhar de várias
  formas (ficheiro em falta, permissão negada, ligação perdida...). Não
  consegues testar todas antecipadamente -- mas um único `except` consegue
  apanhar a própria falha.

Este estilo chama-se **EAFP**: *easier to ask forgiveness than permission*
(mais fácil pedir perdão do que permissão).

## Exemplo

```python
safe_div(10, 4)    # 2.5
safe_div(5, 0)     # None  -- handled, no crash
```

## A tua tarefa

Define `safe_div(a, b)` que devolve `a / b`, ou `None` quando `b` é zero --
usando `try`/`except`, e não um `if`.

## Está feito quando

- `safe_div(10, 4)` é `2.5`; `safe_div(5, 0)` é `None`.
- `safe_div(0, 5)` é `0.0` -- zero no numerador é uma divisão perfeitamente
  válida.
- Apanhaste `ZeroDivisionError` -- um teste com if foge à lição e falha.
""",

"7.3 hints": r"""Tenta a divisão dentro do try -- não testes b primeiro.

---

`except ZeroDivisionError: return None` -- o return antecipado (6.5) dentro
do try trata do caminho feliz.

---

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
""",

"7.3 reference": r"""Dividir por zero levanta **`ZeroDivisionError`**. Apanhá-lo demonstra o
estilo **EAFP** — "mais fácil pedir perdão do que permissão": tentas a
operação e tratas da falha, em vez de testares antecipadamente todos os
casos maus.

- `a / 0` e `a // 0` e `a % 0` levantam todos esta exceção. Envolver a
  divisão num `try` permite-te fornecer uma alternativa quando o divisor
  acaba por ser zero.
- O EAFP muitas vezes lê-se de forma mais limpa do que um `if b != 0:` de
  guarda, e evita uma corrida entre a verificação e a utilização.

```python
try:
    rate = hits / total
except ZeroDivisionError:
    rate = 0.0           # no data yet -- sensible fallback
```
""",

"7.4 brief": r"""# 7.4 -- IndexError e acesso seguro

## Conceito

Indexar para lá do fim de uma lista levanta `IndexError`:

```python
items = ["a", "b"]
items[5]      # IndexError!
```

Um "safe get" devolve uma alternativa em vez de falhar -- e é mais um sítio
onde *tentar* vence *testar antecipadamente*. Lembra-te de que índices
negativos são **válidos** (2.2): `items[-1]` é o último elemento, `items[-2]`
o anterior a esse. Uma verificação de limites escrita à mão tem de acertar em
`0 <= i`... não, espera, `-len <= i < len`... exatamente, nas duas direções.
Ou simplesmente tentas:

```python
try:
    return items[i]
except IndexError:
    return default
```

O `except` está correto *por definição* -- dispara precisamente quando o
próprio Python diz que o índice é mau, negativos incluídos.

## Exemplo

```python
item_or(["a", "b"], 0, "?")     # "a"
item_or(["a", "b"], -1, "?")    # "b"   -- valid negative index
item_or(["a", "b"], 5, "?")     # "?"   -- out of range, fallback
```

## A tua tarefa

Define `item_or(items, i, default)` que devolve `items[i]`, ou `default`
quando `i` está fora do intervalo -- usando `try`/`except IndexError`.

## Está feito quando

- `item_or(["a", "b"], 1, "?")` é `"b"`; o índice `5` dá `"?"`.
- `item_or(["a", "b"], -1, "?")` é `"b"` -- negativos que cabem são válidos.
- `item_or([], 0, "?")` é `"?"` -- uma lista vazia não tem nenhum índice
  válido.
- Usaste `try`/`except` -- aritmética de limites foge à lição e falha.
""",

"7.4 hints": r"""Basta indexar dentro de um try -- o Python já sabe exatamente quais os
índices que são maus.

---

`except IndexError: return default` -- isto acerta nos negativos de graça,
o que uma verificação de limites escrita à mão normalmente não consegue.

---

def item_or(items, i, default):
    try:
        return items[i]
    except IndexError:
        return default
""",

"7.4 reference": r"""Indexar para lá do fim de uma lista (ou string) levanta **`IndexError`**.
Apanhá-lo transforma uma pesquisa arriscada num **acesso seguro** que
devolve uma alternativa quando a posição não existe.

- `lst[i]` levanta uma exceção se `i >= len(lst)` (ou `i < -len(lst)`); o
  `except` fornece uma alternativa em vez de deixar cair o programa.
- Este é o contraponto EAFP de verificar primeiro `if i < len(lst):` —
  útil quando o caso fora do intervalo é normal e não um bug.

```python
def get(lst, i, default=None):
    try:
        return lst[i]
    except IndexError:
        return default   # position absent -> fallback
```
""",

"7.5 brief": r"""# 7.5 -- raise: os erros também são teus

## Conceito

Até agora tens *apanhado* erros que o Python levantou. Também podes
**levantar os teus próprios** -- e boas funções fazem-no, assim que lhes é
entregue algo sem sentido:

```python
def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

`raise` cria o erro e lança-o ali mesmo: a função para, e quem a chamou
recebe o mesmo tratamento que `int("nope")` dá -- apanhável com `try`,
ruidoso se ignorado.

Porquê levantar em vez de devolver algo como `None` ou `-1`? Porque um valor
errado viaja: é guardado, somado, impresso, e a falha (se houver) acontece
longe do erro real. Um raise fixa a falha no momento e na mensagem --
`ValueError("age cannot be negative")` diz exatamente o que correu mal, e
onde correu mal. Lixo à entrada, **erro** à saída -- nunca lixo à saída.

## Exemplo

```python
checked_age(30)     # 30
checked_age(0)      # 0    -- zero is a fine age
checked_age(-1)     # ValueError: age cannot be negative
```

## A tua tarefa

Define `checked_age(age)` que devolve a idade sem alterações -- mas levanta
um `ValueError` quando ela é negativa. Dá-lhe uma mensagem que diga o que
está errado.

## Está feito quando

- `checked_age(30)` devolve `30`; `checked_age(0)` devolve `0`.
- `checked_age(-1)` levanta `ValueError`.
- Usaste `raise` -- o verificador procura a própria instrução.
""",

"7.5 hints": r"""Protege primeiro, devolve depois: se a idade for negativa, levanta a
exceção; caso contrário está bem como está.

---

A proteção são duas linhas: if age < 0: e depois
raise ValueError("age cannot be negative").

---

def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
""",

"7.5 reference": r"""**`raise`** dispara uma exceção **por ti próprio**, parando a função e
sinalizando que algo está errado. Permite que o teu código rejeite entradas
inválidas no momento em que são detetadas, tal como fazem as funções nativas.

- `raise ValueError("amount must be positive")` constrói uma exceção com uma
  mensagem e lança-a; a execução para a menos que um `try` mais acima na
  cadeia de chamadas a apanhe.
- Escolhe o tipo que se adequa: `ValueError` para um valor errado, `TypeError`
  para um tipo errado. A mensagem explica o que era esperado.
- Levantar a exceção na fronteira (assim que a entrada chega) mantém o resto
  do código capaz de confiar nos seus dados.

```python
def withdraw(amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    ...
```
""",

"7.6 brief": r"""# 7.6 -- Pergunta outra vez: o ciclo de repetição

## Conceito

O uso clássico de `try`/`except` num programa a sério: **continuar a
perguntar até a entrada fazer sentido.** Combina um ciclo `while True` (3.7),
`break` (3.11), e o `except` de 7.1:

```python
while True:
    try:
        n = int(input())
        break              # got a good one -- leave the loop
    except ValueError:
        pass               # bad line -- silently go around again
```

A forma a interiorizar:

- o **caminho feliz** termina em `break`;
- o **except** absorve a falha e deixa o ciclo tentar outra vez;
- depois do ciclo, `n` está garantidamente válido -- o código a seguir pode
  confiar nele.

(`pass` é a instrução do Python para "não fazer nada" -- o bloco except tem
de conter *alguma coisa*.)

## Exemplo

Para as linhas de entrada `cat`, `dog`, `21` o programa ignora as duas
primeiras e imprime `42`.

## A tua tarefa

Lê linhas até uma se converter num número inteiro, depois imprime esse
número **duplicado**. Linhas inválidas não produzem qualquer saída.

## Está feito quando

- `21` como primeira linha imprime `42`.
- `cat`, `dog`, `21` também imprime apenas `42` -- o lixo é repetido em
  silêncio.
- Números negativos funcionam.
- Usaste um ciclo e `try`/`except`.
""",

"7.6 hints": r"""while True à volta de um try: converte e break; o except simplesmente volta
a tentar.

---

except ValueError: pass -- `pass` significa "não faças nada", o que aqui
significa "tenta outra vez". Imprime DEPOIS do ciclo, onde n está garantido
que é bom.

---

while True:
    try:
        n = int(input())
        break
    except ValueError:
        pass
print(n * 2)
""",

"7.6 reference": r"""O **ciclo de repetição** continua a perguntar até obter um valor válido.
Combina um `while True` com `try` / `except`: se tiver sucesso, faz `break`
para sair; se falhar, volta ao ciclo para perguntar outra vez.

- O `try` tenta a conversão/operação; um caminho bem-sucedido termina com
  `break`, saindo do ciclo.
- O `except` trata da entrada inválida (muitas vezes só imprimindo uma dica
  e continuando), para que o `while True` faça mais uma passagem.
- Um `while True` sem outra saída depende desse `break` — o caso válido é a
  única forma de sair.

```python
while True:
    try:
        n = int(input("number: "))
        break                 # valid -> leave the loop
    except ValueError:
        print("not a number, try again")
```
""",

"7.7 brief": r"""# 7.7 -- Ler o erro: except ... as e

## Conceito

Uma exceção não é apenas um sinal -- é um **objeto que transporta uma
mensagem**. Apanha-a *para uma variável* com `as`, e podes usar essa
mensagem:

```python
try:
    n = int(text)
except ValueError as e:
    print(e)
```

Para `text = "5x"`, isso imprime o próprio diagnóstico do Python:

```
invalid literal for int() with base 10: '5x'
```

`e` é o objeto de erro; imprimi-lo mostra a sua mensagem. É assim que
programas a sério registam o que realmente correu mal, em vez de um vago
"algo falhou" -- a diferença entre um relatório de bug em que consegues agir
e um em que não consegues.

(Não escreves a mensagem tu próprio aqui -- tu *transmites* a que o Python
anexou quando a levantou.)

## Exemplo

A entrada `7` imprime `7`. A entrada `5x` imprime
`invalid literal for int() with base 10: '5x'`.

## A tua tarefa

Lê uma linha. Se ela se converter num número inteiro, imprime o número. Se
não se converter, apanha o `ValueError` **como `e`** e imprime o próprio `e`
-- a mensagem do Python, não uma tua.

## Está feito quando

- `7` imprime `7`.
- `5x` imprime exatamente a mensagem `invalid literal ...: '5x'` -- com o
  texto ofensor citado lá dentro.
- Não escreveste a mensagem à mão (tem de corresponder para *qualquer*
  entrada, o que só imprimir `e` consegue fazer bem).
""",

"7.7 hints": r"""O `as e` vai mesmo na linha do except: except ValueError as e:

---

Dentro do bloco except, basta print(e) -- o objeto imprime-se como a sua
mensagem.

---

line = input()
try:
    print(int(line))
except ValueError as e:
    print(e)
""",

"7.7 reference": r"""**`except ValueError as e:`** liga o objeto da exceção apanhada a um nome,
para que o possas inspecionar — mais simplesmente imprimindo-o para mostrar
o que correu mal.

- O objeto da exceção transporta o detalhe; `str(e)` (ou `print(e)`) produz
  a sua mensagem. `type(e).__name__` dá o nome da classe do erro.
- O nome `e` só existe dentro do bloco `except`.
- Um único handler pode apanhar uma família inteira nomeando uma classe
  base: `except Exception as e:` liga qualquer uma das suas subclasses (usa
  com moderação — apanhar de forma demasiado ampla esconde bugs).

```python
try:
    int("xyz")
except ValueError as e:
    print("bad input:", e)    # bad input: invalid literal for int()...
```
""",

"7.8 brief": r"""# 7.8 -- Capstone: uma calculadora robusta

## Conceito

Um único `try` pode ter **vários** blocos `except` -- um por cada tipo de
falha, cada um escolhendo a sua própria recuperação:

```python
try:
    ...
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
```

Seja qual for o erro levantado, este escolhe o seu bloco correspondente; os
outros são ignorados. Este capstone liga todo o capítulo ao exercício
clássico: uma calculadora que **não pode ser feita cair** pela sua entrada.
Também precisa de `split` (4.4), indexação (2.1), `elif` (3.4), e `/` (1.9).

## Exemplo

```
input "8 + 5"   ->  13
input "9 / 2"   ->  4.5
input "9 / 0"   ->  cannot divide
input "two * 3" ->  bad number
input "8 ? 5"   ->  unknown op
```

## A tua tarefa

Lê uma linha da forma `<number> <op> <number>` (três partes separadas por
espaços). Para as operações `+`, `-`, `*` imprime o resultado como número
inteiro; para `/` imprime o resultado como float. Trata todas as falhas:

- uma parte que não é um número inteiro -> imprime `bad number`
- divisão por zero -> imprime `cannot divide`
- qualquer outro símbolo de operação -> imprime `unknown op`

## Está feito quando

- `8 + 5` -> `13`, `9 / 2` -> `4.5`, `3 * -2` -> `-6`.
- `9 / 0` -> `cannot divide`; `two * 3` -> `bad number`; `8 ? 5` ->
  `unknown op`.
- Nenhuma entrada o faz cair: cada falha imprime a sua própria mensagem
  através de blocos `except` (e um `else`/`elif` para a operação
  desconhecida).
""",

"7.8 hints": r"""split() a linha em três partes; converte parts[0] e parts[2] dentro do try.

---

Empilha os dois excepts depois de um try: ValueError -> "bad number",
ZeroDivisionError -> "cannot divide". A cadeia da operação é if/elif/else,
com o else a imprimir "unknown op".

---

parts = input().split()
try:
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("unknown op")
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
""",

"7.8 reference": r"""Um único `try` pode ser seguido por **vários `except`**, cada um a tratar
de uma falha diferente com a sua própria resposta. São testados de cima
para baixo; o **primeiro** tipo correspondente corre, e os restantes são
ignorados.

- Isto constrói um tratamento robusto de entradas: um `try` à volta do
  trabalho, depois um `except` por cada coisa que pode correr mal
  (`ValueError` para um número inválido, `ZeroDivisionError` para `/0`),
  cada um dando uma mensagem à medida.
- Ordena do específico para o geral se os tipos estiverem relacionados, já
  que o primeiro a corresponder ganha.

```python
try:
    a, b = int(x), int(y)
    print(a / b)
except ValueError:
    print("please enter whole numbers")
except ZeroDivisionError:
    print("cannot divide by zero")
```
""",
}
