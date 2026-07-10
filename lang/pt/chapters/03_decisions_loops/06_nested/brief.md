# 3.6 -- Condições aninhadas

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
