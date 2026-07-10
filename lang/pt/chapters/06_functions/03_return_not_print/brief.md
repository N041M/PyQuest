# 6.3 -- return, não print

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
