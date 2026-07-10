# 3.2 -- if

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
