# PyQuest translations -- language 'pt' -- chapter 15_advanced_classes -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"15.1 brief": r"""# 15.1 -- Herança: construir a partir de uma classe base

## Conceito

O Capítulo 9 construiu classes isoladas. A **herança** permite que uma classe se
construa a partir de outra: uma **subclasse** obtém automaticamente os métodos da
**classe base**, e depois acrescenta ou altera os seus próprios.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return self.name + " the animal"

class Dog(Animal):           # Dog IS an Animal
    def speak(self):
        return "Woof"
```

- `class Dog(Animal):` faz de `Dog` uma subclasse de `Animal`. Uma instância de
  `Dog` pode chamar `describe()` -- herdado de `Animal` -- *e* `speak()`, o seu
  próprio.
- A relação é "**é-um**": um `Dog` **é um** `Animal`, logo
  `isinstance(dog, Animal)` é `True`.
- O comportamento partilhado vive apenas uma vez na base; as subclasses não o
  repetem.

## A tua tarefa

Define uma classe base `Animal` com um `__init__(self, name)` e um
`describe(self)` que devolve `"<name> the animal"`. Depois define `Dog(Animal)`
que **herda** dela e acrescenta `speak(self)` que devolve `"Woof"`.

## Está feito quando

- `Dog("Rex").describe()` devolve `"Rex the animal"` (herdado).
- `Dog("Rex").speak()` devolve `"Woof"`.
- Um `Dog` **é um** `Animal`: herda em vez de copiar `describe`.
""",

"15.1 hints": r"""Escreve primeiro `Animal`, com `__init__` a guardar `self.name` e `describe`
a devolver a frase. Depois `class Dog(Animal):` -- é o `(Animal)` que faz Dog
herdar.

---

Dentro de `Dog` só escreves `speak`; `describe` vem de graça de `Animal`.
Não redefinas `describe` em `Dog`.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name + " the animal"


class Dog(Animal):
    def speak(self):
        return "Woof"
""",

"15.1 reference": r"""A **herança** permite que uma classe se construa a partir de outra. Escrever
`class Child(Parent):` faz de `Child` uma **subclasse**: automaticamente tem
todos os métodos de `Parent`, e pode acrescentar novos ou substituir os
existentes.

- A relação é **"é-um"**: um `Dog(Animal)` *é um* `Animal`, logo
  `isinstance(dog, Animal)` é `True` e um `Dog` funciona em qualquer sítio onde
  se espera um `Animal`.
- O comportamento partilhado vive **uma só vez** na classe base; as subclasses
  herdam-no em vez de o copiarem, por isso uma correção no pai chega a todos os
  filhos.
- O Python encontra um método percorrendo o **MRO** (method resolution order,
  ordem de resolução de métodos): primeiro a classe da instância, depois as
  suas bases. `object` é a base implícita de todas as classes.

```python
class Animal:
    def __init__(self, name): self.name = name
    def describe(self): return self.name + " the animal"

class Dog(Animal):
    def speak(self): return "Woof"

d = Dog("Rex")
d.describe()              # 'Rex the animal'  -- inherited
isinstance(d, Animal)    # True
```
""",

"15.2 brief": r"""# 15.2 -- super(): estender o pai

## Conceito

Uma subclasse muitas vezes precisa de tudo o que o `__init__` do pai faz **e
mais** um pouco. **`super()`** dá-te acesso ao pai, para que possas chamar o
seu método e depois acrescentar-lhe algo -- em vez de copiares o código do
pai:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # run Animal's __init__ (sets self.name)
        self.breed = breed         # then add Dog's own attribute
```

- `super().__init__(name)` chama o `__init__` do **pai** nesta instância, para
  que `self.name` seja definido por `Animal`.
- Depois disso, o filho acrescenta o que lhe é próprio (`self.breed`).
- Isto mantém a configuração do pai num único sítio; se `Animal.__init__`
  mudar, `Dog` recebe a mudança automaticamente.

## A tua tarefa

Define `Animal` com `__init__(self, name)` a guardar `self.name`. Depois
define `Dog(Animal)` cujo `__init__(self, name, breed)` chama
**`super().__init__(name)`** e depois guarda `self.breed`.

## Está feito quando

- `Dog("Rex", "Lab").name` é `"Rex"` (definido via `super().__init__`).
- `Dog("Rex", "Lab").breed` é `"Lab"`.
- Um `Dog` é um `Animal`, e o nome é definido pelo pai, não reatribuído à mão.
""",

"15.2 hints": r"""`Dog` recebe dois argumentos. O primeiro, `name`, pertence a `Animal` -- passa-o
para cima com `super().__init__(name)`.

