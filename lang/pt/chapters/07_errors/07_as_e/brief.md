# 7.7 -- Ler o erro: except ... as e

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
