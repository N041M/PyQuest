# PyQuest translations -- language 'pt' -- chapter 09_classes -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"9.1 brief": r"""# 9.1 -- A primeira classe

## Conceito

Uma **classe** é um molde para um objeto que junta dados relacionados. Até
agora, o nome e a idade de um cão seriam duas variáveis soltas; uma classe
une-as numa única coisa que podes passar de um lado para o outro.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `class Dog:` dá nome ao molde.
- `__init__` é o **construtor** -- corre quando constróis um novo Dog, e a sua
  função é preparar os dados do objeto.
- `self` é o objeto que está a ser construído; `self.name = name` guarda o
  valor **no objeto** para que continue lá mais tarde.

Constróis um (uma *instância*) chamando a classe como se fosse uma função, e
lês os seus dados com um ponto:

```python
d = Dog("Rex", 3)
print(d.name)   # Rex
print(d.age)    # 3
```

## A tua tarefa

Define uma classe `Dog` cujo `__init__` recebe um `name` e uma `age` e guarda
cada um no objeto como `self.name` e `self.age`.

## Está feito quando

- `Dog("Rex", 3)` cria um objeto cujo `.name` é `"Rex"` e `.age` é `3`.
- Funciona para qualquer nome e idade.
- Usaste uma `class` com um `__init__` que guarda os dois valores em `self`.
""",

"9.1 hints": r"""Começa com `class Dog:` e dá-lhe um método `__init__(self, name, age)`.

---

Dentro de `__init__`, copia cada parâmetro para o objeto com `self.`:
`self.name = name`. É isso que faz o valor ficar guardado.

---

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
""",

"9.1 reference": r"""Uma **classe** define um novo tipo de objeto, juntando dados relacionados num
único valor. **`__init__`** é o inicializador: o Python chama-o
automaticamente quando crias uma instância, para preparar os seus dados
iniciais.

- `class Point:` abre a definição; chamar `Point(3, 4)` cria uma **instância**
  e executa `__init__`.
- **`self`** é a instância que está a ser construída; `self.x = x` guarda um
  valor como **atributo** nela, onde qualquer método o pode alcançar mais
  tarde.
- O primeiro parâmetro de `__init__` é sempre `self`; os restantes são os
  argumentos que quem chama passa.

```python
class Point:
    def __init__(self, x, y):
        self.x = x          # store data on the instance
        self.y = y

p = Point(3, 4)
p.x                         # 3
```
""",

"9.2 brief": r"""# 9.2 -- Métodos: comportamento sobre os dados

## Conceito

Os objetos não guardam apenas dados -- têm **métodos**, funções que vivem no
objeto e trabalham com os seus próprios dados através de `self`.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

`area` é um método: recebe `self` (o objeto sobre o qual é chamado) e usa
`self.side`. Chama-lo com um ponto e parênteses -- não precisas de passar
`self`, o Python trata disso:

```python
s = Square(5)
print(s.area())   # 25
```

O objetivo de um método é que o comportamento viaja *com* os dados: qualquer
Square já sabe como calcular a sua própria área.

## A tua tarefa

Define uma classe `Square` cujo `__init__` guarda um `side`, e acrescenta um
método `area()` que devolve a área do quadrado (`side * side`).

## Está feito quando

- `Square(5).area()` devolve `25`.
- Funciona para qualquer comprimento de lado, incluindo `0`.
- `area` é um método na classe e calcula a partir de `self.side`.
""",

"9.2 hints": r"""Guarda o lado em `__init__` como da última vez, depois acrescenta um segundo
método `area`.

---

Um método recebe `self` primeiro: `def area(self):`. Dentro, devolve
`self.side * self.side`.

---

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
""",

"9.2 reference": r"""Um **método** é uma função definida dentro de uma classe. Recebe sempre
**`self`** primeiro e calcula a partir dos próprios atributos do objeto, para
que o comportamento viva junto dos dados sobre os quais atua.

- Chama-o com `instance.method()`; o Python passa a instância como `self`
  automaticamente, por isso `p.dist()` chama `dist(p)`.
- Lá dentro, alcança os dados do objeto através de `self`: `self.x`, `self.y`.
- Um método pode receber mais parâmetros depois de `self` e `return` um valor
  como qualquer função.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

Point(3, 4).dist()      # 5.0
```
""",

"9.3 brief": r"""# 9.3 -- Estado que se lembra

## Conceito

Os dados de um objeto vivem **entre** chamadas de métodos -- um método pode
alterar `self`, e a chamada seguinte vê a alteração. É isso que torna os
objetos úteis: eles *lembram-se*.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count = self.count + 1
        return self.count
```