---

Depois da linha `super().__init__(name)`, define `self.breed = breed` para a
parte própria de Dog.

---

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
""",

"15.2 reference": r"""**`super()`** devolve um proxy para a **classe pai**, para que uma subclasse
possa chamar o método do pai e construir a partir dele em vez de duplicar o
seu código. O caso habitual é o `__init__`:

- `super().__init__(args)` executa o inicializador do pai nesta instância,
  configurando tudo o que o pai possui; o filho acrescenta depois os seus
  próprios atributos.
- Mantém a lógica do pai num **único sítio** — muda `Animal.__init__` e todas
  as subclasses que chamam `super().__init__` herdam a mudança.
- `super()` funciona para qualquer método, não só `__init__`: um método que
  sobrepõe pode chamar `super().method()` para reutilizar a versão do pai e
  estendê-la.
- Sem `super().__init__`, o inicializador do pai **não** é executado, pelo que
  os atributos que ele definiria ficam em falta.

```python
class Animal:
    def __init__(self, name): self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Animal sets self.name
        self.breed = breed         # Dog adds self.breed

Dog("Rex", "Lab").name             # 'Rex'
```
""",

"15.3 brief": r"""# 15.3 -- Sobreposição: a versão própria de um filho

## Conceito

Uma subclasse pode **sobrepor** um método do pai -- definir a sua própria
versão de um método que o pai já tem. Para as instâncias da subclasse, a nova
versão prevalece:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."          # generic

class Cat(Animal):
    def speak(self):
        return "Meow"         # Cat's own
```

- `Cat("Felix").speak()` devolve `"Meow"`; um simples `Animal(...).speak()`
  continua a devolver `"..."`.
- Isto é **polimorfismo**: a *mesma* chamada, `x.speak()`, faz a coisa certa
  para qualquer que seja o tipo de `x`.
- A subclasse continua a herdar tudo o que não sobrepõe (aqui, `__init__` e
  `self.name`).

## A tua tarefa

Define `Animal` com `__init__(self, name)` e `speak(self)` a devolver `"..."`.
Depois define `Cat(Animal)` que **sobrepõe** `speak` para devolver `"Meow"`.

## Está feito quando

- `Cat("Felix").speak()` devolve `"Meow"`.
- `Animal("thing").speak()` devolve `"..."` (inalterado).
- `Cat("Felix").name` é `"Felix"` (`__init__` herdado), e um Cat é um Animal.
""",

"15.3 hints": r"""Dá a `Animal` tanto `__init__` como `speak` (a devolver "..."). Depois
`Cat(Animal)` define o seu próprio `speak`.

---

O `speak` de Cat simplesmente devolve "Meow". Não redefinas `__init__` em Cat
-- é herdado.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"
""",

"15.3 reference": r"""**Sobrepor** é definir, numa subclasse, um método que o pai já tem. Para as
instâncias da subclasse, o Python encontra primeiro a versão da subclasse
(está mais acima no MRO), pelo que o comportamento do filho substitui o do
pai.

- Isto é **polimorfismo**: um único ponto de chamada, `x.speak()`, executa o
  código certo para o tipo que `x` realmente é — `Cat` diz "Meow", um `Animal`
  genérico diz "...". O código que chama não precisa de saber o tipo exato.
- A subclasse continua a **herdar** tudo o que *não* sobrepõe (aqui,
  `__init__`).
- Uma sobreposição pode reutilizar a versão do pai com `super().method()` —
  estender em vez de substituir por completo.

```python
class Animal:
    def speak(self): return "..."
class Cat(Animal):
    def speak(self): return "Meow"

for a in [Animal(), Cat()]:
    print(a.speak())     # '...' then 'Meow' -- same call, different result
```
""",

"15.4 brief": r"""# 15.4 -- @property: um atributo calculado

## Conceito

Por vezes um valor é **derivado** de outros -- a área de um retângulo a partir
da largura e da altura. Podias guardá-lo, mas depois fica desatualizado
quando a largura muda. Uma **`@property`** calcula-o em cada acesso,
continuando a ser lida como um simples atributo:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12   -- no parentheses, but the method runs
r.width = 5
r.area        # 20   -- recomputed from the new width
```

- `@property` acima de um método faz com que `obj.area` (sem `()`) chame esse
  método e devolva o seu resultado.
