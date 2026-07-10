# 7.3 -- ZeroDivisionError: pede perdão

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
