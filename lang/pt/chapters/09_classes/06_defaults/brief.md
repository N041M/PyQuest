# 9.6 -- Um valor por omissão sensato

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