- Como é executado de cada vez, o valor está sempre atualizado -- ao contrário
  de um valor guardado uma única vez no `__init__`.

## A tua tarefa

Define `Rectangle` com `__init__(self, width, height)` e uma **propriedade**
**`area`** que devolve `width * height`.

## Está feito quando

- `Rectangle(3, 4).area` é `12` (acedido sem parênteses).
- Depois de `r = Rectangle(3, 4); r.width = 5`, `r.area` é `20` -- recalculado,
  não guardado.
""",

"15.4 hints": r"""Escreve `area` como um método normal que devolve `self.width * self.height`,
e depois coloca `@property` na linha imediatamente acima de `def area`.

---

Com `@property`, quem chama escreve `r.area` (sem parênteses) e o método
executa-se de cada vez, por isso reflete sempre a largura e a altura atuais.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
""",

"15.4 reference": r"""**`@property`** é um decorador que transforma um método num **atributo
calculado, só de leitura**. `obj.area` (sem parênteses) executa o método e
devolve o seu resultado, pelo que um valor derivado é recalculado em cada
acesso e nunca fica desatualizado.

- Esconde o facto de haver trabalho a ser feito: quem chama usa `obj.area`,
  não `obj.area()`, exatamente como para um atributo guardado — mas o valor
  reflete sempre o estado atual.
- Uma `@property` simples é só de leitura; atribuir-lhe um valor levanta
  `AttributeError`. Acrescenta um `@area.setter` correspondente para permitir
  a atribuição com validação.
- Prefere uma propriedade a um valor guardado no `__init__` sempre que o valor
  *depende* de outros atributos que podem mudar.

```python
class Rectangle:
    def __init__(self, w, h): self.width, self.height = w, h
    @property
    def area(self): return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12
r.width = 5
r.area        # 20  -- recomputed
```
""",

"15.5 brief": r"""# 15.5 -- @classmethod: um construtor alternativo

## Conceito

Um método normal recebe `self` (uma instância). Um **`@classmethod`** recebe
**`cls`** (a própria classe), pelo que pode construir e devolver uma **nova
instância** -- uma forma prática de oferecer um construtor alternativo, com
nome:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

p = Point.from_tuple((3, 4))     # called on the class, not an instance
p.x, p.y                          # (3, 4)
```

- `@classmethod` faz de `cls` o primeiro parâmetro -- a classe em que o
  método é chamado (`Point` aqui).
- `cls(...)` é o mesmo que `Point(...)`, mas usar `cls` significa que as
  subclasses recebem de graça uma instância do *seu próprio* tipo.
- Chama-se na **classe**: `Point.from_tuple(...)`.

## A tua tarefa

Define `Point` com `__init__(self, x, y)`, e um **classmethod**
`from_tuple(cls, pair)` que constrói um `Point` a partir de um tuplo `(x, y)`.

## Está feito quando

- `Point.from_tuple((3, 4)).x` é `3` e `.y` é `4`.
- `from_tuple` é um `@classmethod` que recebe `cls`, e constrói o ponto com
  `cls(...)`.
""",

"15.5 hints": r"""Escreve `__init__` como habitualmente. Depois acrescenta um método decorado
com `@classmethod` cujo primeiro parâmetro é `cls`, não `self`.

---

Dentro de `from_tuple`, desempacota o par e constrói o objeto com `cls`:
`return cls(pair[0], pair[1])`.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])
""",

"15.5 reference": r"""Um **`@classmethod`** está ligado à **classe**, não a uma instância: o seu
primeiro parâmetro é **`cls`** (a própria classe) em vez de `self`. Como tem a
classe, pode construir instâncias — o uso clássico é um **construtor
alternativo**.

- Chama-se na classe: `Point.from_tuple((3, 4))`. O Python passa `Point` como
  `cls`.
- Construir com `cls(...)` em vez do nome literal da classe significa que uma
  **subclasse** que chame o classmethod herdado recebe uma instância de *si
  própria*.
- Contrasta com **`@staticmethod`**, que não recebe nem `self` nem `cls` —
  apenas uma função simples colocada no espaço de nomes da classe, usada
  quando o método não precisa de acesso à instância nem à classe.

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    @classmethod
    def from_tuple(cls, pair): return cls(pair[0], pair[1])

Point.from_tuple((3, 4)).x     # 3
```
""",

"15.6 brief": r"""# 15.6 -- __eq__: igualdade de valor