Cada `tick()` aumenta `self.count` e devolve o novo valor:

```python
c = Counter()
c.tick()   # 1
c.tick()   # 2
c.tick()   # 3
```

Crucialmente, a contagem vive **na instância** (`self.count`), por isso dois
contadores mantêm totais separados -- fazer tick num nunca toca no outro.

## A tua tarefa

Define uma classe `Counter` que começa o seu `count` em `0`. Acrescenta um
método `tick()` que soma um à contagem e **devolve a nova contagem**.

## Está feito quando

- Um `Counter` novo, chamado três vezes, devolve `1`, `2`, `3`.
- Dois contadores são independentes -- fazer tick num não altera o outro.
- A contagem está guardada em `self`, não partilhada entre todos os
  contadores.
""",

"9.3 hints": r"""`__init__` define o ponto de partida: `self.count = 0`. Depois `tick`
altera-o.

---

Dentro de `tick`, faz `self.count = self.count + 1` (ou `self.count += 1`),
depois `return self.count`. Mantém a contagem em `self` para que cada
contador tenha a sua própria.

---

class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1
        return self.count
""",

"9.3 reference": r"""Um objeto guarda **estado** — dados que persistem entre chamadas. Um método
pode **alterar** `self`, e a chamada seguinte ao método vê a mudança, por isso
o objeto lembra-se do que lhe aconteceu.

- `self.count += 1` atualiza um atributo no próprio lugar; o novo valor
  mantém-se até ser alterado de novo.
- É esse o objetivo dos objetos: transportam os seus dados consigo entre
  chamadas, ao contrário de uma função simples cujas variáveis locais
  desaparecem quando ela termina.
- Cada instância tem a sua **própria** cópia dos atributos, por isso dois
  contadores contam de forma independente.

```python
class Counter:
    def __init__(self):
        self.n = 0
    def tick(self):
        self.n += 1         # remembered for next time

c = Counter(); c.tick(); c.tick(); c.n   # 2
```
""",

"9.4 brief": r"""# 9.4 -- Mais dados, mais métodos

## Conceito

Uma classe pode guardar várias peças de dados e oferecer vários métodos sobre
elas. Nada de novo na sintaxe -- apenas mais dela:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

Os dois métodos leem os mesmos dados guardados através de `self`; cada
Rectangle responde a qualquer uma das duas perguntas sobre si próprio:

```python
r = Rectangle(3, 4)
r.area()        # 12
r.perimeter()   # 14
```

## A tua tarefa

Define uma classe `Rectangle` cujo `__init__` guarda um `width` e um `height`,
com dois métodos: `area()` devolve `width * height`, e `perimeter()` devolve
`2 * (width + height)`.

## Está feito quando

- `Rectangle(3, 4).area()` é `12` e `.perimeter()` é `14`.
- Ambos funcionam para qualquer largura e altura.
- Ambos são métodos na classe, calculando a partir de `self`.
""",

"9.4 hints": r"""Guarda os dois valores em `__init__`: `self.width = width` e
`self.height = height`.

---

Acrescenta dois métodos. `area` devolve `self.width * self.height`;
`perimeter` devolve `2 * (self.width + self.height)`.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
""",

"9.4 reference": r"""Uma classe pode guardar **vários atributos** e oferecer **vários métodos**
que trabalham em conjunto sobre eles — modelando algo com mais do que uma
propriedade.

- `__init__` guarda cada peça de dados (`self.width`, `self.height`); cada
  método lê os atributos de que precisa.
- Os métodos podem basear-se nos mesmos dados para respostas diferentes:
  `area` multiplica, `perimeter` soma — um objeto, muitas perguntas.
- Manter os dados e as operações numa só classe significa que quem chama
  pergunta ao objeto em vez de andar a gerir variáveis soltas.

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

