# 6.5 -- return termina a função

## Conceito

`return` não se limita a devolver um valor -- **para a função no
momento**. Nada depois de um `return` executado corre. Isso torna as funções com
ramificações fáceis de ler: resolve cada caso e sai.

```python
def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
```

Repara que não há `else` -- não é preciso nenhum. Se o primeiro `return` disparou, a
função já terminou; chegar à última linha *significa* que `n` era positivo.
Este estilo chama-se **retorno antecipado**.

Uma função com vários `return` continua a devolver exatamente **um**
valor por chamada: o do primeiro `return` que executar.

## Exemplo

```python
sign(-3)    # "negative"
sign(0)     # "zero"
sign(42)    # "positive"
```

## A tua tarefa

Define `sign(n)` que devolva `"negative"`, `"zero"`, ou `"positive"` para um
número inteiro `n`.

## Está feito quando

- `sign(-3)`, `sign(0)`, `sign(42)` devolvem as três palavras acima.
- Os casos-limite `-1` e `1` também estão corretos.