## Conceito

Por omissão, `==` em objetos pergunta "são o **mesmo objeto**?" -- por isso
dois objetos construídos separadamente com dados idênticos *não* são iguais.
O método dunder **`__eq__`** muda isso para **igualdade de valor**:

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):
        return self.cents == other.cents

Money(500) == Money(500)     # True   -- same value
Money(500) == Money(750)     # False
```

- O Python chama `a.__eq__(b)` para `a == b`. Devolves se devem ser
  considerados iguais -- normalmente comparando os atributos que definem o
  valor.
- `!=` é tratado por ti (é a negação de `__eq__`).
- (Definir `__eq__` também é o que permite que os teus objetos sejam
  comparados por valor em testes, listas, e verificações com `in`.)

## A tua tarefa

Define `Money` com `__init__(self, cents)` e um **`__eq__`** para que dois
objetos `Money` sejam iguais exatamente quando os seus `cents` coincidem.

## Está feito quando

- `Money(500) == Money(500)` é `True`.
- `Money(500) == Money(750)` é `False`.
- A igualdade compara `cents`, não a identidade do objeto.
""",

"15.6 hints": r"""Acrescenta um método `__eq__(self, other)` a Money. O Python chama-o para
`==`.

---

Devolve a comparação dos valores: `return self.cents == other.cents`.

---

class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        return self.cents == other.cents
""",

"15.6 reference": r"""Por omissão, `==` entre objetos testa a **identidade** — se são exatamente o
mesmo objeto — por isso dois objetos construídos de forma independente com
dados idênticos comparam como diferentes. Definir **`__eq__(self, other)`**
redefine `==` como **igualdade de valor**.

- O Python chama `a.__eq__(b)` para avaliar `a == b`; devolve se devem contar
  como iguais, normalmente comparando os atributos que definem o valor. `!=`
  segue-se automaticamente como a sua negação.
- A igualdade de valor é o que faz os objetos funcionarem de forma intuitiva
  em testes com `==`, na pertença a `list` (`in`), e ao comparar resultados.
- Se definires `__eq__`, a classe torna-se **não hasheável** (o seu
  `__hash__` é definido como `None`), pelo que não pode entrar num `set` ou
  ser chave de `dict` até também definires `__hash__` — muitas vezes
  `return hash(self.cents)`.

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other): return self.cents == other.cents

Money(500) == Money(500)     # True
Money(500) == Money(750)     # False
```
""",

"15.7 brief": r"""# 15.7 -- __lt__: tornar objetos ordenáveis

## Conceito

`sorted`, `min` e `max` ordenam tudo usando o operador **`<`**. Por omissão,
o Python não sabe comparar dois dos teus objetos -- ordená-los levanta
`TypeError`. Define **`__lt__`** ("less than", menor que) e tornam-se
ordenáveis:

```python
class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees
    def __lt__(self, other):
        return self.degrees < other.degrees

temps = [Temperature(30), Temperature(10), Temperature(20)]
sorted(temps)        # ordered 10, 20, 30 -- by degrees
```

- O Python chama `a.__lt__(b)` para `a < b`. Devolve se `a` deve vir
  **antes** de `b` -- normalmente comparando o atributo pelo qual queres
  ordenar.
- `sorted` só precisa de `<`, por isso só `__lt__` já torna uma lista dos teus
  objetos ordenável.

## A tua tarefa

Define `Temperature` com `__init__(self, degrees)` e um **`__lt__`** para que
as temperaturas se comparem por `degrees`.

## Está feito quando

- `Temperature(10) < Temperature(20)` é `True`.
- `sorted([Temperature(30), Temperature(10), Temperature(20)])` fica ordenado
  `10, 20, 30` por degrees.
- A comparação usa `degrees`.
""",

"15.7 hints": r"""Acrescenta `__lt__(self, other)` a Temperature. O Python chama-o para `<`, e
o `sorted` usa `<`.

---

Devolve a comparação dos valores: `return self.degrees < other.degrees`. Esse
único método já chega para tornar uma lista ordenável.

---

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __lt__(self, other):
        return self.degrees < other.degrees
""",

"15.7 reference": r"""**`__lt__(self, other)`** define o operador **`<`** para os teus objetos, e
`<` é exatamente o que **`sorted`**, **`min`** e **`max`** usam para ordenar
as coisas. Sem ele, comparar dois dos teus objetos levanta `TypeError`; com
ele, uma lista deles ordena-se diretamente.