r = Rectangle(3, 4); r.area(), r.perimeter()   # (12, 14)
```
""",

"9.5 brief": r"""# 9.5 -- Imprimir um objeto: `__str__`

## Conceito

Imprime um objeto tal como está e obténs algo inútil como
`<__main__.Point object at 0x10f3d2b80>`. Para controlar o aspeto de um
objeto como texto, define o método especial `__str__`, que devolve a cadeia
de caracteres que o Python deve mostrar.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

`__str__` é um **dunder** (duplo sublinhado) -- o Python chama-o por ti sempre
que o objeto é transformado em texto, por `print()` ou `str()`:

```python
p = Point(3, 4)
print(p)        # (3, 4)
str(p)          # "(3, 4)"
```

Nunca chamas `__str__` diretamente; apenas o defines, e `str(p)` aciona-o.

## A tua tarefa

Define uma classe `Point` que guarda `x` e `y`, com um método `__str__` para
que `str(Point(3, 4))` seja exatamente `"(3, 4)"` -- os dois valores entre
parênteses, com vírgula e espaço entre eles.

## Está feito quando

- `str(Point(3, 4))` é `"(3, 4)"`.
- Funciona para qualquer `x` e `y`, incluindo negativos.
- A formatação vem de um método `__str__` na classe.
""",

"9.5 hints": r"""Guarda `x` e `y` em `__init__` como habitualmente, depois acrescenta um
método `__str__(self)`.

---

`__str__` tem de **devolver** o texto (não imprimi-lo). Constrói-o com uma
f-string: `return f"({self.x}, {self.y})"`. Repara na vírgula e no espaço.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
""",

"9.5 reference": r"""**`__str__`** define o texto legível por humanos para um objeto. Quando fazes
`print` de uma instância ou chamas `str()` sobre ela, o Python chama `__str__`
e usa o que ele devolver.

- Sem ele, imprimir um objeto mostra um padrão pouco útil como
  `<Point object at 0x...>`; `__str__` substitui isso por algo com
  significado.
- Tem de **devolver** uma cadeia de caracteres (não imprimir uma),
  normalmente construída com uma f-string a partir dos atributos do objeto.
- `__str__` é um dos vários métodos **dunder** ("duplo sublinhado") que o
  Python chama em teu nome, como `__init__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(3, 4))      # (3, 4)
```
""",

"9.6 brief": r"""# 9.6 -- Um valor por omissão sensato

## Conceito

Um construtor é apenas uma função, por isso também pode receber **parâmetros
por omissão** (6.4). Isso permite que quem chama omita o que não lhe
interessa e ainda assim obtenha um objeto funcional.

```python
class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
```

Se não passares uma saudação, obténs `"Hello"`; se passares, é essa que é
usada:

```python
Greeter().greet("Ada")        # "Hello, Ada!"
Greeter("Hi").greet("Bo")     # "Hi, Bo!"
```

O valor por omissão vive na assinatura de `__init__` (`greeting="Hello"`),
por isso o objeto é configurado uma vez na construção e cada `greet` reutiliza-o.

## A tua tarefa

Define uma classe `Greeter` cujo `__init__` recebe um `greeting` que **tem
por omissão `"Hello"`** e guarda-o. Acrescenta um método `greet(name)` que
devolve `"{greeting}, {name}!"`.

## Está feito quando

- `Greeter().greet("Ada")` é `"Hello, Ada!"` (valor por omissão usado).
- `Greeter("Hi").greet("Bo")` é `"Hi, Bo!"` (valor por omissão substituído).
- O valor por omissão é um *parâmetro* por omissão de `__init__`, não um `if`
  lá dentro.
""",

"9.6 hints": r"""Dá a `__init__` um parâmetro com valor por omissão:
`def __init__(self, greeting="Hello"):`, depois guarda-o em `self`.

---

`greet` constrói a mensagem: `return f"{self.greeting}, {name}!"`. O valor
por omissão pertence à assinatura, por isso não escrevas um
`if greeting is None` em vez disso.

---

class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
""",

"9.6 reference": r"""`__init__` é uma função comum, por isso os seus parâmetros podem ter
**valores por omissão** — permitindo criar um objeto com ou sem determinados
argumentos.

- `def __init__(self, balance=0):` permite `Account()` (começa em 0) ou
  `Account(100)` (começa em 100).
- Aplicam-se as mesmas regras: os parâmetros com valor por omissão vêm depois
  dos que não têm, e um valor por omissão mutável precisa do truque do
  sentinela `None`
  (`def __init__(self, items=None): self.items = items or []`).
- Os valores por omissão tornam o caso comum simples, mantendo a opção em
  aberto.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance

Account().balance        # 0
Account(100).balance     # 100
```
""",

"9.7 brief": r"""# 9.7 -- Objetos a trabalhar em conjunto

## Conceito

Um método pode receber **outro objeto** como argumento e construir um **novo**
objeto como resultado. É assim que os objetos se combinam sem perder a sua
própria identidade.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

`add` vai buscar dados a `other` (outro Vector), e **devolve um `Vector` novo
em folha** -- não altera `self` nem `other`:

