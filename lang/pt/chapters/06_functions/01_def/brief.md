# 6.1 -- def: a tua primeira função

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