- O Python chama `a.__lt__(b)` para `a < b`; devolve se `a` deve vir
  **antes** de `b`, normalmente comparando o atributo pelo qual ordenas.
- `sorted` só precisa de `<`, por isso só `__lt__` já torna os objetos
  ordenáveis. O conjunto completo dos dunders de ordenação é `__lt__`,
  `__le__`, `__gt__`, `__ge__`.
- `functools.total_ordering` é um decorador de classe que preenche os outros
  três a partir de `__lt__` e `__eq__`, se quiseres todas as comparações.

```python
class Temperature:
    def __init__(self, degrees): self.degrees = degrees
    def __lt__(self, other): return self.degrees < other.degrees

sorted([Temperature(30), Temperature(10), Temperature(20)])   # 10, 20, 30
min([Temperature(30), Temperature(10)]).degrees               # 10
```
""",

"15.8 brief": r"""# 15.8 -- Capstone: uma hierarquia de formas

## Conceito

Junta o capítulo todo numa pequena hierarquia. Uma classe base `Shape` guarda
um nome e sabe descrever-se; um `Rectangle` herda dela, acrescenta tamanho,
calcula a sua área como propriedade, e compara-se com outros retângulos pela
área.

```python
class Shape:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return "%s with area %d" % (self.name, self.area)   # uses the property

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
    def __eq__(self, other):
        return self.area == other.area
    def __lt__(self, other):
        return self.area < other.area
```

Repara que `Shape.describe` usa `self.area`, que só `Rectangle` define -- o
método da base funciona através da propriedade da subclasse (polimorfismo).

## A tua tarefa

Constrói exatamente as duas classes acima:

- `Shape.__init__(self, name)` e `describe(self)` -> `"<name> with area
  <area>"`.
- `Rectangle(Shape)`: `__init__(self, width, height)` define o nome como
  `"rectangle"` via `super()`, guarda width/height; uma **propriedade**
  `area`; e `__eq__` / `__lt__` a comparar por `area`.

## Está feito quando

- `Rectangle(3, 4).area` é `12`; `.name` é `"rectangle"`; `.describe()` é
  `"rectangle with area 12"`; é um `Shape`.
- `Rectangle(2, 6) == Rectangle(3, 4)` é `True` (áreas iguais).
- `sorted([Rectangle(3, 4), Rectangle(1, 1), Rectangle(2, 5)])` fica ordenado
  pela área (1, 10, 12).
""",

"15.8 hints": r"""Começa com `Shape`: `__init__(self, name)` e `describe` a devolver
`"%s with area %d" % (self.name, self.area)`. Isto refere-se a `self.area`,
que a subclasse vai fornecer.

---

`Rectangle(Shape)`: no `__init__` chama `super().__init__("rectangle")`,
guarda width/height; acrescenta `@property area` a devolver
`width * height`; acrescenta `__eq__` e `__lt__` que comparam `self.area` com
`other.area`.

---

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "%s with area %d" % (self.name, self.area)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area
""",

"15.8 reference": r"""O capstone junta o capítulo todo numa única hierarquia, tal como as classes
reais são construídas:

- **Herança** — `Rectangle(Shape)` *é um* `Shape`, por isso recebe `describe`
  de graça e `isinstance(r, Shape)` é verdadeiro.
- **`super()`** — `Rectangle.__init__` chama `super().__init__("rectangle")`
  para deixar a base definir `self.name`, e depois acrescenta a sua própria
  largura e altura.
- **`@property`** — `area` é calculada a partir da largura e da altura em
  cada acesso, por isso mantém-se correta quando um lado muda.
- **Polimorfismo** — `Shape.describe` lê `self.area`, que só `Rectangle`
  define; o método da base funciona através da propriedade da subclasse.
- **Dunders** — `__eq__` e `__lt__` (ambos por área) fazem com que os
  retângulos se comparem e ordenem como valores nativos, por isso `==` e
  `sorted` simplesmente funcionam.

Juntas, estas peças transformam um objeto simples num que se comporta como um
valor de primeira classe: tem uma identidade numa hierarquia, dados
derivados, e igualdade e ordenação com significado — o resultado de todo o
capítulo.

```python
r = Rectangle(3, 4)
r.describe()                              # 'rectangle with area 12'
Rectangle(2, 6) == Rectangle(3, 4)        # True  -- equal areas
sorted([Rectangle(3, 4), Rectangle(1, 1)])   # by area: 1, then 12
```
""",
}