```python
a = Vector(1, 2)
b = Vector(3, 4)
c = a.add(b)      # Vector(4, 6)
a.x               # still 1 -- a is untouched
```

Construir um `Vector(...)` *dentro* do próprio método de `Vector` é normal: a
classe pode usar-se a si própria.

## A tua tarefa

Define uma classe `Vector` que guarda `x` e `y`, com um método `add(other)`
que devolve um **novo** `Vector` cujas coordenadas são a soma das coordenadas
dos dois vetores. Os originais têm de ficar inalterados.

## Está feito quando

- `Vector(1, 2).add(Vector(3, 4))` é um Vector com `.x == 4` e `.y == 6`.
- Os dois vetores de entrada ficam inalterados depois.
- `add` devolve um novo objeto `Vector` (não um tuplo), construído dentro do
  método.
""",

"9.7 hints": r"""Guarda `x` e `y` em `__init__`. O método recebe o outro vetor:
`def add(self, other):`.

---

Lê os dois vetores através do ponto (`self.x`, `other.x`) e **devolve um novo
Vector**: `return Vector(self.x + other.x, self.y + other.y)`. Não atribuas
de volta a `self`.

---

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
""",

"9.7 reference": r"""Os objetos **colaboram**: um método pode receber **outro objeto** da mesma
classe como parâmetro, ler os seus atributos, e **devolver um novo** objeto
com o resultado — deixando ambas as entradas inalteradas.

- `def add(self, other):` alcança `self.x` e `other.x`, depois
  `return Vector(self.x + other.x, ...)`. Devolver uma instância nova mantém
  os operandos imutáveis.
- É assim que os objetos do tipo valor se compõem (pontos, vetores, dinheiro).
  Definir o dunder `__add__` deixaria mesmo `a + b` chamá-lo.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

Vector(1, 2).add(Vector(3, 4)).x    # 4
```
""",

"9.8 brief": r"""# 9.8 -- Capstone: uma conta bancária

## Conceito

Chegou a hora de juntar o capítulo todo: uma classe com estado, vários
métodos, um valor por omissão sensato, e uma regra que ela própria impõe.

Uma `BankAccount` mantém um `balance`. Podes depositar (cresce) e levantar
(diminui) -- mas um levantamento que deixasse a conta a descoberto tem de ser
**recusado**, mantendo o saldo intocado.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

- `balance` tem por omissão `0`, por isso `BankAccount()` é uma conta vazia.
- `deposit` e `withdraw` alteram o saldo guardado (estado que persiste).
- `withdraw` **devolve `True`** quando tem sucesso e **`False`** quando
  recusa -- e, ao recusar, o saldo não muda.

```python
acc = BankAccount(100)
acc.deposit(50)       # balance 150
acc.withdraw(70)      # True,  balance 80
acc.withdraw(999)     # False, balance still 80
```

## A tua tarefa

Define `BankAccount` exatamente como acima: um `balance` com valor por
omissão `0`, um método `deposit(amount)`, e um método `withdraw(amount)` que
subtrai e devolve `True` só quando há saldo suficiente -- caso contrário não
muda nada e devolve `False`.

## Está feito quando

- `BankAccount()` começa em `0`; `BankAccount(100)` começa em `100`.
- `deposit` e `withdraw` atualizam `balance`, e levantar demasiado devolve
  `False` e deixa `balance` inalterado.
- Levantar exatamente o saldo é permitido.
""",

"9.8 hints": r"""`__init__(self, balance=0)` guarda o saldo inicial. `deposit` limita-se a
somar a `self.balance`.

---

`withdraw` precisa de uma guarda: `if amount <= self.balance:` subtrai e
`return True`; caso contrário não muda nada e `return False`.

---

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
""",

"9.8 reference": r"""O capstone é uma **classe com estado** que junta o capítulo todo: um valor
por omissão em `__init__`, métodos que **alteram** o estado, uma **guarda**
que lança um erro em operações inválidas, e `__str__` para exibição.

- `__init__` define o saldo inicial (com um valor por omissão); `deposit` e
  `withdraw` alteram `self.balance` no próprio lugar.
- Uma guarda protege o invariante: `withdraw` verifica os fundos e
  `raise ValueError(...)` em vez de permitir um estado impossível.
- `__str__` representa o objeto para impressão. Juntas, estas peças fazem um
  objeto fiável de usar e agradável de ler.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
    def __str__(self):
        return f"balance: {self.balance}"
```
""",
}
